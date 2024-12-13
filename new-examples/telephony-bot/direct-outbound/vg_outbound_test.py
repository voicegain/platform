import requests
import time
import configparser

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')
CONF_NAME="CLOUD-DEV"

# Read values from the DEFAULT section
JWT = config[CONF_NAME]['JWT']
APP_ID = config[CONF_NAME]['AIVRAPPID']
DESTINATION = config['DEFAULT']['DESTPHONE']

class ApiClient:
    def __init__(self):
        self.base_url = "https://{hostport}/{urlprefix}/".format(
            hostport=config[CONF_NAME]['HOSTPORT'],
            urlprefix=config[CONF_NAME]['URLPREFIX']
        )
        self.jwt = JWT

    def dial(self, destination, app_id=APP_ID):
        response = self.make_request(
            method="POST",
            url="{base_url}aivr/dial/{destination}".format(
                base_url=self.base_url, destination=destination
            ),
            json={
                "aivrAppId": app_id
            }
        )
        response = response.json()
        print("Dial response: {}".format(response))
        return response

    def make_request(self, method, url, json=None):
        headers = {"Authorization": self.jwt}
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            json=json
        )
        return response

TOTAL = 5
SLEEP = 2
remain = TOTAL
for _ in range(TOTAL):
    print("Remain: {}".format(remain))
    remain -= 1
    api_client = ApiClient()
    # Prod bot
    # To call prod bot, add "prod=true" appData to ahcm-inbound-traversal-bot in Dev env
    # destination="+13464760718"  # Prod bot

    # Dev bot
    # destination="+14693333606"
    api_client.dial(destination=DESTINATION)
    time.sleep(SLEEP)
