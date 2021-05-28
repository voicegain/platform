"""
pip install websockets
pip install ffmpy
"""

# same as ffmpeg-grammar-test-set.py but uses websocket instead of RTP
# try it in case RTP is blocked on router/firewall

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


JWT = "<Your JWT here>"
headers = {"Authorization":JWT}
# new transcription session request
# it specifies audio input via an websocket stream
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
    "source": { "stream": { "protocol": "WEBSOCKET" } },
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
          ## digit sequence recognition ##
            # "name" : "digit",
            # "parameters" : {
            #   "minlength" : 16,
            #   "maxlength" : 19
            # }
          ## Yes/No recognition ##
            # "name" : "boolean"
          }
      ],
      "maxAlternatives" : 10,
      "noInputTimeout": 7000,
      "incompleteTimeout" : 5000,
      "completeTimeout": 2000,
      "speedVsAccuracy" : 1.0,
      "sensitivity" : 0.5,
      "acousticModelRealTime" : "VoiceGain-rt-ivr-en-us" # this is the model optimized for IVR use
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
  result["audio_ws_url"] = init_response["audio"]["stream"]["websocketUrl"]
  result["capturedAudio"] = init_response["audio"].get("capturedAudio")

  print("        sessionId: {}".format(result["session_id"]))
  print("  Audio Websocket: {}".format(result["audio_ws_url"]))
  if( not(result.get("capturedAudio") is None)):
    print("captured audio id: {}".format(result["capturedAudio"]))
  print("Results Websocket: {}".format(result["ws_url"]), flush=True)
  return result


# function to print results sent as messages over websocket
def process_ws_msg(wsMsg, fname):
  print(str(datetime.datetime.now())+" received -> "+wsMsg, flush=True)
  global recognition_results 
  recognition_results[fname] = wsMsg


# function to read audio from file and convert it to ulaw and send to websocket
async def stream_audio(file_name, audio_ws_url):
  print("START stream_audio", flush=True)
  conv_fname = (file_name+'.ulaw').replace(input_path, "./")
  ff = FFmpeg(
      inputs={file_name: []},
      outputs={conv_fname : ['-ar', '8000', '-f', 'mulaw', '-y', '-map_channel', '0.0.0']}
  )
  ff.cmd
  ff.run()
  print("\nstreaming "+conv_fname+" to "+audio_ws_url, flush=True)
  with open(conv_fname, "rb") as f:
    async with websockets.connect(audio_ws_url, 
      # we need to lower the buffer size - otherwise the sender will buffer for too long
      write_limit=4096, 
      # compression needs to be disabled otherwise will buffer for too long
      compression=None) as websocket:
      try:
        print("connected", flush=True)
        n_buf = 2 * 1024
        byte_buf = f.read(n_buf)
        while byte_buf:
          n = len(byte_buf)
          print(".", end =" ", flush=True)
          await websocket.send(byte_buf)
          time.sleep(n/8000.0) # to simulate real time streaming
          byte_buf = f.read(n_buf)
        await websocket.close()
      except Exception as e:
        print("Exception when sending audio via websocket: "+str(e)) # usually because the session closed due to NOMATCH or NOINPUT

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
  asyncio.get_event_loop().run_until_complete( stream_audio(file_name, web_res["audio_ws_url"]) )

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
