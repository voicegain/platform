# Lambda Function Voicebot using Voicegain and RASA (or other Bot framework) #

This folder contains code for a simple Voicebot built using:
* Voicegain Telephone Bot API
* RASA (this is used in the example but you can modify the code to use other bot framework)
* AWS Lambda (this is the "glue" between Voicegain Telephone Bot API and the Bot)


Included files:
* `voicegainIvrOne.py` - AWS Lambda function code (python version)
  * If you have a bot other than RASA you will need to modify the implementation of `make_bot_request(sender, messageForBot)` function
  * voicegainIvrOne.js - node.js version AWS Lambda function code 
* `lambdaEchoRasa.py` - a simple lambda function that simulates an Echo Bot, you can point `voicegainIvrOne.py` to this function to do so some testing before integration with RASA  

Settings:
* In [Voicegain Web Console](https://console.voicegain.ai) you need to configure your Phone App to use `query` as value for `CSID Callback` - this is what the lambda function expects

## Sequence diagrams

Currently, Voicegain Telephony Bot API can take inbound calls over a normal phone number or over SIP.
It cannot make outbound calls on its own. 

If you need to make outbound calls, you can use a CPaaS like e.g. Twilio to place the outbound call and then SIP INVITE Voicegain into that established call. 

For more info about SIP INVITE see [this blog post](https://www.voicegain.ai/post/sip-invite-voicegain-from-twilio-signalwire-cpaas).   
</br>

Inbound call via CPaaS

![Sequence Diagram (inbound call via CPaaS)](./VG-AWS-RASA-inb.png)

Outbound call via CPaaS

![Sequence Diagram (outbound call via CPaaS)](./VG-AWS-RASA-outb.png)

Direct inbound call via embedded AWS VoiceConnect. (Direct outbound not supported yet.)

![Sequence Diagram (direct inbound call)](./VG-AWS-RASA.png)

## License ##

License applies only to example files in this folder.

The MIT License

Copyright (c) Voicegain.

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
