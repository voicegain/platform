"""
pip install websockets
pip install ffmpy
"""

from ffmpy import FFmpeg

import requests, time, os, json
import threading
import asyncio
import websockets
import datetime

## specify here the directory with files to test
input_path = "./cc-wav/"
list_of_files = []

for root, dirs, files in os.walk(input_path):
	for file in files:
		list_of_files.append(os.path.join(root,file))

print("files to test")
for name in list_of_files:
    print(name)

# global 
# map from filename to recognition result
recognition_results = {}

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
          ## credit card recognition ##
            "name" : "creditcard"
          ## CVV recognition ##
            # "name" : "digit",
            # "parameters" : {
            #   "minlength" : 3,
            #   "maxlength" : 3
            # }
          ## Yes/No recognition ##
            # "name" : "boolean"
          }
      ],
      "maxAlternatives" : 10,
      "noInputTimeout": 5000,
      "incompleteTimeout" : 2000,
      "completeTimeout": 1000,
      "speedVsAccuracy" : 0.75
    }
  }
}

def web_api_request(headers, body):
  init_response_raw = requests.post("https://api.voicegain.ai/v1/asr/recognize/async", json=body, headers=headers)
  init_response = init_response_raw.json()
  if(init_response.get("sessions") is None):
    print("did not obtain session")
    print(init_response_raw.status_code)
    print(init_response_raw.text)
    exit()

  result = {}
  # retrieve values from response
  # sessionId and capturedAudio are printed for debugging purposes
  result["session_id"] = init_response["sessions"][0]["sessionId"]
  result["ws_url"] = init_response["sessions"][0]["websocket"]["url"]
  result["rtp_ip"] = init_response["audio"]["stream"]["ip"]
  result["rtp_port"] = init_response["audio"]["stream"]["port"]
  result["capturedAudio"] = init_response["audio"].get("capturedAudio")

  print("        sessionId: {}".format(result["session_id"]))
  print("         RTP   ip: {}".format(result["rtp_ip"]))
  print("         RTP port: {}".format(result["rtp_port"]))
  if( not(result.get("capturedAudio") is None)):
    print("captured audio id: {}".format(result["capturedAudio"]))
  print("    Websocket Url: {}".format(result["ws_url"]), flush=True)
  return result


# function to print results sent as messages over websocket
def process_ws_msg(wsMsg, fname):
  print(str(datetime.datetime.now())+" received -> "+wsMsg, flush=True)
  global recognition_results 
  recognition_results[fname] = wsMsg


# function to read audio from file and stream to Voicegain via RTP - we are using ffmpeg to do all the work
# note that we are using the -re parameter to stream at about real-time speed
def stream_audio(file_name, rtp_ip, rtp_port):
  ff = FFmpeg(
      inputs={file_name: ['-re']},
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
   def __init__(self, ws_uri, fname):
      threading.Thread.__init__(self)
      self.ws_uri = ws_uri
      self.fname = fname
   def run(self):
      print ("Starting "+str(datetime.datetime.now()), flush=True)
      try:
        asyncio.new_event_loop().run_until_complete(websocket_receive(self.ws_uri, self.fname))  
      except Exception as e: 
        print(e)
      print ("Exiting "+str(datetime.datetime.now()), flush=True)

# function that connects to the websocket and receives the results
async def websocket_receive(uri, fname):
    async with websockets.connect(uri) as websocket:
        try:
          while True:
            ws_msg = await websocket.recv()
            process_ws_msg(ws_msg, fname)
        except Exception as e: 
          print(e)  

def process_audio(file_name):
  print("START processing: "+file_name)
  web_res = web_api_request(headers, body)

  # create and start the websocket thread
  threadWs = wsThread(web_res["ws_url"], file_name)
  threadWs.start()

  # stream audio
  stream_audio(file_name, web_res["rtp_ip"], web_res["rtp_port"])

  # wait for websocket thread to join 
  threadWs.join()
  print("END processing: "+file_name)

for aFile in list_of_files:
  process_audio(aFile)

print("\nRECOGNITION RESULTS:")
for x in recognition_results:
  print(x)
  print(recognition_results[x])
  print("\n")
