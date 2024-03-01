#!/usr/bin/env python

from flask import Flask, jsonify, request
import websockets
import asyncio
import json
import threading
import time
from enum import Enum


app = Flask(__name__)


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


# Define Enum for message types
class MessageTypes(Enum):
    PING = "ping"
    NEW_AIVR_SESSION = "new_aivr_session"
    AIVR_EVENT = "aivr_event"
    AIVR_VARS_CHANGED = "aivr_vars_changed"
    WS_WORD = "ws_word"
    WORD_CORRECTION = "word_correction"
    SEGMENT_HYPOTHESIS_OR_RECOGNITION = "segment_hypothesis_or_recognition"
    NOT_FOUND = "not_found"



# Function to determine the type of received message
def get_received_msg_type(received_msg):

   if received_msg.get("ping") is not None:
     return MessageTypes.PING
   elif received_msg.get("sid") is not None:
     return MessageTypes.NEW_AIVR_SESSION
   elif received_msg.get("event") is not None:
     return MessageTypes.AIVR_EVENT
   elif received_msg.get("vars") is not None:
     return MessageTypes.AIVR_VARS_CHANGED
   elif received_msg.get("utt") is not None:
     return MessageTypes.WS_WORD
   elif received_msg.get("del") is not None:
     return MessageTypes.WORD_CORRECTION
   elif received_msg.get("type") is not None:
     return MessageTypes.SEGMENT_HYPOTHESIS_OR_RECOGNITION
   return MessageTypes.NOT_FOUND


# Function to respond to new AIVR sessions
async def respond_to_new_aivr_session(websocket):
   await websocket.send(json.dumps(new_aivr_session_response))


# Function to respond to AIVR events
async def respond_to_aivr_event(websocket, received_msg):
   #Echo the same message back
   message = received_msg["event"]["vuiAlternatives"][0]["utterance"]
   aivr_response["prompt"]["text"] = message
   await websocket.send(json.dumps(aivr_response))


# Function to respond to AIVR disconnect events
async def respond_to_aivr_disconnect_event(websocket):
   await websocket.send(json.dumps(aivr_disconnect_response))


# Function to run the echo bot
async def run_echo_bot(uri):
    async with websockets.connect(uri, write_limit=128, compression=None) as websocket:
      # Continuously receive messages from the WebSocket
      while(True):
         print("Receiving message...")

         # Receive a message from the WebSocket
         received_msg_str = await websocket.recv()

         # Parse the received message as JSON
         received_msg = json.loads(received_msg_str)

         print("Received message: ", received_msg)
         
         # Determine the type of the received message
         msg_type = get_received_msg_type(received_msg)

         # Check if the received message is a ping
         if(msg_type == MessageTypes.PING):
            continue

         # Check if the received message is a new AIVR session
         if(msg_type == MessageTypes.NEW_AIVR_SESSION):
            # Respond to the new AIVR session
            await respond_to_new_aivr_session(websocket)

         # Check if the received message is an AIVR event
         if(msg_type == MessageTypes.AIVR_EVENT):

            # Check if the AIVR event is of type "input", as we have to respond to only input events.
            if received_msg.get("event").get("type") == "input":
               print("Received an AIVR event of type input, echoing the same message back...")

               # Respond to the AIVR event by echoing the same message back
               await respond_to_aivr_event(websocket, received_msg)

               print("Disconnecting... Goodbye!!")
               await respond_to_aivr_disconnect_event(websocket)


# Function to manage WebSocket flow
def websocket_flow_main(uri):
   try:
      asyncio.run(run_echo_bot(uri))
   except Exception as e:
      print("Exception caught within websocket_flow_main", e)


# Flask app route to handle POST requests.
# This method is called whenever someone calls the telephony bot.
@app.route("/", methods=["POST"])
def post():

   # Print a message indicating a POST request has been received
   print("Post req recieved. ")

   # Retrieve the payload from the request
   payload = request.json

   # Print the payload received in the POST request
   print("POST Req!! Payload is: " + str(payload))

   try:
      # Extract wsUrl from the payload and initiate WebSocket connection
      # Start a new thread to call websocket_flow_main function with wsUrl as argument
      thread = threading.Thread(target=websocket_flow_main, args=(payload["wsUrl"],))
      thread.start()
   except Exception as e: 
      # Print any exception that occurs during WebSocket connection setup
      print(e)

   # Prepare response data to acknowledge the POST request
   data = {"response": "accept"}

   # Print a message indicating successful processing of the POST request
   print("POST Req returning")

   # Return JSON response containing acknowledgment data
   return jsonify(data)


# Flask app route to handle DELETE requests
@app.route("/", methods=["DELETE"])
def delete():
   print("Del req recieved.")
   seq = request.args.get("seq", type=int)
   print("Del Req!! seq is: " + str(seq))
   # Create a WebSocket connection
   print("Exiting DELETE Req"+str(datetime.datetime.now()))
   data = {"termination": "normal"}
   return jsonify(data)


# Flask app route to handle GET requests
@app.route("/", methods=["GET"])
def get():
   return "GET req recieved."


# Flask app route for testing
@app.route("/run")
def run():
   return "Run test flask server..."


# Main function to run the Flask app
if __name__ == "__main__":
   app.run(port=80)



"""
For ascalon bot:

33f3421e-b476-4783-b6db-cb0d116c3b7f@fs.ascalon.ai:5080;transport=tcp

"""