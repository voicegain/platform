# Microphone capture sample code - node.js version #

What this code demonstrates:
* microphone capture in a browser
* sending captured audio over one websocket
* receiving transcribed audio over another websocket

## Prerequisites
* Account with Voicegain: https://console.voicegain.ai/signup
* JWT token for authentication: https://support.voicegain.ai/hc/en-us/articles/360028023691-JWT-Authentication

## Steps to Run ##

1. Install node js - https://nodejs.org/en/download/
1. Set JWT in config.js 
1. Run command "npm install" in project directory to install dependencies
1. To start server, run command "node server.js" while in project directory
1. Open index.html in browser (you can use library http-server also)
