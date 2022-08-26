"""
pip install ffmpy
"""
import ffmpy
import requests, time, os, json, re, base64

# this script uses ffmepg to transcode files before submitting them for transcription

## specify here the directory with input audio files to test

# type 1 member ID
# input_path = "Recordings/Member ID"
# grammar_path = "grxml/member_id_type_1.grxml"

# type 2 member ID
# input_path = "Recordings/Member ID Type 2"
# grammar_path = "grxml/member_id_type_2.grxml"

# Taxonomy
input_path = "Recordings/Taxonomy"
grammar_path = "grxml/taxonomy.grxml"

## this script will create two subdirectories
## 1) temp for transcoded audio files
## 2) output for the output (output is also written to stdout)

## voicegain
host = "https://api.voicegain.ai/v1"
## credential
JWT = "<your JWT token here, you can get it from https://console.voicegain.ai>"




## read grammar and prepare it to be inlined bas64 encoded
with open(grammar_path, "rb") as gf:
    grammar_base64 = base64.b64encode(gf.read()).decode()

grammar_name = os.path.splitext(os.path.basename(grammar_path))[0]

## simple digit + yes/no grammar included inline
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
            "acousticModelRealTime": "VoiceGain-kappa",
            "acousticModelNonRealTime": "VoiceGain-kappa",
            "grammars": [
                {
                    "type": "GRXML",
                    "name": grammar_name,
                    "inline": {
                        "data": grammar_base64
                    }
                }
            ],
            "speechContext" : "normal",
            "noInputTimeout": 6000,
            "completeTimeout": 2000,
            "incompleteTimeout" : 5000,
            "sensitivity" : 0.5,
            "speedVsAccuracy" : 0.5,
            "maxAlternatives" : 5,
            "confidenceThreshold" : 0.0001
            , "languages" : ["en"]
        }
        #,"formatters" : [{"type" : "digits"}]
    }
}

#### all settings above this line ####

## use to store transcoded input files
if not os.path.exists("temp"):
    os.mkdir("temp")

results = {}

audio_type = "audio/wav"

output_path = "output-{}".format(time.strftime("%Y-%m-%d_%H-%M-%S"))

headers = {"Authorization":JWT}


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

    conv_fname = "temp/{}.wav".format(fname)
    ff = ffmpy.FFmpeg(
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
    asr_response_raw = requests.post("{}/asr/recognize".format(host), json=asr_body, headers=headers)
    print(asr_response_raw)
    if(asr_response_raw.status_code != 200):
        exit(-1)

    asr_response = asr_response_raw.json()
    # print(asr_response)

    if(asr_response.get("result") is None):
        print(asr_response)
    else:
        alternatives = asr_response.get("result").get("alternatives")
        print(str(alternatives), flush=True)
        results[fname] = alternatives

#######3######## M A I N ###################
def main():
    print("START", flush=True)

    list_of_files = getListOfFiles(input_path)

    print("files to test")
    for name in list_of_files:
        print(name)

    numProcessed = 0
    for name in list_of_files:
        process_one_file(name)
        numProcessed = numProcessed+1
   
    if not os.path.exists("output"):
        os.mkdir("output")
    output_path = "output{}".format("/english-grammar")
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    transcript_text_path = os.path.join(output_path, "{}.txt".format(time.strftime("%Y-%m-%d_%H-%M-%S")))
    with open(transcript_text_path, 'w') as file_object:
        for name in results:

            alts = results.get(name)
            reference = "".join(os.path.splitext(name)[0].split())
            print(name + "---" + reference)
            if alts is not None:
                # print("\t"+str(alts))
                for alt in alts:
                    result = alt.get("semanticTags")['result']
                    match = (result.lower() == reference.lower())

                    print("\tutt: >{}< ref: {} result: {} conf: {} match: {}".format(
                        alt.get("utterance"), reference, result, alt.get("confidence"), match)
                    )
                    file_object.write(
                        "{}\tutt: >{}<\tref: {}\tresult: {}\tconf: {}\tmatch: {}\n".format(
                            name, alt.get("utterance"), reference, result,
                            alt.get("confidence"), match
                        )
                    )
                    # we only print the best result
                    break

    print("Output stored in: {}".format(transcript_text_path))
    print("THE END", flush=True)


if __name__ == "__main__":
    main()
