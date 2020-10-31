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

### Minor release 1.16.0 is scheduled for 10/9/2020 between 5pm and 8pm CST.

Features in this release:
* Support for transcription on Twilio Media Streams - provides `TwiML <Gather>` like functionality
* Ability to select different audio channel per session
* RTC-API supports large vocabulary transcription
* RTC-API supports prompt playback from external URLs
* RTC-API `input` action supports non-bargeinable intro prompt and bargeinable main question prompt 
* added continuous recognition option

### Maintenance release 1.15.1 is scheduled for 9/18/2020 between 6pm and 8pm CST.

This release fixes bugs related to clipstore (Prompt Manager) and Twilio Media Stream.

It also adds speaker diarization (beta).



























