# Voicegain Platform

Voicegain provides a Speech-to-Text Platform built around a Deep Neural Network ASR engine.
It supports open vocabulary speech transcription (real-time and off-line) and speech recognition (using context-free grammars).
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
Repostory also provides a lot of useful code:
* [example code](https://github.com/voicegain/platform/tree/master/examples)
* [audio-sender bootstrap bundle](https://github.com/voicegain/platform/tree/master/audio-sender/bootstrap-bundle) - this is for [Live Transcription](https://support.voicegain.ai/hc/en-us/articles/360050677791-Live-Transcription-Overview). 
Normally you would download it via the [Web Console](https://console.voicegain.ai). Here is [Zendesk help article](https://support.voicegain.ai/hc/en-us/articles/360041262731-Deploying-and-using-Audio-Sender-Daemon) which describes the whole process.
* utilities, e.g.
  * [test-transcribe.py](https://github.com/voicegain/platform/tree/master/utility-scripts/test-transcribe)

## How-To Guides
* [Deploy Voicegain into AWS](./how-to/deploy-voicegain-into-aws.md)

---

You can learn more about Voicegain at https://voicegain.ai. BTW, we are offering a generous free tier that renews each month so [Signup Now](https://www.voicegain.ai/trial).

[Voicegain Github Home](https://voicegain.github.io/)
