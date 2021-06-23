"""
pip install websockets
pip install ffmpy
"""

import requests, time, os, json, random
import threading
import asyncio
import websockets
import stomper as stomper
import datetime

# global 
# map from filename to recognition result
from_stomp = []
received_results = []

JWT = "<Your JWT here>"
wsUrl = "wss://cc.voicegain.ai/nats-websocket/port"
topic = "/topic/1234567890987654321"

headers = {"Authorization":JWT}

fut = None

websocket = None
websocketRes = None
keepRunning = True

sa_results = []
utts = {}
utts[1] = []
utts[2] = []
ends = {}
ends[1] = -5000
ends[2] = -5000
output = {}
output[1] = ""
output[2] = ""

# function to print results sent as messages over websocket
def process_ws_msg(wsMsg):
  print(str(datetime.datetime.now())+" received -> "+wsMsg, flush=True)
  global from_stomp 
  from_stomp.append( wsMsg )
  groups = wsMsg.split('\n\n') 
  msg = groups[1]
  print("Msg: "+msg, flush=True)
  msgObj = json.loads(msg)
  if msgObj.get("websocket") is None:
    return
  url = msgObj.get("websocket").get("url")
  ## set the future
  #fut.set_result("url")

# try to receive from websocket
async def receiveWs():
  try:
    ws_msg = await asyncio.wait_for(websocket.recv(), timeout=0.25)
    process_ws_msg(ws_msg)
  except asyncio.TimeoutError:
    print("~", end =" ", flush=True)

# connect to stomp
async def ws_conn_to_stomp():
  print("START ws_conn_to_stomp", flush=True)
  print ("Connecting to: "+wsUrl+" for topic "+topic, flush=True)
  global websocket, keepRunning
  async with websockets.connect(
    wsUrl, 
    #extra_headers={"Authorization":JWT},
    # we need to lower the buffer size - otherwise the sender will buffer for too long
    write_limit=1024, 
    # compression needs to be disabled otherwise will buffer for too long
    compression=None) as ws:
      print ("Connected to: "+wsUrl, flush=True)
      # Initate Stomp connection!
      await ws.send("CONNECT\naccept-version:1.0,1.1,2.0\n\n\x00\n")
      print ("Connected to STOMP", flush=True)

      # Subscribing to topic
      client_id = str(random.randint(0, 1000))
      sub = stomper.subscribe(topic, client_id, ack='auto')
      await ws.send(sub)
      print ("subscribed to topic "+topic+" with client_id "+client_id, flush=True)

      websocket = ws # store to a global
      try:
        while keepRunning:
          ws_msg = await receiveWs()

        print ("Stopping: "+wsUrl, flush=True)
        await ws.close(code=1002, reason="stopped by request")
        print ("Stopped", flush=True)
      except Exception as e: 
        print ("Stopped by exception from ws receive: "+str(e), flush=True)  

      keepRunning = False

  print("  END ws_conn_to_stomp", flush=True)


def appendUtt(spk, utt, start, end):
  global utts, ends
  if((start - ends[spk])>2000):
    utts[spk] = [] # clear
  utts[spk].append(utt)
  n = len(utts[spk])
  if(n > 40):
    # drop first 20 words
    for i in range(20):
      utts[spk].pop(0)
    n = len(utts[spk])
  ends[spk] = end

def outputUtt():
  outputSpkUtt(1)
  outputSpkUtt(2)  

def outputSpkUtt(spk):
  global utts, output, sa_results, ends
  out = " ".join(utts[spk])
  if(out != output[spk]):
    output[spk] = out
    txt = ("SPK "+str(spk)+" [{:6d}] "+out).format(ends[spk])
    print("\n"+txt, flush=True)
    sa_results.append(txt)

def handleEmotion(start, end, spk, sentiment, mood):
  if sentiment is not None:
    txt = ("SPK "+str(spk)+" [{:6d} - {:6d}] {} sentiment={:6.4f}").format(start, end, "NEGATIVE" if sentiment<0 else "POSITIVE", sentiment)
    print("\n"+txt, flush=True)
    sa_results.append(txt)
  if mood is not None:
    moods = []
    for moodName in mood:
      moods.append((moodName+"={}").format(+mood[moodName]))
    txt = ("SPK "+str(spk)+" [{:6d} - {:6d}] moods: "+" ".join(moods)).format(start, end)
    print("\n"+txt, flush=True)
    sa_results.append(txt)

def handleKwd(kwd):
  txt = ("SPK "+str(kwd.get("spk"))+" [{:6d} - {:6d}] keyword {}: {}").format(kwd.get("start"), kwd.get("end"),  kwd.get("tag"),  kwd.get("phrase"))
  print("\n"+txt, flush=True)
  sa_results.append(txt)

def handlePhrase(phrase):
  txt = ("SPK "+str(phrase.get("spk"))+" [{:6d} - {:6d}] phrase {}: {} [slots:{}]").format(phrase.get("start"), phrase.get("end"),  phrase.get("tag"),  phrase.get("phrase"), phrase.get("slots"))
  print("\n"+txt, flush=True)
  sa_results.append(txt)

def handleNER(ner):
  txt = ("SPK "+str(ner.get("spk"))+" [{:6d} - {:6d}] named entity {}: {} [concepts:{}]").format(ner.get("start"), ner.get("end"),  ner.get("entity"),  ner.get("phrase"), ner.get("concepts"))
  print("\n"+txt, flush=True)
  sa_results.append(txt)


# function to print results sent as messages over websocket
def process_ws_res_msg(wsMsg):
  #print("json: "+wsMsg, flush=True)
  data = json.loads(wsMsg)
  global sa_results, utts 
  for key in data:
    if(key == "word"):
      words = data["word"]
      for word in words:
        appendUtt(word.get("spk"), word.get("utt"), word.get("start"), word.get("end"))
    if(key == "emotion"):
      emotions = data["emotion"]
      for emotion in emotions:
        handleEmotion(emotion.get("start"), emotion.get("end"), emotion.get("spk"), emotion.get("sentiment"), emotion.get("mood"))
    if(key == "keyword"):
      keywords = data["keyword"]
      for kwd in keywords:
        handleKwd(kwd)
    if(key == "phrase"):
      phrases = data["phrase"]
      for phrase in phrases:
        handlePhrase(phrase)
    if(key == "ner"):
      ners = data["ner"]
      for ner in ners:
        handleNER(ner)

    outputUtt()

# try to receive from websocket
async def receiveWsRes():
  try:
    ws_msg = await asyncio.wait_for(websocketRes.recv(), timeout=0.25)
    process_ws_res_msg(ws_msg)
  except asyncio.TimeoutError:
    print("~", end =" ", flush=True)

# connect to resultswebsocket
async def ws_conn_to_results():
  print("START ws_conn_to_results -> waiting for websocket url", flush=True)
  await fut
  wsUrlResults = fut.result()
  print ("Connecting to: "+wsUrlResults, flush=True)
  global websocketRes, keepRunning
  async with websockets.connect(
    wsUrlResults, 
    extra_headers={"Authorization":JWT},
    # we need to lower the buffer size - otherwise the sender will buffer for too long
    write_limit=1024, 
    # compression needs to be disabled otherwise will buffer for too long
    compression=None) as ws:
      print ("Connected to: "+wsUrlResults, flush=True)

      wsUrlResults = ws # store to a global
      try:
        while keepRunning:
          ws_msg = await receiveWsRes()

        print ("Stopping: "+wsUrlResults, flush=True)
        await ws.close(code=1002, reason="stopped by request")
        print ("Stopped", flush=True)
      except Exception as e: 
        print ("Stopped by exception from ws receive: "+str(e), flush=True)  

      keepRunning = False

  print("  END ws_conn_to_results", flush=True)

async def main():
  print("START main", flush=True)
  """
  This is the main entry point for the program
  """
  loop = asyncio.get_running_loop()
  global fut
  fut = loop.create_future()

  await asyncio.gather(
    asyncio.create_task(ws_conn_to_stomp()),
    asyncio.create_task(ws_conn_to_results())
   )

  print("  END main", flush=True)

if __name__ == "__main__":
  asyncio.run(main())
  print("\nStomp messages received:")
  for x in from_stomp:
    print(x)

  print("\nSpeech Analytics Results:")
  for x in sa_results:
    print(x)