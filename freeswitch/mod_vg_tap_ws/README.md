Illustration of the 2nd scenario from: https://support.voicegain.ai/hc/en-us/articles/13318469102100-Tapping-into-FreeSWITCH-for-real-time-transcription

```markdown
# Testing mod_vg_tap_ws for ASR with FreeSWITCH

This guide outlines steps for testing mod_vg_tap_ws for real-time Automatic Speech Recognition (ASR) using FreeSWITCH.
```
# 1. Invoking mod_vg_tap_ws Command

You can invoke the mod_vg_tap_ws command to start Speech-to-Text live streaming in several ways:

## a) From XML dialplan:

```xml
<action application="export" data="nolocal:api_on_answer=uuid_vg_tap_ws ${uuid} start http://localhost:8000/get_ws_url"/>
<action application="set" data="api_result=${uuid_vg_tap_ws ${uuid} start http://localhost:8000/get_ws_url}"/> 
```

## b) CLI Invocation during Live Call

```sh
uuid_vg_tap_ws 6292cbd6-a49c-4ff5-aecf-172cd0fda850 start/stop http://localhost:8000/get_ws_url
```

## c) Using Lua Script
```lua
api = freeswitch.API()
sofia = api:executeString("uuid_vg_tap_ws ${uuid} start http://localhost:8000/get_ws_url")
```
## d) Stop Streaming

If you want to stop streaming intentionally, invoke the same command with 'stop', for example:
```sh
uuid_vg_tap_ws 6292cbd6-a49c-4ff5-aecf-172cd0fda850 stop http://localhost:8000/get_ws_url
```

# 2. Writing Your Own Application

Once the dialplan is ready, you need to develop an application that listens for incoming HTTP requests and passes back the WebSocket URL to FreeSWITCH for live streaming. You can use the provided sample web service application vg_asr_service.py.

## Steps for Debian 12:

a) vg_asr_service.py is implemented based on the FastAPI library. You can choose to use any other libraries like Flask or Django.

b) Install required packages and run the application:
```sh
apt install python3.11-venv
python -m venv myenv
source myenv/bin/activate
pip install fastapi uvicorn websockets requests
uvicorn vg_asr_service:app --host 0.0.0.0 --port 8000
```

## 3. Testing

After setting up the application, make a call from one extension to another extension using FreeSWITCH. Once the B party answers the call, you will see live audio text messages on the vg_asr_service.py console.

```sh
LOGS: START processing:
SessionId L: 3-0lus5iw5l1iodrj5unkncgiv3vu3
SessionId R: 3-0lus5iw5l0rvcs5xoso64clzod28
Audio Websocket URL: wss://api.voicegain.ai/v1/3/socket/3f58e065-d04a-4de8-ad4e-951786128f0c
Captured audio id: b32472eb-a821-4a0a-992f-454e4f9adac4
Result Websocket Url L: wss://api.voicegain.ai/v1/3/plain/3-0lus5iw5l1iodrj5unkncgiv3vu3
Result Websocket Url R: wss://api.voicegain.ai/v1/3/plain/3-0lus5iw5l0rvcs5xoso64clzod28
L >> Starting WS receive thread
2024-04-09 04:00:49.682597 INFO: 127.0.0.1:35380 - "GET /get_ws_url HTTP/1.1" 200 OK
R << Starting WS receive thread
R << Exiting WS receive thread
2024-04-09 04:00:53.942004
L >> the person had
L >> the person had extension received 1000 (OK); then sent 1000 (OK)
L >> Exiting WS receive thread
2024-04-09 04:00:54.054106
END processing:
```
