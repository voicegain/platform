# Voicegain.ai ASR Real-Time Transcription with Websocket

from ffmpy import FFmpeg
import requests, time, os, json
import threading
import asyncio
import websockets
import datetime
import configparser

cfg = configparser.ConfigParser()
cfg.read("config.ini")
configSection = cfg.get("DEFAULT", "CONFIG")
protocol = cfg.get(configSection, "PROTOCOL")
hostPort = cfg.get(configSection, "HOSTPORT")
JWT = cfg.get(configSection, "JWT")
urlPrefix = cfg.get(configSection, "URLPREFIX")
inputFolder = cfg.get("DEFAULT", "INPUTFOLDER")
inputFile = cfg.get("DEFAULT", "INPUTFILE")

inputFilePath = f"{inputFolder}/{inputFile}"

sampleRate = 16000
channels = 1
bytesPerSample = 2

sendingWSProtocol = "WSS"
#sendingWSProtocol = "WS"

receivingWSProtocol = "wss"
#receivingWSProtocol = "ws"

#acousticModelRealTime = "VoiceGain-rho-en-us"
#acousticModelRealTime = "VoiceGain-rho"
acousticModelRealTime = "VoiceGain-kappa"


headers = {"Authorization":JWT}

# new transcription session request
# it specifies audio input via an RTP stream
# and output is via a plain websocket
body = {
    "sessions": [
        {
            "asyncMode": "REAL-TIME",
            "audioChannelSelector": "mix",
            "websocket": {
                "mode": 'adHoc',
                "protocol": receivingWSProtocol,
                "useSTOMP": 'false',
                "minimumDelay": 0
            },
            "content": {
                "incremental": ['words'],
                "full": ["words", "transcript"]
            },
            "poll": {
                "persist": 300000,
                "afterlife": 60000
            }
        }
    ],
    "audio": {
        "source": {"stream": {"protocol": sendingWSProtocol}},
        "format": "L16",
        "channels": "mono",
        "rate": sampleRate,
        "capture": 'true'
    },
    "settings": {
        "asr": {
            "languages" : ["en"],
            "acousticModelRealTime" : acousticModelRealTime,
            "noInputTimeout": 59999,
            "incompleteTimeout": 3599999,
            "sensitivity": 0.5
            # ,"hints": [
            #     "Starburst:10",
            #     "Mars_Wrigley:10",
            #     "contacting:8",
            #     "Mars_Consumer_Care:10",
            #     "mints:8"
            # ]
        }
        # ,"formatters": [
        #     {
        #         "type": "digits"
        #     },
        #     {
        #         "type": "enhanced",
        #         "parameters": {
        #             "CC": True,
        #             "EMAIL": True
        #         }
        #     },
        #     {
        #         "type": "spelling",
        #         "parameters": {
        #             "lang": "en-US"
        #         }
        #     },
        #     {
        #         "type": "redact",
        #         "parameters": {
        #             "CC": "partial"
        #         }
        #     }
        # ]
    }
}

def web_api_request(headers, body):
  url = "{}://{}/{}/asr/transcribe/async".format(protocol, hostPort, urlPrefix)
  print(f"making POST request to {url}", flush=True)

  init_response_raw = requests.post(url, json=body, headers=headers)
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
  audio_ws_url = init_response["audio"]["stream"]["websocketUrl"]
  capturedAudio = init_response["audio"].get("capturedAudio")

  print("          SessionId: {}".format(session_id))
  print("Audio Websocket URL: {}".format(audio_ws_url))

  ## mod_vg_tap_ws would get this `audio_ws_url` as input parameter

  if( not(capturedAudio is None)):
    print("   captured audio id: {}".format(capturedAudio))
  print("Result Websocket Url: {}".format(ws_url), flush=True)

  web_res = {}
  web_res["session_id"] = session_id
  web_res["ws_url"] = ws_url
  web_res["audio_ws_url"] = audio_ws_url
  return web_res 

msgCnt = 0
startTime = 0

# function to process JSON with incremental transcription results sent as messages over websocket
def process_ws_msg(wsMsg, stack, prefix):
  global msgCnt, startTime
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
      if( len(stack) > 500 ):
        while(len(stack) > 30):
          stack.pop(0)

    time_difference = time.time() - startTime
    formatted_time_difference = format(time_difference, '.3f')

    if prefix == "R <<":
      #'\033[92m'
      print("\033[92m\n\t"+formatted_time_difference+' '+prefix+" \t"+' '.join(stack) + '\033[0m', flush=True)
    else:
      print("\033[94m\n\t"+formatted_time_difference+' '+prefix+" \t"+' '.join(stack) + '\033[0m', flush=True)
  except Exception as e: 
    print("ERROR: "+str(e), flush=True)


# function to read audio from file and convert it to ulaw and send to websocket
async def stream_audio(file_name, audio_ws_url):
  global epoch_start_audio_stream
  print("START stream_audio", flush=True)
  conv_fname = (file_name+'.ulaw')
  ff = FFmpeg(
      inputs={file_name: []},
      #outputs={conv_fname : ['-ar', '8000', '-f', 'mulaw', '-y']}
      outputs={conv_fname : ['-ar', str(sampleRate), '-f', 's16le', '-y', '-ac', '1']}
  )
  ff.cmd
  ff.run()
  print("\nstreaming "+conv_fname+" to "+audio_ws_url, flush=True)
  with open(conv_fname, "rb") as f:
    async with websockets.connect(audio_ws_url, 
      # we need to lower the buffer size - otherwise the sender will buffer for too long
      write_limit=512, 
      # compression needs to be disabled otherwise will buffer for too long
      compression=None) as websocket:
      try:
        print(str(datetime.datetime.now())+" connected", flush=True)
        global startTime
        startTime = time.time()
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
        print(str(datetime.datetime.now())+" done streaming audio in "+str(elapsed_time_fl), flush=True)
        print("Waiting 10 seconds for processing to finish...", flush=True)  
        time.sleep(10.0)
        print("done waiting", flush=True)  
        global keep_running
        keep_running = False
        await websocket.close()
        print(str(datetime.datetime.now())+" websocket closed", flush=True)
      except Exception as e:
        print(str(datetime.datetime.now())+" Exception 2 when sending audio via websocket: "+str(e)) 


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
      write_limit=128, 
      # compression needs to be disabled otherwise will buffer for too long
      compression=None) as websocket:
        try:
          print(prefix+" connected to "+uri, flush=True)
          while True:
            ws_msg = await websocket.recv()
            process_ws_msg(ws_msg, stack, prefix)
        except Exception as e: 
          print(e, flush=True)  



# stream audio
def process_audio(file_name):
  print(f"START processing: {file_name}", flush=True)
  
  web_res = web_api_request(headers, body)

  # create and start the websocket thread
  threadWs = wsThread(web_res["ws_url"], ">>\t")
  threadWs.start()
  
  # stream audio
  asyncio.get_event_loop().run_until_complete( stream_audio(file_name, web_res["audio_ws_url"]) )

  # wait for websocket thread to join 
  threadWs.join()

  time.sleep(10) # give it some time to process the last messages

  url = "{}://{}/{}/asr/transcribe/{}/transcript".format(protocol, hostPort, urlPrefix, web_res["session_id"])
  print(f"making GET request to {url}", flush=True)
  right_script = requests.get(url, json=body, headers=headers, params={"format": "json"})
  # Print the HTTP response code
  print(f"HTTP response code: {right_script.status_code}", flush=True)
  print(f"text: {right_script.text}", flush=True)
  # download text transcript
  with open(f"{file_name}.json", "wt", encoding="utf-8") as f:
    f.write(right_script.text)
  print(f"downloaded transcript to {file_name}.json", flush=True)


  print(f"END processing: {file_name}")

## end of function and variable definitions
## main run starts here


process_audio(inputFilePath)

