#!/usr/bin/env python

from flask import Flask, jsonify
from flask import request
import websockets
import datetime
import asyncio
import json
import requests
import threading
import time
from enum import Enum


app = Flask(__name__)


class MessageTypes(Enum):
    PING = "ping",
    NEW_AIVR_SESSION = "new_aivr_session"
    AIVR_EVENT = "aivr_event"
    AIVR_VARS_CHANGED = "aivr_vars_changed"
    WS_WORD = "ws_word"
    WORD_CORRECTION = "word_correction"
    SEGMENT_HYPOTHESIS_OR_RECOGNITION = "segment_hypothesis_or_recognition"
    NOT_FOUND = "not_found"




def get_received_msg_type(received_msg):

   if(received_msg.get("ping") is not None):
      return MessageTypes.PING

   elif(received_msg.get("sid") is not None):
      return MessageTypes.NEW_AIVR_SESSION

   elif(received_msg.get("event") is not None):
      if(received_msg.get("event").get("type") == "input"):
         return MessageTypes.AIVR_EVENT
   
   elif(received_msg.get("vars") is not None):
      return MessageTypes.AIVR_VARS_CHANGED

   elif(received_msg.get("utt") is not None):
      return MessageTypes.WS_WORD
   
   elif(received_msg.get("del") is not None):
      return MessageTypes.WORD_CORRECTION

   elif(received_msg.get("type") is not None):
      return MessageTypes.SEGMENT_HYPOTHESIS_OR_RECOGNITION

   return MessageTypes.NOT_FOUND




# Responses:
new_aivr_session_response = {
      "question": {
      "text": "This is an echo bot. Say Something..."
      }
   }


aivr_response = {
      "prompt": {
      "text": ""
      }
   }


aivr_disconnect_response = {

      "disconnect": {
      "reason": "Successfully received feedback",
      "prompt": {
         "text": "Good Bye!!"
         }
      }
   }



async def respond_to_new_aivr_session(websocket):
   await websocket.send(json.dumps(new_aivr_session_response))



async def respond_to_aivr_event(websocket, received_msg):
   #Echo the same message back
   message = received_msg["event"]["vuiAlternatives"][0]["utterance"]
   aivr_response["prompt"]["text"] = message
   await websocket.send(json.dumps(aivr_response))



async def respond_to_aivr_disconnect_event(websocket):
   await websocket.send(json.dumps(aivr_disconnect_response))



async def run_echo_bot(uri):
    async with websockets.connect(uri, write_limit=128, compression=None) as websocket:
       while(True):
         print("Receiving message...")
         received_msg_str = await websocket.recv()
         received_msg = json.loads(received_msg_str)
         print("Received message: ", received_msg)
         
         msg_type = get_received_msg_type(received_msg)
         
         if(msg_type == MessageTypes.PING):
            continue

         if(msg_type == MessageTypes.NEW_AIVR_SESSION):
            await respond_to_new_aivr_session(websocket)

         if(msg_type == MessageTypes.AIVR_EVENT):
            print("Sending the same message back...")
            await respond_to_aivr_event(websocket, received_msg)
            print("Disconnecting... Goodbye!!")
            await respond_to_aivr_disconnect_event(websocket)


# Function websocket_flow_main, recv and sends the results over websocket
def websocket_flow_main(uri):
   try:
      asyncio.run(run_echo_bot(uri))
   except Exception as e:
      print("Exception caught within websocket_flow_main", e)



@app.route("/", methods=["POST"])
def post():
   global ws_url_final
   print("Post req recieved. ")
   payload = request.json
   print("POST Req!! Payload is: " + str(payload))
   # Create a WebSocket connection
   try:
      # In the first post request, we fetched the wsUrl and began receiving and sending messages.
      ws_url_final = payload["wsUrl"]
      # Start a thread to call websocket_flow_send_main
      thread = threading.Thread(target=websocket_flow_main, args=(payload["wsUrl"],))
      thread.start()
   except Exception as e: 
      print(e)
   data = {"response": "accept"}
   print("POST Req returning")
   return jsonify(data)



@app.route("/", methods=["DELETE"])
def delete():
   print("Del req recieved.")
   seq = request.args.get("seq", type=int)
   print("Del Req!! seq is: " + str(seq))
   # Create a WebSocket connection
   print("Exiting DELETE Req"+str(datetime.datetime.now()))
   data = {"termination": "normal"}
   return jsonify(data)



@app.route("/", methods=["GET"])
def get():
   return "GET req recieved."


@app.route("/run")
def run():
   return "Run, Shivam VG.AI!"

if __name__ == "__main__":
   app.run(port=80)



"""
For ascalon bot:

33f3421e-b476-4783-b6db-cb0d116c3b7f@fs.ascalon.ai:5080;transport=tcp

"""