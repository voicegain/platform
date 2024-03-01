# Websocket Type Telephony Bot API #

HOW TO RUN A BOT:

1) Install the python packages, make sure that you have downloaded the requirements.txt file. Run the below command to install the relevant packages.
pip install -r requirements.txt

 like :flask, asyncio, time, websockets, threading etc.

2) Run the python script that starts a flask server on port 80. 
Run: python <script-name>.py

3) You can have a service like ngrok to a web url that create a tunnel and provides a weburl that redirects APIs the locally running server.
Run the ngrok server by the command: ngrok http 80

4) You can add the weburl provided by ngrok in the telephony bot, as the Inbound speech callback url. Make sure the connect method is set to websocket which is the POST API endpoint.

5) You can now call the bot and it should work.



NOTE:

The above steps is an easy way to test the bot script. Ideally you have to create a server and host it, that way the POST which invokes the bot session will be available on web.
