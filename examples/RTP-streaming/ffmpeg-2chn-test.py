#pip install websockets
#pip install ffmpy

from ffmpy import FFmpeg

import requests, time, os, json
import threading
import asyncio
import websockets
import datetime

JWT = "<Your JWT HERE>"
headers = {"Authorization":JWT}
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
    "channel" : "stereo",
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

init_response_raw = requests.post("https://api.voicegain.ai/v1/asr/transcribe/async", json=body, headers=headers)
init_response = init_response_raw.json()
if(init_response.get("sessions") is None):
  print("did not obtain session")
  print(init_response_raw.status_code)
  print(init_response_raw.text)
  exit()

# retrieve values from response
# sessionId and capturedAudio are printed for debugging purposes
session_id_left = init_response["sessions"][0]["sessionId"]
session_id_right = init_response["sessions"][1]["sessionId"]
ws_url_left = init_response["sessions"][0]["websocket"]["url"]
ws_url_right = init_response["sessions"][1]["websocket"]["url"]
rtp_ip = init_response["audio"]["stream"]["ip"]
rtp_port = init_response["audio"]["stream"]["port"]
rtp_port_2 = init_response["audio"]["stream"]["portChn2"]
capturedAudio = init_response["audio"].get("capturedAudio")

print("      SessionId L: {}".format(session_id_left))
print("      SessionId R: {}".format(session_id_right))
print("         RTP   ip: {}".format(rtp_ip))
print("       RTP port 1: {}".format(rtp_port))
print("       RTP port 2: {}".format(rtp_port_2))
if( not(capturedAudio is None)):
  print("captured audio id: {}".format(capturedAudio))
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

# function to read audio from file and stream to Voicegain via RTP - we are using ffmpeg to do all the work
# note that we are using the -re parameter to stream at about real-time speed
def stream_audio():
  ff = FFmpeg(
      inputs={'pcm_stereo_10sec.wav': ['-re']},
      outputs={
        'rtp://'+rtp_ip+':'+str(rtp_port)   : ['-ar', '8000', '-f', 'mulaw', '-f', 'rtp', '-map_channel', '0.0.0'],
        'rtp://'+rtp_ip+':'+str(rtp_port_2) : ['-ar', '8000', '-f', 'mulaw', '-f', 'rtp', '-map_channel', '0.0.1']
        }
      #outputs={'mono-52sec.ulaw' : ['-ar', '8000', '-f', 'mulaw']}
  )
  ff.cmd
  ##'ffmpeg -i input.ts output.mp4'
  ff.run()

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
threadWsLeft = wsThread(ws_url_left, "L >>\t")
threadWsRight = wsThread(ws_url_right, "R <<")
threadWsLeft.start()
threadWsRight.start()

# stream audio
stream_audio()

# wait for websocket thread to join 
print("Waiting to join Left  "+str(datetime.datetime.now()), flush=True)
threadWsLeft.join()   
print("Joined Left           "+str(datetime.datetime.now()), flush=True)
print("Waiting to join Right "+str(datetime.datetime.now()), flush=True)
threadWsRight.join()   
print("Joined Right          "+str(datetime.datetime.now()), flush=True)

