import requests
import os

MISTRAL_API_KEY = ""

response = requests.post(
    "https://4xxxj4xxxkh1vw-5000.proxy.runpod.net/v1/chat/completions",
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json"
        #,"Authorization": f"Bearer {MISTRAL_API_KEY}"
    },
    json={
        #"model": "mistral-tiny",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Who is the most renowned French writer?"}
            ]
        #"prompt": "Who is the most renowned French writer?"
    }
)

print(response.status_code)
print(response.content)
print(response)