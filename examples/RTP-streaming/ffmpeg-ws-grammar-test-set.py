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

import configparser

# Read JWT from config.ini
config = configparser.ConfigParser()
config.read('config.ini')
JWT = config['auth']['jwt']

## specify here the directory with files to test
input_path = "../../new-examples/data/Recordings/en-GARBAGE"

list_of_files = []

for root, dirs, files in os.walk(input_path):
	for file in files:
		list_of_files.append(os.path.join(root,file))

print("files to test from path: "+input_path)
for name in list_of_files:
    print(name)

# global 
# map from filename to recognition result
startTime = 0
recognition_results = {}

sampleRate = 8000
channels = 1
bytesPerSample = 1




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
    "source": { "stream": { "protocol": "WS" } },
    "format": "PCMU",
    "channel" : "mono",
    "rate": 8000, 
    "capture": 'true'
  },
  "settings": {
    "asr": {
      "grammars" : [
          {
             "type": "GRXML",
             "name" : "menu-selection",
             "fromUrl":{
            #     #"url" : "https://s3.us-east-2.amazonaws.com/files.public.voicegain.ai/mystery.grxml"
            #     "url" : "https://s3.us-east-2.amazonaws.com/files.public.voicegain.ai/Menu0to9Voice.grxml"
                "url" : "https://s3.us-east-2.amazonaws.com/files.public.voicegain.ai/YesNoAgent.grxml"
             }

          #  "type" : "BUILT-IN",
          ## credit card recognition ##
          ##  "name" : "creditcard"
          ## digit sequence recognition ##
            # "name" : "digit",
            # "parameters" : {
            #   # "length" : 4, 
            #   "minlength" : 2,
            #   "maxlength" : 5,
            #  "lang" : "es-es"
            # }
          ## number recognition ##
            #"name" : "number",
            #"parameters" : {
#              "minallowed" : 0,
#              "maxallowed" : 5000,
             # "lang" : "es-es"
            #}
          ## Yes/No recognition ##
          #   "name" : "boolean",
          #   "parameters" : {
          #     "lang" : "es-es"
          #   }
          }
      ],
      "maxAlternatives" : 10,
      "noInputTimeout": 10000,
      "incompleteTimeout" : 5000,
      "completeTimeout": 2000,
      "speedVsAccuracy" : 0.5,
      "sensitivity" : 0.5,
      "confidenceThreshold" : 0.0001,
      "acousticModelRealTime" : "VoiceGain-kappa",
      "languages" : ["en"]
    }
  }
}

def web_api_request(headers, body):
  global startTime
  startTime = time.time()

  host_url = config['api']['host']
  print("Invoking URL: ", host_url + "/v1/asr/recognize/async", flush=True)
  init_response_raw = requests.post(host_url + "/v1/asr/recognize/async", json=body, headers=headers)
  init_response = init_response_raw.json()
  if(init_response.get("sessions") is None):
    print("did not obtain session")
    print(init_response_raw.status_code)
    print(init_response_raw.text)
    exit()

  print("init response received in "+str(time.time()-startTime), flush=True)

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
  print("at "+str(time.time()-startTime)+"ms received -> "+wsMsg, flush=True)
  global recognition_results 
  recognition_results[fname] = wsMsg


# function to read audio from file and convert it to ulaw and send to websocket
async def stream_audio(conv_fname, audio_ws_url):
  print("\nStreaming "+conv_fname+" to "+audio_ws_url, flush=True)
  with open(conv_fname, "rb") as f:
    async with websockets.connect(audio_ws_url, 
      # we need to lower the buffer size - otherwise the sender will buffer for too long
      write_limit=512, 
      # compression needs to be disabled otherwise will buffer for too long
      compression=None) as websocket:
      try:
        global startTime
        print("audio websocket connected in "+str(time.time()-startTime), flush=True)
        n_buf = 1 * 1024
        byte_buf = f.read(n_buf)
        start = time.time()
        epoch_start_audio_stream = start
        elapsed_time_fl = 0
        count = 0
        while byte_buf:
          n = len(byte_buf)
          print(".", end =" ", flush=True)
          try:
            await websocket.send(byte_buf)
          except Exception as e:
              print(str(datetime.datetime.now())+" Exception 1 when sending audio via websocket: "+str(e)) # usually because the session closed due to NOMATCH or NOINPUT
              break
          count += n
          elapsed_time_fl = (time.time() - start)
          expected_time_fl = count / (sampleRate * channels * bytesPerSample)
          time_to_wait = expected_time_fl - elapsed_time_fl
          if time_to_wait >= 0: 
            time.sleep(time_to_wait) # to simulate real time streaming
          byte_buf = f.read(n_buf)
        elapsed_time_fl = (time.time() - start)
        print("done streaming audio in "+str(time.time()-startTime), flush=True)
        print("ellapsed time "+str(elapsed_time_fl), flush=True)
        print("Waiting 5 seconds for processing to finish...", flush=True)  
        time.sleep(5.0)
        print("done waiting", flush=True)  
        global keep_running
        keep_running = False
        await websocket.close()
        print(str(datetime.datetime.now())+" websocket closed", flush=True)
      except Exception as e:
        print(str(datetime.datetime.now())+" Exception 2 when sending audio via websocket: "+str(e)) 

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

  conv_fname = (file_name+'.ulaw').replace(input_path, "./tmp/")
  if not os.path.exists(os.path.dirname(conv_fname)):
    os.makedirs(os.path.dirname(conv_fname))

  ff = FFmpeg(
      inputs={file_name: []},
      outputs={conv_fname : ['-ar', '8000', '-f', 'mulaw', '-y', '-map_channel', '0.0.0']}
  )
  ff.cmd
  ff.run()

  print("Converted to ulaw: "+conv_fname)

  web_res = web_api_request(headers, body)

  # create and start the websocket thread
  threadWs = wsThread(web_res["ws_url"], file_name)
  threadWs.start()

  # stream audio
  asyncio.get_event_loop().run_until_complete( stream_audio(conv_fname, web_res["audio_ws_url"]) )

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
