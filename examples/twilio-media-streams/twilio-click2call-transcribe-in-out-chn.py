import requests, time, os, json, sys
import threading
import asyncio
import websockets
import datetime
from twilio.rest import Client


# Twilio credentials
# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
twilio_account_sid = 'AC054c13f4xxxxb04f2f710160'
twilio_auth_token = '51007bf909xxxxx7e178ee973557f46'

# VG credentials
# voicegain
#JWT = "eyJhbGciOiJIUzI1xxxxR5cCI6IkpXVCJ9.eyJhdWQiOiJodHRwczovL2FwaS52b2ljZWdhaW4uYWkvdjExxxxxiJhZWRiNjAwMC0xMzdiLTQ4YzMtOWFjYi0wNDVmM2UxNjNhZmQifQ.JWTzFwk4Lorgu_Lxxxxxxwx0AnhiBwEttD2VHI"
#vg_api_url="https://api.voicegain.ai/v1/asr/transcribe/async"

# ascalon
JWT = "eyJhbGciOiJIUzxxxxR5cCI6IkpXVCJ9.eyJhdWQiOiIqLmFzY2FsbG9uLmFpIiwic3ViIjoiMWZiNTAzMDxxxxS00ZGMyLWFjNDctMDRkNDI3YzU1MzBmIn0.Q66m2z7hDQyGN3ivV2xxxxxnkEXf-d6AhwPgtsI2km0"
vg_api_url="https://api.ascalon.ai/v1/asr/transcribe/async"


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
init_response_raw = requests.post(vg_api_url, json=body, headers=headers)
try:
    init_response = init_response_raw.json()
except:
    print(str(init_response_raw))
    sys.exit("Received error response from http")

# retrieve values from response
# sessionId and capturedAudio are printed for debugging purposes
session_id_left = init_response["sessions"][0]["sessionId"]
session_id_right = init_response["sessions"][1]["sessionId"]
ws_url_left = init_response["sessions"][0]["websocket"]["url"]
ws_url_right = init_response["sessions"][1]["websocket"]["url"]
audio_ws_url = init_response["audio"]["stream"]["websocketUrl"]
capturedAudio = init_response["audio"].get("capturedAudio")

print("           SessionId L: {}".format(session_id_left))
print("           SessionId R: {}".format(session_id_right))
print("  Audio  Websocket Url: {}".format(audio_ws_url))
if( not(capturedAudio is None)):
    print("     Captured audio id: {}".format(capturedAudio))
print("Result Websocket Url L: {}".format(ws_url_left), flush=True)
print("Result Websocket Url R: {}".format(ws_url_right), flush=True)

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
    <Say voice="woman" language="en-US">outbound, channel, speaking.</Say> \n \
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
    async with websockets.connect(uri) as websocket:
        try:
          print(prefix+" connected to "+uri, flush=True)
          while True:
            ws_msg = await websocket.recv()
            process_ws_msg(ws_msg, stack, prefix)
        except Exception as e: 
          print(e, flush=True)  


# create and start the websocket thread
threadWsLeft = wsThread(ws_url_left, "L")
threadWsRight = wsThread(ws_url_right, "R")
threadWsLeft.start()
threadWsRight.start()


# now launch twilio call
client = Client(twilio_account_sid, twilio_auth_token)

print("Calling Twilio")
print(twiml_cmd, flush=True)


call = client.calls.create(
                        twiml=twiml_cmd,
                        to='+18174002096',
                        from_='+14694895554'
                    )

print("Twilio call sid: "+call.sid, flush=True)

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
