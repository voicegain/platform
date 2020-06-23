# Microphone capture sample code #

What this code demonstrates:
* microphone capture in a browser
* sending captured audio over one websocket
* receiving transcribed audio over another websocket

See comments throughout the code for details.

Before you run the demo:
* Disable same-origin policy in chrome: https://www.thegeekstuff.com/2016/09/disable-same-origin-policy/ </br>
This is needed because we will run the web client on localhost and will be making web api requests to api.voicegain.ai</br>
On Windows, the command may be:</br>
`"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" --disable-web-security --user-data-dir="c:/someFolderName`
* Add a valid Voicegain JWT-token in config.js file for authorization

Running the demo:
* launch the `index.html` file

**Notes regarding JWT and security**

In this simple demo the JWT token is accessible on client side plus we have issues with cross-origin.

In real application, the JWT would be hidden on back-end server side and all Voicegain api requests proxied from the same origin as the rest of the application code.