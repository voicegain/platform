import requests, time, os, json, re


## specify here the directory with input audio files to test
input_path = "./my-mono-audio/"

spanish = False

#voicegain
host = "https://api.voicegain.ai/v1"
JWT = "< JWT token obtained from Web Console https://console.voicegain.ai >"

asr_body = {
    "sessions": [
        {
            "asyncMode": "OFF-LINE",
            "poll": {
                "afterlife": 60000,
                "persist": 120000
            },
            "content": {
                "incremental": ["progress"],
                "full" : ["words"]
            }
        }
    ],
    "audio":{
        "source": {
            "dataStore": {
                "uuid": "to be filled later"
            }
        }
    },
    "settings" : {
        "asr" : {
            "sensitivity" : 0.5,
            "speedVsAccuracy" : 0.5
        }
        , "formatters" : [{"type" : "digits"}]
    }
}

#### all settings above this line ####

if(spanish):
    asr_body["settings"]["asr"]["acousticModelNonRealTime"] = "VoiceGain-ol-es"

audio_type = "audio/wav"

output_path = "output-{}".format(time.strftime("%Y-%m-%d_%H-%M-%S"))

data_url = "{}/data/file?reuse=true&transcode=disable".format(host)

headers = {"Authorization":JWT}

def process_one_file(audio_fname):

    path, fname = os.path.split(audio_fname)

    print("Processing {}/{}".format(path,fname), flush=True)

    data_body = {
        "name" : re.sub("[^A-Za-z0-9]+", "-", fname),
        "description" : audio_fname,
        "contentType" : audio_type,
        "tags" : ["test"]
    }

    multipart_form_data = {
        'file': (audio_fname, open(audio_fname, 'rb'), audio_type),
        'objectdata': (None, json.dumps(data_body), "application/json")
    }
    print("uploading audio data {} ...".format(audio_fname), flush=True)
    data_response = None
    data_response_raw = None
    try:
        data_response_raw = requests.post(data_url, files=multipart_form_data, headers=headers)
        data_response = data_response_raw.json()
    except Exception as e:
        print(str(data_response_raw))
        exit() 

    print("data response: {}".format(data_response), flush=True)

    if data_response.get("status") is not None and data_response.get("status") == "BAD_REQUEST":
        print("error uploading file {}".format(audio_fname), flush=True)
        exit()

    object_id = data_response["objectId"]
    print("objectId: {}".format(object_id), flush=True)

    ## set the audio id in the asr request
    asr_body["audio"]["source"]["dataStore"]["uuid"] = object_id


    print("making asr request ...", flush=True)
    asr_response = requests.post("{}/asr/transcribe/async".format(host), json=asr_body, headers=headers).json()
    session_id = asr_response["sessions"][0]["sessionId"]
    polling_url = asr_response["sessions"][0]["poll"]["url"]

    print("sessionId: {}".format(session_id), flush=True)
    print(" poll.url: {}".format(polling_url), flush=True)

    
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    index = 0
    while True:
        if(index<5):
            time.sleep(0.3)
        else:
            time.sleep(4.9)
        poll_response = requests.get(polling_url+"?full=false", headers=headers).json()
        phase = poll_response["progress"]["phase"]
        is_final = poll_response["result"]["final"]
        print("Phase: {} Final: {}".format(phase, is_final), flush=True)
        # write poll_response to JSON
        # poll_response_path = os.path.join(output_path, "{}-{}-{}.json".format(audio_fname, session_id, index))
        # with open(poll_response_path, 'w') as outfile:
        #     json.dump(poll_response, outfile)
        # print("Phase: {} Final: {} -> Save result to {}".format(phase, is_final, poll_response_path), flush=True)

        index += 1
        if is_final:
            break

    # poll_response = requests.get(polling_url+"?full=true", headers=headers).json()
    # # write poll_response to JSON
    # poll_response_path = os.path.join(output_path, "{}--{}.json".format(session_id, index))
    # with open(poll_response_path, 'w') as outfile:
    #     json.dump(poll_response, outfile)
    # print("Save final result to {}".format(poll_response_path), flush=True)

    # get result as text file

    txt_url = "{}/asr/transcribe/{}/transcript?format=text".format(host, session_id)
    print("Retrieving transcript using url: {}".format(txt_url), flush=True)
    txt_response = requests.get(txt_url, headers=headers)
    transcript_text_path = os.path.join(output_path, "{}.txt".format(fname))
    with open(transcript_text_path, 'w') as file_object:
        file_object.write(txt_response.text)
    print("Save final transcript text to {}".format(transcript_text_path), flush=True)


## MAIN ##

print("START", flush=True)

list_of_files = []

for root, dirs, files in os.walk(input_path):
	for file in files:
		list_of_files.append(os.path.join(root,file))

print("files to test")
for name in list_of_files:
    print(name)

for name in list_of_files:
    process_one_file(name)

print("THE END", flush=True)
