import requests

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/7p1Ofvcwsv7UBPoFNcpI?output_format=pcm_16000"

headers = {
  "Accept": "audio/wav",
  "Content-Type": "application/json",
  "xi-api-key": "<key>"
}

data = {
  "text": "<prosody rate=\"medium\">To verify your account, I will need 3 things:<break time=\"0.5s\"/> your full name,<break time=\"0.3s\"/> your date of birth,<break time=\"0.3s\"/> and your address. Can you provide me those 3 things please?</prosody>",
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
}

response = requests.post(url, json=data, headers=headers)
with open('11-labs-output-e1.wav', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
