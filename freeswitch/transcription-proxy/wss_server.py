import asyncio
import websockets
import json
import ssl
import time

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

    try:
        data = json.loads(wsMsg)
        utter = data.get('utt')
        if utter is None:
            toDel = data.get('del')
            if toDel is None:
                print("EDIT->" + wsMsg, flush=True)
                return
            else:
                if channelOfLastWordReceived != prefix:
                    stack.clear()
                for i in range(toDel):
                    if len(stack) > 0:
                        stack.pop()
                edits = data.get('edit')
                if edits:
                    for edit in edits:
                        utter = edit.get('utt')
                        stack.append(utter)
                    channelOfLastWordReceived = prefix
        else:
            if channelOfLastWordReceived != prefix:
                stack.clear()
            stack.append(utter)
            channelOfLastWordReceived = prefix
            if len(stack) > 50:
                while len(stack) > 30:
                    stack.pop(0)

        time_difference = time.time() - startTime
        formatted_time_difference = format(time_difference, '.3f')

        if prefix == "CH1":
            print("\033[92m\n\t" + formatted_time_difference + ' ' + prefix + " \t" + ' '.join(stack) + '\033[0m', flush=True)
        else:
            print("\033[94m\n\t" + formatted_time_difference + ' ' + prefix + " \t" + ' '.join(stack) + '\033[0m', flush=True)
    except Exception as e:
        print("ERROR: " + str(e), flush=True)


async def handle_connection(websocket):
    stack = []
    valid = False

    # Access headers from websocket.request
    headers = websocket.request.headers

    for header, value in headers.items():
        print(f"Header: {header}: {value}")
        if header == "authorization":
            if SECRET_KEY in value.split():
                print("Authentication success")
                valid = True
            else:
                valid = False
                print("Authentication failed")

    if not valid:
        await websocket.send("Authentication failed: Invalid token")
        await websocket.close()
        return

    # Retrieve the path directly from the websocket object

    prefix = None
    async for message in websocket:
        try:
            message_data = json.loads(message)
            print(f"Received JSON message: {message_data}")

            if "metadata" in message_data:
                for item in message_data["metadata"]:
                    if item.get("name") == "CALLER1":
                        prefix = item.get("value")
                        print(f"LEFT value: {prefix}")
                    elif item.get("name") == "CALLER2":
                        prefix = item.get("value")
                        print(f"RIGHT value: {prefix}")

            process_ws_msg(message, stack, prefix)

        except json.JSONDecodeError:
            print(f"Received non-JSON message: {message}")


async def main():
    start_server = websockets.serve(
        handle_connection,
        DOMAIN_NAME,
        8765,
        ssl=ssl_context
    )
    async with start_server:
        print("WebSocket server started")
        await asyncio.Future()  # Run forever


if __name__ == "__main__":
    asyncio.run(main())

