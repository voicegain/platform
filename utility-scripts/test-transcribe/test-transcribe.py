# MIT License

# Copyright (c) 2020 Voicegain (Resolvity, Inc.)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import logging
import sys
import os
import glob
import wave
from voicegain_speech import ApiClient
from voicegain_speech import Configuration
from voicegain_speech import TranscribeApi
from voicegain_speech import DataApi
import base64
import time
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
from google.oauth2 import service_account
from transcription_compare.levenshtein_distance_calculator import UKKLevenshteinDistanceCalculator
from transcription_compare.tokenizer import CharacterTokenizer, WordTokenizer
from transcription_compare.local_optimizer.digit_util import DigitUtil
from transcription_compare.local_optimizer.local_cer_optimizer import LocalCerOptimizer
from transcription_compare.results import MultiResult
from queue import Queue as MultiThreadQueue
import logging
from collections import defaultdict
import threading
import nltk
nltk.download('wordnet')

# set this to the number of processing threads you want to run
THREAD_NUMBER = 1


class GoogleStreamRequests:
    def __init__(self, stream_file, n_channels, sleep_time=0.1):

        with wave.open(stream_file, mode='rb') as wavread:
            sample_rate = wavread.getframerate()
            content = wavread.readframes(wavread.getnframes())
            sampwidth = wavread.getsampwidth()

        n = int(sample_rate * sleep_time * sampwidth* n_channels)
        n_group_content = [content[i * n:(i + 1) * n] for i in range((len(content) + n - 1) // n)]
        self.n_group_len = len(n_group_content)

        stream = n_group_content
        # self.requests = (types.StreamingRecognizeRequest(audio_content=chunk) for chunk in stream)
        self.requests = [types.StreamingRecognizeRequest(audio_content=chunk) for chunk in stream]
        # print(self.requests)
        self.index = 0
        self.request_time_list = []
        self.sleep_time = sleep_time
        self.first_request_time = None

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.n_group_len:
            raise StopIteration
        new_r = self.requests[self.index]
        # new_r = next(self.requests)
        if self.index != 0:
            # time_to_sleep = self.sleep_time - (time.time() - self.request_time_list[-1])
            time_to_sleep = self.sleep_time - (time.time() - self.request_time_list[-1]) - 0.01
            if time_to_sleep > 0:
                time.sleep(time_to_sleep)
        else:
            self.first_request_time = time.time()
            time.sleep(self.sleep_time)

        self.index += 1
        self.request_time_list.append(time.time())
        return new_r


def print_help():
    help_msg = '''
    python 8x8.py <JWT> <input_dir> <output_dir> <google_api_cred> <google_model>
    
    JWT: Voicegain JWT token
    input_dir: input directory with all wav files (*.wav) and reference txt (*-reference.txt [Optional])
    output_dir: output directory for Voicegain and Google result, and transcription compare HTML
    google_api_cred: Path to google json file. Optional
    google_model: Which model(default/video/phone_call) to select for Google recognizer. The default would be Google Standard. Optional
    '''
    print(help_msg)


def get_all_audio_file_in_input_dir(input_dir):
    # support wav and mp3

    # all_wav = glob.glob(os.path.join(input_dir, "*.wav"))
    # all_mp3 = glob.glob(os.path.join(input_dir, "*.mp3"))

    return glob.glob(os.path.join(input_dir, "*.wav"))


def get_ext_from_channel(is_left_channel):
    if is_left_channel is True:
        ext = "-left"
    elif is_left_channel is False:
        ext = "-right"
    else:
        ext = ""
    return ext


def run_voicegain_recognizer(audio_file, output_dir, voicegain_api_client, n_channel):
    """

    :param audio_file:
    :param output_dir:
    :param voicegain_api_client:
    :param n_channel:
    :return: a list of result path. (one / two items)
    """
    file_dir, base_name = os.path.split(audio_file)
    base_name_without_ext, _ = os.path.splitext(base_name)

    logging.info("Start to run voicegain recognizer")

    transcribe_api = TranscribeApi(voicegain_api_client)
    data_api = DataApi(voicegain_api_client)

    with open(audio_file, "rb") as f:
        audio_base64 = base64.b64encode(f.read()).decode()

    data_post_response = data_api.data_audio_post(
        data_object_with_audio={
            "audio": {
                "source": {
                    "inline": {
                        "data": audio_base64
                    }
                }
            }
        },
        _request_timeout=300
    )
    object_id = data_post_response.object_id
    logging.info("Object ID: {}".format(object_id))

    def run_transcribe(transcribe_left_channel):
        """

        :param transcribe_left_channel: True/ False / None
        :return:
        """
        ext = get_ext_from_channel(transcribe_left_channel)
        voicegain_result_txt_path = os.path.join(output_dir, "{}-voicegain{}.txt".format(base_name_without_ext, ext))

        async_transcription_request = {
            "sessions": [
                {
                    "asyncMode": "OFF-LINE",
                    "poll": {
                        "afterlife": 60000,
                        "persist": 0
                    }
                }
            ],
            "audio": {
                "source": {
                    "dataStore": {
                        "uuid": object_id
                    }
                }
            }
        }

        if transcribe_left_channel is True:
            async_transcription_request["sessions"][0]["audioChannelSelector"] = "left"
        elif transcribe_left_channel is False:
            async_transcription_request["sessions"][0]["audioChannelSelector"] = "right"

        async_transcribe_init_response = transcribe_api.asr_transcribe_async_post(
            async_transcription_request=async_transcription_request
        )

        async_response_session = async_transcribe_init_response.sessions[0]
        session_id = async_response_session.session_id
        logging.info("session id {}".format(session_id))
        logging.info("Waiting for voicegain result...")

        while True:
            time.sleep(5)
            poll_response = transcribe_api.asr_transcribe_async_get(
                session_id=session_id,
                full=True
            )
            poll_response_result = poll_response.result

            if poll_response_result.final:
                # get to final
                result_transcript = poll_response_result.transcript
                # print("final transcription: " + result_transcript)
                with open(os.path.join(voicegain_result_txt_path), "w", encoding='utf-8') as file:
                    file.write(result_transcript)
                logging.info("Got Voicegain result. Saved to {}".format(voicegain_result_txt_path))
                break
        return voicegain_result_txt_path

    voicegain_result_txt_path_list = []
    if n_channel == 1:
        logging.info("Transcribe mono audio")
        voicegain_result_txt_path_list.append(run_transcribe(None))
    else:
        logging.info("Transcribe left channel")
        voicegain_result_txt_path_list.append(run_transcribe(True))
        logging.info("Transcribe right channel")
        voicegain_result_txt_path_list.append(run_transcribe(False))

    return voicegain_result_txt_path_list


def run_google_recognizer(audio_file, output_dir, google_api_client, n_channel, sample_rate_hertz, model="default"):
    """
        "default" for GoogleStandard test, and select "video" for GoogleVideo test.
    """
    if google_api_client is None:
        logging.info("Google json key is not configured. Will not run google recognizer")
        return None

    file_dir, base_name = os.path.split(audio_file)
    base_name_without_ext, _ = os.path.splitext(base_name)


    logging.info("Start to run Google recognizer")

    # In practice, stream should be a generator yielding chunks of audio data.
    requests = GoogleStreamRequests(audio_file, n_channel)

    # config = types.RecognitionConfig(
    #     encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    #     sample_rate_hertz=sample_rate_hertz,
    #     language_code='en-US',
    #     model="video")
    if n_channel != 1:
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=sample_rate_hertz,
            language_code='en-US',
            use_enhanced=True,
            model=model,
            audio_channel_count=2,
            enable_separate_recognition_per_channel=True
        )

    else:
        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=sample_rate_hertz,
            language_code='en-US',
            use_enhanced=True,
            model=model

        )

    all_output = defaultdict(list)
    streaming_config = types.StreamingRecognitionConfig(config=config, interim_results=False)

    # streaming_recognize returns a generator.
    responses = google_api_client.streaming_recognize(streaming_config, requests)

    for response in responses:
        # Once the transcription has settled, the first result will contain the
        # is_final result. The other results will be for subsequent portions of
        # the audio.
        for result in response.results:
            alternatives = result.alternatives
            # The alternatives are ordered from most likely to least.
            for alternative in alternatives:
                if result.is_final:
                    # all_output.append(alternative.transcript.strip())
                    if n_channel != 1:
                        # print(u'channel_tag: {}'.format(result.channel_tag))
                        all_output[result.channel_tag].append(alternative.transcript.strip())
                    else:
                        all_output[0].append(alternative.transcript.strip())

                    break

    def write_to_txt(tag, output_dict):
        if tag == 1:
            ext = "-left"
        elif tag == 2:
            ext = "-right"
        elif tag == 0:
            ext = ""
        google_result_txt_path = os.path.join(output_dir, "{}-google{}.txt".format(base_name_without_ext, ext))
        all_output = " ".join(output_dict[tag])

        with open(os.path.join(google_result_txt_path), "w", encoding='utf-8') as file:
            file.write(all_output)
        return google_result_txt_path

    google_result_txt_path_list = []

    if n_channel == 1:
        google_result_txt_path_list.append(write_to_txt(0, all_output))

    else:
        google_result_txt_path_list.append(write_to_txt(1, all_output))
        google_result_txt_path_list.append(write_to_txt(2, all_output))

    logging.info("Got Google result")
    return google_result_txt_path_list


def compare(audio_file, output_dir, voicegain_result_txt_path_list, google_result_txt_path_list, n_channel):

    if (voicegain_result_txt_path_list and len(voicegain_result_txt_path_list) != n_channel) or \
            (google_result_txt_path_list and len(google_result_txt_path_list) != n_channel):
        logging.warning("number of results do not match n_channl")
        return

    # check whether we have reference file
    file_dir, base_name = os.path.split(audio_file)
    base_name_without_ext, _ = os.path.splitext(base_name)

    def run_compare(is_left_channel):
        if is_left_channel is True:
            channel_ind = 0
        elif is_left_channel is False:
            channel_ind = 1
        else:
            channel_ind = 0

        ext = get_ext_from_channel(is_left_channel)

        reference_path = os.path.join(file_dir, "{}-reference{}.txt".format(base_name_without_ext, ext))

        output_path_list = []
        if os.path.exists(reference_path):
            logging.info("Reference file exist")
            output_path_list.append(voicegain_result_txt_path_list[channel_ind])
            if google_result_txt_path_list:
                output_path_list.append(google_result_txt_path_list[channel_ind])
                logging.info("Compare reference with Voicegain and Google result")
            else:
                logging.info("Compare reference with Voicegain result")
        else:
            reference_path = voicegain_result_txt_path_list[channel_ind]
            if not google_result_txt_path_list:
                logging.info("Do not compare, because we only have Voicegain result")
            else:
                output_path_list.append(google_result_txt_path_list[channel_ind])
                logging.info("Compare Google result with Voicegain result, using Voicegain as reference")

        if not output_path_list:
            return

        output_html_path = os.path.join(output_dir, "{}{}.html".format(base_name_without_ext, ext))

        run_transcription_compare(reference_path, output_path_list, output_html_path)

    if n_channel == 1:
        logging.info("compare mono audio")
        run_compare(None)
    else:
        logging.info("compare left channel")
        run_compare(True)
        logging.info("compare right channel")
        run_compare(False)


def run_transcription_compare(reference_path, output_file_list, output_html_path):
    logging.info("Start to compare results")

    with open(reference_path, "r", encoding='utf-8') as reference_file:
        reference_text = reference_file.read()

    calculator = UKKLevenshteinDistanceCalculator(
        tokenizer=WordTokenizer(),
        get_alignment_result=True,
        local_optimizers=[DigitUtil(process_output_digit=True), LocalCerOptimizer()]
    )

    output_all = dict()  # (output identifier -> output string)
    for output_path in output_file_list:
        with open(output_path, "r", encoding='utf-8') as output_file:
            output_text = output_file.read()
        output_path_name = os.path.basename(output_path)
        output_all[output_path_name] = output_text
    logging.info("Finish reading all results")

    output_results = dict()  # (output_identifier -> output_string)
    for (key, value) in output_all.items():
        logging.info("Start to process {}".format(key))
        output_results[key] = calculator.get_distance(reference_text, value,
                                                      brackets_list=["[]", "()", "<>"],
                                                      to_lower=True,
                                                      remove_punctuation=True,
                                                      use_alternative_spelling=True)

    logging.info("Merge all results into one HTML")
    calculator_local = UKKLevenshteinDistanceCalculator(
                tokenizer=CharacterTokenizer(),
                get_alignment_result=False)

    result = MultiResult(output_results, calculator_local)
    s = result.to_html()

    with open(output_html_path, 'w') as f:
        f.write(s)


def process_one_audio(recognizer_queue):
    while True:
        item = recognizer_queue.get()
        if item is None:
            logging.info("Get None in transcribe queue")
            break
        audio_file, output_dir, voicegain_api_client, google_api_client, google_model = item

        logging.info("Start to process audio {}".format(audio_file))

        with wave.open(audio_file, mode='rb') as wavread:
            sample_rate_hertz = wavread.getframerate()
            logging.info("audio sample rate: {}".format(sample_rate_hertz))
            n_channel = wavread.getnchannels()
            logging.info("n_channels: {}".format(n_channel))

        if n_channel not in {1, 2}:
            logging.warning("We only support mono / stereo audio, get {} channels".format(n_channel))
            continue

        # voicegain
        voicegain_result_txt_path_list = run_voicegain_recognizer(
            audio_file, output_dir, voicegain_api_client, n_channel)
        # google
        try:
            google_result_txt_path_list = run_google_recognizer(
                audio_file, output_dir, google_api_client, n_channel, sample_rate_hertz, google_model)
        except Exception as e:
            logging.warning(e)
            google_result_txt_path_list = None
        # compare
        compare(audio_file, output_dir, voicegain_result_txt_path_list, google_result_txt_path_list, n_channel)

        recognizer_queue.task_done()


def main():
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO, stream=sys.stdout)
    if len(sys.argv) < 4:
        print_help()
        return

    # required
    JWT = sys.argv[1]

    configuration = Configuration()
    # configuration.host = "https://api.ascalon.ai/v1"
    configuration.access_token = JWT
    voicegain_api_client = ApiClient(configuration=configuration)

    input_dir = sys.argv[2]
    output_dir = sys.argv[3]

    # optional
    len_of_argv = len(sys.argv)
    if len_of_argv > 4:
        google_api_cred = sys.argv[4]
        google_creds = service_account.Credentials.from_service_account_file(google_api_cred)
        google_client = speech.SpeechClient(credentials=google_creds)

        if len_of_argv == 6:
            google_model = sys.argv[5]
            if google_model == "default":
                logging.info("Using 'default' model for Google recognizer")
            elif google_model == "video":
                logging.info("Using 'video' model for Google recognizer")
            else:
                logging.info("Using 'phone_call' model for Google recognizer")
        else:
            google_model = "default"
            logging.info("Using 'default' model for Google recognizer")


    else:
        # google_api_cred = None
        google_client = None
        google_model = None

    recognizer_queue = MultiThreadQueue()

    recognizer_threads = []
    for i in range(THREAD_NUMBER):
        transcribe_thread = threading.Thread(target=process_one_audio, args=(recognizer_queue,))
        transcribe_thread.start()
        recognizer_threads.append(transcribe_thread)

    # get all audio file in input path
    audio_files = get_all_audio_file_in_input_dir(input_dir)
    logging.info("In total, we have {} files".format(len(audio_files)))
    for audio_file in audio_files:
        # process_one_audio(audio_file, output_dir, voicegain_api_client, google_client)
        recognizer_queue.put((audio_file, output_dir, voicegain_api_client, google_client, google_model))

    recognizer_queue.join()

    for i in range(THREAD_NUMBER):
        recognizer_queue.put(None)

    for thread in recognizer_threads:
        thread.join()


if __name__ == '__main__':
    main()
