import requests, time, os, json, re


platform =      "voicegain"
JWT =           "<Your JWT here>"   # <-= put here the JWT token obtained from the Web Console (https://console.voicegain.ai)
audio_fname =   "radio-talk.wav"    # <-= your audio file name here
audio_type =    "audio/wav"         # <-= mime type of your audio if not WAV



headers = {"Authorization":JWT}
data_url = "https://api.{}.ai/v1/data/file".format(platform)

data_body = {
    "name" : re.sub("[^A-Za-z0-9]+", "-", audio_fname),
    "description" : audio_fname,
    "contentType" : audio_type,
    "tags" : ["test"]
}

multipart_form_data = {
    'file': (audio_fname, open(audio_fname, 'rb'), audio_type),
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
            "asyncMode": "OFF-LINE",
            "poll": {
                "afterlife": 60000,
                "persist": 600000
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
    }
}


print("making asr request ...", flush=True)
asr_response = requests.post("https://api.{}.ai/v1/asr/transcribe/async".format(platform), json=asr_body, headers=headers).json()
session_id = asr_response["sessions"][0]["sessionId"]
polling_url = asr_response["sessions"][0]["poll"]["url"]

print("sessionId: {}".format(session_id), flush=True)
print(" poll.url: {}".format(polling_url), flush=True)

output_path = "output"
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
    # write poll_response to JSON
    poll_response_path = os.path.join(output_path, "{}--{}.json".format(session_id, index))
    with open(poll_response_path, 'w') as outfile:
        json.dump(poll_response, outfile)
    print("Phase: {} Final: {} -> Save result to {}".format(phase, is_final, poll_response_path), flush=True)

    index += 1
    if is_final:
        break

poll_response = requests.get(polling_url+"?full=true", headers=headers).json()
# write poll_response to JSON
poll_response_path = os.path.join(output_path, "{}--{}.json".format(session_id, index))
with open(poll_response_path, 'w') as outfile:
    json.dump(poll_response, outfile)
print("Save final result to {}".format(poll_response_path), flush=True)

# get result as text file

txt_url = "https://api.{}.ai/v1/asr/transcribe/{}/transcript?format=text&interval=30".format(platform, session_id)
print("Retrieving transcript using url: {}".format(txt_url), flush=True)
txt_response = requests.get(txt_url, headers=headers)
transcript_text_path = os.path.join(output_path, "{}.txt".format(session_id))
with open(transcript_text_path, 'w') as file_object:
    file_object.write(txt_response.text)
print("Save final transcript text to {}".format(transcript_text_path), flush=True)
