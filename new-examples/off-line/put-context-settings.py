import requests, json
import configparser

cfg = configparser.ConfigParser()
cfg.read("config.ini")
configSection = cfg.get("DEFAULT", "CONFIG")
protocol = cfg.get(configSection, "PROTOCOL")
hostPort = cfg.get(configSection, "HOSTPORT")
JWT = cfg.get(configSection, "JWT")
urlPrefix = cfg.get(configSection, "URLPREFIX")
ctxId = cfg.get(configSection, "CTX_ID")

request_body = {
    "formatters" : [
        {
            "type": "digits"
        }
        # {
        #     "type": "basic",
        #     "parameters": {"enabled": False}
        # }
        ,{
            "type": "enhanced",
            "parameters": {
            "CC": True,
            "SSN": True,
            "URL": True,
            "PHONE": True,
            "EMAIL": True
            }
        },
        {
            "type": "profanity",
            "parameters": {"mask": "partial"}
        },
        {
            "type": "spelling",
            "parameters": {"lang": "en-US"}
        }
        ,{
            "type": "redact",
            "parameters": {
                "CC": "partial",
                "ZIP": "full",
                "PERSON": "[PERSON]",
                "EMAIL" : "partial",
                "PHONE" : "partial",
                "SSN" : "partial",
            }
        }
        ,{
            "type": "regex",
            "parameters": {
                "pattern": "([1-9]|1[0-2]):[0-5][0-9] [ap]m",
                "mask": "full",
                "options": "IA"
            }
        }
    ]   
}

host = f"{protocol}://{hostPort}/{urlPrefix}"

headers = {"Authorization":JWT}

url = "{}/confgroup/{}".format(host, ctxId)
print(f"making PUT Context request {url}...", flush=True)
asr_response = requests.put(url, json=request_body, headers=headers).json()

print(f"Response: {asr_response}", flush=True)