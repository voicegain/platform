import asyncio
import websockets
import json
import time

# Clients must connect with an "Authorization: Bearer <key>" header matching this value.
# Set to None to disable authentication and allow all connections.
#SECRET_KEY="12345"
SECRET_KEY=None

# Sequential connection counter
connection_counter = 0

def process_ws_msg(wsMsg, stack, prefix, conn_state):
    conn_state["msgCnt"] += 1
    cid = conn_state["id"]

    try:
        data = json.loads(wsMsg)
        print(f"[conn-{cid}] Raw message: {data}", flush=True)
        utter = data.get('utt')
        if utter is None:
            toDel = data.get('del')
            if toDel is None:
                print(f"[conn-{cid}] EDIT->" + wsMsg, flush=True)
                return
            else:
                if conn_state["channelOfLastWordReceived"] != prefix:
                    stack.clear()
                for i in range(toDel):
                    if len(stack) > 0:
                        stack.pop()
                edits = data.get('edit')
                if edits:
                    for edit in edits:
                        utter = edit.get('utt')
                        stack.append(utter)
                    conn_state["channelOfLastWordReceived"] = prefix
        else:
            if conn_state["channelOfLastWordReceived"] != prefix:
                stack.clear()
            stack.append(utter)
            conn_state["channelOfLastWordReceived"] = prefix
            if len(stack) > 50:
                while len(stack) > 30:
                    stack.pop(0)

        time_difference = time.time() - conn_state["startTime"]
        formatted_time_difference = format(time_difference, '.3f')

        if prefix == "CH1":
            print(f"\033[92m\n\t[conn-{cid}] " + formatted_time_difference + ' ' + prefix + " \t" + ' '.join(stack) + '\033[0m', flush=True)
        else:
            print(f"\033[94m\n\t[conn-{cid}] " + formatted_time_difference + ' ' + prefix + " \t" + ' '.join(stack) + '\033[0m', flush=True)
    except Exception as e:
        print(f"[conn-{cid}] ERROR: " + str(e), flush=True)


async def handle_connection(websocket):
    global connection_counter
    connection_counter += 1
    cid = connection_counter

    print(f"[conn-{cid}] New client connected")
    stack = []
    conn_state = {"id": cid, "msgCnt": 0, "startTime": time.time(), "channelOfLastWordReceived": ""}

    # Access headers from websocket.request
    headers = websocket.request.headers
    for header, value in headers.items():
        print(f"[conn-{cid}] Header: {header}: {value}")

    if SECRET_KEY is not None:
        valid = False
        for header, value in headers.items():
            if header == "authorization":
                if SECRET_KEY in value.split():
                    print(f"[conn-{cid}] Authentication success")
                    valid = True
                else:
                    print(f"[conn-{cid}] Authentication failed")

        if not valid:
            await websocket.send("Authentication failed: Invalid token")
            await websocket.close()
            return
    else:
        print(f"[conn-{cid}] Authentication disabled (SECRET_KEY is None)")

    # Retrieve the path directly from the websocket object

    prefix = None
    async for message in websocket:
        try:
            message_data = json.loads(message)
            print(f"[conn-{cid}] Received JSON message: {message_data}")

            if "metadata" in message_data:
                for item in message_data["metadata"]:
                    if item.get("name") == "CALLER1":
                        prefix = item.get("value")
                        print(f"[conn-{cid}] LEFT value: {prefix}")
                    elif item.get("name") == "CALLER2":
                        prefix = item.get("value")
                        print(f"[conn-{cid}] RIGHT value: {prefix}")

            process_ws_msg(message, stack, prefix, conn_state)

        except json.JSONDecodeError:
            print(f"[conn-{cid}] Received non-JSON message: {message}")


async def main():
    start_server = websockets.serve(
        handle_connection,
        "0.0.0.0",
        8765
    )
    async with start_server:
        print("WebSocket server started on ws://0.0.0.0:8765")
        await asyncio.Future()  # Run forever


if __name__ == "__main__":
    asyncio.run(main())
