import requests
import os

transcript = ""

FW_API_KEY = ""

response = requests.post(
    "https://api.fireworks.ai/inference/v1/chat/completions",
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {FW_API_KEY}"
    },
    json={
        "model": "accounts/fireworks/models/mixtral-8x7b-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that answers questions about transcripts."},
            {"role": "user", "content": "Here is transcript: "+transcript+" \n Prompt about this transcript: what is going on?"}
            ]
    }
)

print(response.status_code)
print(response.content)
print(response)