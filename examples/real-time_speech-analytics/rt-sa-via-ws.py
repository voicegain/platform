#pip install websockets
#pip install ffmpy

from ffmpy import FFmpeg

import requests, time, os, json
import threading
import asyncio
import websockets
import datetime


JWT = "<Your JWT here>" # get it from the Web Console
headers = {"Authorization":JWT}
platform="voicegain"

audio_fname = 'your-stereo-test-file.wav'


sa_config_name = "SA-RTAA-Demo-script-test"

# Speech Analytics Configuration
sa_body = {
    "name": sa_config_name,
 
    "sentiment": True,
    "summary": False,
    "wordCloud": False,
    "gender": True,
    "age": False,
    "profanity": True,    
    "overtalkTotalPercentageThreshold": 1.0,
    "overtalkSingleDurationMaximumThreshold": 1,
    "silenceTotalPercentageThreshold": 10.0,
    "silenceSingleDurationMaximumThreshold": 3,

    "moods": [
        "anger"
    ],

    "entities": [
        "ADDRESS",
        "PHONE",
        "PERSON",
        "MONEY",
        "DATE",
        "TIME"
    ],

    "keywords": [
        {
            "tag": "CANCEL",
            "examples": [
                {
                    "phrase": "cancel",
                    # "usage": null
                }
            ],
            "expand": False,
            "hide": False
        },
        {
            "tag": "EXPENSIVE",
            "examples": [
                {"phrase": "expensive"}, {"phrase": "pricey"}, {"phrase": "costs a lot"}
            ],
            "expand": False,
            "hide": False
        }
    ],

    "phrases": [
        {
            "tag": "AGENT_GREETING",
            "builtIn": False,
            "examples": [
                {
                    "sentence": "hello, good morning my name is Jane",
                    "sensitivity": 0.4
                },
                {
                    "sentence": "well, good morning my name is John",
                    "sensitivity": 0.4
                },
                {
                    "sentence": "good morning my name is Anne, I'll be happy",
                    "sensitivity": 0.4
                }
            ],
            "slots" : {
              "entities" : [
                {
                  "entity" : "PERSON",
                  "required" : True
                }
              ]
            },
             "location" : {
               "channel" : "agent",
               "time" : 20
            },
            "hideIfGroup": False
        },         
        {
            "tag": "ACCOUNT_VERIFY",
            "builtIn": False,
            "examples": [
                {
                    "sentence": "can you please verify your phone number for me",
                    "sensitivity": 0.75
                }
            ],
            "hideIfGroup": False
        },
        {
            "tag": "ANYTHING_ELSE_HELP",
            "builtIn": False,
            "examples": [
                {
                    "sentence": "is there anything else I can help you with",
                    "sensitivity": 0.75
                }
            ],
            "hideIfGroup": False
        },
        {
            "tag": "NOT_FUNCTIONING",
            "builtIn": False,
            "examples": [
                {
                    "sentence": "my radio quit working",
                    "sensitivity": 0.4
                },
                {
                    "sentence": "receiver doesn't work anymore",
                    "sensitivity": 0.6
                },     
                {
                    "sentence": "it is completely dead",
                    "sensitivity": 0.4
                },  
                {
                    "sentence": "it does not power on at all",
                    "sensitivity": 0.4
                }                  
            ],
            "hideIfGroup": False
        },
    ]
}
sa_config_id = None

# new SA session request
# it specifies audio input via a a websocket
# and output is via a plain websocket
body = {
  "asyncMode": "REAL-TIME",
  "audio": {
    "source": { "stream": { "protocol": "WEBSOCKET" } },
    "format": "PCMU",
    "channel" : "stereo",
    "rate": 8000, 
    "capture": 'true'
  },
  "speakerChannels" : [
    { "audioChannelSelector" : "left", "isAgent" : 'true', "vadMode" : "total_music_reject"},
    { "audioChannelSelector" : "right", "isAgent" :'false', "vadMode" : "normal"}
  ],
  "asr": {
    "noInputTimeout": -1,
    "completeTimeout": -1,
    "sensitivity" : 0.3
  },
  "saConfig":sa_config_id
}


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

keep_running = True

epoch_start_audio_stream = None

# setup SA configuration
def web_api_request_sa_config(headers, body):
  print("create new SA config")
  init_response_raw = requests.post("https://api.{}.ai/v1/sa/config".format(platform), json=body, headers=headers)
  init_response = init_response_raw.json()
  if("BAD_REQUEST" == init_response.get("status") and  "the specified name is being used" in  init_response.get("message")):
    print(init_response.get("message"))
    init_response_raw = requests.get("https://api.{}.ai/v1/sa/config?name={}".format(platform, sa_config_name), headers=headers)
    sa_config_list = init_response_raw.json()
    existing_sa_config_id = None
    for sa_config in sa_config_list:
      if(sa_config_name == sa_config.get("name")):
        existing_sa_config_id = sa_config.get("saConfId")
        print("existing SA config: "+existing_sa_config_id)
    if(existing_sa_config_id is None):
      exit()
    ## delete old config
    print("delete old SA config: "+existing_sa_config_id)
    init_response_raw = requests.delete("https://api.{}.ai/v1/sa/config/{}".format(platform, existing_sa_config_id), headers=headers)
    print(init_response_raw.status_code)
    print(init_response_raw.text)
    ## create new config
    web_api_request_sa_config(headers, sa_body)
    return
  elif(init_response.get("saConfId") is None):
    print("did not start create SA config")
    print(init_response_raw.status_code)
    print(init_response_raw.text)
    exit()
  else:
    print("response: {}".format(str(init_response)))

  # retrieve values from response
  global sa_config_id
  sa_config_id = init_response["saConfId"]

  print("          SA Config: {}".format(sa_config_id))

def web_api_request(headers, body):
  body["saConfig"] = sa_config_id
  init_response_raw = requests.post("https://api.{}.ai/v1/sa".format(platform), json=body, headers=headers)
  init_response = init_response_raw.json()
  if(init_response.get("saSessionId") is None):
    print("did not start SA session")
    print(init_response_raw.status_code)
    print(init_response_raw.text)
    exit()

  print("response: {}".format(str(init_response)))

  # retrieve values from response
  # sessionId and capturedAudio are printed for debugging purposes
  sa_session_id = init_response["saSessionId"]
  session_id_left = init_response["speakerChannels"][0]["transcribeSessionId"]
  session_id_right = init_response["speakerChannels"][1]["transcribeSessionId"]
  ws_url = init_response["websocket"]["url"]
  audio_ws_url = init_response["audio"]["stream"]["websocketUrl"]
  capturedAudio = init_response["audio"].get("capturedAudio")

  print("       SA SessionId: {}".format(sa_session_id))
  print("        SessionId L: {}".format(session_id_left))
  print("        SessionId R: {}".format(session_id_right))
  print("Audio Websocket Url: {}".format(audio_ws_url))
  if( not(capturedAudio is None)):
    print("captured audio id: {}".format(capturedAudio))
  print("Result Websocket Url: {}".format(ws_url), flush=True)

  web_res = {}
  web_res["ws_url"] = ws_url
  web_res["audio_ws_url"] = audio_ws_url
  return web_res 

msgCnt = 0

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

def outputUtt(audio_pos):
  outputSpkUtt(audio_pos, 1)
  outputSpkUtt(audio_pos, 2)  

def outputSpkUtt(audio_pos, spk):
  global utts, output, sa_results, ends
  out = " ".join(utts[spk])
  if(out != output[spk]):
    output[spk] = out
    txt = ("SPK "+str(spk)+" <{:5d}>[{:6d}] "+out).format(audio_pos-ends[spk], ends[spk])
    print("\n"+txt, flush=True)
    sa_results.append(txt)

def handleEmotion(audio_pos, start, end, spk, sentiment, mood):
  if sentiment is not None:
    txt = ("SPK "+str(spk)+" <{:5d}>[{:6d} - {:6d}] {} sentiment={:6.4f}").format(audio_pos-end, start, end, "NEGATIVE" if sentiment<0 else "POSITIVE", sentiment)
    print("\n"+txt, flush=True)
    sa_results.append(txt)
  if mood is not None:
    moods = []
    for moodName in mood:
      moods.append((moodName+"={}").format(+mood[moodName]))
    txt = ("SPK "+str(spk)+" <{:5d}>[{:6d} - {:6d}] moods: "+" ".join(moods)).format(audio_pos-end, start, end)
    print("\n"+txt, flush=True)
    sa_results.append(txt)

def handleKwd(audio_pos, kwd):
  txt = ("SPK "+str(kwd.get("spk"))+" <{:5d}>[{:6d} - {:6d}] keyword {}: {}").format(audio_pos-kwd.get("end"), kwd.get("start"), kwd.get("end"),  kwd.get("tag"),  kwd.get("phrase"))
  print("\n"+txt, flush=True)
  sa_results.append(txt)

def handlePhrase(audio_pos, phrase):
  txt = ("SPK "+str(phrase.get("spk"))+" <{:5d}>[{:6d} - {:6d}] phrase {}: {} [slots:{}]").format(audio_pos-phrase.get("end"), phrase.get("start"), phrase.get("end"),  phrase.get("tag"),  phrase.get("phrase"), phrase.get("slots"))
  print("\n"+txt, flush=True)
  sa_results.append(txt)

def handleNER(audio_pos, ner):
  txt = ("SPK "+str(ner.get("spk"))+" <{:5d}>[{:6d} - {:6d}] named entity {}: {} [concepts:{}]").format(audio_pos-ner.get("end"), ner.get("start"), ner.get("end"),  ner.get("entity"),  ner.get("phrase"), ner.get("concepts"))
  print("\n"+txt, flush=True)
  sa_results.append(txt)

# function to print results sent as messages over websocket
def process_ws_msg(wsMsg):
  #print("json: "+wsMsg, flush=True)
  now = time.time()
  audio_pos = int(round(1000.0*(now - epoch_start_audio_stream)))
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
        handleEmotion(audio_pos, emotion.get("start"), emotion.get("end"), emotion.get("spk"), emotion.get("sentiment"), emotion.get("mood"))
    if(key == "keyword"):
      keywords = data["keyword"]
      for kwd in keywords:
        handleKwd(audio_pos,kwd)
    if(key == "phrase"):
      phrases = data["phrase"]
      for phrase in phrases:
        handlePhrase(audio_pos, phrase)
    if(key == "ner"):
      ners = data["ner"]
      for ner in ners:
        handleNER(audio_pos, ner)


    outputUtt(audio_pos)

 #   sa_results.append( wsMsg )


# function to read audio from file and convert it to ulaw and send to websocket
async def stream_audio(file_name, audio_ws_url):
  global epoch_start_audio_stream
  print("START stream_audio", flush=True)
  conv_fname = (file_name+'.ulaw')
  ff = FFmpeg(
      inputs={file_name: []},
      outputs={conv_fname : ['-ar', '8000', '-f', 'mulaw', '-y']}
  )
  ff.cmd
  ff.run()
  print("\nstreaming "+conv_fname+" to "+audio_ws_url, flush=True)
  with open(conv_fname, "rb") as f:
    async with websockets.connect(audio_ws_url, 
      # we need to lower the buffer size - otherwise the sender will buffer for too long
      write_limit=2048, 
      # compression needs to be disabled otherwise will buffer for too long
      compression=None) as websocket:
      try:
        print(str(datetime.datetime.now())+" connected", flush=True)
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
          expected_time_fl = count / 16000.0
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
   def __init__(self, ws_uri):
      threading.Thread.__init__(self)
      self.ws_uri = ws_uri
   def run(self):
      print ("Starting receive loop "+str(datetime.datetime.now()), flush=True)
      try:
        asyncio.new_event_loop().run_until_complete(websocket_receive(self.ws_uri))  
      except Exception as e: 
        print(e)
      print ("Exited receive loop "+str(datetime.datetime.now()), flush=True)

# try to receive from websocket
async def receiveWs(websocket):
  try:
    ws_msg = await asyncio.wait_for(websocket.recv(), timeout=0.25)
    process_ws_msg(ws_msg)
  except asyncio.TimeoutError:
    print("~", end =" ", flush=True)

# function that connects to the websocket and receives the results
async def websocket_receive(uri):
    async with websockets.connect(uri) as websocket:
        try:
          global keep_running
          while keep_running:
            await receiveWs(websocket)
          print("keep_running="+str(keep_running)) 
        except Exception as e: 
          print("Exception within receive: "+str(e))  

def process_audio(file_name):
  print("START processing: "+file_name)
  web_res = web_api_request(headers, body)

  # create and start the websocket thread
  threadWs = wsThread(web_res["ws_url"])
  threadWs.start()

  # stream audio
  asyncio.get_event_loop().run_until_complete( stream_audio(file_name, web_res["audio_ws_url"]) )

  # wait for websocket thread to join 
  threadWs.join()
  print("END processing: "+file_name)


## end of function and variable definitions
## main run starts here

web_api_request_sa_config(headers, sa_body)

process_audio(audio_fname)

print("\nSpeech Analytics Results:")
for x in sa_results:
  print(x)

