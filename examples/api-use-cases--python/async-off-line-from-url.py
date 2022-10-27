'''
pip install requests
'''
import requests, time, os, json

platform= "voicegain"
JWT = "<put your JWT here - get it from https://console.voicegain.ai>"
#audio_url = "https://s3.us-east-2.amazonaws.com/files.public.voicegain.ai/3sec.wav"
audio_url = "https://s3.us-east-2.amazonaws.com/files.public.voicegain.ai/radio-talk.wav"

headers = {"Authorization":JWT}
body = {
    "sessions": [
        {
            "asyncMode": "OFF-LINE",
            "poll": {
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
            "fromUrl": {
                "url": audio_url
            }
        }
    }
}

init_response = requests.post("https://api.{}.ai/v1/asr/transcribe/async".format(platform), json=body, headers=headers).json()
session_id = init_response["sessions"][0]["sessionId"]
polling_url = init_response["sessions"][0]["poll"]["url"]

print("sessionId: {}".format(session_id), flush=True)
print(" poll.url: {}".format(polling_url), flush=True)

output_path = "output"
if not os.path.exists(output_path):
    os.mkdir(output_path)

index = 0
while True:
    time.sleep(4.9)
    poll_response = requests.get(polling_url+"?full=false", headers=headers).json()
    # write poll_response to JSON
    poll_response_path = os.path.join(output_path, "{}--{}.json".format(session_id, index))
    with open(poll_response_path, 'w') as outfile:
        json.dump(poll_response, outfile)
    print("Save intermediate result to {}".format(poll_response_path), flush=True)

    is_final = poll_response["result"]["final"]
    index += 1
    if is_final:
        break

poll_response = requests.get(polling_url+"?full=true", headers=headers).json()
# write poll_response to JSON
poll_response_path = os.path.join(output_path, "{}--{}.json".format(session_id, index))
with open(poll_response_path, 'w') as outfile:
    json.dump(poll_response, outfile)
print("Save final result to {}".format(poll_response_path), flush=True)

# extract trascript text from final result

tr_text = poll_response["result"]["transcript"];

print("transcript text: {}".format(tr_text), flush=True)
tr_text_path = os.path.join(output_path, "{}--transcript.txt".format(session_id))
with open(tr_text_path, 'w') as outfile:
    outfile.write(tr_text)
print("Save final transcript text to {}".format(tr_text_path), flush=True)


# [OPTIONAL] get result as text file divided into paragraphs (optional timestamps)

txt_url = "https://api.{}.ai/v1/asr/transcribe/{}/transcript?format=text".format(platform, session_id)
print("Retrieving transcript using url: {}".format(txt_url), flush=True)
txt_response = requests.get(txt_url, headers=headers)
transcript_text_path = os.path.join(output_path, "{}.txt".format(session_id))
with open(transcript_text_path, 'w') as file_object:
    file_object.write(txt_response.text)
print("Save final transcript to {}".format(transcript_text_path), flush=True)
