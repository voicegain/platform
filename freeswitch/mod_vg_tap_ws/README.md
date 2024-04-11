Illustration of the 2nd scenario from: https://support.voicegain.ai/hc/en-us/articles/13318469102100-Tapping-into-FreeSWITCH-for-real-time-transcription

Here are the steps for testing mod_vg_tap_ws for ASR.
1) Write a below dialplan to invoke mod_vg_tap_ws command to start Speech to text live streaming

    There are couple of ways you can do this 

    a) From XML dialplan <action application="export" data="nolocal:api_on_answer=uuid_vg_tap_ws ${uuid} start http://localhost:8000/get_ws_url"/>
    b) when live call is going on you can invoke this command from CLI: uuid_vg_tap_ws 6292cbd6-a49c-4ff5-aecf-172cd0fda850 start http://localhost:8000/get_ws_url
    c)<action application="set" data="api_result=${uuid_vg_tap_ws ${uuid} start http://localhost:8000/get_ws_url}"/>
    d) From Lua also you can try to call this :
        api = freeswitch.API();
        sofia = api:executeString("uuid_vg_tap_ws ${uuid} start http://localhost:8000/get_ws_url");
    e) If you want to intentionally stop streaming you invoke the same command again with stop. ex "uuid_vg_tap_ws 6292cbd6-a49c-4ff5-aecf-172cd0fda850 stop http://localhost:8000/get_ws_url"
2) Once the dialplan is ready now it time to write your own application that listens for incoming requests and pass back webscoket URL to freeswitch for live streaming so please check out our uploaded sample web service application vg_asr_service.py for achieving the same. 
    Steps to be followed on Debian 12
    a) vg_asr_service.py is implemented based on FastAPI library you can also choose to use any other libs like FLask,Django etc.
    b) apt install python3.11-venv
        python -m venv myenv
        source myenv/bin/activate
        pip install fastapi uvicorn websockets requests
        uvicorn vg_asr_service:app --host 0.0.0.0 --port 8000

3) Go back to Freeswitch and make a call from one extension to another extension once B party answers the call you can see on vg_asr_service.py console text messages of live audio some thing like below.

LOGS: 
        START processing: 
                SessionId L: 3-0lus5iw5l1iodrj5unkncgiv3vu3
                SessionId R: 3-0lus5iw5l0rvcs5xoso64clzod28
        Audio Websocket URL: wss://api.voicegain.ai/v1/3/socket/3f58e065-d04a-4de8-ad4e-951786128f0c
        captured audio id: b32472eb-a821-4a0a-992f-454e4f9adac4
        Result Websocket Url L: wss://api.voicegain.ai/v1/3/plain/3-0lus5iw5l1iodrj5unkncgiv3vu3
        Result Websocket Url R: wss://api.voicegain.ai/v1/3/plain/3-0lus5iw5l0rvcs5xoso64clzod28
        L >>	 Starting WS receive thread 2024-04-09 04:00:49.682597
        INFO:     127.0.0.1:35380 - "GET /get_ws_url HTTP/1.1" 200 OK
        R << Starting WS receive thread 2024-04-09 04:00:49.683528
        R << connected to wss://api.voicegain.ai/v1/3/plain/3-0lus5iw5l0rvcs5xoso64clzod28
        EDIT->{ "ping":1712653249854 }
            R << 	
        L >>	 connected to wss://api.voicegain.ai/v1/3/plain/3-0lus5iw5l1iodrj5unkncgiv3vu3
        EDIT->{ "ping":1712653250024 }
            L >>	 	
            R << 	the
            R << 	the person
            R << 	the person at
            R << 	the person at extension
            R << 	the person at extension on
            R << 	the person at extension one
            R << 	the person at extension one ze
            L >>	 	the
            R << 	the person at extension one zero
            L >>	 	the person
        received 1000 (OK); then sent 1000 (OK)
        R << Exiting WS receive thread 2024-04-09 04:00:53.942004
            L >>	 	the person had
            L >>	 	the person had extension
        received 1000 (OK); then sent 1000 (OK)
        L >>	 Exiting WS receive thread 2024-04-09 04:00:54.054106
        END processing: 
