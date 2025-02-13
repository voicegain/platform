import configparser
import requests

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

print(f"   Host Auth: {hostAuth}", flush=True)
print(f"    Host API: {hostApi}", flush=True)


email_to_find = "jj@gmail.com"
project_name_to_find = "Clean Project"


def find_user_by_email(email):
    url = f"{hostAuth}/user"
    print(f"Fetching users from {url}", flush=True)
    response = requests.get(url, headers=headers)
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

def find_user_project_by_name(userUuid, projectName):
    print(f"Searching for project with name {projectName}", flush=True)
    if(userUuid == None):
        print(f"User UUID is None", flush=True)
        return None
    
    url = f"{hostApi}/confgroup?type=Transcription&userId={userUuid}"
    print(f"Fetching projects from {url}", flush=True)
    response = requests.get(url, headers=headers)
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


# Example usage
user_uuid = find_user_by_email(email_to_find)
print(f"User UUID for email {email_to_find}: {user_uuid}", flush=True)

project_uuid = find_user_project_by_name(user_uuid, project_name_to_find)
print(f"Project UUID for project name {project_name_to_find}: {project_uuid}", flush=True)


