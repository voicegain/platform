import requests

SID = "test-sid"
seq = 1

URL = "http://localhost:8000/bot"


# init post
response = requests.post(
    URL,
    json={
        "sid": SID,
        "sequence": seq
    }
).json()
init_prompt = response['question']['text']
csid = response["csid"]

print("Assistant: {}".format(init_prompt))

while True:
    user_input = input("You: ")
    seq += 1
    response = requests.put(
        f"{URL}?seq={seq}", json={
            "sid": SID,
            "csid": csid,
            "events": [
                {
                    "sequence": str(seq),
                    "type": "input",
                    "timeMsec": 0,
                    "vuiResult": "MATCH",
                    "vuiAlternatives": [
                        {
                            "utterance": user_input,
                            "confidence": 1.0
                        }
                    ]
                }
            ]

        }
    ).json()
    print(response)
    print("Assistant: {}".format(response['question']['text']))


