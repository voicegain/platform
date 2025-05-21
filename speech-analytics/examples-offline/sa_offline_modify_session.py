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
    'file': (
        file_name,
        open(audio, 'rb').read(),
        'audio/wav'
    ),
    'objectdata': (
        None,
        json.dumps({
            'name': file_name,
            'description' : file_name,
            'contentType' : 'audio/wav',
            'tags': ['test'],
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
    'optimizeForWebUi': 'level2', # Set to level2 to support Voicegain Speech Analytics App. If you do not need the additional fields then set to none to save resources and speed up processing.
    'audio': [{
        'source': {
            'dataObjectUuid': audio_id,
        },
    }],
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


sa_modify_body = {
    'label': 'test_sa_session_modified',
    'persistSeconds': 400000,
    #'context': context_id
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
def test(audio, sa_session, sa_modify_session, sa_data):
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

    # 2. Create SA session
    sa_session["audio"][0]["source"]["dataObjectUuid"] = audio_id

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

    print(f'SA Session ID: {create_sa_session.json()["saSessionId"]}')
    sa_session_id = create_sa_session.json()['saSessionId']

    # 3. Poll for SA session status until done or error
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
                sa_session_persist = get_sa_session.json()['persist']
                sa_session_label = get_sa_session.json()['label']
                #print(f'Info: {get_sa_session.json()}')
                break
            elif get_sa_session.json()['progress']['phase'] == 'ERROR':
                print('Error while processing SA session:')
                print(f'Status code: {get_sa_session.status_code}')
                print(f'Info: {get_sa_session.json()}')
                sa_session_persist = get_sa_session.json()['persist']
                sa_session_label = get_sa_session.json()['label']
                break
            else:
                print('SA Session still processing...')
                print(f'Status code: {get_sa_session.status_code}')
                #print(f'Info: {get_sa_session.json()}')
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
            exit()
        
        time.sleep(sleep_time)

    # 4. Get SA session Data:
    if get_sa_session.status_code == 200:
        get_sa_session_data = requests.get(
            url + '/sa/offline/' + sa_session_id + '/data',
            headers={'Authorization': jwt},
            params=sa_data
        )

        print('Getting SA session data...')
        print(f'Status code: {get_sa_session_data.status_code}')
        print(f'Info: {get_sa_session_data.json()}')

    # 5. modify session
    modify_sa_session = requests.put(
        url + '/sa/offline/' + sa_session_id,
        headers={'Authorization': jwt},
        json=sa_modify_session,
    )

    print('SA Session Modification...')
    print(f'Status code: {modify_sa_session.status_code}')

    if modify_sa_session.status_code != 200:
        print(f'Info: {modify_sa_session.json()}')
        delete_sa_session(sa_session_id)
        delete_audio(audio_id)
        exit()

    # 6. Poll again and check if modification was successful
    get_sa_session = requests.get(
        url + '/sa/offline/' + sa_session_id,
        headers={'Authorization': jwt},
    )

    print('Checking if modification was successful...')
    print(f'Status code: {get_sa_session.status_code}')

    if get_sa_session.status_code != 200:
        print(f'Info: {modify_sa_session.json()}')
        delete_sa_session(sa_session_id)
        delete_audio(audio_id)
        exit()
    
    if get_sa_session.json()['persist'] != sa_session_persist or get_sa_session.json()['label'] != sa_session_label:
        print('Modification was successful!')
    else:
        print('Modification was not successful!')

    print(f'New persist: {get_sa_session.json()["persist"]}')
    print(f'Old persist: {sa_session_persist}')
    print(f'New label: {get_sa_session.json()["label"]}')
    print(f'Old label: {sa_session_label}')

    # 7. Final cleanup
    delete_sa_session(sa_session_id)
    delete_audio(audio_id)
    print('Test complete!')

test(audio_body, sa_session_body, sa_modify_body, sa_data_params)