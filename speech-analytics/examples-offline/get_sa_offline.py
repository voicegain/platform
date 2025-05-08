from configparser import ConfigParser
import requests
import base64
config = ConfigParser()
config.read(r'C:\Users\FilipJarmulak\API_testing\MISC-68\platform\speech-analytics\examples-offline\config.ini')

conf = config['DEFAULT']['CONFIG']
jwt = config[conf]['JWT']
url = config[conf]['PROTOCOL'] + '://' + config[conf]['HOSTPORT'] + '/' + config[conf]['URLSUFFIX']
audio = config['DEFAULT']['INPUTFILE']
with open(audio, 'rb') as f:
    audio64 = base64.b64encode(f.read()).decode('utf-8')

upload_audio = requests.post(
    url + '/data/audio',
    headers={'Authorization': 'Bearer ' + jwt},
    json={
        'name': 'testing_audio_file_filip',
        'contentType': 'audio/wav',
        'encryption': 'none',
        'tags': ['testing', 'filip', 'audio'],
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

print(upload_audio.status_code)

oid = None
if upload_audio.status_code == 200:
    oid = upload_audio.json()['objectId']

    delete_audio = requests.delete(
        url + '/data/' + oid,
        headers={'Authorization': 'Bearer ' + jwt},
    )

    print(delete_audio.status_code)

else:
    print(f'Error uploading audio: {upload_audio.status_code} {upload_audio.text}')
