### Maintenance release 1.15.1 is scheduled for 9/18/2020 between 6pm and 8pm CST.

This release fixes bugs related to clipstore (Prompt Manager) and Twilio Media Stream.

It also adds speaker diarization (beta).


### Minor release 1.15.0 is scheduled for 9/15/2020 between 5pm and 8pm CST.

Features in this release:
* Support for speech recognition on Twilio Media Streams via TwiML `<Connect><Stream>` command
  * [Voicegain Speech-to-Text integrates with Twilio Media Streams](https://www.voicegain.ai/post/announcing-twilio-twiml-connect-stream-support) blog post
  * [How to use Voicegain with Twilio Media Streams](https://www.voicegain.ai/post/how-to-use-voicegain-with-twilio-media-streams) blog post
* Prompt Manager for dynamic concatenation for prerecorded prompts - can be combined with TTS - currently available only from TwiML `<Connect><Stream>`

### Minor release 1.14.0 is scheduled for 8/28/2020 between 5pm and 8pm CST.

Features in this release:
* Significantly reduced time for recognition and transcription session setup.
* JJSGF now supports tags - both semantics/1.0-literals and semantics/1.0 formats.
* Improved accuracy for both offline and real-time acoustic models.

### Maintenance release 1.13.1 is scheduled for 8/21/2020 between 6pm and 8pm CST.

This release fixes the bug with {sessionId} in callback and improves response time in API requests. 
























