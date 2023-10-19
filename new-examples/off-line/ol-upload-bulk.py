import requests, time, os, json, re
import configparser

## Note: rate-limit (429 code) handling is only partially implemented in this script

cfg = configparser.ConfigParser()
cfg.read("config.ini")
configSection = cfg.get("DEFAULT", "CONFIG")
protocol = cfg.get(configSection, "PROTOCOL")
hostPort = cfg.get(configSection, "HOSTPORT")
JWT = cfg.get(configSection, "JWT")
urlPrefix = cfg.get(configSection, "URLPREFIX")
inputFolder = cfg.get("DEFAULT", "INPUTFOLDER")
outputFolder = cfg.get("DEFAULT", "OUTPUTFOLDER")

model = "VoiceGain-omega"
#model = "whisper:small"

print("model: {}".format(model))

maxFilesToProcess = 1

if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

host = f"{protocol}://{hostPort}/{urlPrefix}"

print("host: {}".format(host))  

asr_body = {
    "sessions": [
        {
            "asyncMode": "OFF-LINE",
            "poll": {
                # will delete the session after 1 minute
                #"afterlife": 60000
                "persist" : 600000
            },
            "content": {
                "incremental": ["progress"],
                "full" : ["progress", "words"]
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
    "settings": {
        "asr": {
            "languages" : ["nl"],
            #"languages" : ["ru"],
            "acousticModelNonRealTime" : model,
            "noInputTimeout": -1,
            "completeTimeout": -1,
            "sensitivity" : 0.5,
            # , "hints" : [
                # "rupees[roopiece|ruppes]"
            # ]
            #, "diarization" : {
            #  "minSpeakers" : 2,
            #  "maxSpeakers" : 2
            #}
        }
        ,"formatters" : [
        {
            "type": "digits"
        }
        # ,{
        #     "type": "basic",
        #     "parameters": {"enabled": "true"}
        # },
        , {
            "type": "enhanced",
            "parameters": {
                "CC": True,
                "SSN": True,
                "URL": True,
                "PHONE": True,
                "EMAIL": True
            }
        }
        , {
            "type": "profanity",
            "parameters": {"mask": "partial"}
        }
        ,{
            "type": "spelling",
            "parameters": {"lang": "en-US"}
        }
        # ,{
        #     "type": "redact",
        #     "parameters": {
        #         "CC": "[CC]",
        #         "ZIP": "[ZIP]",
        #         "PERSON": "[PERSON]",
        #         "EMAIL" : "[EMAIL]",
        #         "PHONE" : "[PHONE]",
        #         "SSN" : "[SSN]",
        #         "DMY" : "[DMY]"
        #     }
        # }
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+([1-9]|0[1-9]|[12][0-9]|3[01]),\s+\d{4}\b",
        #         "mask": "[DATE3]",
        #         "options": "IA"
        #     }
        # }  
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+([1-9]|0[1-9]|[12][0-9]|3[01])(st|nd|rd|th),\s+\d{4}\b",
        #         "mask": "[DATE2]",
        #         "options": "IA"
        #     }
        # }  
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b([1-9]|0[1-9]|[12][0-9]|3[01])(st|nd|rd|th)\s+of\s+(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{4}\b",
        #         "mask": "[DATE1]",
        #         "options": "IA"
        #     }
        # }            
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{2}\b",
        #         "mask": "[EXPD3]",
        #         "options": "IA"
        #     }
        # }            
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b(January|February|March|April|May|June|July|August|September|October|November|December)(\s+of)?\s+\d{4}\b",
        #         "mask": "[EXPD2]",
        #         "options": "IA"
        #     }
        # }            
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b(0[1-9]|1[0-2])\s([0-9]{2})\b",
        #         "mask": "[EXPD1]",
        #         "options": "IA"
        #     }
        # }            
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b(0?[1-9]|1[0-2])\s(0?[1-9]|[12][0-9]|3[01])\s(19|20)\d{2}\b",
        #         "mask": "[DATE4]",
        #         "options": "IA"
        #     }
        # }  
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b3[47][0-9]{13}\b",
        #         "mask": "[AMEX]",
        #         "options": "IA"
        #     }
        # }   
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b(5[1-5][0-9]{14}|2[2-7][0-9]{14})\b",
        #         "mask": "[MC16]",
        #         "options": "IA"
        #     }
        # }   
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b4\d{15}\b",
        #         "mask": "[VISA16]",
        #         "options": "IA"
        #     }
        # }   
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b\d{4}\b",
        #         "mask": "[CVV4]",
        #         "options": "IA"
        #     }
        # }   
        # ,{
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b\d{3}\b",
        #         "mask": "[CVV3]",
        #         "options": "IA"
        #     }
        # }   
        ]
    }
}

#### all settings above this line ####

audio_type = "audio/wav"

output_path = "{}/{}".format(outputFolder, time.strftime("%Y-%m-%d_%H-%M-%S"))
if not os.path.exists(output_path):
    os.makedirs(output_path)

data_url = "{}/data/file".format(host)

headers = {"Authorization":JWT}

def process_one_file(audio_fname):
    ## steps:
    ## 1. upload audio
    ## 2. start offline transcription session
    ## 3. keep polling untill we are done
    ## 4. retrieve transcript

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
        code = data_response_raw.status_code
        print("   response code: {}".format(code))

        if(code != 200 and code != 429):
            print("unexpected response code")
            print(data_response_raw.text)
            exit()

        resp_headers = data_response_raw.headers
        print("response headers: {}".format(resp_headers))

        ## note: ideally we should add rate-limit response handling also in the asr request
        if(code == 429):
            retry_after = resp_headers.get("Retry-After")
            if(retry_after is None):
                print("rate limit exceeded but response missing Retry-After")
                exit()
            return int(retry_after)

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

    ## test the rate limit
    # for i in range(10):
    #     get_response_raw = requests.get("{}/data/{}".format(host, object_id), headers=headers)
    #     get_response = get_response_raw.json()

    #     print("CHECK get response: {}".format(get_response), flush=True)

    #     code = get_response_raw.status_code

    #     if(code != 200 and code != 429):
    #         print("CHECK unexpected response code")
    #         exit()

    #     resp_headers = get_response_raw.headers
    #     print("CHECK response headers: {}".format(resp_headers))

    

    ## set the audio id in the asr request
    if not os.path.exists(output_path):
        os.mkdir(output_path)

    asr_body["audio"]["source"]["dataStore"]["uuid"] = object_id

    printTranscribeQueueStatus()

    print("making asr request ...", flush=True)
    asr_response_raw = requests.post("{}/asr/transcribe/async".format(host), json=asr_body, headers=headers)
    start_time = time.time()
    if(asr_response_raw.status_code != 200):
        print("unexpected response code {} for asr request".format(asr_response_raw.status_code), flush=True)
        exit()

    asr_response = asr_response_raw.json()
    session_id = asr_response["sessions"][0]["sessionId"]
    polling_url = asr_response["sessions"][0]["poll"]["url"]

#    print("sessionId: {}".format(session_id)) #, flush=True)
#    print(" poll.url: {}".format(polling_url)) #, flush=True)

    # printTranscribeQueueStatus()

    index = 0
    ## poll untill we have final result
    while True:
        if(index == 0):
            #first
            print("no wait for first poll request")
        elif(index<5):
            time.sleep(0.3)
        else:
            time.sleep(4.9)

        elapsed_time = time.time() - start_time
        print("Time taken just before poll request:", elapsed_time, "seconds")
        poll_response_raw = requests.get(polling_url+"?full=false", headers=headers)
        elapsed_time = time.time() - start_time
        print("Time taken just after poll request:", elapsed_time, "seconds")

        code = poll_response_raw.status_code
        print("   response code: {}".format(code))

        if(code != 200 and code != 429):
            print("unexpected response code")
            exit()

        if(code == 429):
            retry_after = resp_headers.get("Retry-After")
            if(retry_after is None):
                print("rate limit exceeded but response missing Retry-After")
                exit()
            time.sleep(retry_after)
            continue

        poll_response = poll_response_raw.json()
        phase = poll_response["progress"]["phase"]
        is_final = poll_response["result"]["final"]
        print("Phase: {} Final: {}".format(phase, is_final), flush=True)

        # # write poll_response to JSON
        if(False):
            poll_response_path = os.path.join(output_path, "{}-{}-{}.json".format("audio_fname", session_id, index))
            with open(poll_response_path, 'w') as outfile:
                json.dump(poll_response, outfile)
            print("Phase: {} Final: {} -> Save result to {}".format(phase, is_final, poll_response_path), flush=True)

        index += 1
        if is_final:
            break

    # write full response
    if(True):
        poll_response_raw = requests.get(polling_url+"?full=true", headers=headers)
        print(poll_response_raw.headers['Content-Type'])
        poll_response = poll_response_raw.json()
        # write poll_response to JSON
        phase = poll_response["progress"]["phase"]
        print("Phase: {} Final: {}".format(phase, is_final), flush=True)
        poll_response_path = os.path.join(output_path, "{}--{}.json".format(session_id, index))
        with open(poll_response_path, 'w',  encoding='utf-8') as outfile:
            json.dump(poll_response, outfile, ensure_ascii=False)
        print("Save final result to {}".format(poll_response_path), flush=True)

    #get result as text file

    txt_url = "{}/asr/transcribe/{}/transcript?format=text".format(host, session_id)
    print("Retrieving transcript using url: {}".format(txt_url), flush=True)
    txt_response = requests.get(txt_url, headers=headers)
    txt_response.encoding = txt_response.apparent_encoding ## << needed to get the encoding correct
    transcript_text_path = os.path.join(output_path, "{}.txt".format(fname))
    with open(transcript_text_path, 'w',  encoding='utf-8') as file_object:
        file_object.write(txt_response.text)
    print("Save final transcript text to {}".format(transcript_text_path))
    print("", flush=True)

    printTranscribeQueueStatus()

    return -1

def printTranscribeQueueStatus():
    print("making asr queue request ...", flush=True)
    asr_response_raw = requests.get("{}/asr/transcribe/status/queue".format(host), headers=headers)
    if(asr_response_raw.status_code != 200):
        print("unexpected response code {} for asr request".format(asr_response_raw.status_code), flush=True)
    else:
        asr_response = asr_response_raw.json()
        pretty_asr_response = json.dumps(asr_response, indent=4)  # Pretty-printing here
        print("asr queue status:\n{}".format(pretty_asr_response), flush=True)

## MAIN ##

print("START", flush=True)

list_of_files = []

for root, dirs, files in os.walk(inputFolder):
    for file in files:
        maxFilesToProcess -= 1
        if(maxFilesToProcess >= 0): 
            list_of_files.append(os.path.join(root,file))

print("files to test")
for name in list_of_files:
    print(name)

for name in list_of_files:
    retry_after = process_one_file(name)
    while(retry_after >=0 ):
        print("rate-limit hit - need to wait {} seconds".format(retry_after), flush=True)
        time.sleep(retry_after)
        print("will retry now", flush=True)
        retry_after = process_one_file(name)


print("THE END", flush=True)