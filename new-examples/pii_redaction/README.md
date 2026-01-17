## How to run a test

* launch callback receiver: `callback-receiver.py`
  * by default it runs on port 8888 (http://localhost:8888/upload)
  * writes received data to `../data/callback`
* use ngrok to make it visible to our APIs running in the Cloud
* configure the test parameters in config.ini
  * the input audio is obtained from `INPUTURL`
* configure addition settings, like language e.g., in the python script `ol-from-url.py`
* run the python script `ol-from-url.py`
* check results in the output from `callback-receiver.py` and in `../data/callback`

