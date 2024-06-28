#!/usr/bin/env python

from flask import Flask, jsonify
from flask import request
import json
import requests


app = Flask(__name__)


# Function to generate response for POST request
def get_post_resp(payload):
   sid = payload['sid']
   csid = "csid-" + sid
   data = {
      "csid":csid,
      "sid":sid,
      "sequence":1,
      "prompt": {
      "text":"This is an echo bot.",
      "audioProperties":{"voice":"catherine"}
      }
   }
   return data


# Function to generate response for POST request
def get_put_resp_first(payload, seq):
   sid = payload['sid']
   csid = "csid-" + sid
   resp = {
      "csid":csid,
      "sid":payload['sid'],
      "sequence":seq+1,
      "question":{
         "name":"phone",
         "text":"Say Something...",
         "audioProperties":{"voice":"catherine"}
      }
   }
   return resp


# Function to generate response for PUT request (echo interaction)
def get_put_resp_echo(payload, seq):
   sid = payload['sid']
   csid = "csid-" + sid
   events = payload["events"]
   resp = {}
   # Iterate over events to read input event and echo the utterance
   for event in events:
      event_type =  event["type"]
      if(event_type == "input"):
         utterance = event["vuiAlternatives"][0]["utterance"]
         resp = {
            "csid":csid,
            "sid":payload['sid'],
            "sequence":seq+1,
            "prompt":{
               "text":utterance,
               "audioProperties":{"voice":"catherine"}
            }
         }
         break
   return resp


# Function to generate response for PUT request (disconnect)
def get_put_resp_disconnest(payload, seq):
   sid = payload['sid']
   csid = "csid-" + sid
   resp = {
      "csid":csid,
      "sid":payload['sid'],
      "sequence":seq+1,
      "disconnect": {
         "reason" : "END of CALL",
         "prompt" : {
            "audioProperties": { "voice": "Catherine" },
            "text": "Goodbye, disconnecting"
         }
      }  
   }
   return resp


# POST request route
@app.route("/", methods=["POST"])
def post():
   payload = request.json
   print("POST req recieved!! Payload is: " + str(payload))
   try:      
      data = get_post_resp(payload)
      return jsonify(data)
   except Exception as e: 
      print(e)


# PUT request route
@app.route("/<csid>", methods=["PUT"])
def put(csid):
   print("PUT req recieved. ")
   payload = request.json
   seq = int(request.args.get('seq'))
   print("PUT Req!! Payload is: " + str(payload))
   try:      
      resp = {}

      if(seq==2):
         resp = get_put_resp_first(payload, seq)

      if(seq==3):
         resp = get_put_resp_echo(payload, seq)

      if(seq>3):
         resp = get_put_resp_disconnest(payload, seq)
      
      return jsonify(resp)
   except Exception as e: 
      print(e)



# DELETE request route
@app.route("/<csid>", methods=["DELETE"])
def delete(csid):
   print("Delete req recieved.")
   payload = request.json
   seq = int(request.args.get('seq'))

   data = {
        "csid":csid,
        "sid":payload["sid"],
        "sequence":seq+1,
        "termination":"normal"
      }
   return jsonify(data)



# GET request route
@app.route("/", methods=["GET"])
def get():
   return "GET req recieved."



# Run route
@app.route("/run")
def run():
   return "Run, Shivam VG.AI!"

if __name__ == "__main__":
   app.run(port=80)
