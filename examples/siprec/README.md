# Examples Illustrating Interfacing with SIPREC

## Real-Time Speech Analytics

You will need:
* Create a Context using Web Console
  * Specify the Speech Analytics Configuration in that Context
  * Set that SA Config as the default in Settings ->  Speech Recognition
* Generate a JWT
  * put it in `stomp-triggered-rtsa-receiver.py` file
  * give it to whoever has access to the SIPREC receiver so that it can be plugged into the notifier
* If you change the topic name in `stomp-triggered-rtsa-receiver.py` then provide it to whoever has access to the SIPREC receiver so that it can be plugged into the notifier

After these steps you can launch `stomp-triggered-rtsa-receiver.py`, make a call and observe the Transcript and SA results in the terminal printed by the python script. 