import requests, time, os, json, re
import configparser

## Note: rate-limit (429 code) handling is only partially implemented in this script

cfg = configparser.ConfigParser()
cfg.read("config.ini")
configSection = cfg.get("DEFAULT", "CONFIG")
protocol = cfg.get(configSection, "PROTOCOL")
hostPort = cfg.get(configSection, "HOSTPORT")
JWT = cfg.get(configSection, "JWT")
urlPrefix = cfg.get(configSection, "URLPREFIX")
aivrAppId = cfg.get(configSection, "AIVRAPPID")
destPhone = cfg.get(configSection, "DESTPHONE")

host = f"{protocol}://{hostPort}/{urlPrefix}"

print("host: {}".format(host))  

request_body = {
    "aivrAppId" : aivrAppId
}

url = f"{host}/aivr/dial/{destPhone}"

print("url: {}".format(url))

headers = {"Authorization":JWT}

try:
    data_response_raw = requests.post(url, json=request_body, headers=headers)
    code = data_response_raw.status_code
    print("   response code: {}".format(code))

    if(code != 200 and code != 429):
        print("unexpected response code")
        print(data_response_raw.text)
        exit()

    resp_headers = data_response_raw.headers
    print("response headers: {}".format(resp_headers))

    response_content = data_response_raw.json()
    print("response content: {}".format(response_content))
except Exception as e:
    print(str(data_response_raw))
    exit() 

print("done")