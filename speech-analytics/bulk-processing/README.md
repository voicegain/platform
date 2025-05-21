This script illustrates creating many /sa/offline sessions from list of audio with call metadata.

How to set up the config.ini file:
1. Choose what "CONFIG" to use (CLOUD-PROD for voicegain, DEV for ascalon)
2. Paste in your JWT token into the "JWT" variable of the "CONFIG" you are using. It can be found by going to console.voicegain.ai (or console.ascalon.ai), then to "API Security and clicking "+ GENERATE NEW SECRET". Note that the JWT token can only be copied until the page is closed or refreshed. After that you will need to refresh the token.
3. Place the csv file to be bulk processed in the same folder as the script and config.ini file. Change the name of "inputFname" to the name of the csv file.
4. Change the name of the "pathBase" to where you will store the audio data.
5. Change the names of "error_log_file", "upload_log_file" and "config_log_file" to whatever you want to name them. Make sure they don't overlap.
6. Choose how long the SA sessions should persist in the database.
7. Choose the acoustic model to use.
8. Choose how many hours of audio to process during and outside of working hours.

Explanation of config.ini fields:
* inputFname - the name of the csv file to process. The file needs to be placed in the same folder as the script.
* pathbase - the path where the audio files will be located.
* MAX_ROWS_TO_PROCESS - number of rows to process before stopping.
* host - what platform to use between https://api.ascalon.ai/v1 or https://api.voicegain.ai/v1.
* JWT - your JWT token. To access it
* error_log_file - if an error occurs during processing, it will be written down here.
* upload_log_file - keeps track of what audio files have been uploaded already.
* config_log_file - keeps track of what SA configurations have been created already.
* persist_days - for how many days should SA sessions persist in the database.
* hours_per_hour_dbh - how many hours of audio data to process during Voicegain business hours.
* hours_per_hour_obh - The same as hours_per_hour_dbh but outside of Voicegain business hours.