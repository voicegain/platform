import requests, time, os, json

JWT = "<Your JWT here>"
headers = {"Authorization":JWT}
audio_url = "https://s3.us-east-2.amazonaws.com/files.public.voicegain.ai/3sec.wav"
body = {
    "sessions": [
        {
            "asyncMode": "OFF-LINE",
            "poll": {
                "afterlife": 60000,
                "persist": 86400000
            },
            "content": {
                "incremental": ["progress"],
                "full" : ["transcript", "words"]
            }
        }
    ],
    "audio":{
        "source": {
            "fromUrl": {
                "url": audio_url
            }
        }
    }
}

init_response = requests.post("https://api.voicegain.ai/v1/asr/transcribe/async", json=body, headers=headers).json()
session_id = init_response["sessions"][0]["sessionId"]
polling_url = init_response["sessions"][0]["poll"]["url"]

print("sessionId: {}".format(session_id))
print(" poll.url: {}".format(polling_url))

output_path = "output"
if not os.path.exists(output_path):
    os.mkdir(output_path)

index = 0
while True:
    time.sleep(0.99)
    poll_response = requests.get(polling_url+"?full=false", headers=headers).json()
    # write poll_response to JSON
    poll_response_path = os.path.join(output_path, "{}--{}.json".format(session_id, index))
    with open(poll_response_path, 'w') as outfile:
        json.dump(poll_response, outfile)
    print("Save result to {}".format(poll_response_path))

    is_final = poll_response["result"]["final"]
    index += 1
    if is_final:
        break

poll_response = requests.get(polling_url+"?full=true", headers=headers).json()
# write poll_response to JSON
poll_response_path = os.path.join(output_path, "{}--{}.json".format(session_id, index))
with open(poll_response_path, 'w') as outfile:
    json.dump(poll_response, outfile)
print("Save final result to {}".format(poll_response_path))

# get result as text file

txt_url = "https://api.voicegain.ai/v1/asr/transcribe/"+session_id+"/transcript?format=text"
print("Retrieving transcript using url: {}".format(txt_url))
txt_response = requests.get(txt_url, headers=headers)
transcript_text_path = os.path.join(output_path, "{}.txt".format(session_id))
with open(transcript_text_path, 'w') as file_object:
    file_object.write(txt_response.text)
print("Save final transcript text to {}".format(transcript_text_path))
