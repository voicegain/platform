### Known Issues 

* Issue #572: on Firefox browser microphone capture end signal is not received on server side. The Transcription hangs in "Processing" stage.</br>
There are no issues with microphone capture on Chrome ot latests Edge browsers.

### Minor release 1.10.0 is scheduled for 7/18/2020 between 8am and 10am CST.

Features in this release:
* Added basic JJSGF grammar support (no tags yet)
* Changes to Transcription Mode UI
* Microphone capture has better compatibility with different browsers
* Only a single session is billed if running multiple sessions on same audio input

### Minor release 1.9.0 is scheduled for 7/10/2020 between 5pm and 9pm CST.

Features in this release:
* New API to generate short-lived JWT authentication tokens. 
* Ability to set `allowedOrigins` for web API requests to allow cross-origin web API requests (CORS)
* More responsive TTS
* Real-time Speech-to-Text price is now 1.25 cent/minute

### Maintenance release 1.8.1 is scheduled for 7/2/2020 between 6pm and 9pm CST.
This maintenance release provides fixes for following bugs:
* #534: Transcript Review page stops spinner before the audio file has finished loading
* #530: Last part of incremental word-tree content missing in web api response
* #528: GREG chart tool-tip showing incorrect values











