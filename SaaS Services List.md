
# List of Voicegain SaaS Services
Effective: June 20th, 2019

Last Updated: June 18th, 2021

## A. Developer PaaS Services
Developer PaaS Services are accessed through Voicegain Developer Web Console. Voicegain offers the following PaaS Services

## A1. Voicegain Speech-To-Text (STT) APIs:
**Voicegain  Speech to Text (STT) APIs** are RESTful APIs that enable developers to embed both offline and realtime Speech-to-Text into their product, application 
or Service. Developers may invoke these APIs over http, gRPC and WebSockets. Developers may use the STT APIs with our large vocabulary model or 
they can also invoke these APIs with Speech Grammars. 

## A2. Voicegain Telephony Bot APIs: 
**Voicegain Telephony Bot APIs** are JSON based Callback APIs that can be invoked after the Voicegain platform joins a SIP Session as a SIP endpoint. Telephony Bot APIs are a good fit for developers building long lasting speech interactions ober telephony - voice bots, speech IVRs, live agent assist, etc. Clients may bring their own supported SIP trunk provider (BYOC) or may integrate with Voicegain's SIP Trunk provider and carrier infrastructure. Developers may specify the Bot/IVR  logic in a programming language they prefer - Python, Node.JS, PHP.

## A3. Voicegain Speech Analytics APIs:
**Voicegain Speech Analytics APIs** are Voicegain's APIs that convert speech-to-text (transcription)and then analyze the text for sentiment, keywords, phrases, entities and intents. Voicegain offers both realtime and offline Speech Analytics APIs.

## A4. Voicegain MRCP ASR:
**Voicegain MRCP ASR** is a real-time speech recognition service accessed over MRCP (Media Resource Control Protocol) and is built for access by VoiceXML compliant platforms. It supports speech grammars using GRXML & JSGF and provides n-best results. We also provide results from our large vocabulary model for utterances that are either out-of-Grammar(OOG) or have low confidence. 

## B. End-User/Business-User SaaS Apps

## B1. Voicegain Speech Analytics: 
**Voicegain Speech Analytics** is a full featured product for analyzing audio recordings of calls in contact centers, web meetings in sales/enterprise, voicemails 
in UCaaS or more. These recordings get accurately transcribed and analyzed using AI. We inspect both audio and the transcript to extract keywords, sentiment 
and topics. The annotated recordings can accessed using our full featured Web UI that is purpose built for (a) contact centers call coaching and (b) sales managers 
to review performance of inside sales representatives.

## B2. Voicegain Transcribe:
**Voicegain Transcribe** allows end-users to transcribe audio both offline and realtime transcription using the Voicegain Transcribe app. With an intuitive UI, users can easily view and correct the transcript. Our offline transcription can be used for call recordings, voicemails and podcasts and our real-time transcription can be used for meetings, live virtual events, talks, and presentations. Streaming audio is supported using WebSockets and gRPC. Transcripts include timestamps, punctuation and support for custom language models.



