# Examples Illustrating Interfacing with SIPREC

## Real-Time Speech Analytics

You will need:
* Create a Context using Web Console
* Generate a JWT in Settings -> API Security
  * put the JWT in `stomp-triggered-rtsa-receiver.py` file
  * give the JWT to whoever has access to the SIPREC receiver so that it can be plugged into the notifier
* Configure Speech Analytics
  * Switch to Speech Analytics Mode (orange 4 square menu)
  * Enter the Speech Analytics Configuration under Transcribe+ -> SA Configuration
    * Alternatively you can create SA Config using the API in the same context (JWT) and give it a name you will recognize
  * Set that SA Config as the default in Settings ->  Speech Recognition: Default SA Configuration  
* If you change the topic name in `stomp-triggered-rtsa-receiver.py` then provide it to whoever has access to the SIPREC receiver so that it can be plugged into the notifier

After these steps you can launch `stomp-triggered-rtsa-receiver.py`, make a call and observe the Transcript and SA results in the terminal printed by the python script. 

You need to restart `stomp-triggered-rtsa-receiver.py` after each call.