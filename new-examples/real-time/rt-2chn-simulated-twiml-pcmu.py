#pip install websockets

import requests, time, os, json
import threading
import asyncio
import websockets
import datetime
import base64
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
inputFile2 = cfg.get("DEFAULT", "INPUTFILE2")

inbound_audio = f"{inputFolder}/{inputFile}"
outbound_audio = f"{inputFolder}/{inputFile2}"

headers = {"Authorization":JWT}
# new transcription session request
# it specifies audio input via an TWIML stream
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
    "source": { "stream": { "protocol": "TWIML", "noAudioTimeout" : 150000 } },
    "format": "PCMU",
    "channel" : "stereo",
    "rate": 8000, 
    "capture": 'true'
  },
  "settings": {
    "asr": {
      "acousticModelRealTime": "VoiceGain-kappa",
      "noInputTimeout": 60000,
      "completeTimeout": 0
    }
  }
}

print("making request", flush=True)
url = "{}://{}/{}/asr/transcribe/async".format(protocol, hostPort, urlPrefix)
init_response_raw = requests.post(url, json=body, headers=headers)
print("done request: {}".format(init_response_raw), flush=True)
print("response headers: {}".format(init_response_raw.headers), flush=True)


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
audio_ws_url = init_response["audio"]["stream"]["websocketUrl"]
capturedAudio = init_response["audio"].get("capturedAudio")

print("      SessionId L: {}".format(session_id_left))
print("      SessionId R: {}".format(session_id_right))
print(" Audio webscocket: {}".format(audio_ws_url))

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
async def stream_audio():
  print("stream_audio start", flush=True)
  print("Inbound audio file: {}".format(inbound_audio), flush=True)
  print("Outbound audio file: {}".format(outbound_audio), flush=True)
  with open(inbound_audio, mode='rb') as file1: 
      with open(outbound_audio, mode='rb') as file2: 
        async with websockets.connect(audio_ws_url, 
          # we need to lower the buffer size - otherwise the sender will buffer for too long
          write_limit=480, 
          # compression needs to be disabled otherwise will buffer for too long
          compression=None) as websocket:
          try:
            print(str(datetime.datetime.now())+" sender connected", flush=True)


            # print("sleeping 3 seconds before shutting down websocket", flush=True)
            # timeLeft = 3
            # while timeLeft > 0:
            #   print(str(timeLeft)+" ", end =" ", flush=True)
            #   time.sleep(1)
            #   # try:
            #   #   await websocket.ping()
            #   # except Exception as e:
            #   #     print(str(datetime.datetime.now())+" Exception 0 when sending ping via websocket: "+str(e)) 
            #   #     break
            #   timeLeft -= 1

            # # test websocket close before sending audio  
            # await websocket.close()
            # print(str(datetime.datetime.now())+" audio websocket closed", flush=True)
            # return            

            conn_msg = {
              "event": "connected",
              "protocol": "Call",
              "version": "1.0.0"
            }

            try:
              print("send connect", flush=True)
              await websocket.send(json.dumps(conn_msg))
            except Exception as e:
              print(str(datetime.datetime.now())+" connected message "+str(e))

            seq_num = 1

            start_msg = {
              "event": "start",
              "sequenceNumber": seq_num,
              "start": {
                "streamSid": "MZ18ad3ab5a668481ce02b83e7395059f0",
                "accountSid": "AC123",
                "callSid": "CA123",
                "tracks": ["inbound","outbound"],
                "mediaFormat": {
                  "encoding": "audio/x-mulaw",
                  "sampleRate": 8000,
                  "channels": 1
                }
              },
              "streamSid": "MZ18ad3ab5a668481ce02b83e7395059f0"
            }
            seq_num = seq_num+1

            try:
              print("send start", flush=True)
              await websocket.send(json.dumps(start_msg))
            except Exception as e:
              print(str(datetime.datetime.now())+" connected message "+str(e))

            inb_ts = 0
            outb_ts = 0
            inb_chk = 1
            outb_chk = 1
            inbound_bytes = file1.read(44) 
            outbound_bytes = file2.read(44) 
            while True:
              inbound_bytes = file1.read(512)  
              if not inbound_bytes:
                break
              if(inb_chk == 1):
                print("4 inbound bytes: {} {} {} {}".format(inbound_bytes[0], inbound_bytes[1], inbound_bytes[2], inbound_bytes[3]))
              encoded_data = base64.b64encode(inbound_bytes).decode('ascii')

              media_msg = {
                "event": "media",
                "sequenceNumber": seq_num,
                "media": {
                  "track": "inbound",
                  "chunk": inb_chk,
                  "timestamp": inb_ts,
                  "payload": encoded_data
                },
                "streamSid": "MZ18ad3ab5a668481ce02b83e7395059f0"
              }

              try:
                #print("send media inbound {}".format(inb_ts), flush=True)
                if(inb_chk <= 20):
                    print("send media inbound {}".format(json.dumps(media_msg)), flush=True)
                await websocket.send(json.dumps(media_msg))
              except Exception as e:
                print(str(datetime.datetime.now())+" connected message "+str(e))
                break
              seq_num = seq_num+1
              inb_chk = inb_chk+1
              inb_ts = inb_ts+64


              outbound_bytes = file2.read(512)  
              if not outbound_bytes:
                break
              if(outb_chk == 1):
                print("4 outbound bytes: {} {} {} {}".format(outbound_bytes[0], outbound_bytes[1], outbound_bytes[2], outbound_bytes[3]))
              encoded_data = base64.b64encode(outbound_bytes).decode('ascii')

              media_msg = {
                "event": "media",
                "sequenceNumber": seq_num,
                "media": {
                  "track": "outbound",
                  "chunk": outb_chk,
                  "timestamp": outb_ts,
                  "payload": encoded_data
                },
                "streamSid": "MZ18ad3ab5a668481ce02b83e7395059f0"
              }

              # to trigger issue
#              if(outb_chk != 5 ):
#                time.sleep(0.222)

              try:
                #print("send media outbound {}".format(outb_ts), flush=True)
                if(outb_chk <= 20):
                    print("send media outbound {}".format(json.dumps(media_msg)), flush=True)
                await websocket.send(json.dumps(media_msg))
              except Exception as e:
                print(str(datetime.datetime.now())+" connected message "+str(e))
                break            

              seq_num = seq_num+1
              outb_chk = outb_chk+1
              outb_ts = outb_ts+64 # 512 bytes is 64 ms of audio at 8kHz PCMU mono
              time.sleep(0.064)
              print(".", end =" ", flush=True)

              # if(outb_ts > 15000):
              #   # test websocket close before sending audio  
              #   await websocket.close()
              #   print(str(datetime.datetime.now())+" audio websocket closed", flush=True)
              #   return            

            stop_msg = {
              "event": "stop",
              "sequenceNumber": seq_num,
              "stop": {
                "accountSid": "AC123",
                "callSid": "CA123"
              },
              "streamSid": "MZ18ad3ab5a668481ce02b83e7395059f0"
            }

            try:
              print("send stop", flush=True)
              await websocket.send(json.dumps(stop_msg))
            except Exception as e:
              print(str(datetime.datetime.now())+" connected message "+str(e))

            time.sleep(3.0)
            await websocket.close()
          except Exception as e:
            print("Exception when sending audio via websocket: "+str(e)) # usually because the session closed due to NOMATCH or NOINPUT

  print(str(datetime.datetime.now())+" done streaming audio", flush=True)
        

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
asyncio.get_event_loop().run_until_complete( stream_audio() )

# wait for websocket thread to join 
print("")
print("Waiting to join Left  "+str(datetime.datetime.now()), flush=True)
threadWsLeft.join()   
print("Joined Left           "+str(datetime.datetime.now()), flush=True)
print("")
print("Waiting to join Right "+str(datetime.datetime.now()), flush=True)
threadWsRight.join()   
print("Joined Right          "+str(datetime.datetime.now()), flush=True)

print("sleeping 10 seconds to ", flush=True  )
time.sleep(10.0)
print("done", flush=True)