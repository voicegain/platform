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
twilio_account_sid = 'AC054c13f4d.............74b04f2f710160'
twilio_auth_token = 'c36eca6a180c............11498d900f6ec'

# VG credentials
# voicegain
JWT = "eyJhbGciOiJIUz....................IkpXVCJ9.eyJhdWQiOiJodHRwczovL2FwaS52b2ljZWdhaW4u...................LTQ4YzMtOWFjYi0wNDVmM2UxNjNhZmQifQ.JWTzFwk4Lor..............ttD2VHI"
vg_api_url="https://api.voicegain.ai/v1/asr/transcribe/async"

# ascalon
#JWT = "eyJhbGciOiJIUz.............R5cCI6IkpXVCJ9.eyJhdWQiOiIqLmFzY2FsbG9uLmF..........................jNDctMDRkNDI3YzU1MzBmIn0.pu3Cv5COVghH4....................7LE-n_uB6tTao"
#vg_api_url="https://api.ascalon.ai/v1/asr/transcribe/async"


headers = {"Authorization":JWT}

# VG session initiation request

# new transcription session request
# it specifies audio input via an RTP stream
# and output is via a plain websocket
body = {
  "sessions": [
    {
      "asyncMode": "REAL-TIME",
      "audioChannelSelector" : "left",
      "websocket": { 
        "adHoc": 'true', 
        "useSTOMP" : 'false',
        "minimumDelay": 0 
      },
      "content" : {
        "incremental" : ['words'],
        "full" : []
      }
    },
    {
      "asyncMode": "REAL-TIME",
      "audioChannelSelector" : "right",
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
    "channels" : "stereo",
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
vg_response = requests.post(vg_api_url, json=body, headers=headers)
print("response code: "+str(vg_response.status_code))
if(200 != vg_response.status_code):
  print(vg_response.content)
  sys.exit("Received error response from http")

try:
    vg_response_body = vg_response.json()
except:
    sys.exit("Response from http has no JSON body")


# retrieve values from response
# sessionId and capturedAudio are printed for debugging purposes
try:
  session_id_left = vg_response_body["sessions"][0]["sessionId"]
  session_id_right = vg_response_body["sessions"][1]["sessionId"]
  ws_url_left = vg_response_body["sessions"][0]["websocket"]["url"]
  ws_url_right = vg_response_body["sessions"][1]["websocket"]["url"]
  audio_ws_url = vg_response_body["audio"]["stream"]["websocketUrl"]
  capturedAudio = vg_response_body["audio"].get("capturedAudio")
except Exception as e:
  print("Error getting parameters from response: "+str(e))
  print(vg_response_body)
  sys.exit("Bad body !?")

print("           SessionId L: {}".format(session_id_left))
print("           SessionId R: {}".format(session_id_right))
print("  Audio  Websocket Url: {}".format(audio_ws_url))
if( not(capturedAudio is None)):
    print("     Captured audio id: {}".format(capturedAudio))
print("Result Websocket Url L: {}".format(ws_url_left), flush=True)
print("Result Websocket Url R: {}".format(ws_url_right), flush=True)

# TwiML command to pass to Twilio client
# the key thing is the <Start> <Stream> which will send inbound and outbound audio to Voicegain 
twiml_cmd = ' \
<Response> \n \
    <Say voice="woman" language="en-US">connected </Say> \n \
        <Start> \n \
            <Stream name="Test-stream-transcribe-001" url="'+audio_ws_url+'" track="both_tracks" /> \n \
        </Start> \n \
    <Pause length="1"/> \n \
    <Say voice="woman" language="en-US">start talking, </Say> \n \
    <Pause length="1"/> \n \
    <Say voice="woman" language="en-US">outbound, channel, speaking.</Say> \n \
    <Pause length="1"/> \n \
    <Say voice="woman" language="en-US">outbound, channel, speaking.</Say> \n \
    <Pause length="1"/> \n \
    <Say voice="woman" language="en-US">outbound, channel, speaking.</Say> \n \
    <Pause length="1"/> \n \
    <Say voice="woman" language="en-US">the end </Say> \n \
    <Pause length="1"/> \n \
</Response>'

# keep tranck of number of websocket messages received from Voicegain
msgCnt = 0

# function to process JSON with incremental transcription results sent as messages over websocket
def process_ws_msg(wsMsg, stack, prefix):
  global msgCnt
  msgCnt += 1
  # uncomment this to see raw messages 
  # print(prefix+" "+wsMsg, flush=True)

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
    print("\t"+prefix+" \t"+' '.join(stack), flush=True)
  except Exception as e: 
    print("ERROR: "+str(e), flush=True)

# thread that connects to the websocket and receives the results
# we do it in a separate thread because in the main thread we are streaming the audio
class wsThread (threading.Thread):
   def __init__(self, ws_uri, prefix):
      threading.Thread.__init__(self)
      self.ws_uri = ws_uri
      self.prefix = prefix
      self.stack = []
   def run(self):
      print (self.prefix+" Starting WS receive thread "+str(datetime.datetime.now()), flush=True)
      try:
        asyncio.new_event_loop().run_until_complete(websocket_receive(self.ws_uri, self.stack, self.prefix))  
      except Exception as e: 
        print(e, flush=True)
      print (self.prefix+" Exiting WS receive thread "+str(datetime.datetime.now()), flush=True)

# function that connects to the websocket and receives the results
async def websocket_receive(uri, stack, prefix):
    async with websockets.connect(uri, 
      # we need to lower the buffer size - otherwise the sender will buffer for too long
      write_limit=480, 
      # compression needs to be disabled otherwise will buffer for too long
      compression=None) as websocket:
        try:
          print(prefix+" connected to "+uri, flush=True)
          while True:
            ws_msg = await websocket.recv()
            process_ws_msg(ws_msg, stack, prefix)
        except Exception as e: 
          print(e, flush=True)  


# create and start the websocket threads to receive results from Voicegain
# inbound telephone channel
threadWsLeft = wsThread(ws_url_left, "L >>\t")
# outbound telephone channel
threadWsRight = wsThread(ws_url_right, "R <<")
threadWsLeft.start()
threadWsRight.start()


# now launch twilio call
client = Client(twilio_account_sid, twilio_auth_token)

print("Calling Twilio")
print(twiml_cmd, flush=True)

# set the phone numbers
call = client.calls.create(
                        twiml=twiml_cmd,
                        to='+1817.....96',
                        from_='+1469.....54'
                    )

print("Twilio call sid: "+call.sid, flush=True)

# show the status of the Twilio call until it is complete
while True:
    call = client.calls(call.sid).fetch()
    print(call.status+" msgs rcvd "+str(msgCnt), flush=True)
    if "completed" == call.status:
        break
    time.sleep(1)

# wait for websocket thread to join 
print("Waiting to join Left  "+str(datetime.datetime.now()), flush=True)
threadWsLeft.join()   
print("Joined Left           "+str(datetime.datetime.now()), flush=True)
print("Waiting to join Right "+str(datetime.datetime.now()), flush=True)
threadWsRight.join()   
print("Joined Right          "+str(datetime.datetime.now()), flush=True)
