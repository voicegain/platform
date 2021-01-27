## Prerequisites
* Account with Voicegain: https://console.voicegain.ai/signup
* JWT token for authentication: https://support.voicegain.ai/hc/en-us/articles/360028023691-JWT-Authentication

# ffmpeg-rtp-ws.py

Before running you will need to install:
```
pip install websockets
pip install ffmpy
```
This python script does the following:
* starts Voicegain transcription session configured for:
    * audio input via RTP stream
    * result of transcription sent incrementally via websocket 
* opens an audio file using `ffmpeg`
* uses `ffmpeg` to stream audio real-time to RTP ip:port provided in response to opening Voicegain session
* opens websocket to url provided in response to opening Voicegain session
* receives messages via websocket and assembles them into transcript which is printed to console
