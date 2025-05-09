Example scripts showing use of **/sa/offline** API

How to set up the config.ini file:
1. Choose what "CONFIG" to use (CLOUD-PROD for voicegain, DEV for ascalon)
2. Paste in your JWT token into the "JWT" variable of the "CONFIG" you are using. It can be found by going to console.voicegain.ai (or console.ascalon.ai), then to "API Security and clicking "+ GENERATE NEW SECRET". Note that the JWT token can only be copied until the page is closed or refreshed. After that you will need to refresh the token.
3. Place the audio file you want to use into the same folder as the script you want to run and add its name to "INPUTFILES".
4. Set the "MAX_POLLS" and "SLEEP_TIME".

Currently there are three test scripts:
* for custom SA configurations.
* for polling SA sessions.
* for Querying SA data.