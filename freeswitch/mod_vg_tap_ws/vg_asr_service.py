from fastapi import FastAPI,Response
import requests, time, os, json
import asyncio
import threading
import datetime
import websockets

JWT = "TOKEN HERE"
headers = {"Authorization":JWT}

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
      },
      "metadata" : [
        {"name" : "ANI", "value" : "+19725180012"}
      ]
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
      },
      "metadata" : [
        {"name" : "DNIS", "value" : "983476"}
      ]
    }
  ],
  "audio": {
    "source": { "stream": { "protocol": "WEBSOCKET" } },
    "format": "L16",
    "channels" : "stereo",
    "rate": 8000,
    "capture": 'true'
  },
  "settings": {
    "asr": {
      "acousticModelRealTime": "VoiceGain-kappa",
      "noInputTimeout": 60000,
      "completeTimeout": 0,
      "sensitivity" : 0.99
    }
  }
}

audio_ws_url =None
app = FastAPI()

@app.get("/get_ws_url")
def read_root():    
    print("START processing: ")
    web_res = web_api_request(headers, body)
    audio_ws_url=web_res["audio_ws_url"]
    response = Response(content=audio_ws_url)
    response.headers["Content-Type"] = "text/plain"
    threading.Thread(target=listen_for_audio_transcriptons,args=(web_res,)).start()  
    return response

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

def web_api_request(headers, body):
  init_response_raw = requests.post("https://api.voicegain.ai/v1/asr/transcribe/async", json=body, headers=headers)
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

# stream audio
def listen_for_audio_transcriptons(web_res):

  # create and start the websocket thread
  threadWsLeft = wsThread(web_res["ws_url_left"], "L >>\t")
  threadWsRight = wsThread(web_res["ws_url_right"], "R <<")  
  threadWsLeft.start()
  threadWsRight.start()  

  # wait for websocket thread to join 
  threadWsLeft.join()
  threadWsRight.join()
  print("END processing: ")

## end of function and variable definitions
## main run starts here
