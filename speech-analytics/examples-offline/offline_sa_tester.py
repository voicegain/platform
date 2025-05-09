from ascalon_web_api_internal_client import ApiClient, Configuration, SaOfflineApi, DataApi, SaApi, SaInternalApi, OfflineSpeechAnalyticsCoreResultResponse
import logging
import sys
import time
logging.basicConfig(format='%(thread)s:%(asctime)s %(levelname)s:%(message)s', level=logging.INFO, stream=sys.stdout)

JWT = "<JWT>"
WEB_API_URL = "https://api.ascalon.ai/v1"

configuration = Configuration()
configuration.access_token = JWT
configuration.host = WEB_API_URL


api_client = ApiClient(configuration=configuration)
sa_offline_api = SaOfflineApi(api_client)
sa_api = SaApi(api_client)
sa_internal_api = SaInternalApi(api_client)
data_api = DataApi(api_client)


def get_data_object():
    AUDIO_FILE_PATH = "wtB41-stereo.wav"

    data_object = data_api.data_file_post(
        reuse=False,
        file=AUDIO_FILE_PATH
    )
    object_id = data_object.object_id
    logging.info("Upload file {} to {}".format(AUDIO_FILE_PATH, object_id))
    return object_id


object_id = get_data_object()
# object_id = "4e0f5422-7fb5-496e-bee2-98e627e22a16"
# object_id = "8d59baad-3985-467a-8a5c-0f087074dd9a"  # stereo
# object_id = "3a00bde5-afca-4ff4-adf3-2567ae5d7c45"  # better stereo


def create_sa_config():
    sa_config = {
        "name": "kuo-test-sa-04182025-v2",
        "entities": ["PERSON"],
        "keywords": [
            {
                "tag": "keyword-hi",
                "examples": [
                    {
                        "phrase": "hi"
                    }
                ]
            },
            {
                "tag": "keyword-bye",
                "examples": [
                    {
                        "phrase": "bye"
                    }
                ]
            }
        ],
        "phrases": [
            {
                "tag": "phrase-radio-service",
                "advancedRegex": [
                    {
                        "positiveRule": "radio service"
                    }
                ]
            }
        ],
        "criteria": [
            {
                "tag": "hi-and-bye",
                "requiredSubCriteria": [
                    {
                        "keywords": ["keyword-hi"]
                    },
                    {
                        "keywords": ["keyword-bye"]
                    }
                ]
            },
            {
                "tag": "regex-radio",
                "requiredSubCriteria": [
                    {
                        "regex": ["radio"]
                    }
                ]
            }
        ],
        "wordCloud": True,
        "profanity": True,
        "sentiment": True,
        "summary": True,
        "moods": ["neutral", "anger", "happiness", "sadness", "surprise"]

    }
    sa_config_result = sa_api.sa_config_post(
        speech_analytics_config=sa_config
    )
    sa_conf_id = sa_config_result.sa_conf_id
    print(sa_conf_id)
    return sa_conf_id


def create_sa_config_phrase():
    sa_config = {
        "name": "kuo-test-sa-01282025-es-4",
        "phrases": [
            {
                "tag": "ask-first-last-name",
                "examples": [
                    {
                        "sentence": "Se les ha llamado de muchas formas."
                        # "sentence": "Can you tell me your first and last name?"
                    }
                ]
            }
        ],
        "sentiment": True
    }
    sa_config_result = sa_api.sa_config_post(
        speech_analytics_config=sa_config
    )
    sa_conf_id = sa_config_result.sa_conf_id
    print(sa_conf_id)
    return sa_conf_id


# sa_conf_id = create_sa_config_phrase()
# sa_conf_id = "XpdPlMKll0u6ASUcTe02"
# sa_conf_id = "rE0g2gAyeB5DYma0X0EM"  # without criteria
# sa_conf_id = "UGwPcCVRpdIaejBMZNUK"  # with moods
# sa_conf_id = "28j0OJA8zNEK4fYYoM3X" # with summary
# sa_conf_id = "wMsr94B8nh0sJHaHcTFG"  # kuo-test-sa-01282025-en
# sa_conf_id = "FDm6J5HjS6h76jm0S1wo"  # kuo-test-sa-01282025-es
# sa_conf_id = "nBvjHGtOELZ4oVcjPpgq"
# sa_conf_id = create_sa_config()
sa_conf_id = "ix9BkpKoFvV8BWd1dcJe"  # kuo-test-sa-04182025-v2

def create_call_review_config():
    call_review_config = {
        "name": "kuo-llm-call-review-config-05012025",
        "sections": [
            {
                "sectionName": "S1",
                "questions": [
                    {
                        "question": "S1Q1",
                        "llm": {
                            "prompt": "Is this call a customer service call?",
                            "responseFormat": "yesNo"
                        },
                        "autopopulated": [
                            {
                                "answerValue": 2,
                                "criterion": "regex-radio"
                            }
                        ]
                    },
                    {
                        "question": "S1Q2",
                        "autopopulated": [
                            {
                                "answerValue": 2,
                                "criterion": "regex-radio"
                            }
                        ]
                    }
                ]
            },
            {
                "sectionName": "S2",
                "questions": [
                    {
                        "question": "S2Q1",
                        "llm": {
                            "prompt": "How polite is the agent?",
                            "responseFormat": "score1to10"
                        },
                    }
                ]
            }
        ]
    }
    response = sa_internal_api.sa_call_review_config_post(
        call_review_config_modifiable=call_review_config
    )
    cr_config_id = response.cr_config_id
    print(cr_config_id)
    return cr_config_id


call_review_config_id = "phlGYPcmMkuMdkIhZjcU"
# call_review_config_id = create_call_review_config()


def get_sa_id():
    # make offline SA request
    # offline_sa_request = {
    #     "label": "kuo-test-{}".format(int(time.time())),
    #     "saConfig": sa_conf_id,
    #     # "callReviewConfig": call_review_config_id,
    #     "audio": [
    #         {
    #             "source": {
    #                 "dataObjectUuid": object_id
    #             },
    #             "diarization": {
    #                 "minSpeakers": 2,
    #                 "maxSpeakers": 2
    #             },
    #             "audioChannelSelector": "left",
    #             # "audioOffset": 10000,
    #             # "speakers": [1001]
    #         },
    #         {
    #             "source": {
    #                 "dataObjectUuid": object_id
    #             },
    #             "audioChannelSelector": "right",
    #             # "speakers": [1002]
    #         }
    #     ],
    #     # "speakers": [
    #     #     {
    #     #         "spkUserId": 1001,
    #     #         # "isAgent": True
    #     #     },
    #     #     {
    #     #         "spkUserId": 1002,
    #     #         # "isAgent": False
    #     #     }
    #     # ]
    #     # "settings": {
    #     #     "asr": {
    #     #     }
    #     # }
    # }

    offline_sa_request = {
        "label": "kuo-test-{}".format(int(time.time())),
        "saConfig": sa_conf_id,
        "callReviewConfig": call_review_config_id,
        "audio": [
            {
                "source": {
                    "dataObjectUuid": object_id
                },
                "audioChannelSelector": "left",
            },
            {
                "source": {
                    "dataObjectUuid": object_id
                },
                "audioChannelSelector": "right",
            }
        ],
        "settings": {
            "formatters": [
                {"type": "redact", "parameters": {"CC": "partial"}}
            ],
            "asr": {
                "acousticModel": "whisper",
                "languages": ["en"]
            }
        },
        # "optimizeForWebUi": "level2"
    }

    offline_sa_init_response = sa_offline_api.sa_offline_post(
        offline_speech_analytics_request=offline_sa_request
    )
    print(offline_sa_init_response)
    return offline_sa_init_response.sa_session_id


sa_session_id = get_sa_id()
# sa_session_id = "eYBHiMmAuTMD0yMcrXez"
print(sa_session_id)
#

def get_sa_session(session_id):
    result = sa_offline_api.sa_offline_get(sa_session_id=session_id)
    return result

for i in range(50):
    result = get_sa_session(sa_session_id)
    print(result)
    if result.progress and result.progress.phase == "DONE":
        break
    time.sleep(1)

result = sa_offline_api.sa_offline_get_data(sa_session_id=sa_session_id, words=True, summary=True)
print(result)

# get_sa_session(sa_session_id)
#
# async_response_session = async_transcribe_init_response.sessions[0]
# session_id = async_response_session.session_id
#
#
# class ResultTracker:
#     def __init__(self, start_time):
#         self.start_time = start_time
#         logging.info("start time: {}".format(start_time))
#         self.total_processed_audio_s = 0
#         self.total_process_time = 0
#         self.lock = threading.Lock()
#
#     def correct_start_time(self):
#         self.start_time = (self.start_time + time.time()) / 2
#         logging.info("Change the start time to {}".format(self.start_time))
#
#     def track(self, session_id, session_start_time, session_end_time, process):
#         with self.lock:
#             d = session_end_time - session_start_time
#             logging.debug("session {} take {}s to process, rate: {}".format(session_id, d, process/d))
#             self.total_processed_audio_s += process
#             self.total_process_time += d
#             current_time = time.time()
#             total_time = current_time - self.start_time
#
#             is_full_load = (total_time < TOTAL_SECONDS)
#             logging.info("[Full load: {}] Processed {}s audio in {}s. Rate: {} . Total processing time is {}s, Rate: {}".format(
#                 is_full_load, self.total_processed_audio_s, total_time, self.total_processed_audio_s / total_time,
#                 self.total_process_time, self.total_processed_audio_s / self.total_process_time
#             ))
#
#
# class Task:
#     def __init__(self, session_id, result_tracker, duration):
#         logging.debug("Created session: {}. File duration: {}s".format(session_id, duration))
#         self.session_id = session_id
#         self.duration = duration
#         self.result_tracker = result_tracker
#         self.start_time = time.time()
#
#     def is_done(self):
#         poll_response = transcribe_api.asr_transcribe_async_get(
#             session_id=self.session_id,
#             full=True
#         )
#         poll_response_result = poll_response.result
#
#         if poll_response_result.final:
#             logging.debug("Get final result on session : {}".format(self.session_id))
#             transcript = poll_response_result.transcript.lower()
#             print(transcript)
#             print(poll_response_result)
#             ##### debug print ############
#             # words = poll_response_result.words
#             # channel_count = dict()
#             # for word in words:
#             #     spk = word.spk
#             #     if spk not in channel_count:
#             #         channel_count[spk] = 0
#             #     print("[spk {}] ({}) {}".format(spk, channel_count[spk], word.utterance))
#             #     channel_count[spk] += 1
#             # words = poll_response_result.words
#             # current_spk = None
#             # current_words = []
#             # for word in words:
#             #     spk = word.spk
#             #     if spk != current_spk:
#             #         if current_words:
#             #             print("[spk {}] {}".format(current_spk, " ".join([x.utterance for x in current_words])))
#             #         current_spk = spk
#             #         current_words.clear()
#             #     current_words.append(word)
#             # if current_words:
#             #     print("[spk {}] {}".format(current_spk, " ".join([x.utterance for x in current_words])))
#             ########
#             # print(poll_response_result.transcript)
#             # if (not transcript.startswith("hi")) or (not (transcript.endswith("bye.") or transcript.endswith("bye") or transcript.endswith("right."))):
#             #     logging.warning("Get bad transcript on session {} : {}".format(
#             #         self.session_id, transcript
#             #     ))
#             self.result_tracker.track(self.session_id, self.start_time, time.time(), self.duration)
#             return True
#         else:
#             # logging.info("Not get to final on session: {}".format(self.session_id))
#             return False
#
#
# def start_transcribe(start_time, result_tracker):
#     logging.info("Start new thread")
#     while time.time() - start_time < TOTAL_SECONDS:
#         new_task = create_new_task(result_tracker)
#         current_time = time.time()
#         while True:
#             sleep_time = GAP_SECONDS - (time.time() - current_time)
#             if sleep_time > 0:
#                 # logging.info("Sleep {}s".format(sleep_time))
#                 time.sleep(sleep_time)
#             else:
#                 pass
#                 # logging.info("Do not sleep, {}s delay".format(-sleep_time))
#             current_time = time.time()
#
#             if new_task.is_done():
#                 break
#
#
# def create_new_task(result_tracker):
#     file_path, duration, base64_encoded, object_id = random.choice(AUDIO_FILES)
#
#     async_transcription_request = {
#         "sessions": [
#             {
#                 "asyncMode": "OFF-LINE",
#                 "poll": {
#                     "afterlife": 60000,
#                     "persist": 0
#                 },
#                 "audioChannelSelector": "two-channel",
#                 # "callback": {
#                 #     "uri": "https://j85rosrub4.execute-api.us-east-2.amazonaws.com/default/AsrCallback"
#                 # },
#                 "content": {
#                     "full": ["progress", "words", "transcript"]
#                 },
#                 # "vadMode": "disabled"
#             }
#         ],
#         "audio": {
#             "source": {
#                 "dataStore": {
#                     "uuid": object_id
#                 }
#                 # "fromUrl": {
#                 #     "url": "https://s3.us-east-2.amazonaws.com/files.public.voicegain.ai/6m-stereo.wav"
#                 # }
#             }
#         },
#         "settings": {
#             "asr": {
#                 # "acousticModelNonRealTime": "whisper"
#                 # "languages": ["es"],
#                 # "acousticModelNonRealTime": "VoiceGain-omega-x",
#                 # "speedVsAccuracy": 0
#                 # "diarization": {
#                 #     "minSpeakers": 2,
#                 #     "maxSpeakers": 2
#                 # }
#             },
#             # "formatters": [
#             #     # {"type": "basic", "parameters" : {"enabled" : False}}
#             #     {"type": "digits"},
#             #     {
#             #         "type": "enhanced",
#             #         "parameters": {"URL": True, "EMAIL": True, "SSN": True, "PHONE": True, "CC": True}
#             #     },
#             #     {
#             #         "type": "redact",
#             #         "parameters": {"EMAIL": "full", "SSN": "full", "PHONE": "full", "CC": "full"}
#             #     }
#             # ]
#         }
#     }
#
#     if DIARIZATION:
#         async_transcription_request["settings"] = {
#             "asr": {
#                 "diarization": {
#                     "minSpeakers": 2,
#                     "maxSpeakers": 2
#                 }
#             },
#             "formatters": [
#                 {"type": "digits"}
#             ]
#         }
#     logging.debug("make request")
#     async_transcribe_init_response = transcribe_api.asr_transcribe_async_post(
#         async_transcription_request=async_transcription_request
#     )
#     logging.debug("get response")
#
#     # print(async_transcribe_init_response)
#
#     async_response_session = async_transcribe_init_response.sessions[0]
#     session_id = async_response_session.session_id
#     return Task(session_id, result_tracker, duration)
#
#
# def main():
#     start_time = time.time()
#     result_tracker = ResultTracker(start_time)
#     transcribe_start_threads = []
#
#     for i in range(CONCURRENT_THREAD):
#         transcribe_start_thread = threading.Thread(target=start_transcribe,
#                                                    args=(start_time, result_tracker,))
#         transcribe_start_thread.start()
#         transcribe_start_threads.append(transcribe_start_thread)
#         time.sleep(0.2)
#     result_tracker.correct_start_time()
#
#     logging.info("Start thread join")
#     for t in transcribe_start_threads:
#         t.join()
#     logging.info("Thread join is done")
#
#
# if __name__ == '__main__':
#     """
#     """
#     main()
