"""
pip install websockets
pip install ffmpy
"""
# you will need ffmpeg utility installed on your system

from ffmpy import FFmpeg

import requests, time, os, json
import threading
import asyncio
import websockets
import datetime

## specify here the directory with files to test
input_path = "./single/"

#voicegain
platform = "voicegain"
JWT = "< your JWT >"


list_of_files = []

for root, dirs, files in os.walk(input_path):
	for file in files:
		list_of_files.append(os.path.join(root,file))

print("files to test")
for name in list_of_files:
    print(name)

# global
session_url = None
streamingStart =  time.time()


headers = {"Authorization":JWT}
# new transcription session request
# it specifies audio input via an websocket stream
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
      "speechContext" : "normal",
      "noInputTimeout": -1,
      "completeTimeout": -1.,
      "sensitivity" : 0.5
    }
  }
}


def web_api_request(headers, body):
  init_response_raw = requests.post("https://api.{}.ai/v1/asr/transcribe/async".format(platform), json=body, headers=headers)
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
  result["session_url"] = init_response["sessions"][0]["sessionUrl"]
  result["audio_ws_url"] = init_response["audio"]["stream"]["websocketUrl"]
  result["capturedAudio"] = init_response["audio"].get("capturedAudio")

  print("        sessionId: {}".format(result["session_id"]))
  print("  Audio Websocket: {}".format(result["audio_ws_url"]))
  if( not(result.get("capturedAudio") is None)):
    print("captured audio id: {}".format(result["capturedAudio"]))
  print("Results Websocket: {}".format(result["ws_url"]), flush=True)
  print("      Session Url: {}".format(result["session_url"]), flush=True)

  global session_url
  session_url = result["session_url"]
  return result

# stack will contain the words returned from transcription
stack = []

# function to process JSON with incremental transcription results sent as messages over websocket
def process_ws_msg(wsMsg, fname):
  print("at "+str(time.time() - streamingStart)+"sec "+wsMsg, flush=True)
  try:
    data = json.loads(wsMsg)
    utter = data.get('utt')
    if( utter is None ):
      toDel = data.get('del')
      if( toDel is None):
        print("EDIT->"+wsMsg, flush=True)
      else:
        for i in range(toDel):
          stack.pop()
        edits = data.get('edit')
        if(not (edits is None)):
          for edit in edits:
            utter = edit.get('utt')
            stack.append(utter)
    else:
      stack.append(utter)
    print(' '.join(stack), flush=True)
  except Exception as e: 
    print("ERROR: "+str(e), flush=True)


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
  global streamingStart
  with open(conv_fname, "rb") as f:
    async with websockets.connect(audio_ws_url, 
      # we need to lower the buffer size - otherwise the sender will buffer for too long
      write_limit=480, 
      # compression needs to be disabled otherwise will buffer for too long
      compression=None) as websocket:
      try:
        print(str(datetime.datetime.now())+" sender connected", flush=True)
        n_buf = 1 * 480
        byte_buf = f.read(n_buf)
        start = time.time()
        epoch_start_audio_stream = start
        elapsed_time_fl = 0
        count = 0
        streamingStart =  time.time()
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

          expected_time_fl = count / 8000.0
          time_to_wait = expected_time_fl - elapsed_time_fl
          if time_to_wait >= 0: 
            time.sleep(time_to_wait) # to simulate real time streaming
          byte_buf = f.read(n_buf)
        elapsed_time_fl = (time.time() - start)
        print(str(datetime.datetime.now())+" done streaming audio in "+str(elapsed_time_fl), flush=True)
        print("Waiting 5 seconds for processing to finish...", flush=True)  
        time.sleep(5.0)
        print("done waiting", flush=True)  

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
      print ("Starting receiver "+str(datetime.datetime.now()), flush=True)
      try:
        asyncio.new_event_loop().run_until_complete(websocket_receive(self.ws_uri, self.fname))  
      except Exception as e: 
        print(e)
      print ("Exiting "+str(datetime.datetime.now()), flush=True)

# function that connects to the websocket and receives the results
async def websocket_receive(uri, fname):
  print(str(datetime.datetime.now())+" connecting receiver to "+uri, flush=True)
  async with websockets.connect(uri, 
      # we need to lower the buffer size - otherwise the sender will buffer for too long
      write_limit=480, 
      # compression needs to be disabled otherwise will buffer for too long
      compression=None) as websocket:
    print(str(datetime.datetime.now())+" receiver connected", flush=True)
    try:
      while True:
        ws_msg = await websocket.recv()
        process_ws_msg(ws_msg, fname)
    except Exception as e: 
      print(e)  

def process_audio(file_name):
  print("START processing: "+file_name)
  global stack
  stack = []
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


