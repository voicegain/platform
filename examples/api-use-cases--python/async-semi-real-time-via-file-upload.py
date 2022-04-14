import requests, time, os, json, re

WEB_API_URL = "http://<your edge IP>:31680/ascalon-web-api"  # <-= "http://<your edge IP address>:31680/ascalon-web-api"
#WEB_API_URL = "https://api.voicegain.ai/v1"  # <-= Voicegain Cloud
JWT =           "<Your JWT here>"   # <-= put here the JWT token obtained from the Web Console (https://console.voicegain.ai) or your Edge console
audio_path =   "radio-talk.wav"    # <-= your audio file name here
audio_type =    "audio/wav"         # <-= mime type of your audio if not WAV


audio_basename = os.path.basename(audio_path)

headers = {"Authorization":JWT}
data_url = WEB_API_URL + "/data/file?transcode=enable"

data_body = {
    "name" : re.sub("[^A-Za-z0-9]+", "-", audio_basename),
    "description" : audio_basename,
    "contentType" : audio_type,
    "tags" : ["test"]
}

multipart_form_data = {
    'file': (audio_basename, open(audio_path, 'rb'), audio_type),
    'objectdata': (None, json.dumps(data_body), "application/json")
}
print("uploading audio data ...", flush=True)
data_response = requests.post(data_url, files=multipart_form_data, headers=headers).json()
print("data response: {}".format(data_response), flush=True)
object_id = data_response["objectId"]
print("objectId: {}".format(object_id), flush=True)


asr_body = {
    "sessions": [
        {
            "asyncMode": "SEMI-REAL-TIME",
            "poll": {
                "afterlife": 60000,
                "persist": 60000
            },
            "content": {
                "incremental": ["progress"],
                "full" : ["transcript", "words"]
            }
        }
    ],
    "audio":{
        "source": {
            "dataStore": {
                "uuid": object_id
            }
        }
    },
    "settings" : {
        "asr" :{
            "noInputTimeout" : 15000,
            "completeTimeout" : -1

        }
    }
}


print("making asr request ...", flush=True)
asr_response = requests.post(WEB_API_URL + "/asr/transcribe/async", json=asr_body, headers=headers).json()
if(asr_response.get("sessions") is None):
    print(asr_response)
    exit()

session_id = asr_response["sessions"][0]["sessionId"]
polling_url = asr_response["sessions"][0]["poll"]["url"]

print("sessionId: {}".format(session_id), flush=True)
print(" poll.url: {}".format(polling_url), flush=True)

output_path = "output"
if not os.path.exists(output_path):
    os.mkdir(output_path)

while True:
    time.sleep(2)
    poll_response = requests.get(polling_url+"?full=false", headers=headers).json()
    phase = poll_response["progress"]["phase"]
    is_final = False
    result = poll_response.get("result")
    if result and result.get("final"):
        is_final = True
    print("Phase: {} Final: {}".format(phase, is_final), flush=True)

    if is_final:
        break

txt_url = polling_url+"/transcript?format=text"
print("Retrieving transcript using url: {}".format(txt_url), flush=True)
txt_response = requests.get(txt_url, headers=headers)
transcript_text_path = os.path.join(output_path, "{}.txt".format(session_id))
with open(transcript_text_path, 'w') as file_object:
    file_object.write(txt_response.text)
print("Save final transcript text to {}".format(transcript_text_path), flush=True)

