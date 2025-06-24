from configparser import ConfigParser
import requests
import time
import os
import json
import re

dir_path = os.path.dirname(os.path.realpath(__file__))

config = ConfigParser()
config.read(os.path.join(dir_path, 'config.ini'))

conf = config['DEFAULT']['CONFIG']
jwt = config[conf]['JWT']
url = config[conf]['PROTOCOL'] + '://' + config[conf]['HOSTPORT'] + '/' + config[conf]['URLSUFFIX']
file_name = re.sub("[^A-Za-z0-9]+", "-", config['DEFAULT']['INPUTFILE'])
audio = os.path.join(dir_path, config['DEFAULT']['INPUTFILE'])
max_polls = int(config['DEFAULT']['MAX_POLLS'])
sleep_time = int(config['DEFAULT']['SLEEP_TIME'])
with open(audio, 'rb') as audio_file:
    audio_content = audio_file.read()


audio_body = {
    'file': (file_name, audio_content, 'audio/wav'),
    'objectdata': (
        None,
        json.dumps({
            'name': file_name,
            'description' : file_name,
            'contentType' : 'audio/wav',
        }),
        'application/json'
    ),
}
audio_id = None

# This is a simplified call body
call_body = {
    "startTime": "2019-08-24T14:15:22Z",
    "endTime": "2019-08-24T14:25:22Z",
    "direction": "inbound",
    "recording": audio_id,
    "numAudioChannels": 1,
    "numSpkChannels": 2,
    "callCenterCallId": "string",
    "agent": None,
    "queue": None,
    "tags": [
        "test"
    ],
}


sa_session_body = {
    'label': 'test_sa_session',
    #'saConfig': sa_config_id, # If none given, default config will be used
    'settings': {
        'asr': {
            'languages': ['en-us'],
            'acousticModel': 'VoiceGain-omega',
            'sensitivity': 0.5,
            'speedVsAccuracy': 0.5,
            'hints' : ['Pentium:10']
        },
    },
    'optimizeForWebUi': 'level2', # Set to level2 to support Voicegain Speech Analytics App. If you do not need the additional fields then set to none to save resources and speed up processing.
    'tags': ['testing'],
}
sa_session_id = None

# Modify this to get the data you want. True means the data is returned, False means it is not.
sa_data_params = {
    'words': True,
    'audio': True,
    'meta': True,
    'wordcloud': True,
    'summary': True,
    'keywords': True,
    'entities': True,
    'phrases': True,
}

# Delete functions to clean up after the test
def delete_audio(id):
    delete_audio = requests.delete(
        url + '/data/' + id,
        headers={'Authorization': jwt},
    )
    print('File Deletion...')
    print(f'Status code: {delete_audio.status_code}')
    if delete_audio.status_code != 200:
        print(f'Info: {delete_audio.json()}')

def delete_sa_session(id):
    while True:
        delete_sa_session = requests.delete(
            url + '/sa/offline/' + id,
            headers={'Authorization': jwt},
        )
        print('SA Session Deletion...')
        print(f'Status code: {delete_sa_session.status_code}')
        if delete_sa_session.status_code != 200:
            print(f'Info: {delete_sa_session.json()}')
            print('Sleeping for 10 seconds...')
            time.sleep(10)
        else:
            break

def delete_call(id):
    delete_call = requests.delete(
        url + '/sa/call/' + id,
        headers={'Authorization': jwt},
    )
    print('Call Deletion...')
    print(f'Status code: {delete_call.status_code}')
    if delete_call.status_code != 200:
        print(f'Info: {delete_call.json()}')

# Test function
def test(audio, sa_session, sa_data, call):
    # 1. Upload audio to datastore
    upload_audio = requests.post(
        url + '/data/file',
        headers={'Authorization': jwt},
        files=audio,
    )

    print('File Upload...')
    print(f'Status code: {upload_audio.status_code}')

    if upload_audio.status_code != 200:
        exit()
        
    audio_id = upload_audio.json()['objectId']
    print(f'Audio ID: {audio_id}')

    # 2. Create Call
    call["recording"] = audio_id
    create_call = requests.post(
        url + '/sa/call',
        headers={'Authorization': jwt},
        json=call,
    )

    print('Call Creation...')
    print(f'Status code: {create_call.status_code}')

    if create_call.status_code != 200:
        print(f'Info: {create_call.json()}')
        delete_audio(audio_id)
        exit()

    call_id = create_call.json()['callId']
    print(f'Call ID: {call_id}')

    # 3. Create SA session
    create_sa_session = requests.post(
        url + '/sa/offline/call/' + call_id,
        headers={'Authorization': jwt},
        json=sa_session,
    )

    print('SA Session Creation...')
    print(f'Status code: {create_sa_session.status_code}')

    if create_sa_session.status_code != 200:
        print(f'Info: {create_sa_session.json()}')
        delete_audio(audio_id)
        delete_call(call_id)
        exit()

    print(f'SA Session ID: {create_sa_session.json()["saSessionId"]}')
    sa_session_id = create_sa_session.json()['saSessionId']

    # 4. Poll for SA session status until done or error
    print('Polling for SA session status...')
    polls = 0
    while True:
        polls += 1
        get_sa_session = requests.get(
            url + '/sa/offline/' + sa_session_id,
            headers={'Authorization': jwt},
        )

        if get_sa_session.status_code == 200:
            if get_sa_session.json()['progress']['phase'] == 'DONE':
                print('SA Session Done!')
                print(f'Status code: {get_sa_session.status_code}')
                #print(f'Info: {get_sa_session.json()}')
                break
            elif get_sa_session.json()['progress']['phase'] == 'ERROR':
                print('Error while processing SA session:')
                print(f'Status code: {get_sa_session.status_code}')
                print(f'Info: {get_sa_session.json()}')
                break
            else:
                print('SA Session still processing...')
                print(f'Status code: {get_sa_session.status_code}')
                print(f'Info: {get_sa_session.json()["progress"]["phase"]}')
                print('Sleeping for 10 seconds...')
        else:
            print('Error getting SA session:')
            print(f'Status code: {get_sa_session.status_code}')
            print(f'Info: {get_sa_session.json()}')
            break

        if polls >= max_polls:
            print('Max number of polls reached. Deleting SA session...')
            delete_sa_session(sa_session_id)
            delete_audio(audio_id)
            delete_call(call_id)
            exit()
        
        time.sleep(sleep_time)

    # 5. Get SA session Data:
    if get_sa_session.status_code == 200:
        get_sa_session_data = requests.get(
            url + '/sa/offline/' + sa_session_id + '/data',
            headers={'Authorization': jwt},
            params=sa_data
        )

        print('Getting SA session data...')
        print(f'Status code: {get_sa_session_data.status_code}')
        print(f'Info: {get_sa_session_data.json()}')

    # 6. Final cleanup
    delete_sa_session(sa_session_id)
    delete_audio(audio_id)
    delete_call(call_id)
    print('Test complete!')

test(audio_body, sa_session_body, sa_data_params, call_body)