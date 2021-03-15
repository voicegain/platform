# Overview

This folder has sample code that illustrates uses cases for Twilio Streams with Voicegain Speech-to-Text (and soon Voicegain Speech Analytics). 

# `<Start> <Stream>`

With Twilio TwiML `<Start> <Stream>` command you can send inbound, outbound, or both phone channels to Voicegain Real-Time Speech-to-Text API.

`twilio-click2call-transcribe-in-out-chn.py` script does the following:
* Start a Voicegain REAL-TIME transcription session specifying TWIML websocket protocol as input and two websocket channels for output of the transcription results
* Start two threads for connecting to websocket with transcription results. One for Left (inbound) channel and one for Right (outbound) channel
* Start an outbound telephone call using Twilio Client API. We pass the initial TwiML code that contains `<Start> <Stream>` and has some prompts that will be said on the outbound channel.
* Wait for the Twilio call to be completed. During this time the two threads will print the transcription results received from Voicegain.

Below is sample output:
```
$ python launch-twilio-recorder.py
Connecting to: https://api.ascalon.ai/v1/asr/transcribe/async
response code: 200
           SessionId L: 0-0kmatf40e06m2e0fmcgkizs7sswr
           SessionId R: 0-0kmatf40f1tbcgfpy3s41b8465sy
  Audio  Websocket Url: wss://api.ascalon.ai/v1/0/socket/39fe0080-02a1-47ea-afdb-5b3cb81ab41a
     Captured audio id: 92dfb4b5-ddd4-404a-a7e5-34d9746c0155
Result Websocket Url L: wss://api.ascalon.ai/v1/0/plain/0-0kmatf40e06m2e0fmcgkizs7sswr
Result Websocket Url R: wss://api.ascalon.ai/v1/0/plain/0-0kmatf40f1tbcgfpy3s41b8465sy
L >>     Starting WS receive thread 2021-03-15 11:42:49.652391
R << Starting WS receive thread 2021-03-15 11:42:49.653389
Calling Twilio
 <Response>
     <Say voice="woman" language="en-US">connected </Say>
         <Start>
             <Stream name="Test-stream-transcribe-001" url="wss://api.ascalon.ai/v1/0/socket/39fe0080-02a1-47ea-afdb-5b3cb81ab41a" track="both_tracks" />
         </Start>
     <Pause length="1"/>
     <Say voice="woman" language="en-US">start talking, </Say>
     <Pause length="1"/>
     <Say voice="woman" language="en-US">outbound, channel, speaking.</Say>
     <Pause length="1"/>
     <Say voice="woman" language="en-US">outbound, channel, speaking.</Say>
     <Pause length="1"/>
     <Say voice="woman" language="en-US">outbound, channel, speaking.</Say>
     <Pause length="1"/>
     <Say voice="woman" language="en-US">the end </Say>
     <Pause length="1"/>
 </Response>
L >>     connected to wss://api.ascalon.ai/v1/0/plain/0-0kmatf40e06m2e0fmcgkizs7sswr
R << connected to wss://api.ascalon.ai/v1/0/plain/0-0kmatf40f1tbcgfpy3s41b8465sy
Twilio call sid: CAdfdc23ad5503844c9421ed97dba1a3b1
queued msgs rcvd 0
ringing msgs rcvd 0
ringing msgs rcvd 0
ringing msgs rcvd 0
ringing msgs rcvd 0
in-progress msgs rcvd 0
in-progress msgs rcvd 0
        L >>            I
        L >>            I have
        L >>            I have just
        R <<    start
in-progress msgs rcvd 4
in-progress msgs rcvd 4
        R <<    start talking
        L >>            I have just answer
        L >>            I have just answered
        L >>            I have just answered phone
        R <<    start talking out
in-progress msgs rcvd 9
        R <<    start talking out bound
        L >>            I have just answered phone it
        L >>            I have just answered phone it's
        L >>            I have just answered phone it's very
        R <<    start talking out bound channel
        L >>            I have just answered phone it's very interest
        L >>            I have just answered phone it's very interesting
in-progress msgs rcvd 16
in-progress msgs rcvd 16
        R <<    start talking out bound channel speak
        R <<    start talking out bound channel speaking
        L >>            I have just answered phone it's very interesting ye
        L >>            I have just answered phone it's very interesting yeah
        L >>            I have just answered phone it's very interesting yeah ye
        L >>            I have just answered phone it's very interesting yeah yes
        L >>            I have just answered phone it's very interesting yeah yes ye
in-progress msgs rcvd 23
        L >>            I have just answered phone it's very interesting yeah yes yes
        R <<    start talking out bound channel speaking out
        R <<    start talking out bound channel speaking out bound
        R <<    start talking out bound channel speaking outbound channel
in-progress msgs rcvd 27
        R <<    start talking out bound channel speaking out bound channel
        R <<    start talking out bound channel speaking out bound channel speak
completed msgs rcvd 29
Waiting to join Left  2021-03-15 11:43:05.596936
        R <<    start talking out bound channel speaking out bound channel speaking
code = 1000 (OK), no reason
L >>     Exiting WS receive thread 2021-03-15 11:43:06.510008
Joined Left           2021-03-15 11:43:06.511001
Waiting to join Right 2021-03-15 11:43:06.511001
code = 1000 (OK), no reason
R << Exiting WS receive thread 2021-03-15 11:43:06.565890
Joined Right          2021-03-15 11:43:06.565890
```

