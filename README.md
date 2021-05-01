# About Voicegain Platform

Voicegain provides a Speech-to-Text Platform built around a Deep Neural Network ASR engine.
Voicegain Speech-to-Text supports:
* open vocabulary speech transcription (real-time and off-line) and 
* speech recognition (using context-free grammars).
Both are accessible via Web API. In addition, the recognizer is available with MRCP interface.

Apart from bare-bones speech recognition we provide other APIs that build on top of that:
* Telephone Bot API - it is a callback api suitable to building IVRs and Voicebots
* Speech Analytics API

Voicegain Platform is accessible in the Cloud and can also be deployed at the [Edge](https://www.voicegain.ai/post/benefits-of-edge-deployment) (on-prem Edge Computing).

# What is available in this Github repository 

## Public information
This repository tracks public components of the Voicegain Platform. Things like:
* [announcements](https://github.com/voicegain/platform/blob/master/ANNOUNCE.md),
* [release notes](https://github.com/voicegain/platform/blob/master/RELEASE.md),
* [terms of service](https://github.com/voicegain/platform/blob/master/TERMS-OF-SERVICE.md),
* [privacy policy](https://github.com/voicegain/platform/blob/master/PRIVACY.md), etc.

## Source code
Repository also provides a lot of useful code:
* [example code](https://github.com/voicegain/platform/tree/master/examples) - we have examples of:
  * [RTP streaming](https://github.com/voicegain/platform/tree/master/examples/RTP-streaming) for real-time transcription or recognition
  * [simple python scripts illustrating use of various APIs](https://github.com/voicegain/platform/tree/master/examples/api-use-cases--python)
  * sample node.js web applications illustrating:
    * [use of grammars for commands](https://github.com/voicegain/platform/tree/master/examples/command-grammar-web-app) 
    * [real-time transcription from microphone](https://github.com/voicegain/platform/tree/master/examples/microphone-websocket-node-js-v2)
    * [offline transcription of uploaded files](https://github.com/voicegain/platform/tree/master/examples/offline-transcription-demo)
  * [scripts illustrating real-time transcription of Twilio Media Stream](https://github.com/voicegain/platform/tree/master/examples/twilio-media-streams)
  * [AWS lambda script for a Voicebot](https://github.com/voicegain/platform/tree/master/examples/voicebot-lambda-vg-rasa) - this uses RASA and Voicegain Telephone Bot API - both node.js and python versions are available
  *  [AWS lambda script for a Voicebot using Twilio](https://github.com/voicegain/platform/tree/master/examples/voicebot-lambda-twilio-vg-rasa) - this is similar to the bot above but uses normal Voicegain Speech-to-Text API together with Twilio Streams - it is quite a bit more complex
  *  [websocket streaming example in Java](https://github.com/voicegain/platform/tree/master/examples/websocket-streaming) - it send audio over websocket and receives real-time transcript result over websocket
* [declarative ivr](https://github.com/voicegain/platform/tree/master/declarative-ivr) - Declarative IVR is a way to specify a complete IVR flow using a simple yaml file. The yaml file gets interpreted by a Lambda fuction and uses Voicegain Telephone Bot API to hear and talk over the phone. Included is a yam file for a simple outbound survey IVR application.
* utilities:
  * [test-transcribe.py](https://github.com/voicegain/platform/tree/master/utility-scripts/test-transcribe) - takes audio files from a directory and runs it through Voicegain and Google speech-to-text - if reference transcripts are available it will report WER for both 
* [audio-sender bootstrap bundle](https://github.com/voicegain/platform/tree/master/audio-sender/bootstrap-bundle) - this is for [Live Transcription](https://support.voicegain.ai/hc/en-us/articles/360050677791-Live-Transcription-Overview). 
Normally you would download it via the [Web Console](https://console.voicegain.ai). Here is [Zendesk help article](https://support.voicegain.ai/hc/en-us/articles/360041262731-Deploying-and-using-Audio-Sender-Daemon) which describes the whole process.

## How-To Guides
* [Deploy Voicegain into AWS](./how-to/deploy-voicegain-into-aws.md)

---

You can learn more about Voicegain at https://voicegain.ai. BTW, we are offering a generous free tier that renews each month so [Signup Now](https://www.voicegain.ai/trial).

[Voicegain Github Home](https://voicegain.github.io/)
