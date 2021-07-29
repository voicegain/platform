This code demonstrates real-time transcription of audio obtained from a [Telnyx](https://telnyx.com/) bridged call using Telnyx Call Control audio fork command.

# Prerequisites

## from Voicegain

You need account with Voicegain. From the Voicegain Web Console you need to obtain:
* JWT token

# from Telnyx

You need account with Telnyx. From the Telnyx Web Console you need to obtain:
* phone number (will be used to dial the outbound call first leg)
* Telnyx application id - you will need to configure that app to use the bare (w/o any parameters) AWS Lambda fuction url as the webhook url
* Telnyx APIAuthKey

# The files

## launch-telnyx-bridge-recorder.py

Python script that:
* starts Voicegain real-time transcription session, the session  response contains the following parameters that are used:
  * ip and 2 ports for the RTP connection that will be used to receive the audio from Telnyx
  * two websocket urls for receiving transcription for the two audio channels
* launches two threads that connect to the websockets and will print received transcript real-time
* dial first leg of the Telnyx phone connection and passes the url to the AWS Lambda function that will execute Call Control commands
* waits for the phone connection to finish
* waits for the websockets to finish   

## lambda.py

This is the Lambda function that serves as destination for Telnyx callbacks. Lambda function is stateless so we pass parameters in the web request parameters and in the Telnyx `client_state`.

The function is a bit ugly because we tried to keep is as simple as possible. For a real application we suggest handling telnyx web callbacks using a stateful webservice with explicit representation of the call state and state transitions.

The lambda function does the following:
* plays a prompt: "Welcome to our test. Dialing number ..."
* dial the other leg of the call
* bridges the two legs of the call
* starts the audio fork to the specified voicegain ip and 2 ports (`tx` and `rx`)