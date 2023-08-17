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
outputFolder = cfg.get("DEFAULT", "OUTPUTFOLDER")

inputFilePath = f"{inputFolder}/{inputFile}"

sampleRate = 8000
channels = 2

#format = "PCMU"
#ffmpegFormat = "mulaw"
format = "L16"
ffmpegFormat = "s16le"
pollingInterval = 0.75

bytesPerSample = 2 if format=="L16" else 1

#sendingWSProtocol = "WSS"
sendingWSProtocol = "WS"

#receivingWSProtocol = "wss"
receivingWSProtocol = "ws"

#acousticModelRealTime = "VoiceGain-rho-en-us"
acousticModelRealTime = "VoiceGain-rho"
#acousticModelRealTime = "VoiceGain-kappa"

## set to True if you want to save all the json responses received 
save_all_json_results = False
## this is the directory where output will be saved
output_path = outputFolder
## name of the file will all results - date will be inserted in place of {}
all_results_file = "all_results_{}.txt"


## ALL settings above this line ##

headers = {"Authorization":JWT}

# new transcription session request
# it specifies audio input via an websocket stream
# and output is via polling
body = {
  "sessions": [
    {
      "asyncMode": "REAL-TIME",
      #"audioChannelSelector" : "left",
      "poll": { 
        "afterlife": '60000',
        "persist": '0',
        },
      "content" : {
        "incremental" : ['transcript'],
        "full" : ['transcript']
      }
    }
  ],
  "audio": {
    "source": { "stream": { "protocol": sendingWSProtocol } },
    "format": format,
    "channel" : "mono" if(channels == 1) else "stereo",
    "rate": sampleRate, 
    "capture": 'true'
  },
  "settings": {
        "asr": {
            "speechContext" : "digits",
            "noInputTimeout": -1,
            "completeTimeout": -1,
            "sensitivity" : 0.5,
            "speedVsAccuracy" : 0.5 
            # , "hints" : [
            #     "rupees[roopiece|ruppes]"
            #     , "rupee[rooppee|ruppe]"
            #     , "lakh_rupees[lack_roopiece|lac_ropiece|lak_ropiece|lacropiece]:10"
            #     , "lakhs[lakx|leks|laks]:10"
            #     , "lakh[lak]"
            #     , "for_Hyderabad[for_Hydrobad|for_Hydrobag|for_Hydroba]:10"
            #     , "Hyderabad[Hydrobad|Hydrobag|Hydroba]"
            #     , "twelve_noon"
            #     , "movie_ticket"
            #     , "GB_RAM"
            #     , "MB_RAM[mbee_ram]"
            #     , "your_reward:10"
            #     , "one_hour:10"
            #     , "CVV_number"
            #     , "hyphen[hi_fen]:10"
            #     , "PM_GMT"
            #     , "IP_address[i_p_address]"
            #     , "NASA_center[nassa_center]"
            #     , "ASCII_character[asskey_characters|askkey_characters]:10"
            #     , "ASAP[ay_sap]"
            #     , "HIPAA_policies[h_i_p_a_a_policies|hippa_policies|hi_pa_policies]:10"
            #     , "UNICEF[uni_sef]"
            #     , "CAPTCHA[cap_cha|cap_tsha]:10"
            #     , "Valuelabs_LLP[value_labs_l_l_p]:10"
            #     , "MetLife_Inc[metlife_ing]:10"
            #     , "in_general"
            #     , "need_details"
            #     , "called_id"
            #     , "eleven[leven|leben]"
            #     , "AT&T[a_t_an_t]"
            #     , "zero_to_hundred"
            #     , "miles_per_hour[miles_per_r]:10"
            #     , "Kore_dot_ai[core_dot_a_i|core_dot_ai]"
            #     , "temperature[tebrature]"
            # ]
        }
      #,"formatters" : [{"type" : "digits"}]
    }
}

### ALL SETTINGS ARE ABOVE

all_results_file = all_results_file.format(time.strftime("%Y-%m-%d_%H-%M-%S"))

list_of_files = []

for root, dirs, files in os.walk(inputFolder):
	for file in files:
		list_of_files.append(os.path.join(root,file))

print("files to test")
for name in list_of_files:
    print(name)

# global
collected_results = []
current_results = {}





def web_api_request(headers, body):
  init_response_raw = requests.post("https://{}/v1/asr/transcribe/async".format(hostPort), json=body, headers=headers)
  try:
    init_response = init_response_raw.json()
    if(init_response.get("sessions") is None):
      print("did not obtain session")
      print(init_response_raw.status_code)
      print(init_response_raw.text)
      exit()
  except:
    print("request failed")
    print(init_response_raw.status_code)
    print(init_response_raw.text)
    exit()

  result = {}
  # retrieve values from response
  # sessionId and capturedAudio are printed for debugging purposes
  result["session_id"] = init_response["sessions"][0]["sessionId"]
  result["poll_url"] = init_response["sessions"][0]["poll"]["url"]
  result["audio_ws_url"] = init_response["audio"]["stream"]["websocketUrl"]
  result["capturedAudio"] = init_response["audio"].get("capturedAudio")

  print("        sessionId: {}".format(result["session_id"]))
  print("  Audio Websocket: {}".format(result["audio_ws_url"]))
  if( not(result.get("capturedAudio") is None)):
    print("captured audio id: {}".format(result["capturedAudio"]))
  print(" Results poll url: {}".format(result["poll_url"]), flush=True)

  return result


# function to read audio from file and convert it to ulaw and send to websocket
async def stream_audio(file_name, audio_ws_url):
  print("START stream_audio", flush=True)
  conv_fname = (file_name+'.ulaw').replace(inputFolder, "./")
  ff = FFmpeg(
      inputs={file_name: []},
      outputs= {conv_fname : ['-ar', ''+str(sampleRate), '-f', ffmpegFormat, '-y', '-map_channel', '0.0.0']} if(channels ==1) else {conv_fname : ['-ar', ''+str(sampleRate), '-f', ffmpegFormat, '-y']}
  )
  ff.cmd
  ff.run()
  print("\nstreaming "+conv_fname+" to "+audio_ws_url, flush=True)
  with open(conv_fname, "rb") as f:
    async with websockets.connect(audio_ws_url, 
      # we need to lower the buffer size - otherwise the sender will buffer for too long
      write_limit=1024, 
      # compression needs to be disabled otherwise will buffer for too long
      compression=None) as websocket:
      try:
        print(str(datetime.datetime.now())+" sender connected", flush=True)
        n_buf = 1 * 1024
        byte_buf = f.read(n_buf)
        start = time.time()
        epoch_start_audio_stream = start
        elapsed_time_fl = 0
        count = 0
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

          expected_time_fl = count / (channels * sampleRate * bytesPerSample)
          time_to_wait = expected_time_fl - elapsed_time_fl
          if time_to_wait >= 0: 
            time.sleep(time_to_wait) # to simulate real time streaming
          byte_buf = f.read(n_buf)
        elapsed_time_fl = (time.time() - start)
        print(str(datetime.datetime.now())+" done streaming audio in "+str(elapsed_time_fl), flush=True)
        #print("Waiting 5 seconds for processing to finish...", flush=True)  
        #time.sleep(5.0)
        #print("done waiting", flush=True)  

        await websocket.close()
      except Exception as e:
        print("Exception when sending audio via websocket: "+str(e)) # usually because the session closed due to NOMATCH or NOINPUT

  print(str(datetime.datetime.now())+" done streaming audio", flush=True)

# thread that Polls for the results
# we do it in a separate thread because in the main thread we are streaming the audio
class wsThread (threading.Thread):
   def __init__(self, sid, poll_uri, fname):
      threading.Thread.__init__(self)
      self.sid = sid
      self.poll_uri =poll_uri
      self.fname = fname
   def run(self):
      print ("Starting receiver "+str(datetime.datetime.now()), flush=True)
      try:
        asyncio.new_event_loop().run_until_complete(poll_results(self.sid, self.poll_uri, self.fname))  
      except Exception as e: 
        print(e)
      print ("Exiting "+str(datetime.datetime.now()), flush=True)



def poll(index, session_id, polling_url):
  #print("poll {} {}".format(index, polling_url), flush=True)
  is_final = False
  poll_response = None
  try:
    poll_response = requests.get(polling_url, headers=headers).json()
    phase = poll_response["progress"]["phase"]
    has_result = poll_response.get("result") is not None
    if(has_result):
      is_final = poll_response["result"]["final"]
      incrementalTranscript = poll_response["result"].get('incrementalTranscript')
      if(incrementalTranscript is not None):
        print("debug incremental transcript: {} ".format(str(incrementalTranscript)), flush=True)
        trFinal = incrementalTranscript.get("final")
        trHypo = incrementalTranscript.get("hypothesis")

        trFinalPlusHypo = None

        if(trFinal is not None and trHypo is not None):
          trFinalPlusHypo = trFinal + " :: (" + trHypo + ")"
        elif trFinal is not None:
          trFinalPlusHypo = trFinal
        elif trHypo is not None:
          trFinalPlusHypo = "("+trHypo+")"
        else:
          trFinalPlusHypo = None

        if(trFinalPlusHypo is not None):
          print("increment transcript: {} ".format(trFinalPlusHypo), flush=True)
          current_results["incremental"].append(trFinalPlusHypo)
    if save_all_json_results:
      # write poll_response to JSON
      poll_response_path = os.path.join(output_path, "{}-{}.json".format(session_id, index))
      with open(poll_response_path, 'w') as outfile:
          json.dump(poll_response, outfile)
      #print("Phase: {} Final: {} -> Save result to {}".format(phase, is_final, poll_response_path), flush=True)
  except Exception as e: 
    print("Exception: "+str(e))
    print(str(poll_response))
  return is_final

def poll_full(index, session_id, polling_url):
  poll_response = requests.get(polling_url+"?full=true", headers=headers).json()
  transcript = poll_response["result"].get('transcript')
  if(transcript is None):
    print("full transcript: {} ".format("NONE"), flush=True)
  else:
    print("full transcript: {} ".format(transcript), flush=True)
    current_results["full"] = transcript

  if save_all_json_results:
    # write poll_response to JSON
    poll_response_path = os.path.join(output_path, "{}-{}.json".format(session_id, index))
    with open(poll_response_path, 'w') as outfile:
        json.dump(poll_response, outfile)
    print("Save final result to {}".format(poll_response_path), flush=True)

# function that polls the results
async def poll_results(sid, uri, fname):
  print(str(datetime.datetime.now())+" start  of polling "+uri, flush=True)
  index = 0
  try:
    while True:
      time.sleep(pollingInterval)
      is_final = poll(index, sid, uri)

      index += 1
      if is_final:
          break  
    poll_full(index, sid, uri)
  except Exception as e: 
    print(e)

  print ("Exiting poll_results "+str(datetime.datetime.now()), flush=True)
  

def process_audio(file_name):
  print("START processing: "+file_name)
  global current_results
  current_results = {}
  current_results["audio"] = file_name
  current_results["incremental"] = []
  current_results["final"] = "NONE"
  web_res = web_api_request(headers, body)

  # create and start the websocket thread
  threadWs = wsThread(web_res["session_id"], web_res["poll_url"], file_name)
  threadWs.start()

  # stream audio
  asyncio.get_event_loop().run_until_complete( stream_audio(file_name, web_res["audio_ws_url"]) )

  # wait for websocket thread to join 
  threadWs.join()
  collected_results.append(current_results)
  print("END processing: "+file_name)

if save_all_json_results:
  if not os.path.exists(output_path):
      os.mkdir(output_path)

for aFile in list_of_files:
  process_audio(aFile)

print("RESULTS")
results_path = os.path.join(output_path, all_results_file)
with open(results_path, 'w') as outfile:
  for result in collected_results:
    print("AUDIO: "+result["audio"])
    outfile.write("AUDIO: "+result["audio"]+"\n")
    print("\tincremental:")
    outfile.write("\tincremental:\n")
    for i in result["incremental"]:
      print("\t\t"+i)
      outfile.write("\t\t"+i+"\n")
    print("\tfull:")
    outfile.write("\tfull:\n")
    print("\t\t"+result["full"])
    outfile.write("\t\t"+result["full"]+"\n")

