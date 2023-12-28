# Voicegain.ai ASR Real-Time Transcription with Websocket

import keyboard
import pyaudio, wave
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

global keep_running
keep_running  = True

wsBufferSize = 4096
sampleRate = 16000
channels = 1
bytesPerSample = 2
chunk = int(wsBufferSize/bytesPerSample)
pythonAudioFormat = pyaudio.paInt16

FILENAME = "output.wav"

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
                "full": []
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


# function to read audio from microphone and send to websocket
async def stream_audio(audio_ws_url):
  global epoch_start_audio_stream
  print("START stream_audio", flush=True)
  # Initialize PyAudio
  audio = pyaudio.PyAudio()
  print("\nstreaming to "+audio_ws_url, flush=True)
  f = audio.open(format=pythonAudioFormat, channels=channels,
                    rate=sampleRate, input=True,
                    frames_per_buffer=chunk)
  # Prepare to write to WAV file
  wf = wave.open(FILENAME, 'wb')
  wf.setnchannels(channels)
  wf.setsampwidth(audio.get_sample_size(pythonAudioFormat))
  wf.setframerate(sampleRate)
  print("started recording", flush=True)

  async with websockets.connect(audio_ws_url, 
    # we need to lower the buffer size - otherwise the sender will buffer for too long
    write_limit=wsBufferSize, 
    # compression needs to be disabled otherwise will buffer for too long
    compression=None) as websocket:
    try:
      print(str(datetime.datetime.now())+" connected", flush=True)
      global startTime
      startTime = time.time()
      global keep_running
      print("You can start speaking now. Press 's' to stop recording", flush=True)
      while keep_running:
        try:
          # read audio from microphone
          data = f.read(chunk, exception_on_overflow=False)  
          # write audio to wav file
          wf.writeframes(data)        
          await websocket.send(data)
        except Exception as e:
            print(str(datetime.datetime.now())+" Exception 1 when sending audio via websocket: "+str(e)) # usually because the session closed due to NOMATCH or NOINPUT
      elapsed_time = (time.time() - startTime)
      print(str(datetime.datetime.now())+" done streaming audio in "+str(elapsed_time), flush=True)
      f.stop_stream()
      f.close()
      print("Waiting 5 seconds for processing to finish...", flush=True)  
      time.sleep(5.0)
      print("done waiting", flush=True)  
      keep_running = False
      await websocket.close()
      print(str(datetime.datetime.now())+" websocket closed", flush=True)
      audio.terminate()
      wf.close()
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

# Keyboard input thread
def keyboard_watch():
    global keep_running
    while keep_running:
        if keyboard.is_pressed('s'):
            print('You Pressed s Key!')
            keep_running = False
            break


# stream audio
def process_audio():
  print(f"START processing: ", flush=True)
  
  web_res = web_api_request(headers, body)

  keyboard_thread = threading.Thread(target=keyboard_watch)
  keyboard_thread.start()

  # create and start the websocket thread
  threadWs = wsThread(web_res["ws_url"], ">>\t")
  threadWs.start()
  
  # stream audio
  asyncio.get_event_loop().run_until_complete( stream_audio(web_res["audio_ws_url"]) )

  # wait for websocket thread to join 
  threadWs.join()
  print(f"END processing: ")

## end of function and variable definitions
## main run starts here




process_audio()

