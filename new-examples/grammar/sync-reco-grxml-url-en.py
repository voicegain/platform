"""
pip install ffmpy
"""
## using ffmpeg to convert audio files to 16-bit 8kHz or 16kHz mono PCM needed for synchronous ASR recognition
from ffmpy import FFmpeg
import requests, time, os, json, re, base64

import configparser

cfg = configparser.ConfigParser()
cfg.read("config.ini")
configSection = cfg.get("DEFAULT", "CONFIG")
protocol = cfg.get(configSection, "PROTOCOL")
hostPort = cfg.get(configSection, "HOSTPORT")
JWT = cfg.get(configSection, "JWT")
urlPrefix = cfg.get(configSection, "URLPREFIX")

## specify here the directory with input audio files to test
input_path = cfg.get("DEFAULT", "INPUTFOLDER")
output_path = cfg.get("DEFAULT", "OUTPUTFOLDER")
temp_path = output_path+"/temp"

sampleRate = 8000

## BTW, for synchronous recognition the model latency is not important

## rho is the fastest (lowest latency) but least accurate
#acousticModelRealTime = "VoiceGain-rho"

## intermediate model
#acousticModelRealTime = "VoiceGain-rho-en-us"

## kappa is most accurate byt also has the longest latency
acousticModelRealTime = "VoiceGain-kappa"

headers = {"Authorization":JWT}


## this script will create two subdirectories
## 1) temp for transcoded audio files
## 2) output for the output (output is also written to stdout)


## GRXML grammar downloaded from a URL
asr_body = {
    "audio":{
        "source": {
            "inline": {
                "data": "to be filled later"
            }
        },
        "format" : "L16",
        "rate" : sampleRate,
        "channels" : "mono"
    },
    "settings": {
        "asr": {
            "acousticModelNonRealTime" : acousticModelRealTime,
            "grammars" : [
                {
                    "type": "GRXML",
                    "name" : "persons",
                    "fromUrl":{
                        # "url" : "https://s3.us-east-2.amazonaws.com/files.public.voicegain.ai/zip_code_no_refs.grxml"
                        # "url" : "https://grammar.host/zip_code_no_refs.grxml"
                        # "url" : "https://raw.githubusercontent.com/voicegain/platform/master/examples/grammars/grxml/member_id_type_1.grxml"
                        # "url" : "https://raw.githubusercontent.com/voicegain/platform/master/examples/grammars/grxml/taxonomy.grxml"
                        # "url" : "https://raw.githubusercontent.com/voicegain/platform/master/new-examples/grammar/grxml/zip_code_no_refs3.grxml"
                        # "url" : "https://support.voicegain.ai/hc/en-us/article_attachments/360062920832"
                        # "url" : "https://raw.githubusercontent.com/voicegain/platform/master/new-examples/grammar/grxml/person_dir_large.grxml"
                        # "url" : "https://raw.githubusercontent.com/TrevorIPI/special-octo-guide/refs/heads/main/transcribe2.grxml"
                        # "url" : "https://s3.us-east-2.amazonaws.com/files.public.voicegain.ai/mystery.grxml"
                        # "url" : "https://raw.githubusercontent.com/voicegain/platform/master/new-examples/grammar/grxml/emergency-1.grxml"
                        "url" : "https://raw.githubusercontent.com/voicegain/platform/master/new-examples/grammar/grxml/help.grxml"
                    }
                }
            ],
            "noInputTimeout": 6000,
            "completeTimeout": 2000,
            "incompleteTimeout" : 5000,
            "sensitivity" : 0.5,
            "speedVsAccuracy" : 0.9,
            "maxAlternatives" : 5,
            "confidenceThreshold" : 0.0001 
            , "languages" : ["en"]			
        }
        #,"formatters" : [{"type" : "digits"}]
    }
}


if not os.path.exists(output_path):
    os.mkdir(output_path)

## use to store transcoded input files
if not os.path.exists(temp_path):
    os.mkdir(temp_path)

results = {}

audio_type = "audio/wav"

output_path = output_path+"/output-{}".format(time.strftime("%Y-%m-%d_%H-%M-%S"))
if not os.path.exists(output_path):
    os.mkdir(output_path)



def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles

def process_one_file(audio_fname):

    path, fname = os.path.split(audio_fname)

    print("Processing {}/{}".format(path,fname), flush=True)

    global results

    ## convert audio file to 16-bit 8 or 16kHz PCM
    conv_fname = temp_path+"/{}.wav".format(fname)
    ff = FFmpeg(
        inputs={audio_fname: []},
        outputs={conv_fname : ['-ar', str(sampleRate), '-f', 's16le', '-y']}#, '-map_channel', '0.0.0']}
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
    url = "{}://{}/{}/asr/recognize".format(protocol, hostPort, urlPrefix)
    print(f"making POST request to {url}", flush=True)
    # print(f"body: {asr_body}", flush=True)

    asr_response_raw = requests.post(url, json=asr_body, headers=headers)

    if(asr_response_raw.status_code != 200):
        print(asr_response_raw.status_code)
        print(asr_response_raw.text)
        exit(-1)

    asr_response = asr_response_raw.json()
    print(asr_response)

    if(asr_response.get("result") is None):
        print(asr_response)
    else:
        alternatives = asr_response.get("result").get("alternatives")
        print(str(alternatives), flush=True)
        results[fname] = alternatives

    
  


## MAIN ##

print("START", flush=True)

list_of_files = getListOfFiles(input_path)

print("files to test")
for name in list_of_files:
    print(name)

numProcessed = 0
for name in list_of_files:
    process_one_file(name)
    numProcessed = numProcessed+1
#    if(numProcessed > 5):
#        break

output_path = output_path+"/english-grxml-grammar"
if not os.path.exists(output_path):
    os.mkdir(output_path)

transcript_text_path = os.path.join(output_path, "{}.txt".format(time.strftime("%Y-%m-%d_%H-%M-%S")))
with open(transcript_text_path, 'w') as file_object:
	for name in results:
		print(name)
		alts = results.get(name)
		if(alts is not None):
			#print("\t"+str(alts))
			for alt in alts:
				print("\tutt: >{}< tag: {} conf: {}".format(alt.get("utterance"), alt.get("literalTag"), alt.get("confidence")))
				file_object.write("{}\tutt: >{}<\ttag: {}\tconf: {}\n".format(name, alt.get("utterance"), alt.get("literalTag"), alt.get("confidence")))

print("Output stored in: {}".format(transcript_text_path))
print("THE END", flush=True)