import requests, os, re, json, time
import configparser

cfg = configparser.ConfigParser()
cfg.read("config.ini")
configSection = cfg.get("DEFAULT", "CONFIG")
protocol = cfg.get(configSection, "PROTOCOL")
hostPort = cfg.get(configSection, "HOSTPORT")
JWT = cfg.get(configSection, "JWT")
urlPrefix = cfg.get(configSection, "URLPREFIX")
outputFolder = cfg.get("DEFAULT", "OUTPUTFOLDER")


## specify here the directory so save the audio files
out_path_base = outputFolder

## note - if the files are other than Wav, please provide appropriate MIME type here
audio_type = "audio/wav"

## tag unique for this upload
#unique_tag = "UPL-RCFT-2-12"
#unique_tag = "UPL-RCFT-6-12-wma"
#unique_tag = "UPL-RCFT-6-12-mp3"
#unique_tag = "UPL-RCFT-6-12-cr"
unique_tag = "UPL-RCFT-20-12-STUDENT1"

out_path = out_path_base+"/"+unique_tag

## set to true for a final run to persist the files
persist = False

#voicegain
host = f"{protocol}://{hostPort}/{urlPrefix}"

data_url_get = "{}/data?tagsIncl={}".format(host, unique_tag)
data_url_get_file = "{}/data/{}/file"
print("query url: {}".format(data_url_get))

headers = {"Authorization":JWT}


## MAIN ##

print("START", flush=True)

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
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
                print(".", end =" ", flush=True)
        print("#", flush=True)


    


print("END", flush=True)