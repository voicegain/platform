'''
The MIT License

Copyright (c) Voicegain.

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
'''

"""
Simple Lambda function implementing an Echo bot that follows the RASA interface.
You can use it for testing before integrating with actual RASA bot
"""

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
        if(msg is None or msg == ""):
            response.append({"text" : "Say something."})
        else:
            msgStr = str(msg)+"."
            
            response.append({"text" : "You said."})
            response.append({"text" : msgStr}) # play back the received message
            response.append({"text" : "Say something else."})

    except Exception as e:
        eStr = str(e)
        response.append({"text" : eStr})
        
    return response