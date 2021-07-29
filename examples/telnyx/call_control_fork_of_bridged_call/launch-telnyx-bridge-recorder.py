import requests, time, os, json, sys
import threading
import asyncio
import websockets
import datetime
import telnyx

phone_telnyx = "<telnyx phone number starting with +1>" # initial outbound call will be made from this twilio number
phone_a = "<first phone number to call starting with +1>" # this is the first phone that we will call
phone_b = "<second phone number to call - w/o +1>" # this is the phone we will dial once phone_a answers and we will bridge a and b

# Telnyx credentials

telnyx_APIAuthKey_fromPortal = "<telnyx APIAuthKey>"

telnyx_app_id = "<telnyx application id>"

# VG credentials
JWT = "<Voicegain JWT>"
vg_api_url="https://api.voicegain.ai/v1/asr/transcribe/async"


headers = {"Authorization":JWT}
telnyx_headers = {"Authorization": "Bearer "+telnyx_APIAuthKey_fromPortal}
telnyx_url = "https://api.telnyx.com/v2/texml/calls/{}".format(telnyx_app_id)

aws_lambda = "<url to AWS lambda function (w/o any parameters)>"

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
    "source": { "stream": { "protocol": "RTP-2CHN" } },
    "format": "PCMU",
    "channels" : "stereo",
    "rate": 8000, 
    "capture": 'true'
  },
  "settings": {
    "asr": {
      "noInputTimeout": -1,
      "completeTimeout": -1,
      "sensitivity" : 0.33
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
  audio_ip = vg_response_body["audio"]["stream"]["ip"]
  audio_port_1 = vg_response_body["audio"]["stream"]["port"]
  audio_port_2 = vg_response_body["audio"]["stream"]["portChn2"]
  capturedAudio = vg_response_body["audio"].get("capturedAudio")
except Exception as e:
  print("Error getting parameters from response: "+str(e))
  print(vg_response_body)
  sys.exit("Bad body !?")

print("           SessionId L: {}".format(session_id_left))
print("           SessionId R: {}".format(session_id_right))
print("              Audio IP: {}".format(audio_ip))
print("          Audio port 1: {}".format(audio_port_1))
print("          Audio port 2: {}".format(audio_port_2))
if( not(capturedAudio is None)):
    print("     Captured audio id: {}".format(capturedAudio))
print("Result Websocket Url L: {}".format(ws_url_left), flush=True)
print("Result Websocket Url R: {}".format(ws_url_right), flush=True)

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
      write_limit=512, 
      # compression needs to be disabled otherwise will buffer for too long
      compression=None) as websocket:
        try:
          print(prefix+" connected to "+uri, flush=True)
          while True:
            ws_msg = await websocket.recv()
            process_ws_msg(ws_msg, stack, prefix)
        except Exception as e: 
          print(e, flush=True)  


# create and start the websocket thread
threadWsLeft = wsThread(ws_url_left, "L >>\t")
threadWsRight = wsThread(ws_url_right, "R <<")
threadWsLeft.start()
threadWsRight.start()


# now launch telnyx call

print("Calling Telnyx")

telnyx_webhook_url = aws_lambda+"?rtpIp={}&port1={}&port2={}&dial={}".format(audio_ip, audio_port_1, audio_port_2, phone_b)

print(telnyx_url, flush=True)
print(telnyx_headers, flush=True)
print(telnyx_webhook_url, flush=True)

telnyx.api_key = telnyx_APIAuthKey_fromPortal
# outgoing call
call = telnyx.Call.create(connection_id=telnyx_app_id, to=phone_a, from_=phone_telnyx, webhook_url=telnyx_webhook_url)

call_control_id = call.get('call_control_id')
print("call_control_id: "+call_control_id, flush=True)


while True:
    time.sleep(1)
    
    status = telnyx.Call.retrieve(call_control_id)
    is_alive = status.get('is_alive')
    #print(is_alive, flush=True)
    if is_alive:
      print(".", flush=True)
      continue
    else:
      print("x", flush=True)
      break


# wait for websocket thread to join 
print("Waiting to join Left  "+str(datetime.datetime.now()), flush=True)
threadWsLeft.join()   
print("Joined Left           "+str(datetime.datetime.now()), flush=True)
print("Waiting to join Right "+str(datetime.datetime.now()), flush=True)
threadWsRight.join()   
print("Joined Right          "+str(datetime.datetime.now()), flush=True)