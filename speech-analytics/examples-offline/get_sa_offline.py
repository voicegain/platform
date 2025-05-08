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

upload_audio = requests.post(
    url + '/data/audio',
    headers={'Authorization': 'Bearer ' + jwt},
    json={
        'name': 'testing_audio_file_filip',
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
    },
)

audio_id = None
if upload_audio.status_code == 200:
    print('File Upload: ' + str(upload_audio.status_code))
    audio_id = upload_audio.json()['objectId']

    create_sa_session = requests.post(
        url + '/sa/offline',
        headers={'Authorization': 'Bearer ' + jwt},
        json={
            'label': 'test_sa_session_by_filip',
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
        },
    )

    if create_sa_session.status_code == 200:
        print('SA Session Creation: ' + str(create_sa_session.status_code))
        sa_session_id = create_sa_session.json()['saSessionId']

        polls = 0
        while True:
            polls += 1
            get_sa_session = requests.get(
                url + '/sa/offline/' + sa_session_id,
                headers={'Authorization': 'Bearer ' + jwt},
            )

            if get_sa_session.status_code == 200:
                if get_sa_session.json()['progress']['phase'] == 'DONE':
                    print(
                        f'''
                        SA Session Status:
                        Status code: {get_sa_session.status_code}
                        Info: {get_sa_session.json()}
                        '''
                    )
                    break
                elif get_sa_session.json()['progress']['phase'] == 'ERROR':
                    print(
                        f'''
                        Error while processing SA session:
                        Status code: {get_sa_session.status_code}
                        Info: {get_sa_session.json()}
                        '''
                    )
                    break
                else:
                    print(
                        f'''
                        SA Session Status:
                        Status code: {get_sa_session.status_code}
                        Info: {get_sa_session.json()}
                        Sleeping for 10 seconds...
                        '''
                    )

            if polls >= max_polls:
                print(
                    f'''
                    Max number of polls reached. Deleting SA session...
                    '''
                )
                break
            
            time.sleep(sleep_time)

        delete_sa_session = requests.delete(
            url + '/sa/offline/' + sa_session_id,
            headers={'Authorization': 'Bearer ' + jwt},
        )

        print('SA Session Deletion: ' + str(delete_sa_session.status_code))
        if delete_sa_session.status_code != 200:
            print(
                f'''
                Error deleting SA session:
                Info: {delete_sa_session.text}
                '''
            )

    else:
        print(
            f'''
            Error creating SA session:
            Status code: {create_sa_session.status_code}
            Info: {create_sa_session.text}
            '''
        )

    delete_audio = requests.delete(
        url + '/data/' + audio_id,
        headers={'Authorization': 'Bearer ' + jwt},
    )

    print('File Deletion: ' + str(delete_audio.status_code))
    if delete_audio.status_code != 200:
        print(
            f'''
            Error deleting audio:
            Info: {delete_audio.text}
            '''
        )

else:
    print(
        f'''
        Error uploading audio:
        Status code: {upload_audio.status_code}
        Info: {upload_audio.text}
        '''
    )
