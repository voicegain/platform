import requests
import os

MISTRAL_API_KEY = "foo"

response = requests.post(
    "https://ofjm0i03ba4l4a-7860.proxy.runpod.net/v1/chat/completions",
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {MISTRAL_API_KEY}"
    },
    json={
        "model": "mistral-tiny",
        "messages": [{"role": "user", "content": "Who is the most renowned French writer?"}]
    }
)

print(response.status_code)
print(response.content)