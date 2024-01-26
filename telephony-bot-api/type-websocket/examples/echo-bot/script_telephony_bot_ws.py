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


app = Flask(__name__)


sequence = 0

resp1 = {
    'sequence': -1,
    'prompt': {
        'text': 'welcome to voicegain echo bot'
    }
}

async def main(uri):
    print("Inside main, connecting to uri: ", uri)
    async with websockets.connect(uri, write_limit=128,
        compression=None) as websocket:
        print("Connected to uri: ", uri)
        while(True):
            print("Waiting to receive msg")
            try:
                global sequence
                received_msg = await websocket.recv()
                print("received msg ", received_msg)
                # we assume all the received messages are JSON
                received = json.loads(received_msg)
                if 'ping' in received:
                    print("ping received - ignore")
                elif 'sid' in received:
                    print("first message received")
                    sequence = received['sequence']
                    print("sequence is ", sequence)
                    if(sequence == 1):
                        resp1["sequence"] = sequence
                        await websocket.send(json.dumps(resp1))
                        print("first prompt is sent")
                    else:
                        print("sequence is not 1 - weird")
                else:
                    ## here we should do the echo question
                    sequence += 1
                    resp1["sequence"] = sequence
                    await websocket.send(json.dumps(resp1))
                    print("Message is sent")
            except Exception as e:
                print("ex in main")
                print(e)
                break



# Function websocket_flow_main, recv and sends the results over websocket
def websocket_flow_main(uri):
    print(f"Inside websocket_flow_main, uri={uri}")
    try:
        asyncio.run(main(uri))
        print("Finish websocket_flow_main . ")
    except Exception as e:
        print("ex in websocket_flow_main")
        print(e)



@app.route('/', methods=["POST"])
def post():
    print("Post req received. ")
    payload = request.json
    print("POST Req!! Payload is: " + str(payload))
    wsUrl = payload["wsUrl"]
    print("POST Req!! wsUrl is: " + str(wsUrl))
    # Create a WebSocket connection
    try:
        # In the first post request, we fetched the wsUrl and began receiving and sending messages.
        # Start a thread to call websocket_flow_send_main
        thread = threading.Thread(target=websocket_flow_main, args=(wsUrl,))
        thread.start()
    except Exception as e: 
        print(e)
    data = {"response": "accept"}
    print(f"POST Req returning {data}")
    return jsonify(data)



@app.route('/', methods=["DELETE"])
def delete():
    print("Del req recieved.")
    seq = request.args.get('seq', type=int)
    print("Del Req!! seq is: " + str(seq))
    # Create a WebSocket connection
    print("Exiting DELETE Req"+str(datetime.datetime.now()))
    data = {"termination": "normal"}
    return jsonify(data)



@app.route('/', methods=["GET"])
def get():
    return "GET req received."



@app.route('/run')
def run():
    return "Run, VG.AI!"

if __name__ == '__main__':
    app.run(port=8084)



"""
For ascalon bot:

33f3421e-b476-4783-b6db-cb0d116c3b7f@fs.ascalon.ai:5080;transport=tcp

"""