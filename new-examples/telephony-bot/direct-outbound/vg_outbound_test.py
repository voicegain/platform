import requests
import time
import configparser

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')
CONF_NAME=config['DEFAULT']['CONFIG']

# Read values from the DEFAULT section
JWT = config[CONF_NAME]['JWT']
APP_ID = config[CONF_NAME]['AIVRAPPID']
DESTINATION = config[CONF_NAME]['DESTPHONE']

print("CONF_NAME: {}".format(CONF_NAME), flush=True)
print("DESTINATION: {}".format(DESTINATION), flush=True)
print("APP_ID: {}".format(APP_ID), flush=True)


class ApiClient:
    def __init__(self):
        self.base_url = "https://{hostport}/{urlprefix}/".format(
            hostport=config[CONF_NAME]['HOSTPORT'],
            urlprefix=config[CONF_NAME]['URLPREFIX']
        )
        self.jwt = JWT
        print("Base URL: {}".format(self.base_url))

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
        print("Dial response: {}".format(response.text))
        json_response = response.json()
        print("Dial response: {}".format(json_response))
        print("Dial response code: {}".format(response.status_code))
        return json_response

    def make_request(self, method, url, json=None):
        print("Making request: {}".format(url))
        headers = {"Authorization": self.jwt}
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            json=json
        )
        return response

TOTAL = 100
SLEEP = 5

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
    print("Dialing to destination: {}, remaining: {}".format(DESTINATION, remain))
    api_client.dial(destination=DESTINATION)
    time.sleep(SLEEP)
