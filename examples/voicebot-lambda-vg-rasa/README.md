# Lambda Function Voicebot using Voicegain and RASA #

This folder contains code for a simple Voicebot built using:
* Voicegain Telephone Bot API
* AWS Lambda
* RASA

Included files - only one is needed:
* voicegainIvrOne.js - AWS Lambda function code (node.js version)
* voicegainIvrOne.py - AWS Lambda function code (python version)

## Sequence diagram
NOTE: AIVR is the Voicegain internal name for the Service on top of which the Telephone Bot API runs.
The diagram is very simple, but that was the point of the design behind the Telephone Bot API - to make implementing voice bots very easy.  
</br>

![Sequence Diagram](./sequence-diagram.png)

## License ##

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
