import requests, os, re, json, time
import csv

## file wiht aivr session-ids

aivr_session_ids_file = "aivr-session-ids.txt"

## specify here the directory so save the audio files
out_path_base = "./download/"

## only files with this tag will be downloaded
unique_tag = "aivr"

out_path = out_path_base+"/"+unique_tag


#voicegain
host = "https://api.voicegain.ai/v1"
config = configparser.ConfigParser()
config.read('config.ini')
JWT_ACP = config.get('default', 'jwt_acp')

headers = {"Authorization":JWT_ACP}

data_url_get = "{}/data?tagsIncl={}".format(host, unique_tag)
data_url_get_file = "{}/data/{}/file"
print("query url: {}".format(data_url_get))

def load_aivr_session_ids(file_path):
    with open(file_path, 'r') as file:
        session_ids = [line.strip().strip('"') for line in file if line.strip()]
    return session_ids

def get_asr_session_id(ivr_sid, jwt):
    url = f"https://api.voicegain.ai/v1/aivr/{ivr_sid}"
    headers = {"Authorization": jwt}
    print(f"\tGET {url}", flush=True)
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        asr_session_id_left = data.get('realTimeAsrTranscribeSession', {}).get('left')
        asr_session_id_right = data.get('realTimeAsrTranscribeSession', {}).get('right')
        print(f"\t\tASR session ID for IVR SID {ivr_sid}: left={asr_session_id_left}, right={asr_session_id_right}", flush=True)
        return asr_session_id_left, asr_session_id_right
    else:
        print(f"\t\tFailed to retrieve ASR session ID for IVR SID {ivr_sid}. Status code: {response.status_code}")
        return None, None

def get_audio_data_object_id(asr_session_id, jwt):
    url = f"https://api.voicegain.ai/v1/asr/transcribe/{asr_session_id}?full=true"
    headers = {"Authorization": jwt}
    print(f"\tGET {url}", flush=True)
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        audio_data_object_id = data.get('audio', {}).get('source', {}).get('datastore', {}).get('uuid')
        print(f"\t\tAudio data object ID for ASR session ID {asr_session_id}: {audio_data_object_id}", flush=True)
        return audio_data_object_id
    else:
        print(f"\t\tFailed to retrieve audio data object ID for ASR session ID {asr_session_id}. Status code: {response.status_code}")
        print(f"\t\tResponse: {response.text}")
        return None

## MAIN ##

print("START", flush=True)

aivr_session_ids = load_aivr_session_ids(aivr_session_ids_file)
print("Loaded AIVR session IDs:", aivr_session_ids, flush=True)
print("number of AIVR session IDs: {}".format(len(aivr_session_ids)), flush=True)

## loop over AIVR session IDs and get ASR session IDs
print("Retrieving ASR session IDs for AIVR session IDs...", flush=True)
asr_session_map = {}    
count=0
with open('aivr2asr.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['aivr_sid', 'asr_sid_L', 'asr_sid_R']) 

    for aivr_sid in aivr_session_ids:
        print(f"Retrieving ASR session ID for AIVR session ID {aivr_sid}...", flush=True)
        asr_sid_left, asr_sif_right = get_asr_session_id(aivr_sid, JWT)
        if asr_sid_left:
            asr_session_map[aivr_sid] = {'left_asr_session_id': asr_sid_left, 'right_asr_session_id': asr_sif_right}
            writer.writerow([aivr_sid, asr_sid_left, asr_sif_right])
        count += 1
        # if count >= 2:
        #     break

exit()

if not os.path.exists(out_path_base):
    os.mkdir(out_path_base)

if not os.path.exists(out_path):
    os.mkdir(out_path)

print("listing uploads with tag {}".format(unique_tag), flush=True)

query_response_raw = requests.get(data_url_get, headers=headers)
code = query_response_raw.status_code
print(" response code: {}".format(code))
query_response = query_response_raw.json()
#print("query response: {}".format(query_response), flush=True)



for data_obj in sorted(query_response, key = lambda i: (i['description'], i['sosRef'])):
    print("objectId: {}".format(data_obj.get('objectId')))
    print("\t       name: {}".format(data_obj.get('name')))
    print("\tdescription: {}".format(data_obj.get('description')))
    print("\tcontentType: {}".format(data_obj.get('contentType')))
    print("\t       tags: {}".format(data_obj.get('tags')))        
    print("\tlongPersist: {}".format(data_obj.get('longPersist')))
    print("\t transcoded: {}".format(data_obj.get('transcoded')))    
    print("\t     sosRef: {}".format(data_obj.get('sosRef')))    
    file_ext = data_obj.get('contentType').split('/')[1]
    if(file_ext == "mpeg"):
        file_ext = "mp3"
    elif(file_ext == "x-ms-wma"):
        file_ext = "wma"
    print("\t   file ext: {}".format(file_ext))


    url_get_file = data_url_get_file.format(host, data_obj.get('objectId'))

    print("\t\tdownloading from: {}".format(url_get_file))
    local_filename = out_path+"/"+data_obj.get('name')+"."+file_ext
    print("\t\tdownloading   to: {}".format(local_filename))
    # NOTE the stream=True parameter below
    with requests.get(url_get_file, headers=headers, stream=True) as r:
        #r.raise_for_status()
        
        code = r.status_code
        while( code != 200):
            print("   response code: {}".format(code), flush=True)

            if(code != 429):
                print("unexpected response code")
                exit()

            if(code == 429):
                resp_headers = r.headers
                retry_after = resp_headers.get("Retry-After")
                if(retry_after is None):
                    print("rate limit exceeded but response missing Retry-After")
                    exit()
                print("sleeping {} seconds".format(retry_after), flush=True)
                time.sleep(int(retry_after))
                print("retrying", flush=True)
                r = requests.get(url_get_file, headers=headers, stream=True)
                code = r.status_code

        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
                print(".", end =" ", flush=True)
        print("#", flush=True)


    


print("END", flush=True)