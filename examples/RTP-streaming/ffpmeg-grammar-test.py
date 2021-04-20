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
      "websocket": { 
        "adHoc": 'true', 
        "useSTOMP" : 'false',
        "minimumDelay": 0 
      }
    }
  ],
  "audio": {
    "source": { "stream": { "protocol": "RTP" } },
    "format": "PCMU",
    "channel" : "mono",
    "rate": 8000, 
    "capture": 'true'
  },
  "settings": {
    "asr": {
      "grammars" : [
          {
            "type" : "BUILT-IN",
            "name" : "creditcard"
          }
      ],
      "maxAlternatives" : 10,
      "noInputTimeout": 5000,
      "incompleteTimeout" : 2000,
      "completeTimeout": 1000
    }
  }
}

init_response_raw = requests.post("https://api.ascalon.ai/v1/asr/recognize/async", json=body, headers=headers)
init_response = init_response_raw.json()
if(init_response.get("sessions") is None):
  print("did not obtain session")
  print(init_response_raw.status_code)
  print(init_response_raw.text)
  exit()

# retrieve values from response
# sessionId and capturedAudio are printed for debugging purposes
session_id = init_response["sessions"][0]["sessionId"]
ws_url = init_response["sessions"][0]["websocket"]["url"]
rtp_ip = init_response["audio"]["stream"]["ip"]
rtp_port = init_response["audio"]["stream"]["port"]
capturedAudio = init_response["audio"].get("capturedAudio")

print("        sessionId: {}".format(session_id))
print("         RTP   ip: {}".format(rtp_ip))
print("         RTP port: {}".format(rtp_port))
if( not(capturedAudio is None)):
  print("captured audio id: {}".format(capturedAudio))
print("    Websocket Url: {}".format(ws_url), flush=True)


# function to print results sent as messages over websocket
def process_ws_msg(wsMsg):
  print(str(datetime.datetime.now())+" received -> "+wsMsg, flush=True)


# function to read audio from file and stream to Voicegain via RTP - we are using ffmpeg to do all the work
# note that we are using the -re parameter to stream at about real-time speed
def stream_audio():
  ff = FFmpeg(
      inputs={'good-cc.wav': ['-re']},
      outputs={'rtp://'+rtp_ip+':'+str(rtp_port) : ['-ar', '8000', '-f', 'mulaw', '-f', 'rtp']}
      #outputs={'mono-52sec.ulaw' : ['-ar', '8000', '-f', 'mulaw']}
  )
  ff.cmd
  ##'ffmpeg -i input.ts output.mp4'
  ff.run()
  print(str(datetime.datetime.now())+" done streaming audio", flush=True)

# thread that connects to the websocket and receives the results
# we do it in a separate thread because in the main thread we are streaming the audio
class wsThread (threading.Thread):
   def __init__(self, ws_uri):
      threading.Thread.__init__(self)
      self.ws_uri = ws_uri
   def run(self):
      print ("Starting "+str(datetime.datetime.now()), flush=True)
      try:
        asyncio.new_event_loop().run_until_complete(websocket_receive(self.ws_uri))  
      except Exception as e: 
        print(e)
      print ("Exiting "+str(datetime.datetime.now()), flush=True)

# function that connects to the websocket and receives the results
async def websocket_receive(uri):
    async with websockets.connect(uri) as websocket:
        try:
          while True:
            ws_msg = await websocket.recv()
            process_ws_msg(ws_msg)
        except Exception as e: 
          print(e)  


# create and start the websocket thread
threadWs = wsThread(ws_url)
threadWs.start()

# stream audio
stream_audio()

# wait for websocket thread to join 
threadWs.join()

