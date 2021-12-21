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

incompleteTimeout = 10
completeTimeout   = 10
print("incompleteTimeout: {}".format(incompleteTimeout))
print("  completeTimeout: {}".format(  completeTimeout))

## specify here the directory with files to test
input_path = "./my-sample-files/"
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
streamingStart = time.time()

#voicegain
platform = "voicegain"
JWT = "<your JWT token here - get it at https://console.voicegain.ai>"
headers = {"Authorization":JWT}

# new transcription session request
# it specifies audio input via an websocket stream
# and output is via a plain websocket
body = {
  "sessions": [
    {
      "asyncMode": "REAL-TIME",
      "continuousRecognition" : {
          "enable" : True,
          "stopOn" : ["ERROR"],
          "noResponseFor" : ["INPUT-STARTED"]
      },
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
    "capture": 'false'
  },
  "settings": {
    "asr": {
      "grammars" : [
          {
            "type":"JJSGF",
            "grammar":"insiderPlayCurrentMessageHeader_default",
            "parameters" : {"tag-format" : "semantics/1.0-literals"},
            "public":{
                "main":"((<menu> {menu})|(<restore> {restore})|(<done> {done})|(<balance> {balance})|(<one> {1})|(<next> {next})|(<two> {2})|(<reply> {reply})|(<four> {4})|(<call> {call})|(<prev> {prev})|(<first> {1st})|(<last> {last})|(<three> {3})|(<play> {play})|(<del> {del}))"
            },
            "rules":{
                "menu":"Main menu",
                "one":"(One | Want | wah)",
                "next":"((Next|nex) [message])",  
                "two":"(Two | Toe | Tao)",
                "reply":"(Reply)",
                "done" : "(done)",
                "balance" : "(balance)",
                "four":"(Four | Fore)",
                "call":"(Call [back])",
                "prev":"(Previous [message])",
                "first":"(First [message])",
                "last":"(Last [message])",
                "three":"Three",
                "play":"(Play | Play | Listen)",
                "del":"(Delete [message])",
                "restore" : "(restore [message])"
            }
          }
        ],
        "maxAlternatives" : 10,
        "confidenceThreshold" : 0.01,
        "noInputTimeout": 60000,
        "incompleteTimeout" : incompleteTimeout,
        "completeTimeout": completeTimeout,
        "sensitivity" : 0.5
        ,
        "acousticModelRealTime" : "VoiceGain-rho-en-us"
    }
  }
}

def web_api_request(headers, body):
  start_req = time.time()
  init_response_raw = requests.post("https://api.{}.ai/v1/asr/recognize/async".format(platform), json=body, headers=headers)
  init_response = init_response_raw.json()
  if(init_response.get("sessions") is None):
    print("did not obtain session")
    print(init_response_raw.status_code)
    print(init_response_raw.text)
    exit()
  end_req = time.time()
  print("time to establish session: {} seconds".format(end_req-start_req))
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
  print(str(datetime.datetime.now())+" within "+str(time.time()-streamingStart)+" sec received -> "+wsMsg, flush=True)
  global recognition_results 
  recognition_results[fname] = wsMsg


# function to read audio from file and convert it to ulaw and send to websocket
async def stream_audio(file_name, audio_ws_url):
  sampleRate = 8000
  print("START stream_audio", flush=True)
  conv_fname = (file_name+'.ulaw').replace(input_path, "./")
  ff = FFmpeg(
      inputs={file_name: []},
      outputs={conv_fname : ['-ar', str(sampleRate), '-f', 'mulaw', '-y', '-map_channel', '0.0.0']}
  )
  ff.cmd
  ff.run()
  print("\nopening audio file "+conv_fname+" to "+audio_ws_url, flush=True)
  global streamingStart
  with open(conv_fname, "rb") as f:
    print(str(datetime.datetime.now())+" opening  "+audio_ws_url, flush=True)
    start_ws = time.time()
    async with websockets.connect(audio_ws_url, 
      # we need to lower the buffer size - otherwise the sender will buffer for too long
      write_limit=480, 
      # compression needs to be disabled otherwise will buffer for too long
      compression=None) as websocket:
      try:
        end_ws = time.time()
        print(str(datetime.datetime.now())+" sender websocket connected within {} seconds".format(end_ws-start_ws), flush=True)
        n_buf = 1 * 480
        byte_buf = f.read(n_buf)
        start = time.time()
        epoch_start_audio_stream = start
        elapsed_time_fl = 0
        count = 0
        streamingStart = time.time()
        while byte_buf:
          n = len(byte_buf)
          
          try:
            print(".", end =" ", flush=True)
            await websocket.send(byte_buf)
          except Exception as e:
            print(str(datetime.datetime.now())+" Exception 1 when sending audio via websocket: "+str(e)) # usually because the session closed due to NOMATCH or NOINPUT
            break
          count += n
          elapsed_time_fl = (time.time() - start)

          expected_time_fl = count / (1.0 * sampleRate)
          time_to_wait = expected_time_fl - elapsed_time_fl
          if time_to_wait >= 0: 
            time.sleep(time_to_wait) # to simulate real time streaming
          byte_buf = f.read(n_buf)
        elapsed_time_fl = (time.time() - start)
        print(str(datetime.datetime.now())+" done streaming audio in "+str(elapsed_time_fl), flush=True)
        #print("Waiting 5 seconds for processing to finish...", flush=True)  
        #time.sleep(5.0)
        #print("done waiting", flush=True)  

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
    async with websockets.connect(uri, 
      # we need to lower the buffer size - otherwise the sender will buffer for too long
      write_limit=256, 
      # compression needs to be disabled otherwise will buffer for too long
      compression=None) as websocket:
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
