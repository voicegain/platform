# Microphone capture sample code - node.js version - V2 #

What this code demonstrates:
* microphone capture in a browser
* sending captured audio over one websocket
* receiving transcribed audio over another websocket
* processing STOMP messages - in `microphone-capture.js` under `//Handle corrections/deletions of words`
* waiting for the transcription to be finalized
* retrieving complete transcript

## CORS Configuration

The allowed origin must be added in the API Security settings menu under settings on the console to prevent CORS 403 error from occuring.

1. Switch to the Context that you have used to generate JWT
1. Go to API Security settings page under the settings menu in the side bar of the console.
1. In the Allowed Origins settings input, enter the origin on which the index.html page is running on (localhost:8080 etc.)
1. Press save to save the settings.

## Steps to Run ##

1. Install node js - https://nodejs.org/en/download/
1. Set JWT and `aud` origin in server.js 
1. Run command "npm install" in project directory to install dependencies
1. To start server, run command "node server.js" while in project directory
1. Open index.html in browser (you can use library http-server also)

**NOTE:** this example with run on Chrome and latest Edge browsers.
It will not run on Firefox because of inability to set the audio sample rate.
For Firefox you need to read the actual sample rate and pass it in the body of the request to https://api.voicegain.ai/v1/asr/transcribe/async 
