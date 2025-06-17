import csv
import os
import requests
import re
import json
import time
from datetime import datetime, timedelta
import pytz
import configparser

# Read configuration from config.ini
config = configparser.ConfigParser()
dir_path = os.path.dirname(os.path.realpath(__file__))
config.read(os.path.join(dir_path, 'config.ini')) # path to config.ini

inputFname = config['DEFAULT']['inputFname']
pathBase = os.path.join(dir_path, config['DEFAULT']['pathBase'])
MAX_ROWS_TO_PROCESS = config.getint('DEFAULT', 'MAX_ROWS_TO_PROCESS')
host = config['DEFAULT']['host']
JWT = config['DEFAULT']['JWT']
error_log_file = config['DEFAULT']['error_log_file']
upload_log_file = config['DEFAULT']['upload_log_file']
config_log_file = config['DEFAULT']['config_log_file']
seconds_per_hour_dbh = int(config['DEFAULT']['hours_per_hour_dbh']) * 3600
seconds_per_hour_obh = int(config['DEFAULT']['hours_per_hour_obh']) * 3600
persist_days = config.getint('DEFAULT', 'persist_days')
acoustic_model = config['DEFAULT']['acoustic_model']

limit = 0
seconds_sent = 0
is_bh = True # global variable to indicate if now is inside business hours


# Print all values except for JWT
print(f'inputFname: {inputFname}')
print(f'pathBase: {pathBase}')
print(f'MAX_ROWS_TO_PROCESS: {MAX_ROWS_TO_PROCESS}')
print(f'host: {host}')
print(f'error_log_file: {error_log_file}')
print(f'upload_log_file: {upload_log_file}')
print(f'config_log_file: {config_log_file}')
print(f'seconds_per_hour_dbh: {seconds_per_hour_dbh}')
print(f'seconds_per_hour_obh: {seconds_per_hour_obh}')
print(f'persist_days: {persist_days}')
print(f'acoustic_model: {acoustic_model}')

# Check if it's outside business hours
def check_bh(now):
    global limit
    global is_bh
    if now.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
        if now.hour == 23:
            is_bh = True
            limit = seconds_per_hour_dbh
        else:
            limit = seconds_per_hour_obh
            is_bh = False
    elif now.hour < 8 or now.hour > 17:
        limit = seconds_per_hour_obh
        is_bh = False
    else:
        limit = seconds_per_hour_dbh
        is_bh = True

check_bh(datetime.now())

# Check if the current upload would exceed the hour per hour limit
def check_upload_limit(current_load_sec):
    global seconds_sent
    print(f'Current upload limit: {limit} seconds', flush=True) ## current limit in seconds
    print(f'Uploaded {seconds_sent} seconds of audio', flush=True)
    print(f'Now uploading {current_load_sec} seconds of audio', flush=True)
    if (current_load_sec + seconds_sent) > int(limit):
        seconds_sent = current_load_sec

        delta = timedelta(hours=1)
        now = datetime.now()
        next_hour = (now + delta).replace(microsecond=0, second=0, minute=0)
        wait_seconds = (next_hour - now).seconds

        check_bh(next_hour)

        print('Hours per hour upload limit reached', flush=True)
        print(f'Waiting {wait_seconds} seconds till the start of the next hour', flush=True)
        time.sleep(wait_seconds)
    else:
        seconds_sent = seconds_sent + current_load_sec

def convert_to_utc(central_time_str, msecOffset=0):
    central = pytz.timezone('US/Central')
    # Handle both formats: "2023-11-02T10:52:56" and "2023-11-02 10:52:56"
    if 'T' in central_time_str:
        naive_datetime = datetime.strptime(central_time_str, "%Y-%m-%dT%H:%M:%S")
    else:
        naive_datetime = datetime.strptime(central_time_str, "%Y-%m-%d %H:%M:%S")
    central_datetime = central.localize(naive_datetime)
    utc_datetime = central_datetime.astimezone(pytz.utc)
    utc_datetime_with_offset = utc_datetime + timedelta(milliseconds=msecOffset)
    return utc_datetime_with_offset.strftime("%Y-%m-%dT%H:%M:%SZ")

def extract_agent_name(agent_str):
    match = re.search(r"\(([^)]+)\)", agent_str)
    if match:
        return match.group(1).split(',')[0].strip()
    return "Unknown"

def log_error(row):
    with open(error_log_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=row.keys())
        writer.writerow(row)

def log_upload(row):
    file_exists = os.path.exists(upload_log_file)
    with open(upload_log_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=row.keys())
        if not file_exists:
            writer.writeheader()  # Write the header if the file doesn't exist
        writer.writerow(row)

def log_config(name, saConfigId):
    log_exists = os.path.exists(config_log_file)
    with open(config_log_file, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "id"])
        if not log_exists:
            writer.writeheader()  # Write the header if the file doesn't exist
        writer.writerow({"name": name, "id": saConfigId})

# Load the upload log file and extract uniqueIDs to a set
def load_uploaded_ids(upload_log_file):
    uploaded_ids = set()
    if os.path.exists(upload_log_file):
        with open(upload_log_file, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                uploaded_ids.add(row['uniqueID'])

    print(f"Number of already uploaded files: {len(uploaded_ids)}", flush=True)

    return uploaded_ids

# load the config log file and extract the config id for each config name
def load_created_configs(config_log_file):
    created_configs = {}
    if os.path.exists(config_log_file):
        with open(config_log_file, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                created_configs[row['name']] = row['id']

    print(f"Number of created configs: {len(created_configs)}", flush=True)

    return created_configs


uploaded_ids = load_uploaded_ids(upload_log_file)
created_configs = load_created_configs(config_log_file)
count_skipped = 0

# process each row in the CSV file
def process_row(row):
    global count_skipped
    id = row.get('uniqueID', 'N/A')
    
    # Check if the file has already been uploaded
    if id in uploaded_ids:
        count_skipped += 1
        print(f'File already uploaded (number {count_skipped})', flush=True)
        return
    
    # Print specified fields
    fields_to_print = [
        'eventDate', 'duration', 'direction', 'ani', 'dialed', 'trunk', 
        'agentIds', 'agents', 'skillIds', 'skillName', 'notes', 'eventNumber'
    ]
    for field in fields_to_print:
        print(f"{field}: {row.get(field, 'N/A')}", flush=True)
    
    # Construct file path
    directory = row.get('directory', '')
    fileName = row.get('fileName', '')
    filePath = os.path.join(pathBase, directory, fileName)

    print(f"Checking file: {filePath}")
    print(f"Absolute path: {os.path.abspath(filePath)}")
    print(f"File exists: {os.path.exists(filePath)}")
    print(f"Is file: {os.path.isfile(filePath)}")

    # Check if every element of the absolute path exists
    path_elements = filePath.split(os.sep)
    for i in range(1, len(path_elements) + 1):
        partial_path = os.sep.join(path_elements[:i])
        if not os.path.exists(partial_path):
            print(f"\tPath does not exist: {partial_path}", flush=True)
            log_error(row)
            return
        else:
            print(f"\tPath exists: {partial_path}", flush=True)
    
    # Check if the file exists
    if not os.path.exists(filePath):
        print(f"Warning: Path {filePath} does not exist.", flush=True)
        log_error(row)
        return
    elif not os.path.isfile(filePath):
        print(f"Warning: File {filePath} not a regular file.", flush=True)
        log_error(row)
        return
    else:
        # Check upload limit
        fileDurationSec = int(row.get('duration', 0)) # in seconds
        check_upload_limit(fileDurationSec)
        
        # Upload file to Voicegain using /data API
        print(f"filePath: {filePath}", flush=True)
        upload_result = upload_file(filePath, fileName)
        
        # Retry if rate limit exceeded
        while isinstance(upload_result, int):
            print(f"Rate limit exceeded. Retrying after {upload_result} seconds...", flush=True)
            time.sleep(upload_result)
            upload_result = upload_file(filePath, fileName)
        if not isinstance(upload_result, str):
            log_error(row)
            return            

        # Log the upload
        log_upload(row)
        uploaded_ids.add(id)  # Add the ID to the set after successful upload

        audio_uuid = upload_result
        print(f"audio_uuid: {audio_uuid}", flush=True)

        # check if the config exists already
        print(f"Checking if the config exists already...", flush=True)
        if row.get('name', '') in created_configs:
            saConfigId = created_configs[row.get('name', '')]
            print(f"Config already exists: {saConfigId}", flush=True)
        else:
            print(f"Config does not exist. Creating new config...", flush=True)

            # create /sa/config
            # these are simplified for now. I will add support for more complex request bodies later on
            context_id = row.get('contextId', '')
            entities = row.get('entities', '').split(', ')
            keywords_tags = row.get('keywordsTags', '')
            keywords_phrases = row.get('keywordsPhrases', '')
            keywords = [{
                "tag": keywords_tags,
                "examples": [{"phrase": keywords_phrases}]
            }]
            phrases_tags = row.get('phrasesTags', '')
            phrases_examples = row.get('phrasesExamples', '')
            phrases_entities = row.get('phrasesEntities', '')
            phrases_keyword_tags = row.get('phrasesKeywordTags', '')
            phrases = [{
                "tag": phrases_tags,
                "examples": [{"sentence": phrases_examples}],
                "slots": {
                    "entities": [{"entity": phrases_entities}],
                    "keywords": [{"tag": phrases_keyword_tags}]
                }
            }]
            profanity = row.get('profanity', '')
            gender = row.get('gender', '')
            age = row.get('age', '')
            sentiment = row.get('sentiment', '')
            summary = row.get('summary', '')
            word_cloud = row.get('wordCloud', '')
            moods = row.get('moods', '')
            name = row.get('name', '')
            
            sa_config_body = {
                "contextId": context_id,
                "entities": entities,
                "keywords": keywords,
                "phrases": phrases,
                "profanity": profanity,
                "gender": gender,
                "age": age,
                "sentiment": sentiment,
                "summary": summary,
                "wordCloud": word_cloud,
                "moods": moods,
                "name": name
            }
            print(f"sa_config_body: {sa_config_body}", flush=True)

            sa_url = "{}/sa/config".format(host)

            headers = {
                "Authorization": f"Bearer {JWT}"    
            }

            print(f"Sending config data to Speech Analytics...", flush=True)
            saConfigId = None

            # we will try multiple times in case of rate limit exceeded
            while True:
                try:
                    response = requests.post(sa_url, json=sa_config_body, headers=headers)
                    code = response.status_code
                    print(f"Response code: {code}", flush=True)
                    if code == 429:
                        retry_after = response.headers.get("Retry-After")
                        if retry_after is None:
                            print("Rate limit exceeded but response missing Retry-After", flush=True)
                            log_error(row)
                            return
                        print(f"Rate limit exceeded. Retrying after {retry_after} seconds...", flush=True)
                        time.sleep(int(retry_after))
                        continue
                    if code != 200:
                        print("Unexpected response code", flush=True)
                        print(response.text, flush=True)
                        log_error(row)
                        return
                    sa_response = response.json()
                    print(f"SA response: {sa_response}", flush=True)
                    saConfigId = sa_response.get("saConfId")
                    log_config(row.get('name', ''), saConfigId)
                    break
                except Exception as e:
                    print(f"Exception occurred: {e}", flush=True)
                    log_error(row)
                    return  # we should log all failed files and retry them later
            
        if saConfigId is None:
            print("Error creating config", flush=True)
            log_error(row)
            return

        print(f"SA config ID: {saConfigId}", flush=True)
        send_offline_request(saConfigId, audio_uuid)

# submit /sa/offline request
def send_offline_request(saConfigId, audio_uuid):
    sa_offline_url = "{}/sa/offline".format(host)
    print(f"sa_offline_url: {sa_offline_url}", flush=True)

    sa_offline_body = {
        "label" : "AHCM-Archival",
        "saConfig" : saConfigId,
        "persistSeconds" : persist_days*(24*3600), 
        "tags" : ["AHCM", "Archival"],
        "settings" : {
            "asr" : {
                "languages" : ["en","es"],
                "languageDetection" : {
                        "aggregation" : "end_weighted"
                },
                "acousticModel" : acoustic_model
            },
            "formatters" : [
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
            ]
        },
        "optimizeForWebUi": "level2", # Set to level2 to support Voicegain Speech Analytics App. If you do not need the additional fields then set to none to save resources and speed up processing.
        "audio" : [{
            "source" : {"dataObjectUuid" : audio_uuid},
        }]
    }

    headers = {
        "Authorization": f"Bearer {JWT}"    
    }

    print(f"Sending offline request to Speech Analytics: {sa_offline_body}", flush=True)    
    while True:
        try:
            response = requests.post(sa_offline_url, json=sa_offline_body, headers=headers)
            code = response.status_code
            print(f"Response code: {code}", flush=True)
            if code == 429:
                retry_after = response.headers.get("Retry-After")
                if retry_after is None:
                    print("Rate limit exceeded but response missing Retry-After", flush=True)
                    return False
                print(f"Rate limit exceeded. Retrying after {retry_after} seconds...", flush=True)
                time.sleep(int(retry_after))
                continue
            if code != 200:
                print("Unexpected response code", flush=True)
                print(response.text, flush=True)
                return False
            sa_offline_response = response.json()
            print(f"SA offline response: {sa_offline_response}", flush=True)
            break
        except Exception as e:
            print(f"Exception occurred: {e}", flush=True)
            return False
    return True

def upload_file(file_path, file_name):
    data_url = "{}/data/file".format(host)
    headers = {
        "Authorization": f"Bearer {JWT}"
    }
    data_body = {
        "name": re.sub("[^A-Za-z0-9]+", "-", file_name),
        "description": file_path,
        "contentType": "audio/wav",
        "tags": ["AHCM"]
    }

    print(f"Uploading audio data {file_path} ...", flush=True)

    try:
        with open(file_path, 'rb') as file:
            multipart_form_data = {
                'file': (file_path, file, "audio/wav"),
                'objectdata': (None, json.dumps(data_body), "application/json")
            }
            response = requests.post(data_url, files=multipart_form_data, headers=headers)
            code = response.status_code
            print(f"Response code: {code}", flush=True)

            if code != 200 and code != 429:
                print("Unexpected response code", flush=True)
                print(response.text, flush=True)
                return None

            resp_headers = response.headers
            print(f"Response headers: {resp_headers}", flush=True)

            ## note: ideally we should add rate-limit response handling also in the asr request
            if code == 429:
                retry_after = resp_headers.get("Retry-After")
                if retry_after is None:
                    print("Rate limit exceeded but response missing Retry-After", flush=True)
                    return None
                return int(retry_after)

            data_response = response.json()
    except Exception as e:
        print(f"Exception occurred: {e}", flush=True)
        return None  # we should log all failed files and retry them later

    print(f"Data response: {data_response}", flush=True)

    if data_response.get("status") is not None and data_response.get("status") == "BAD_REQUEST":
        print(f"Error uploading file {file_path}", flush=True)
        return None

    object_id = data_response["objectId"]
    print(f"objectId: {object_id}", flush=True)

    return object_id

# read the CSV file and process each row
def read_and_process_csv(filename):
    with open(os.path.join(dir_path, filename), mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        # Initialize error log file
        with open(error_log_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, csv_reader.fieldnames)
            writer.writeheader()
        # Initialize already-uploaded file
        #with open(upload_log_file, mode='w', newline='', encoding='utf-8') as file:
        #    writer = csv.DictWriter(file, csv_reader.fieldnames)
        #    writer.writeheader()
        for i, row in enumerate(csv_reader):
            if i >= MAX_ROWS_TO_PROCESS:
                break
            process_row(row)

# main --------------------
read_and_process_csv(inputFname)
