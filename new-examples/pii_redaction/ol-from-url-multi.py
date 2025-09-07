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
outputFolder = cfg.get("DEFAULT", "OUTPUTFOLDER")
inputUrl = cfg.get(configSection, "INPUTURL")

print(f"inputUrl: {inputUrl}")

filesToProcess = 5

if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

host = f"{protocol}://{hostPort}/{urlPrefix}"

asr_body = {
    "sessions": [
        {
            "asyncMode": "OFF-LINE",
            "audioChannelSelector": "two-channel",
            "poll": {
                # will delete the session after 1 minute
                "afterlife": 60000
                #"persist" : 300000
            },
            "content": {
                "incremental": ["progress"],
                "full" : ["words"]
            }
        }
    ],
    "audio":{
        "source": {
            "fromUrl": {
                "url": inputUrl
            }
        },
        "callback": {
            "uri": " https://01ae-2600-1702-5563-6e00-d088-6b77-e0d5-891d.ngrok-free.app/upload",
            "method": "POST",
            "multipartFormData": [{
                "name": "return_object",
                "value" : "my-secret-HASHsh",
                "contentType": "text/plain"
            }]
        }
    },
    "settings": {
        "asr": {
            "languages" : ["en"],
            "acousticModelNonRealTime" : "VoiceGain-omega",
            #"acousticModelNonRealTime" : "whisper:small",
            "noInputTimeout": -1,
            "completeTimeout": -1,
            "sensitivity" : 0.5,
            "hints" : [
                "Cencosud[senkosood|senkosud]:10",
                "Tarjeta[taarheta]:10",
                "Naranja[naranga|naranha]:10",
                "Argencard[arhencard]:10",
                "Hipercard[hiperkard|heeperkard]:10"
            ]
        }
        ,"formatters" : [
        {
            "type": "digits"
        },
        {
            "type": "enhanced",
            "parameters": {
                "CC": True,
                "SSN": True,
                "URL": True,
                "PHONE": True,
                "EMAIL": True
            }
        }
        ,{
            "type": "profanity",
            "parameters": {"mask": "partial"}
        }
        ,{
            "type": "spelling",
            "parameters": {"lang": "en-US"}
        }
        ,{
            "type": "redact",
            "parameters": {
                "CC": "partial:4",
                "CVV": "full:2",
                #"ZIP": "[ZIP]",
                #"PERSON": "[PERSON]",
                #"EMAIL" : "[EMAIL]",
                #"PHONE" : "[PHONE]",
                "SSN" : "partial:4"
                #,"DMY" : "[DMY]"
            }
        }
        # ,{ 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b(?:\d{4}-){3}\d{4}\b",
        #         "mask": "partial",
        #         "options": "IA"
        #     }
        # }
        # ,{ 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"\b(?:3[47]\d{13}|4\d{14,15}|5[1-5]\d{14}|6(?:011|5\d{2})\d{12})\b",
        #         "mask": "partial",
        #         "options": "IA"
        #     }
        # }
        # ,{ 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"(?<=\bcv[v|b|c] is )\d{3,4}\b",
        #         "mask": "full",
        #         "options": "IA"
        #     }
        # },
        # { 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"(?<=\bcv[v|b|c] )\d{3,4}\b",
        #         "mask": "full",
        #         "options": "IA"
        #     }
        # },
        # { 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"(?<=\bcv number is )\d{3,4}\b",
        #         "mask": "full",
        #         "options": "IA"
        #     }
        # },
        # { 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"(?<=\bcv number )\d{3,4}\b",
        #         "mask": "full",
        #         "options": "IA"
        #     }
        # },
        # { 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"(?<=\bcv[v|b|c] number is )\d{3,4}\b",
        #         "mask": "full",
        #         "options": "IA"
        #     }
        # },
        # { 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"(?<=\bcv[v|b|c] number )\d{3,4}\b",
        #         "mask": "full",
        #         "options": "IA"
        #     }
        # },
        # { 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"(?<=\bpin is )\d{3,4}\b",
        #         "mask": "full",
        #         "options": "IA"
        #     }
        # },
        # { 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"(?<=\bpin )\d{3,4}\b",
        #         "mask": "full",
        #         "options": "IA"
        #     }
        # },
        # { 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"(?<=\bpin number is )\d{3,4}\b",
        #         "mask": "full",
        #         "options": "IA"
        #     }
        # },
        # { 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"(?<=\bpin number )\d{3,4}\b",
        #         "mask": "full",
        #         "options": "IA"
        #     }
        # },
        # { 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"(?<=\bsecurity is )\d{3,4}\b",
        #         "mask": "full",
        #         "options": "IA"
        #     }
        # },
        # { 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"(?<=\bsecurity )\d{3,4}\b",
        #         "mask": "full",
        #         "options": "IA"
        #     }
        # },
        # { 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"(?<=\bsecurity[.] )\d{3,4}\b",
        #         "mask": "full",
        #         "options": "IA"
        #     }
        # },
        # { 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"(?<=\bsecurity pin is )\d{3,4}\b",
        #         "mask": "full",
        #         "options": "IA"
        #     }
        # },
        # { 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"(?<=\bsecurity pin )\d{3,4}\b",
        #         "mask": "full",
        #         "options": "IA"
        #     }
        # },
        # { 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"(?<=\bsecurity number is )\d{3,4}\b",
        #         "mask": "full",
        #         "options": "IA"
        #     }
        # },
        # { 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"(?<=\bsecurity number )\d{3,4}\b",
        #         "mask": "full",
        #         "options": "IA"
        #     }
        # }, 
        # { 
        #     "type": "regex",
        #     "parameters": {
        #         "pattern": r"(?<=\bsecurity number[.] )\d{3,4}\b",
        #         "mask": "full",
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

combined_file_path = os.path.join(output_path, "combined-test-result.txt")

def make_request_with_retries(url, method="GET", headers=None, json=None, retries=3, timeout=30):
    for attempt in range(retries):
        try:
            if method == "GET":
                response = requests.get(url, headers=headers, timeout=timeout)
            elif method == "POST":
                response = requests.post(url, headers=headers, json=json, timeout=timeout)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                raise

def process_one_file(seq=0):
    ## steps:
    ## 2. start offline transcription session
    ## 3. keep polling untill we are done
    ## 4. retrieve transcript


  

    if not os.path.exists(output_path):
        os.mkdir(output_path)


    printTranscribeQueueStatus()

    url = "{}/asr/transcribe/async".format(host)

    print(f"making asr request {url}...", flush=True)

    audio_url =  inputUrl.format(num=seq, width=2)
    print("audio_url: {}".format(audio_url), flush=True)

    asr_body["audio"]["source"]["fromUrl"]["url"] = audio_url

    asr_response_raw = make_request_with_retries(url, method="POST", headers=headers, json=asr_body)
    start_time = time.time()
    if(asr_response_raw.status_code != 200):
        print("unexpected response code {} for asr request".format(asr_response_raw.status_code), flush=True)
        print(asr_response_raw, flush=True)
        print(asr_response_raw.text, flush=True)
        print("EXIT", flush=True)
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
        poll_response_raw = make_request_with_retries(polling_url + "?full=false", headers=headers)
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
        # write poll_response to JSON
        # poll_response_path = os.path.join(output_path, "{}-{}-{}.json".format(audio_fname, session_id, index))
        # with open(poll_response_path, 'w') as outfile:
        #     json.dump(poll_response, outfile)
        # print("Phase: {} Final: {} -> Save result to {}".format(phase, is_final, poll_response_path), flush=True)

        index += 1
        if is_final:
            break

    poll_response_raw = make_request_with_retries(polling_url + "?full=true", headers=headers)
    print(poll_response_raw.headers['Content-Type'])
    poll_response = poll_response_raw.json()
    # write poll_response to JSON
    poll_response_path = os.path.join(output_path, "{}--{}.json".format(session_id, index))
    with open(poll_response_path, 'w',  encoding='utf-8') as outfile:
        json.dump(poll_response, outfile, ensure_ascii=False)
    print("Save final result to {}".format(poll_response_path), flush=True)

    #get result as text file

    txt_url = "{}/asr/transcribe/{}/transcript?format=text".format(host, session_id)
    print("Retrieving transcript using url: {}".format(txt_url), flush=True)
    txt_response = make_request_with_retries(txt_url, headers=headers)
    txt_response.encoding = txt_response.apparent_encoding  ## << needed to get the encoding correct
    transcript_text_path = os.path.join(output_path, "transcript-{:02d}.txt".format(seq))
    with open(transcript_text_path, 'w',  encoding='utf-8') as file_object:
        file_object.write(txt_response.text)
    print("Save final transcript text to {}".format(transcript_text_path))
    print("", flush=True)

    # Append to combined file
    with open(combined_file_path, 'a', encoding='utf-8') as combined_file:
        combined_file.write(f"Use case {seq:02d}:\n")
        combined_file.write(txt_response.text)
        combined_file.write("\n\n")

    printTranscribeQueueStatus()

    return -1

def printTranscribeQueueStatus():
    print("making asr queue request ...", flush=True)
    asr_response_raw = make_request_with_retries("{}/asr/transcribe/status/queue".format(host), headers=headers)
    if(asr_response_raw.status_code != 200):
        print("unexpected response code {} for asr request".format(asr_response_raw.status_code), flush=True)
    else:
        asr_response = asr_response_raw.json()
        pretty_asr_response = json.dumps(asr_response, indent=4)  # Pretty-printing here
        print("asr queue status:\n{}".format(pretty_asr_response), flush=True)

## MAIN ##

print("START", flush=True)

# Ensure the combined file is empty at the start
with open(combined_file_path, 'w', encoding='utf-8') as combined_file:
    combined_file.write("")

for i in range(38, 38+1):
    print("processing file {}".format(i), flush=True)

    retry_after = process_one_file(i)
    while(retry_after >=0 ):
        print("rate-limit hit - need to wait {} seconds".format(retry_after), flush=True)
        time.sleep(retry_after)
        print("will retry now", flush=True)
        retry_after = process_one_file(i)

    time.sleep(5.0)


print("THE END", flush=True)