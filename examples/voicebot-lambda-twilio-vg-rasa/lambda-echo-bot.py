import json

print('Loading function')


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    response = []
    try:
        rawRequest = event['body']
        
        print("Raw request: "+rawRequest)
        
        request = json.loads(rawRequest);
        
        msg = request.get('message')
        msgStr = str(msg)+"."
        
        response.append({"text" : "You said."})
        response.append({"text" : msgStr})
        response.append({"text" : "Say something else."})

    except Exception as e:
        eStr = str(e)
        response.append({"text" : eStr})
        
    return response
