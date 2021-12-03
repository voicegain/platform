import requests, os, re, json, time

## specify here the directory with audio files to be uploaded to voicegain
src_path = "/path/to/my/files/to/upload/"

## note - if the files are other than Wav, please provide appropriate MIME type here
audio_type = "audio/wav"

## tag unique for this upload
unique_tag = "UPL-7-11"

## set to true for a final run to persist the files
## if persist is False then the files will be cleaned up after a few hours
persist = True

#voicegain
host = "https://api.voicegain.ai/v1"
JWT = "<put your JWT token here - obtain from console.voicegain.ai>"




data_url_post = "{}/data/file?reuse=true&transcode=disable".format(host)
data_url_get = "{}/data?tagsIncl={}".format(host, unique_tag)
print("upload url: {}".format(data_url_post))
print(" query url: {}".format(data_url_get))

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

def upload_one_file(audio_path):

    path, fname = os.path.split(audio_path)

    data_body = {
        "name" : re.sub("[^A-Za-z0-9]+", "-", fname),
        "description" : audio_path,
        "contentType" : audio_type,
        "tags" : ["UPLOAD", "PERMANENT", unique_tag],
        "longPersist" : persist
    }

    multipart_form_data = {
        'file': (audio_path, open(audio_path, 'rb'), audio_type),
        'objectdata': (None, json.dumps(data_body), "application/json")
    }
    print("uploading audio data {}".format(data_body), flush=True)
    data_response_raw = requests.post(data_url_post, files=multipart_form_data, headers=headers)
    code = data_response_raw.status_code
    print("   response code: {}".format(code))

    if(code != 200 and code != 429):
        print("unexpected response code")
        exit()

    resp_headers = data_response_raw.headers
    print("response headers: {}".format(resp_headers))

    if(code == 429):
        retry_after = resp_headers.get("Retry-After")
        if(retry_after is None):
            print("rate limit exceeded but response missing Retry-After")
            exit()
        return int(retry_after)

    data_response = data_response_raw.json()
    print("data response: {}".format(data_response), flush=True)
    object_id = data_response["objectId"]
    print("successful upload - objectId: {}".format(object_id), flush=True)

    return -1

## MAIN ##

print("START", flush=True)

list_of_files = getListOfFiles(src_path)

print("files to upload")
for name in list_of_files:
    print(name)

print("uploading files...")
for name in list_of_files:
    retry_after = upload_one_file(name)
    while(retry_after >=0 ):
        print("rate-limit hit - need to wait {} seconds".format(retry_after), flush=True)
        time.sleep(retry_after)
        print("will retry now", flush=True)
        retry_after = upload_one_file(name)

time.sleep(3.0)

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
    print("\t       tags: {}".format(data_obj.get('tags')))        
    print("\tlongPersist: {}".format(data_obj.get('longPersist')))
    print("\t transcoded: {}".format(data_obj.get('transcoded')))    
    print("\t     sosRef: {}".format(data_obj.get('sosRef')))    


print("END", flush=True)