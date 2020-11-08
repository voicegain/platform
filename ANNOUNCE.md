### Maintenance release 1.18.1 is scheduled for 11/8/2020 between 2pm and 4pm CST.

This release fixes a.o. the following bugs:
* bug #766: Websocket that returns recognition results is incompatible with OkHttp3
* bug #764: Websocket that returns recognition results is incompatible with OkHttp3

The release also improves the look of transcripts on Transcript+ (beta) page

### Known Defect ###

Bug #766: Websocket that returns recognition results is incompatible with OkHttp3  -- this has already been fixed and tested and awaits deployment scheduling.

### Minor release 1.18.0 is scheduled for 10/30/2020 between 6pm and 9pm CST.

Features in this release:
* Transcribe+ page (beta)
* Switching main url from https://portal.voicegain.ai to https://console.voicegain.ai

#### Bug Fixes 
* bug #764: API requests to incorrect URLs sometimes did not return 404
* bug #755: The account without billing permission cannot see transcript result

### Minor release 1.17.0 is rescheduled for 10/14/2020 between 7pm and 9pm CST.

Features in this release:
* Added support for large vocabulary transcription over MRCP
* Websocket that returns transcription results is now configurable to be either: a plain websocket, or a websocket that uses STOMP protocol.

#### Bug Fixes 
* bug #741: Programmable IVR does not wait with start timers till prompt finishes playing to human





























