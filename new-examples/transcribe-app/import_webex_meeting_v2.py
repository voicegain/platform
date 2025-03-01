import configparser
import re
import time
import requests
import os
import json

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')
CONF_NAME = config['DEFAULT']['CONFIG']

# Read values from the configuration
protocol = config[CONF_NAME]['PROTOCOL']
hostPort = config[CONF_NAME]['HOSTPORT']
JWT = config[CONF_NAME]['JWT']
prefixAuth = config[CONF_NAME]['PREFIX_AUTH']
prefixApi = config[CONF_NAME]['PREFIX_API']
inputFolder = config['DEFAULT']['INPUTFOLDER']
audioFile = config['DEFAULT']['AUDIOFILE']
videoFile = config['DEFAULT']['VIDEOFILE']

# Print the configuration values
print(f"Configuration: {CONF_NAME}")
print(f"     Protocol: {protocol}")
print(f"    Host Port: {hostPort}")
print(f"  Prefix auth: {prefixAuth}")
print(f"   Prefix API: {prefixApi}")
print(f" Input Folder: {inputFolder}")
print(f"   Audio File: {audioFile}")
print(f"   Video File: {videoFile}")

hostAuth = f"{protocol}://{hostPort}/{prefixAuth}"
hostApi = f"{protocol}://{hostPort}/{prefixApi}"
headers = {"Authorization": JWT}

audio_fname = os.path.join(inputFolder, audioFile)
print(f"  Audio file: {audio_fname}", flush=True)

video_fname = os.path.join(inputFolder, videoFile)
print(f"  Video file: {video_fname}", flush=True)

print(f"   Host Auth: {hostAuth}", flush=True)
print(f"    Host API: {hostApi}", flush=True)

verify_ssl_certs = False

email_to_find = "foo2.jacek.jarmulak.edge@voicegain.ai"
user_fname = "Jacek Edge"
user_lname = "Jarmulak"
user_role = "User"
user_notification = "oidc"
project_name_to_find = "Webex Project Jacek foo 6"
meeting_label = "Webex Meeting from " + time.strftime(" %Y-%m-%d %H_%M_%S")
audio_mime_type = "audio/m4a"
video_mime_type = "video/mp4"
persist_seconds = 3600
project_color="red"
project_timezone="America/Chicago"
project_week_starts_on="Monday"
project_languages=["en"]
project_hints=[]


def generate_short_lived_jwt(context_id):
    url = f"{hostApi}/security/jwt"
    params = {
        "contextId": context_id,
        "expInSec": 15,
        "aud" : hostPort
    }
    response = requests.get(url, headers=headers, params=params, verify=verify_ssl_certs)
    if response.status_code != 200:
        print(f"Failed to fetch short-lived JWT: {response.status_code}", flush=True)
        print(response.text, flush=True)
        return None

    short_lived_token = response.text.strip()
    print(f"Short-lived token: {short_lived_token[:16]}...{short_lived_token[-16:]}", flush=True)
    return short_lived_token

##
## find_user_by_email
##
def find_user_by_email(email):
    url = f"{hostAuth}/user"
    print(f"Fetching users from {url}", flush=True)
    response = requests.get(url, headers=headers, verify=verify_ssl_certs)
    if response.status_code != 200:
        print(f"Failed to fetch users: {response.status_code}", flush=True)
        return None

    userUuid = None
    userCount = 0
    users = response.json()
    for user in users:
        if user.get('email').lower() == email.lower():
            userUuid = user.get('userId')
        userCount += 1

    print(f"Found {userCount} users", flush=True)
    if(userUuid):
        print(f"User with email {email} found", flush=True)
        return userUuid
    else:
        print(f"User with email {email} not found", flush=True)
        return None

##
## create_user
##
def create_user(email, first_name, last_name, role, initial_notification):
    permissions = None
    if(role == "User"):
        permissions = ["user"]
    elif(role == "Admin"):
        permissions = ["user","admin"]
    else:
        print(f"Invalid role: {role}", flush=True)
        return None

    url = f"{hostAuth}/user"
    body = {
        "email": email,
        "firstName": first_name,
        "lastName": last_name,
        "role": role,
        "permissions": f"[{",".join(permissions)}]",
        "initialNotification": initial_notification
    }
    print(f"Creating user with email {email}", flush=True)
    response = requests.post(url, json=body, headers=headers, verify=verify_ssl_certs)
    if response.status_code != 200:
        print(f"Failed to create user: {response.status_code}", flush=True)
        print(response.text, flush=True)
        return None

    user_response = response.json()
    print(f"User created: {user_response}", flush=True)
    return user_response.get("userId")

##
## find_user_project_by_name
##
def find_user_project_by_name(userUuid, projectName):
    print(f"Searching for project with name {projectName}", flush=True)
    if(userUuid == None):
        print(f"User UUID is None", flush=True)
        return None
    
    url = f"{hostApi}/confgroup?type=Transcription&userId={userUuid}"
    print(f"Fetching projects from {url}", flush=True)
    response = requests.get(url, headers=headers, verify=verify_ssl_certs)
    if response.status_code != 200:
        print(f"Failed to fetch projects: {response.status_code}", flush=True)
        return None

    projectUuid = None
    projectCount = 0
    projects = response.json()
    for project in projects:
        if project.get('name', '').lower() == projectName.lower():
            print(f"Found project with name {projectName}", flush=True)
            if project.get('creator') == userUuid:
                projectUuid = project.get('confGroupId')
            else:
                print(f"Project with name {projectName} found but creator does not match", flush=True)
        projectCount += 1

    print(f"Found {projectCount} projects", flush=True)
    if(projectUuid):
        print(f"Project with name {projectName} found", flush=True)
        return projectUuid
    else:
        print(f"Project with name {projectName} not found", flush=True)
        return None

##
## create_new_sa_config
##
def create_new_sa_config(context_id):
    url = f"{hostApi}/sa/config"
    body = {
        "contextId": context_id,
        "name": context_id,
        "meetingMinutes": {
            "enabled": True,
        },
        "entities": [],
        "keywords": [],
        "summary": True,
        "wordCloud": True
    }
    print(f"Creating new SA config for context {context_id}", flush=True)
    response = requests.post(url, json=body, headers=headers, verify=verify_ssl_certs)
    if response.status_code != 200:
        print(f"Failed to create SA config: {response.status_code}", flush=True)
        print(response.text, flush=True)
        return None

    sa_config_response = response.json()
    print(f"SA config created: {sa_config_response}", flush=True)
    return sa_config_response.get("saConfId")

##
## create_user_group
##
def create_user_group(context_id, user_id):
    url = f"{hostAuth}/user-group"
    body = {
        "userGroupType": "Context",
        "color": project_color,
        "contextId": context_id,
        "name": context_id,
        "lead": user_id
    }
    print(f"Creating new user group for context {context_id}", flush=True)
    response = requests.post(url, json=body, headers=headers, verify=verify_ssl_certs)
    if response.status_code != 200:
        print(f"Failed to create user group: {response.status_code}", flush=True)
        print(response.text, flush=True)
        return None

    user_group_response = response.json()
    print(f"User group created: {user_group_response}", flush=True)
    return user_group_response.get("userGroupId")

##
## add_user_to_group
##
def add_user_to_group(group_id, user_id):
    url = f"{hostAuth}/user-group/{group_id}/members"
    body = {
        "addUsers": [user_id]
    }
    print(f"Adding user {user_id} to group {group_id}", flush=True)
    response = requests.put(url, json=body, headers=headers, verify=verify_ssl_certs)
    if response.status_code != 200:
        print(f"Failed to add user to group: {response.status_code}", flush=True)
        print(response.text, flush=True)
        return None

    add_user_response = response.json()
    print(f"User added to group: {add_user_response}", flush=True)
    return 

##
## modify_project
##
def modify_project(project_id, sa_config_id, user_group_id):

    sl_jwt = generate_short_lived_jwt(project_id)

    if(sl_jwt == None):
        print(f"Failed to generate short-lived JWT", flush=True)
        return None
    
    print(f"Short-lived JWT generated: {sl_jwt[:16]}...{sl_jwt[-16:]}", flush=True)

    l_headers = {"Authorization": sl_jwt}

    url = f"{hostApi}/confgroup/{project_id}"
    body = {
        "defaultSaConfig": sa_config_id,
        "visibleOnlyTo": {
            "userGroup": user_group_id
        }
    }
    print(f"Modifying project {project_id}", flush=True)
    response = requests.put(url, json=body, headers=l_headers, verify=verify_ssl_certs)
    if response.status_code != 200:
        print(f"Failed to modify project: {response.status_code}", flush=True)
        print(response.text, flush=True)
        return None

    modify_project_response = response.json()
    print(f"Project modified: {modify_project_response}", flush=True)
    return modify_project_response.get("confGroupId")


##
## create_new_project
##
def create_new_project(userUuid, projectName, description):
    url = f"{hostApi}/confgroup"
    body = {
        "name": projectName,
        "description": description,
        "type": "Transcription",
        "creator": userUuid,
        "color": project_color,
        "timeZone": project_timezone,
        "weekStartsOn": project_week_starts_on,
        "timeFormat": "12hour",
        "dateFormat": "mm/dd/yyyy",
        "asrSettingsTranscription": {
            "acousticModelRealTime": "VoiceGain-kappa",
            "acousticModelNonRealTime": "whisper:medium",
            "languages": project_languages,
            "hints": project_hints
        },
        "formatters": [
            {
                "type": "spelling",
                "parameters": {
                    "lang": "en-US"
                }
            },
            {
                "type": "digits",
            },
            {
                "type": "profanity",
                "parameters": {
                    "mask": "partial"
                }
            }
        ]
    }
    print(f"Creating new project with name {projectName}", flush=True)
    response = requests.post(url, json=body, headers=headers, verify=verify_ssl_certs)
    if response.status_code != 200:
        print(f"Failed to create project: {response.status_code}", flush=True)
        print(response.text, flush=True)
        return None

    project_response = response.json()
    print(f"Project created: {project_response}", flush=True)
    project_id = project_response.get("confGroupId")

    # Create SA config for the new project
    sa_config_id = create_new_sa_config(project_id)

    # Create user group for the new project
    user_group_id = create_user_group(project_id, userUuid)

    # Add user to the group
    add_user_to_group(user_group_id, userUuid)

    # Modify project with SA config and user group
    result = modify_project(project_id, sa_config_id, user_group_id)
    if(result == None):
        print(f"ERROR Failed to modify project", flush=True)
        return None

    return project_id

##
## upload_data_file
##
def upload_data_file(project_id, data_fname, mime_type):
    path, fname = os.path.split(data_fname)
    print("Uploading {}/{}".format(path, fname), flush=True)

    data_body = {
        "name": re.sub("[^A-Za-z0-9]+", "-", fname),
        "description": data_fname,
        "contentType": mime_type,
        "tags": ["upload from import_webex_meeting"]
    }

    multipart_form_data = {
        'file': (data_fname, open(data_fname, 'rb'), mime_type),
        'objectdata': (None, json.dumps(data_body), "application/json")
    }

    data_url = f"{hostApi}/data/file?contextId={project_id}"

    max_retries = 5
    retry_count = 0
    while retry_count < max_retries:
        data_response_raw = requests.post(data_url, files=multipart_form_data, headers=headers, verify=verify_ssl_certs)
        code = data_response_raw.status_code
        print("   response code: {}".format(code))

        if code == 200:
            data_response = data_response_raw.json()
            print("data response: {}".format(data_response), flush=True)
            if data_response.get("status") == "BAD_REQUEST":
                print("error uploading file {}".format(data_fname), flush=True)
                return None
            object_id = data_response["objectId"]
            print("objectId: {}".format(object_id), flush=True)
            return object_id
        elif code == 429:
            retry_after = data_response_raw.headers.get("Retry-After")
            if retry_after is None:
                print("rate limit exceeded but response missing Retry-After", flush=True)
                return None
            print("rate limit exceeded, waiting {} seconds".format(retry_after), flush=True)
            time.sleep(int(retry_after))
            retry_count += 1
        else:
            print("unexpected response code", flush=True)
            print(data_response_raw.text, flush=True)
            return None

    print("Max retries exceeded", flush=True)
    return None

##
## create_meeting
##
def create_meeting(context_id, label, creator, video_id, audio_id, num_speakers=1):
    url = f"{hostApi}/asr/meeting?contextId={context_id}"
    body = {
        "label": label,
        "creator": creator,
        "persistSeconds": persist_seconds,
        "videoId": video_id,
        "audio": [
            {
                "source": audio_id,
                "diarization" : {
                    "minSpeakers": num_speakers,
                    "maxSpeakers": num_speakers
                }
            }
        ],
        "tags": ["imported_webex_meeting"],
        "metadata" : [
            {
                "name" : "upload-sccript",
                "value" : "import_webex_meeting.py"
            }
        ]
    }
    print(f"Creating meeting with label {label} for context {context_id}", flush=True)
    response = requests.post(url, json=body, headers=headers, verify=verify_ssl_certs)
    if response.status_code != 200:
        print(f"Failed to create meeting: {response.status_code}", flush=True)
        print(response.text, flush=True)
        return None

    meeting_response = response.json()
    print(f"Meeting created: {meeting_response}", flush=True)
    return meeting_response.get("meetingSessionId")

# Example usage
user_uuid = find_user_by_email(email_to_find)
print(f"User UUID for email {email_to_find}: {user_uuid}", flush=True)

if(user_uuid == None):
    print(f"User with email `{email_to_find}` not found, creating a new one", flush=True)
    user_uuid = create_user(email_to_find, user_fname, user_lname, user_role, user_notification)
    print(f"New User UUID: {user_uuid}", flush=True)

if(user_uuid == None):
    print(f"Failed to create or find user", flush=True)
    exit()

project_uuid = find_user_project_by_name(user_uuid, project_name_to_find)
print(f"Project UUID for project name {project_name_to_find}: {project_uuid}", flush=True)

if(project_uuid == None):
    print(f"Project with name `{project_name_to_find}` not found, creating a new one", flush=True)
    project_uuid = create_new_project(user_uuid, project_name_to_find, "Project created for Webex meeting import")
    print(f"New Project UUID: {project_uuid}", flush=True)

if(project_uuid == None):
    print(f"Failed to create or find project", flush=True)
    exit()

audio_id = upload_data_file(project_uuid, audio_fname, audio_mime_type)
print(f"Audio ID for file {audioFile}: {audio_id}", flush=True)

video_id = upload_data_file(project_uuid, video_fname, video_mime_type)
print(f"Video ID for file {videoFile}: {video_id}", flush=True)

meeting_id = create_meeting(project_uuid, meeting_label, user_uuid, video_id, audio_id)
print(f"Meeting ID: {meeting_id}", flush=True)

