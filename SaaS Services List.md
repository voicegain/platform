
# List of Voicegain SaaS Services
Effective: June 20th, 2019

Last Updated: July 23rd, 2020


## 1. Voicegain Speech-To-Text (STT) APIs:
**Voicegain  Speech to Text (STT) APIs** are RESTful APIs that enable developers to embed both offline and realtime Speech-to-Text into their product, application 
or Service. Developers may invoke these APIs over http, gRPC and WebSockets. Developers may use the STT APIs to our large vocabulary model or 
they can also invoke these APIs with Speech Grammars. One potential advantage of using Speech Grammars is that developers can simultaneously capture 
the utterance and intent and this may work for simple bots/dialogs that can be done without deep NLU expertise.

## 2. Voicegain Realtime Communications (RTC) Callback APIs: 
**Voicegain Realtime Communication (RTC) Callback APIs** allow developers to stream continuous audio to our Speech-to-Text engine directly from a RTC session; 
after which they can interact with it using commands and callbacks. Voicegain supports SIP/RTP and WebRTC. RTC Callback APIs are a good fit for long lasting speech
interactions - voice bots, speech IVRs, live agent assist, live captioning, etc. Clients may bring their own SIP provider (BYOC) or may integrate with Voicegain's
SIP Trunk provider and carrier infrastructure. Developers may write the application logic in a programming language they prefer - Python, Node.JS, PHP.

## 3. Voicegain Speech Analytics: 
**Voicegain Speech Analytics** is a full featured product for analyzing audio recordings of calls in contact centers, web meetings in sales/enterprise, voicemails 
in UCaaS or more. These recordings get accurately transcribed and analyzed using AI. We inspect both audio and the transcript to extract keywords, sentiment 
and topics. The annotated recordings can accessed using our full featured Web UI that is purpose built for (a) contact centers call coaching and (b) sales managers 
to review performance of inside sales representatives.

## 4. Voicegain Transcribe and Captioning:
**Voicegain Transcribe** offers offline transcription at very high accuracy and low cost. The Voiecgain Portal includes a web UI that makes it easy to review and 
correct the transcript. **Voicegain Captioning** is our reatime transcription service for captioining live events, talks, and presentations. Streaming audio is 
supported using WebSockets and gRPC. Transcripts include timestamps, punctuation and support for custom language models.

## 5. Voicegain MRCP ASR:
**Voicegain MRCP ASR** is a realtime speech recognition engine for traditional VoiceXML based IVR applications. It supports speech grammars using GRXML & 
JSGF and provides n-best results. We also provide results from our large vocabulary model for utterances that are out-of-Grammar(OOG) or have
low confidence results. 


