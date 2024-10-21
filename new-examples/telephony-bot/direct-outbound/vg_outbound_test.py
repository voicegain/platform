import requests
import time


JWT = "<JWT>"
APP_ID = "6fa817d0-de45-4e95-8f40-f4256af0316d"


class ApiClient:
    def __init__(self):
        self.base_url = "https://api.ascalon.ai/v1/"
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


TOTAL = 3
SLEEP = 8
for _ in range(TOTAL):
    api_client = ApiClient()
    api_client.dial(
        # Prod bot
        # To call prod bot, add "prod=true" appData to ahcm-inbound-traversal-bot in Dev env
        # destination="+13464760718"  # Prod bot

        # Dev bot
        destination="+14693333606"
    )
    time.sleep(SLEEP)
