"""
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
"""

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
      },
      "content" : {
        "incremental" : ['words'],
        "full" : []
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
    print(' '.join(stack), flush=True)
  except Exception as e: 
    print("ERROR: "+str(e), flush=True)

# function to read audio from file and stream to Voicegain via RTP - we are using ffmpeg to do all the work
# note that we are using the -re parameter to stream at about real-time speed
def stream_audio():
  ff = FFmpeg(
      inputs={'ENS_ending.wav': ['-re']},
      outputs={'rtp://'+rtp_ip+':'+str(rtp_port) : ['-ar', '8000', '-f', 'mulaw', '-f', 'rtp']}
      #outputs={'mono-52sec.ulaw' : ['-ar', '8000', '-f', 'mulaw']}
  )
  ff.cmd
  ##'ffmpeg -i input.ts output.mp4'
  ff.run()

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

