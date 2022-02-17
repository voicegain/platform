"""
pip install requests
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
## all of the files in the directory will be submitted for recognition one by one
input_path = "./2-identical/"


platform ="voicegain"
## the WS configuration id - get from ASR Settings on the Web Console (last part of the wss URL)
wsConfId = "243f8d4f-68c8-445a-8cc7-1050e301ae67"
JWT = "<your JWT token - has to be from the same context as wsConfId - get it from the Web Console at https://console.voicegain.ai>"

list_of_files = []

for root, dirs, files in os.walk(input_path):
	for file in files:
		list_of_files.append(os.path.join(root,file))

print("files to test")
for name in list_of_files:
    print(name)

# global 
# map from filename to recognition result
recognition_results = []

wsUrl = "wss://api.{}.ai/v1/ws/asr/{}".format(platform, wsConfId)

headers = {"Authorization":JWT}

websocket = None
keepRunning = True

# function to print results sent as messages over websocket
def process_ws_msg(wsMsg):
  print(str(datetime.datetime.now())+" received -> "+wsMsg, flush=True)
  global recognition_results 
  recognition_results.append( wsMsg )

# try to receive from websocket
async def receiveWs():
  try:
    ws_msg = await asyncio.wait_for(websocket.recv(), timeout=0.25)
    process_ws_msg(ws_msg)
  except asyncio.TimeoutError:
    print("~", end =" ", flush=True)

# function that connects to the websocket and receives the results
async def ws_conn_receive():
  print("START ws_conn_receive", flush=True)
  print ("Connecting to: "+wsUrl, flush=True)
  global websocket
  async with websockets.connect(
    wsUrl, 
    extra_headers={"Authorization":JWT},
    # we need to lower the buffer size - otherwise the sender will buffer for too long
    write_limit=1024, 
    # compression needs to be disabled otherwise will buffer for too long
    compression=None) as ws:
      print ("Connected to: "+wsUrl, flush=True)
      websocket = ws # store to a global
      try:
        while keepRunning:
          ws_msg = await receiveWs()

        print ("Stopping: "+wsUrl, flush=True)
        await ws.close(code=1002, reason="stopped by request")
        print ("Stopped", flush=True)
      except Exception as e: 
        print ("Stopped by exception from ws receive: "+str(e), flush=True)  

  print("  END ws_conn_receive", flush=True)

# function to send a message over a websocket
async def sendMsg(msg):
  msgStr = json.dumps(msg)
  
  print (str(datetime.datetime.now())+" Sending "+str(msgStr), flush=True)
  try:
    await websocket.send(msgStr)
    print ("Done Sending "+str(msgStr), flush=True)
  except Exception as e:
    print ("Exception while sending "+str(e), flush=True)

# function to read audio from file and convert it to L16 and send to websocket
async def stream_audio(file_name):
  print("START stream_audio", flush=True)
  conv_fname = (file_name+'.wav').replace(input_path, "./")
  ff = FFmpeg(
      inputs={file_name: []},
      outputs={conv_fname : ['-ar', '16000', '-f', 's16le', '-y', '-map_channel', '0.0.0']}
  )
  ff.cmd
  ff.run()
  print("\nstreaming "+conv_fname+" to "+str(websocket), flush=True)
  with open(conv_fname, "rb") as f:
    try:
      print(str(datetime.datetime.now())+" start streaming", flush=True)
      n_buf = 1 * 1024
      byte_buf = f.read(n_buf)
      start = time.time()
      elapsed_time_fl = 0
      count = 0
      while byte_buf:
        n = len(byte_buf)
        print(".", end =" ", flush=True)
        await websocket.send(byte_buf)
        count += n
        elapsed_time_fl = (time.time() - start)
        expected_time_fl = count / 32000.0
        time_to_wait = expected_time_fl - elapsed_time_fl
        if time_to_wait >= 0: 
          time.sleep(time_to_wait) # to simulate real time streaming
        byte_buf = f.read(n_buf)
      elapsed_time_fl = (time.time() - start)
      print(str(datetime.datetime.now())+" done streaming audio in "+str(elapsed_time_fl), flush=True)
    except Exception as e:
      print("Exception when sending audio via websocket: "+str(e)) 

  print(str(datetime.datetime.now())+" done streaming audio", flush=True)

# function to stream content of one file
async def ws_send_one(file_name):
  print("START ws_send_one: "+file_name, flush=True)
  await sendMsg( 
  { "type": "start",
    "language": "en-US",
    "format": "raw",
    "encoding": "LINEAR16",
    "sampleRateHz": 16000}) 

  await asyncio.sleep(2.0)

  await( stream_audio(file_name) )

  await asyncio.sleep(4.5)

  await sendMsg( {"type" : "stop"})

  print("  END ws_send_one: "+file_name, flush=True)

# function to stream all files from directory one after another
async def ws_send():
  print("START ws_send", flush=True)

  while websocket is None:
    print("^", end =" ", flush=True)
    await asyncio.sleep(0.25)

  print ("Connected: "+str(websocket), flush=True)

  for aFile in list_of_files:
    await ws_send_one(aFile)

  print ("sleeping before stop...", flush=True)
  await asyncio.sleep(3.0)
  global keepRunning
  keepRunning = False
  print ("requested a stop", flush=True)

  print("  END ws_send", flush=True)

## main function
async def main():
  print("START main", flush=True)
  """
  This is the main entry point for the program
  """
  await asyncio.gather(
    asyncio.create_task(ws_conn_receive()),
    asyncio.create_task(ws_send())
   )

  print("  END main", flush=True)

if __name__ == "__main__":
  asyncio.run(main())
  print("\nWebsocket responses received:")
  for x in recognition_results:
    print(x)