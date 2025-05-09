import requests
from configparser import ConfigParser

config = ConfigParser()
config.read(r'C:\Users\FilipJarmulak\API_testing\MISC-68\platform\speech-analytics\examples-offline\config.ini')

conf = config['DEFAULT']['CONFIG']
jwt = config[conf]['JWT']
url = config[conf]['PROTOCOL'] + '://' + config[conf]['HOSTPORT'] + '/' + config[conf]['URLSUFFIX']

def delete_sa_config(id):
    delete_sa_config = requests.delete(
        url + '/sa/config/' + id,
        headers={'Authorization': 'Bearer ' + jwt},
    )
    print('SA Config Deletion...')
    print(f'Status code: {delete_sa_config.status_code}')
    if delete_sa_config.status_code != 200:
        print(f'Info: {delete_sa_config.json()}')

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
    delete_sa_session = requests.delete(
        url + '/sa/offline/' + id,
        headers={'Authorization': 'Bearer ' + jwt},
    )
    print('SA Session Deletion...')
    print(f'Status code: {delete_sa_session.status_code}')
    if delete_sa_session.status_code != 200:
        print(f'Info: {delete_sa_session.json()}')

delete_sa_session('INl2wAvDCTlmXZvHam0b')
