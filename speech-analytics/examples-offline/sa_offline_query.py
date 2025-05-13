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


audio_body = {
    'file': (file_name, open(audio, 'rb').read(), 'audio/wav'),
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


sa_session_body = {
    'label': 'test_sa_session',
    #'saConfig': sa_config_id, # If none given, default config will be used
    'settings': {
        'asr': {
            'languages': ['en-us'],
            'sensitivity': 0.5,
            'speedVsAccuracy': 0.5,
        },
    },
    'tags': ['testing'],
    'audio': [{
        'source': {
            'dataObjectUuid': audio_id,
        },
    }],
}
sa_session_id = None

#
sa_query_params = {
    'fromAllContexts': False,
    'limit': 10,
    'detailed': True,
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


# Test function
def test(audio, sa_session, sa_query):
    # 1. Upload audio to datastore
    upload_audio = requests.post(
        url + '/data/file',
        headers={'Authorization': jwt},
        files=audio,
    )

    print('File Upload...')
    print(f'Status code: {upload_audio.status_code}')
    print(f'Info: {upload_audio.json()}')

    if upload_audio.status_code != 200:
        exit()
        
    audio_id = upload_audio.json()['objectId']

    # 2. Create SA session
    create_sa_session = requests.post(
        url + '/sa/offline',
        headers={'Authorization': jwt},
        json=sa_session,
    )

    print('SA Session Creation...')
    print(f'Status code: {create_sa_session.status_code}')

    if create_sa_session.status_code != 200:
        print(f'Info: {create_sa_session.json()}')
        delete_audio(audio_id)
        exit()

    sa_session_id = create_sa_session.json()['saSessionId']

    # 3. Query SA sessions
    query_sa_sessions = requests.get(
        url + '/sa/offline',
        headers={'Authorization': jwt},
        params=sa_query
    )

    print('Query SA sessions...')
    print(f'Status code: {query_sa_sessions.status_code}')
    print(f'Info: {query_sa_sessions.json()}')

    # 4. Final cleanup
    delete_sa_session(sa_session_id)
    delete_audio(audio_id)
    print('Test complete!')

test(audio_body, sa_session_body, sa_query_params)