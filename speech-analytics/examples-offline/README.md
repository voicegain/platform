Example scripts showing use of **/sa/offline** API

How to set up the config.ini file:
1. Choose what "CONFIG" to use (CLOUD-PROD for voicegain, DEV for ascalon)
2. Paste in your JWT token into the "JWT" variable of the "CONFIG" you are using. It can be found by going to console.voicegain.ai (or console.ascalon.ai), then to "API Security and clicking "+ GENERATE NEW SECRET". Note that the JWT token can only be copied until the page is closed or refreshed. After that you will need to refresh the token.
3. Place the audio file you want to use into the same folder as the script you want to run and add its name to "INPUTFILES".
4. Set the "MAX_POLLS" and "SLEEP_TIME".

Explanation of config.ini fields:
* CONFIG - what environment to use for the test: CLOUD-PROD for voicegain or DEV for ascalon.
* INPUTFILE - the name of the audio file you want to use.
* MAX_POLLS - the number of unsuccessful polls after wich the script will go onto the next step.
* SLEEP_TIME - length of the downtime between each polling attempt.
* PROTOCOL - what web protocol to use with the API.
* HOSTPORT - what port to use between ascalon and voicegain API.
* JWT - this is where you paste your corresponding JWT token.
* URLSUFFIC - the suffix at the end of the API url.
The scripts build the API url using PROTOCOL, HOSTPORT and URLSUFFIX.

Currently there are three test scripts:
* for custom SA configurations. For a full documentation on this API, see [THIS_LINK](https://doc1web7b0888269764aux1.ascalon.ai/#tag/sa/operation/saConfigPost)
* for getting SA sessions data. The query parameters include:
    * words, with timing and confidences.
    * audio, original and combined.
    * meta.
    * wordCloud.
    * sumary.
    * keywords.
    * entities.
    * phrases.
* for Querying SA data. This returns bare-bones info about all the sessions that fit the query criteria. For more detailed info, use the GET /sa/offline/{saSessionId} api on each session.
* for modifying already existing SA sessions. This includes:
    * changing the label. Follows the same naming rules as file names. Can contain any unicode character, except for control characters and these: < > : " / \ | ? *. It cannot include dots and spacse at the end or front of the name, so a name like ".file_name " is not allowed but a name like "file. name" is.
    * changing how long the session should persist. This can only be modified after the session is done processing but not after the session has expired.
    * moving the session into a different context. The destination and source context must be of the same type, and the users must have access to both of the contexts.
* for recomputing SA session.
