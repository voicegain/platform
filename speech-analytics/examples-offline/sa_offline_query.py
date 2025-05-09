from configparser import ConfigParser
import requests
import base64
import time

config = ConfigParser()
config.read(r'C:\Users\FilipJarmulak\API_testing\MISC-68\platform\speech-analytics\examples-offline\config.ini')

conf = config['DEFAULT']['CONFIG']
jwt = config[conf]['JWT']
url = config[conf]['PROTOCOL'] + '://' + config[conf]['HOSTPORT'] + '/' + config[conf]['URLSUFFIX']
audio = config['DEFAULT']['INPUTFILE']
max_polls = int(config['DEFAULT']['MAX_POLLS'])
sleep_time = int(config['DEFAULT']['SLEEP_TIME'])
with open(audio, 'rb') as f:
    audio64 = base64.b64encode(f.read()).decode('utf-8')


audio_body = {
    'name': 'testing_audio',
    'contentType': 'audio/wav',
    'encryption': 'none',
    'tags': ['testing', 'audio'],
    'audio': {
        'source': {
            'inline': {
                'data': audio64,
            },
        },
        'format': 'PCMA',
        'rate': 8000,
    },
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
        headers={'Authorization': 'Bearer ' + jwt},
    )
    print('File Deletion...')
    print(f'Status code: {delete_audio.status_code}')
    if delete_audio.status_code != 200:
        print(f'Info: {delete_audio.json()}')

def delete_sa_session(id):
    while True:
        delete_sa_session = requests.delete(
            url + '/sa/offline/' + id,
            headers={'Authorization': 'Bearer ' + jwt},
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
        url + '/data/audio',
        headers={'Authorization': 'Bearer ' + jwt},
        json=audio,
    )

    print('File Upload...')
    print(f'Status code: {upload_audio.status_code}')

    if upload_audio.status_code != 200:
        print(f'Info: {upload_audio.json()}')
        exit()
        
    audio_id = upload_audio.json()['objectId']

    # 2. Create SA session
    create_sa_session = requests.post(
        url + '/sa/offline',
        headers={'Authorization': 'Bearer ' + jwt},
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
        headers={'Authorization': 'Bearer ' + jwt},
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