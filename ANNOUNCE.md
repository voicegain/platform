### Minor release 1.20.0 is scheduled for 12/14/2020 between 6pm and 9pm CST.

New features in this release:
* improved Edge related web UI
* improved Transcribe UI
* improvements to API around websockets (performance and resource use)
* fix to ulaw decoding (bug rcj-164)
* admin tool improvements

### Maintenance release 1.19.2 is scheduled for 11/25/2020 between 5:30pm and 7pm CST.

This release fixes the following bug:
* bug #vgp-758: Error when trying to transcribe audio from URL via portal

It also adjusts the CPU and memory settings for a couple of services in order to be able to handle larger loads.

### Maintenance release 1.19.1 is scheduled for 11/23/2020 between 5:30pm and 7pm CST.

This release fixes the following bug:
* bug #rcj147: Async transcribe result cannot be viewed in cc-app

### Minor release 1.19.0 is scheduled for 11/20/2020 between 6pm and 9pm CST.

New features in this release:
* Keyword and profanity detection in Transcribe+ page (beta)
* Ability to choose real-time or off-line acoustic models for single-GPU Edge deployments
* Delete function added to Transcribe page
* More accurate real-time acoustic model

#### Bug Fixes 
* bug #779: Audio receiving websocket closed too late


### Maintenance release 1.18.2 is scheduled for 11/11/2020 between 7:15pm and 9pm CST.

This release fixes the following bug:
* bug #768: Problems with accounts with business name containing comma.

and ads the following enhancement:
* enhancement #770: add `builtin:speech/transcribe` as another option to specify transcription in MRCP 

The release also includes a higher accuracy offline Acoustic Model



































