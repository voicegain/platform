# Microphone capture sample code #

What this code demonstrates:
* microphone capture in a browser
* sending captured audio over one websocket
* receiving transcribed audio over another websocket

The files included in this example are:
* `audio-services.js` - a service that captures the microphone audio and a service that sends the captured audio via websocket to Voicegain 
* `config.js` - has the JWT token
* `index.html` - simple web page with Start/Stop buttons and a place for recognition output
* `microphone-capture.js`
  * function that initiates connection to https://api.voicegain.ai/v1/asr/transcribe/async Web API - the response will contain the send websocket url (for audio) and the receive websocket url (for transcription results)   

See comments throughout the code for details.

Before you run the demo:
* Disable same-origin policy in chrome: https://www.thegeekstuff.com/2016/09/disable-same-origin-policy/ </br>
This is needed because we will run the web client on localhost and will be making web api requests to api.voicegain.ai</br>
On Windows, the command may be:</br>
`"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --disable-web-security --user-data-dir="c:/someFolderName"`</br>
If your chrome is not 32-bit but 64-bit then use `"C:\Program Files\.."` without `(x86)`
* Add a valid Voicegain JWT-token in config.js file for authorization

Running the demo:
* launch the `index.html` file

**Notes regarding JWT and security**

In this simple demo, the JWT token is accessible on client side plus we have issues with cross-origin.

In a real application, the request to https://api.voicegain.ai/v1/asr/transcribe/async would be wrapped in a server-side http method that would pass the JWT without exposing it to the web client.

The two websocket requests can be done directly from the web client because the websockets they reference have random one-time-use names. Also websockets can cross domain communication, and they are not limited by the SOP (Same Origin Policy).

**STOMP format for websocket messages**

The example code just dumps the JSON from the STOMP messages coming over the websockets.
This help-desk article describes the format that is used: https://support.voicegain.ai/hc/en-us/articles/360045569592-Websocket-STOMP-payload-for-real-time-transcription-results
