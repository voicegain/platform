"""
pip install ffmpy
"""
from ffmpy import FFmpeg
import requests, time, os, json, re, base64


## specify here the directory with input audio files to test
input_path = "./my-files/"

spanish = False

#voicegain
host = "https://api.voicegain.ai/v1"
JWT = "< your JWT token obtained from https://console.voicegain.ai >"

asr_body = {
    "audio":{
        "source": {
            "inline": {
                "data": "to be filled later"
            }
        },
        "format" : "L16",
        "rate" : 16000,
        "channels" : "mono"
    },
    "settings": {
        "asr": {
            "speechContext" : "normal",
            "noInputTimeout": -1,
            "completeTimeout": -1,
            "sensitivity" : 0.5,
            "speedVsAccuracy" : 0.5 
            #, "hints" : ["rupees:10", "Hyderabad:10", "lakh:10", "lakhs:10", "lakh_rupees", "Yen", "GB RAM", "MB RAM"]
            #, "langModel": "af1433a5-4e81-4df8-bf86-a48e0f409157"
        }
        #,"formatters" : [{"type" : "digits"}]
    }
}

#### all settings above this line ####

results = {}

if(spanish):
    asr_body["settings"]["asr"]["acousticModelNonRealTime"] = "VoiceGain-ol-es"

audio_type = "audio/wav"

output_path = "output-{}".format(time.strftime("%Y-%m-%d_%H-%M-%S"))

data_url = "{}/data/file?reuse=true&transcode=disable".format(host)

headers = {"Authorization":JWT}

def process_one_file(audio_fname):

    path, fname = os.path.split(audio_fname)

    print("Processing {}/{}".format(path,fname), flush=True)

    global results

    # convert file using FFMpeg (sync transcription does not support yet all the audio formats that are supported by async OFFLINE transcription)
    conv_fname = (audio_fname+'.wav').replace(input_path, "./")
    ff = FFmpeg(
        inputs={audio_fname: []},
        outputs={conv_fname : ['-ar', '16000', '-f', 's16le', '-y', '-map_channel', '0.0.0']}
    )
    ff.cmd
    ff.run()

    image = open(conv_fname, 'rb')
    image_read = image.read()
    image_64_encode = base64.b64encode(image_read) 

    #print('This is the image in base64: ' + str(image_64_encode))

    ## set the audio in the asr request
    asr_body["audio"]["source"]["inline"]["data"] = image_64_encode.decode("utf-8")


    print("making asr request ...", flush=True)
    asr_response = requests.post("{}/asr/transcribe".format(host), json=asr_body, headers=headers).json()

    if(asr_response.get("result") is None):
        print(asr_response)
    else:
        alternatives = asr_response.get("result").get("alternatives")
        print(str(alternatives), flush=True)
        results[fname] = alternatives

    
  


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

if not os.path.exists("output"):
    os.mkdir("output")
output_path = "output{}".format(input_path.replace("./", "/"))
if not os.path.exists(output_path):
    os.mkdir(output_path)

transcript_text_path = os.path.join(output_path, "{}.txt".format(time.strftime("%Y-%m-%d_%H-%M-%S")))
with open(transcript_text_path, 'w') as file_object:
    for name in results:
        print(name)
        file_object.write(name+"\n")
        alts = results.get(name)
        #print("\t"+str(alts))
        for alt in alts:
            print("\tutt: >{}<  conf: {}".format(alt.get("utterance"), alt.get("confidence")))
            file_object.write("\tutt: >{}<  conf: {}\n".format(alt.get("utterance"), alt.get("confidence")))

print("Output stored in: {}".format(transcript_text_path))
print("THE END", flush=True)