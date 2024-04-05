import requests

url = "https://4xxxj4xxxkh1vw-5000.proxy.runpod.net/v1/chat/completions"

headers = {
    "Content-Type": "application/json"
}

history = []

while True:
    user_message = input("> ")
    history.append({"role": "user", "content": user_message})
    data = {
        "mode": "chat",
        "character": "Example",
        "messages": history
    }

    response = requests.post(url, headers=headers, json=data, verify=False)
    print(response.text)
    assistant_message = response.json()['choices'][0]['message']['content']
    history.append({"role": "assistant", "content": assistant_message})
    print(assistant_message)