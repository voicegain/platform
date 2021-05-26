"""
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
input_path = "./m4a/"
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

#ascalon
JWT = "eyJhbGciOiJIUxxxxInR5cCI6IkpXVCJ9.eyJhdWQiOiIqLmFzY2FsbG9uLmFpIiwic3VxxxxxWI1LWIxNTEtZDY5NzI0OGExNDM5In0.5ihsWN3q0HXz7oxxxHA5vZb6Tw"
wsConfId = "a68a43f7-xxxxx-d697248a1439"
#voicegain
#JWT = "eyJhbGciOiJIUzIxxxx5cCI6IkpXVCJ9.eyJhdWQiOiJodHRwczovL2FwaS52b2ljZWdxxxyNTMtYjc3My1hNmNhNTU2MWRiYTYifQ.Yj4TlKQ92B8gxixxxxv-3qEa_FIEttK8yI"
headers = {"Authorization":JWT}
wsUrl = "wss://api.voicegain.ai/v1/ws/asr/"+wsConfId
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
    write_limit=4096, 
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

async def sendMsg(msg):
  msgStr = json.dumps(msg)
  
  print ("Sending "+str(msgStr), flush=True)
  try:
    await websocket.send(msgStr)
    print ("Done Sending "+str(msgStr), flush=True)
  except Exception as e:
    print ("Exception while sending "+str(e), flush=True)

# function to read audio from file and convert it to ulaw and send to websocket
async def stream_audio(file_name):
  print("START stream_audio", flush=True)
  conv_fname = (file_name+'.ulaw').replace(input_path, "./")
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
      n_buf = 2 * 1024
      byte_buf = f.read(n_buf)
      while byte_buf:
        n = len(byte_buf)
        print(".", end =" ", flush=True)
        await websocket.send(byte_buf)
        time.sleep(n/32000.0) # to simulate real time streaming
        byte_buf = f.read(n_buf)
    except Exception as e:
      print("Exception when sending audio via websocket: "+str(e)) # usually because the session closed due to NOMATCH or NOINPUT

  print(str(datetime.datetime.now())+" done streaming audio", flush=True)

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

  await asyncio.sleep(2.0)

  await sendMsg( {"type" : "stop"})

  print("  END ws_send_one: "+file_name, flush=True)

async def ws_send(file_name):
  print("START ws_send", flush=True)

  while websocket is None:
    print("^", end =" ", flush=True)
    await asyncio.sleep(0.25)

  print ("Connected: "+str(websocket), flush=True)

  for aFile in list_of_files:
    await ws_send_one(file_name)

  await asyncio.sleep(5.0)
  keepRunning = False

  print("  END ws_send", flush=True)

async def main():
  print("START main", flush=True)
  """
  This is the main entry point for the program
  """
  await asyncio.gather(
    asyncio.create_task(ws_conn_receive()),
    asyncio.create_task(ws_send(list_of_files[0]))
   )

  print("  END main", flush=True)

if __name__ == "__main__":
  asyncio.run(main())
  print("\nWebsocket responses received:")
  for x in recognition_results:
    print(x)