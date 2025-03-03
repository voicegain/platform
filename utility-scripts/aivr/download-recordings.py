import requests, os, re, json, time
import csv
import configparser

## file witt aivr session-ids and recording ids

aivr_session_ids_file = "aivr2asr2audio.csv"

## specify here the directory so save the audio files
out_path_base = "./download/more/"


#voicegain
host = "https://api.voicegain.ai/v1"
config = configparser.ConfigParser()
config.read('config.ini')
JWT_ACP = config.get('default', 'jwt_acp')

## load the data from the csv file
with open(aivr_session_ids_file, mode='r') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        aivr_sid = row['aivr_sid']
        channel = row['channel']
        asr_sid = row['asr_sid']
        audio_id = row['audio_id']
        print(f"Processing AIVR session ID: {aivr_sid}, channel: {channel}, ASR session ID: {asr_sid}, audio ID: {audio_id}")

        url = "{}/data/{}/file".format(host, audio_id)
        headers = {"Authorization":JWT_ACP}
        print("GET {}".format(url))
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            out_path = "{}".format(out_path_base)
            if not os.path.exists(out_path):
                os.makedirs(out_path)
            
            file_path = "{}/{}-{}-{}-{}.wav".format(out_path, aivr_sid, channel, asr_sid, audio_id)
            print("\tSaving to {}".format(file_path))
            with open(file_path, 'wb') as file:
                file.write(response.content)
                print("\tSaved to {}".format(file_path))
        else:
            print("\tFailed to download audio file. Status code: {}".format(response.status_code))