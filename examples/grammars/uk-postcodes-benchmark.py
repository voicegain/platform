"""
pip install ffmpy
"""
from lib2to3 import refactor
from ffmpy import FFmpeg
import requests, time, os, json, re, base64
import shutil
from requests_futures.sessions import FuturesSession

jjsgf_grammar_file = "./uk-postcodes-jjsgf.json"


## specify here the directory with input audio files to test
base_path = "/directory-with-files-to-be-tested/"
# wav and text files are ins separate subdirectories
input_path = base_path +"wav/"
txt_path = base_path + "txt/"


csv_path = base_path + "/uk-postcodes.csv"

#voicegain
host = "https://api.voicegain.ai/v1"
JWT = "<your JWT token here - obtain from https://console.voicegain.ai>"

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
			# grammar will be filled later from jjsgf_grammar_file
            "grammars" : [ ],
            "speechContext" : "normal",
            "noInputTimeout": 6000,
            "completeTimeout": 3000,
            "incompleteTimeout" : 6000,
            "sensitivity" : 0.4,
            "speedVsAccuracy" : 0.875,
            "maxAlternatives" : 3,
            "confidenceThreshold" : 0.00001 
            #, "langModel": "ac35500c-08e1-45f5-9fde-666e75c6fc86"
            #, "acousticModelRealTime" : "VoiceGain-rt-en-us:15"
            #, "acousticModelNonRealTime" : "VoiceGain-rt-en-us:15"			
        }
        #,"formatters" : [{"type" : "digits"}]
    }
}
#### all settings above this line ####

# Opening JSON grammar file
f = open(jjsgf_grammar_file)
 
# returns JSON object as a dictionary
grammar = json.load(f)

asr_body["settings"]["asr"]["grammars"].append(grammar)

# tmp directory is used for audion conversion
if not os.path.exists("temp"):
    os.mkdir("temp")

results = {}
comps = {}
csv = []
csv.append("wav_name,reference,recognition")

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

def process_one_file_step1(audio_full_name):

	path, fname = os.path.split(audio_full_name)

	name, ext = fname.split('.')

	txt_fname = txt_path+name+".txt"

	f = open(txt_fname)
	reference_text = f.read()

	print("Processing {}/{} with reference: {}".format(path,fname, reference_text), flush=True)

	future_from_request = make_request_for_file(audio_full_name, fname)

	ret_val = {}
	ret_val["future"] = future_from_request
	ret_val["audio_full_name"] = audio_full_name
	ret_val["fname"] = fname
	ret_val["reference_text"] = reference_text

	return ret_val


def make_request_for_file(audio_full_name, fname):

	conv_fname = "temp/{}.wav".format(fname)
	ff = FFmpeg(
		inputs={audio_full_name: []},
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

	session = FuturesSession()
	# first request is started in background
	future_one = session.post("{}/asr/recognize".format(host), json=asr_body, headers=headers)

	return future_one


def process_future(ret_val):

	future_from_request = ret_val["future"]
	audio_full_name = ret_val["audio_full_name"]
	fname = ret_val["fname"]
	reference_text = ret_val["reference_text"]

	global results
	global comps
	global csv
	print("reference: "+reference_text, flush=True)
	comps[fname] = {}
	comps[fname]["target"] = reference_text

	asr_response_raw = future_from_request.result()

	print(asr_response_raw)
	asr_response = asr_response_raw.json()
	print(asr_response)

	if(asr_response.get("result") is None):
		print(asr_response)
		csv.append("{},{},{}".format(fname, reference_text, 'NULL'))
	else:
		alternatives = asr_response.get("result").get("alternatives")
		print(str(alternatives), flush=True)
		results[fname] = alternatives
		comps[fname] = {}
		if(alternatives is None):
			print('NOMATCH')
			csv.append("{},{},{}".format(fname, reference_text, 'NOMATCH'))
		else:
			top = alternatives[0]
			top_utt = top.get("utterance")
			comps[fname]["utt"] = top_utt
			utt = " " + top_utt + " "
			print("utt: "+utt, flush=True)

			csv.append("{},{},{}".format(fname, reference_text, top_utt))

			if(top_utt == reference_text):
				print(":) SAME :)")
				comps[fname]["comp"] = "SAME"
			else:
				print(":( DIFFERENT :(")
				comps[fname]["comp"] = "DIFFERENT"

  


## MAIN ##

print("START", flush=True)

list_of_files = getListOfFiles(input_path)

# for root, dirs, files in os.walk(input_path):
# 	for file in files:
# 		list_of_files.append(os.path.join(root,file))

print("files to test")
for name in list_of_files:
    print(name)

# for name in list_of_files:
#     process_one_file(name)

n = len(list_of_files)
i = 0
k=5

while i<n:
	j=0
	ret_vals = []
	while (j<k and i<n):
		print("--->>> i={}, j={} <<<---".format(i,j), flush=True)
		ret_vals.append( process_one_file_step1(list_of_files[i] ))
		if(i==0):
			time.sleep(10.0)
		else:
			time.sleep(1.25)
		i = i+1
		j = j+1

	for ret_val in ret_vals:
		process_future(ret_val)

if not os.path.exists("output"):
    os.mkdir("output")
output_path = "output{}".format(input_path.replace("./", "/"))
output_path = "output{}".format("/uk-postcode")
if not os.path.exists(output_path):
    os.mkdir(output_path)

transcript_text_path = os.path.join(output_path, "{}.txt".format(time.strftime("%Y-%m-%d_%H-%M-%S")))
with open(transcript_text_path, 'w') as file_object:
	for name in results:
		print(name)
		comp = comps.get(name)
		if(comp is not None):
			print("\t{} vs {} -> {}".format(comp.get("target"), comp.get("utt"), comp.get("comp")))
			file_object.write("{}\t{} vs {} -> {}".format(name, comp.get("target"), comp.get("utt"), comp.get("comp")))		
		alts = results.get(name)
		if(alts is not None):
			#print("\t"+str(alts))
			for alt in alts:
				print("\tutt: >{}<  conf: {}".format(alt.get("utterance"), alt.get("confidence")))
				file_object.write("{}\tutt: >{}<  conf: {}\n".format(name, alt.get("utterance"), alt.get("confidence")))

with open(csv_path, "a") as file_object:
	for row in csv:
		print(row)
		file_object.write(row+"\n")


print("Output stored in: {}".format(transcript_text_path))
print("THE END", flush=True)