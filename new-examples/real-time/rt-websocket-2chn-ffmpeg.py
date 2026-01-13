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
outputFolder = cfg.get("DEFAULT", "OUTPUTFOLDER")
inputFile = cfg.get("DEFAULT", "INPUTFILE")

inputFilePath = f"{inputFolder}/{inputFile}"

##vgFormat = "PCMU"
vgFormat = "L16"
#ffmpegFormat = "mulaw"
ffmpegFormat = "s16le"
sampleRate = 16000
channels = 2
bytesPerSample = 2

sendingWSProtocol = "WSS"
#sendingWSProtocol = "WEBSOCKET"
#sendingWSProtocol = "WS"

receivingWSProtocol = "wss"
#receivingWSProtocol = "ws"

#acousticModelRealTime = "VoiceGain-rho-en-us"
#acousticModelRealTime = "VoiceGain-rho"
acousticModelRealTime = "VoiceGain-kappa"

session_id_left = ""
session_id_right = ""
capturedAudio = ""

channelOfLastWordReceived = ""
  
headers = {"Authorization":JWT}

# new transcription session request
# it specifies audio input via an RTP stream
# and output is via a plain websocket
body = {
    "sessions": [
        {
            "asyncMode": "REAL-TIME",
            "audioChannelSelector": "left",
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
        },
        {
            "asyncMode": "REAL-TIME",
            "audioChannelSelector": "right",
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
        "source": {"stream": 
                    {"protocol": sendingWSProtocol,
                     "noAudioTimeout": 65000
                     },                             
                  },
        "format": vgFormat,
        "channels": "stereo" if channels == 2 else "mono",
        "rate": sampleRate,
        "capture": 'true'
    },
    "settings": {
        "asr": {
            "acousticModelRealTime" : acousticModelRealTime,
            "noInputTimeout": 59999,
            "incompleteTimeout": 3599999,
            "sensitivity": 0.4
            # ,
            # "hints": [
            #     "Starburst:10",
            #     "Mars_Wrigley:10",
            #     "contacting:8",
            #     "Mars_Consumer_Care:10",
            #     "mints:8"
            #     "ezCater:10",
            # ]
        },
        "formatters": [
            {
                "type": "basic",
                "parameters": {"enabled": "true"}
            },          
            {
                "type": "digits"
            },
            {
                "type": "enhanced",
                "parameters": {
                    "CC": True,
                    "EMAIL": True
                }
            },
            {
                "type": "spelling",
                "parameters": {
                    "lang": "en-US"
                }
            },
            {
                "type": "redact",
                "parameters": {
                    "CC": "partial"
                }
            }
        ]
    }
}

def web_api_request(headers, body):
  url = "{}://{}/{}/asr/transcribe/async".format(protocol, hostPort, urlPrefix)
  print(f"making POST request to {url}", flush=True)
  print("with body: {}".format(json.dumps(body)), flush=True)

  init_response_raw = requests.post(url, json=body, headers=headers)
  init_response = init_response_raw.json()
  if(init_response.get("sessions") is None):
    print("did not obtain session")
    print(init_response_raw.status_code)
    print(init_response_raw.text)
    exit()

  # retrieve values from response
  # sessionId and capturedAudio are printed for debugging purposes
  global session_id_left, session_id_right, capturedAudio
  session_id_left = init_response["sessions"][0]["sessionId"]
  session_id_right = init_response["sessions"][1]["sessionId"]
  ws_url_left = init_response["sessions"][0]["websocket"]["url"]
  ws_url_right = init_response["sessions"][1]["websocket"]["url"]
  audio_ws_url = init_response["audio"]["stream"]["websocketUrl"]
  capturedAudio = init_response["audio"].get("capturedAudio")

  # body = {"pause": {"action" : "start"}}

  # url = "{}://{}/{}/asr/transcribe/{}".format(protocol, hostPort, urlPrefix, session_id_left)
  # print(f"making PUT request to {url}", flush=True)
  # requests.put(url, json=body, headers=headers)
  # url = "{}://{}/{}/asr/transcribe/{}".format(protocol, hostPort, urlPrefix, session_id_right)
  # print(f"making PUT request to {url}", flush=True)
  # requests.put(url, json=body, headers=headers)



  print("        SessionId L: {}".format(session_id_left))
  print("        SessionId R: {}".format(session_id_right))
  print("Audio Websocket URL: {}".format(audio_ws_url))

  ## mod_vg_tap_ws would get this `audio_ws_url` as input parameter

  if( not(capturedAudio is None)):
    print("captured audio id: {}".format(capturedAudio))
  print("Result Websocket Url L: {}".format(ws_url_left), flush=True)
  print("Result Websocket Url R: {}".format(ws_url_right), flush=True)

  web_res = {}
  web_res["ws_url_left"] = ws_url_left
  web_res["ws_url_right"] = ws_url_right
  web_res["audio_ws_url"] = audio_ws_url
  return web_res 

msgCnt = 0
startTime = 0

# function to process JSON with incremental transcription results sent as messages over websocket
def process_ws_msg(wsMsg, stack, prefix):
  global msgCnt, startTime, channelOfLastWordReceived
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
        return
      else:
        # delete and edits
        if(channelOfLastWordReceived != prefix):
          # new channel
          stack.clear()        
        for i in range(toDel):
          if(len(stack) > 0):
            stack.pop()
        edits = data.get('edit')
        if(not (edits is None)):
          for edit in edits:
            utter = edit.get('utt')
            stack.append(utter)
          channelOfLastWordReceived = prefix
    else:
      # simple utterance
      if(channelOfLastWordReceived != prefix):
        # new channel
        stack.clear()        
      stack.append(utter)
      channelOfLastWordReceived = prefix
      if( len(stack) > 50 ):
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
      outputs={conv_fname : ['-ar', str(sampleRate), '-f', ffmpegFormat, '-y']}
  )
  ff.cmd
  ff.run()
  print("\nstreaming "+conv_fname+" to "+audio_ws_url, flush=True)
  with open(conv_fname, "rb") as f:
    async with websockets.connect(audio_ws_url, 
      # we need to lower the buffer size - otherwise the sender will buffer for too long
      write_limit=512, 
      # compression needs to be disabled otherwise will buffer for too long
      compression=None,
      ping_timeout=None
      ) as websocket:
      try:
        print(str(datetime.datetime.now())+" audio websocket connected", flush=True)

        # print("sleeping 3 seconds to trigger timeout", flush=True)
        # timeLeft = 3
        # while timeLeft > 0:
        #   print(str(timeLeft)+" ", end =" ", flush=True)
        #   time.sleep(1)
        #   try:
        #     await websocket.ping()
        #   except Exception as e:
        #       print(str(datetime.datetime.now())+" Exception 0 when sending ping via websocket: "+str(e)) 
        #       break
        #   timeLeft -= 1

        # test websocket close before sending audio  
        # await websocket.close()
        # print(str(datetime.datetime.now())+" audio websocket closed", flush=True)
        # return

        global startTime
        startTime = time.time()
        n_buf = 512 #1 * 1024
        byte_buf = f.read(n_buf)
        start = time.time()
        epoch_start_audio_stream = start
        elapsed_time_fl = 0
        count = 0
        slept = False
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
          
          # if(not slept and elapsed_time_fl > 0.0001):
          #   print("elapsed time: "+str(elapsed_time_fl))
          #   print("sleeping 3 seconds to trigger timeout", flush=True)
          #   left = 3
          #   while left > 0:
          #     print(str(left)+" ", end =" ", flush=True)
          #     time.sleep(1)
          #     left -= 1
          #   start += 35
          #   slept = True
          #   # test websocket close before sending audio  
          #   await websocket.close()
          #   print(str(datetime.datetime.now())+" audio websocket closed", flush=True)
          #   return            

          #   global session_id_left, session_id_right
          #   body = {"pause": {"action" : "stop"}}
          #   url = "{}://{}/{}/asr/transcribe/{}".format(protocol, hostPort, urlPrefix, session_id_left)
          #   print(f"making PUT request to {url}", flush=True)
          #   requests.put(url, json=body, headers=headers)
          #   url = "{}://{}/{}/asr/transcribe/{}".format(protocol, hostPort, urlPrefix, session_id_right)
          #   print(f"making PUT request to {url}", flush=True)
          #   requests.put(url, json=body, headers=headers)

        elapsed_time_fl = (time.time() - start)
        print(str(datetime.datetime.now())+" done streaming audio in "+str(elapsed_time_fl), flush=True)
        print("Waiting 10 seconds for processing to finish...", flush=True)  
        time.sleep(10.0)
        print("done waiting", flush=True)  
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

  # print("sleeping 35 seconds to trigger timeout", flush=True)
  # timeLeft = 15 * 60
  # while timeLeft > 0:
  #   print(str(timeLeft)+" ", end =" ", flush=True)
  #   time.sleep(1)
  #   timeLeft -= 1
  
  # global session_id_left, session_id_right

  # pausebody = {"pause": {"action" : "stop"}}

  # url = "{}://{}/{}/asr/transcribe/{}".format(protocol, hostPort, urlPrefix, session_id_left)
  # print(f"making PUT request to {url}", flush=True)
  # requests.put(url, json=body, headers=headers)
  # url = "{}://{}/{}/asr/transcribe/{}".format(protocol, hostPort, urlPrefix, session_id_right)
  # print(f"making PUT request to {url}", flush=True)
  # requests.put(url, json=pausebody, headers=headers)

  threadWsLeft = wsThread(web_res["ws_url_left"], "L >>\t")
  threadWsRight = wsThread(web_res["ws_url_right"], "R <<")  
  threadWsLeft.start()
  threadWsRight.start()
  
  # stream audio
  asyncio.get_event_loop().run_until_complete( stream_audio(file_name, web_res["audio_ws_url"]) )

  # wait for websocket thread to join 
  print("waiting for receiving websocket threads to join", flush=True)
  threadWsLeft.join()
  threadWsRight.join()

  print("downloading captured audio", flush=True)

  time.sleep(2)
  print("done sleeping", flush=True)

  if( not(capturedAudio is None or capturedAudio == "")):
    url = "{}://{}/{}/data/{}/file".format(protocol, hostPort, urlPrefix, capturedAudio)
    print(f"making GET request to {url}", flush=True)
    audio_response = requests.get(url, headers=headers)
    with open(f"{file_name}-captured.wav", "wb") as f:
      f.write(audio_response.content)
    print(f"downloaded captured audio to {file_name}-captured.wav", flush=True)

  print(f"END processing: {file_name}")

## end of function and variable definitions
## main run starts here


process_audio(inputFilePath)

print("sleeping 60 seconds", flush=True )
time.sleep(60)
print("done sleeping", flush=True )