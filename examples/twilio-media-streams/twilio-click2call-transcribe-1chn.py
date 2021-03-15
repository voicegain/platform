'''
The MIT License

Copyright (c) Voicegain.

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
'''

import requests, time, os, json, sys
import threading
import asyncio
import websockets
import datetime
from twilio.rest import Client


# Twilio credentials
# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
twilio_account_sid = 'AC054c13f4de...............4b04f2f710160'
twilio_auth_token = '51007bf9094e....................ee973557f46'

# VG credentials
# voicegain
# replace with your token obtained from https://console.voicegain.ai
JWT = "eyJhbGciOiJI.............InR5cCI6IkpXVCJ9.eyJhdWQiOiJodHRwczovL2Fwa.......................YWkvdjEiLCJzdWIiOiJhZWRiNjA...........................Awx0AnhiBwEttD2VHI"
vg_api_url="https://api.voicegain.ai/v1/asr/transcribe/async"


headers = {"Authorization":JWT}

# VG session initiation request

# new transcription session request
# it specifies audio input via an RTP stream
# and output is via a plain websocket
body = {
  "sessions": [
    {
      "asyncMode": "REAL-TIME",
      "audioChannelSelector" : "mix",
      "websocket": { 
        "adHoc": 'true', 
        "useSTOMP" : 'false',
        "minimumDelay": 0 
      },
      "content" : {
        "incremental" : ['words'],
        "full" : []
      }
    }
  ],
  "audio": {
    "source": { "stream": { "protocol": "TWIML" } },
    "format": "PCMU",
    "channels" : "mono",
    "rate": 8000, 
    "capture": 'true'
  },
  "settings": {
    "asr": {
      "noInputTimeout": 60000,
      "completeTimeout": 0
    }
  }
}

print("Connecting to: "+vg_api_url, flush=True)
init_response_raw = requests.post(vg_api_url, json=body, headers=headers)
try:
    init_response = init_response_raw.json()
except:
    print(str(init_response_raw))
    sys.exit("Received error response from http")

# retrieve values from response
# sessionId and capturedAudio are printed for debugging purposes
session_id = init_response["sessions"][0]["sessionId"]
ws_url = init_response["sessions"][0]["websocket"]["url"]
audio_ws_url = init_response["audio"]["stream"]["websocketUrl"]
capturedAudio = init_response["audio"].get("capturedAudio")

print("           SessionId 0: {}".format(session_id))
print("  Audio  Websocket Url: {}".format(audio_ws_url))
if( not(capturedAudio is None)):
    print("     Captured audio id: {}".format(capturedAudio))
print("Result Websocket Url 0: {}".format(ws_url), flush=True)


# in Twiml command you can adjust which Twilio channel will be streamed for transcription
# this script is setup only for 1 channel transcription so the choices are "inbound_track" and "outbound_track"
twiml_cmd = ' \
<Response> \n \
    <Say voice="woman" language="en-US">connected </Say> \n \
        <Start> \n \
            <Stream name="Test-stream-transcribe-001" url="'+audio_ws_url+'" track="inbound_track" /> \n \
        </Start> \n \
    <Say voice="woman" language="en-US">one blah blah blah blah blah blah blah blah blah </Say> \n \
    <Say voice="woman" language="en-US">two blah blah blah blah blah blah blah blah blah </Say> \n \
    <Say voice="woman" language="en-US">three blah blah blah blah blah blah blah blah blah </Say> \n \
    <Say voice="woman" language="en-US">the end </Say> \n \
</Response>'

# stack will contain the words returned from transcription
stack = []

# function to process JSON with incremental transcription results sent as messages over websocket
def process_ws_msg(wsMsg):
  #print(wsMsg, flush=True)
  try:
    data = json.loads(wsMsg)
    utter = data.get('utt')
    if( utter is None ):
      toDel = data.get('del')
      if( toDel is None):
        # unknown edit
        print("EDIT->"+wsMsg, flush=True)
      else:
        # delete and edits
        for i in range(toDel):
          stack.pop()
        edits = data.get('edit')
        if(not (edits is None)):
          for edit in edits:
            utter = edit.get('utt')
            stack.append(utter)
    else:
      # simple utterance
      stack.append(utter)
    print("\t"+' '.join(stack), flush=True)
  except Exception as e: 
    print("ERROR: "+str(e), flush=True)

 # thread that connects to the websocket and receives the results
# we do it in a separate thread because in the main thread we are streaming the audio
class wsThread (threading.Thread):
   def __init__(self, ws_uri):
      threading.Thread.__init__(self)
      self.ws_uri = ws_uri
   def run(self):
      print ("Starting WS receive thread "+str(datetime.datetime.now()), flush=True)
      try:
        asyncio.new_event_loop().run_until_complete(websocket_receive(self.ws_uri))  
      except Exception as e: 
        print(e, flush=True)
      print ("Exiting WS receive thread "+str(datetime.datetime.now()), flush=True)

# function that connects to the websocket and receives the results
async def websocket_receive(uri):
    async with websockets.connect(uri) as websocket:
        try:
          print("connected to "+uri, flush=True)
          while True:
            ws_msg = await websocket.recv()
            process_ws_msg(ws_msg)
        except Exception as e: 
          print(e, flush=True)  


# create and start the websocket thread
threadWs = wsThread(ws_url)
threadWs.start()



# now launch twilio call
client = Client(twilio_account_sid, twilio_auth_token)

print("Calling Twilio")
print(twiml_cmd, flush=True)


call = client.calls.create(
                        twiml=twiml_cmd,
                        to='+1817.....96',
                        from_='+1469.....54'
                    )

print("Twilio call sid: "+call.sid, flush=True)

# show progress of the call and terminate when call is "compelted"
while True:
    call = client.calls(call.sid).fetch()
    print(call.status, flush=True)
    if "completed" == call.status:
        break
    time.sleep(1)

# wait for websocket thread to join 
print("Waiting to join", flush=True)
threadWs.join()   
print("Joined")