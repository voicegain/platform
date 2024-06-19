import asyncio
import websockets
import json
import datetime
import time
import ssl
import pathlib

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ssl_cert = "/etc/letsencrypt/live/mydomain.com/fullchain.pem"
ssl_key ="/etc/letsencrypt/live/mydomain.com/privkey.pem"
ssl_context.load_cert_chain(ssl_cert, keyfile=ssl_key)

SECRET_KEY="12345"

msgCnt = 0
startTime = 0
channelOfLastWordReceived = ""

def process_ws_msg(wsMsg, stack, prefix):
  global msgCnt, startTime, channelOfLastWordReceived
  msgCnt += 1
  # uncomment this to see raw messages 
  # print(prefix+" "+wsMsg, flush=True)

  try:
    data = json.loads(wsMsg)
    utter = data.get('utt')
    if( utter is None ):
      toDel = data.get('del')
      if( toDel is None):
        # unknown edit
        print("EDIT->"+wsMsg, flush=True)
        return
      else:
        # delete and edits
        if(channelOfLastWordReceived != prefix):
          # new channel
          stack.clear()        
        for i in range(toDel):
          if(len(stack) > 0):
            stack.pop()
        edits = data.get('edit')
        if(not (edits is None)):
          for edit in edits:
            utter = edit.get('utt')
            stack.append(utter)
          channelOfLastWordReceived = prefix
    else:
      # simple utterance
      if(channelOfLastWordReceived != prefix):
        # new channel
        stack.clear()        
      stack.append(utter)
      channelOfLastWordReceived = prefix
      if( len(stack) > 50 ):
        while(len(stack) > 30):
          stack.pop(0)

    time_difference = time.time() - startTime
    formatted_time_difference = format(time_difference, '.3f')

    if prefix == "CH1":
      #'\033[92m'
      print("\033[92m\n\t"+formatted_time_difference+' '+prefix+" \t"+' '.join(stack) + '\033[0m', flush=True)
    else:
      print("\033[94m\n\t"+formatted_time_difference+' '+prefix+" \t"+' '.join(stack) + '\033[0m', flush=True)
  except Exception as e: 
    print("ERROR: "+str(e), flush=True)


async def handle_connection(websocket, path):
    stack = []
    # Access headers
    headers = websocket.request_headers
    for header, value in headers.items():
        print(f"Header: {header}: {value}")
        if header == "authorization":
            if SECRET_KEY in value.split():
                print("Authentication success")
                valid=True
            else:
                valid=False
                print("Authentication failed")
    
    #Header: authorization: Bearer 12345
    if not valid: 
       await websocket.send("Authentication failed: Invalid token")
       await websocket.close()

    # Access path
    print(f"Path: {path}")

    
    prefix =None
    async for message in websocket:
        # Assuming the message is a JSON object
        try:
            message_data = json.loads(message)
            print(f"Received JSON message: {message_data}")

            # Check for metadata in the first message and get the value of "LEFT"
            if "metadata" in message_data:
                for item in message_data["metadata"]:
                    if item.get("name") == "CALLER1":
                        prefix = item.get("value")
                        print(f"LEFT value: {prefix}")
                    elif item.get("name") == "CALLER2":
                        prefix = item.get("value")
                        print(f"RIGHT value: {prefix}")

            # Print the LEFT value in all subsequent messages
            process_ws_msg(message, stack, prefix)

        except json.JSONDecodeError:
            print(f"Received non-JSON message: {message}")

start_server = websockets.serve(
    handle_connection, 
    "mydomain.com", 
    8765, 
    ssl=ssl_context
)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
