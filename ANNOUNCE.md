## Spanish language Speech-to-Text coming soon!

We plan to release a beta of Spanish language Acoustic Model end of February / early March.
We are now in the process of training on additional data to improve accuracy.

If you are interested in using the Spanish model send us an email at info@voicegain.ai

### Maintenance release 1.23.1 is scheduled for 2/12/2021 between 6pm and 9pm CST.

This release has fixes for the following issues:
* bug #rcj-195: Some short speech audio not being recognized in OFFLINE mode
* bug #rcj-194: RTP streaming in 8-bit format fails intermittently


### Minor release 1.23.0 is scheduled for 1/27/2021 between 6pm and 9pm CST.

New features in this release:
* Support for RTP streaming fully tested and working - includes ulaw and L16 audio formats
* Improved support for simultaneous grammar recognition and large-vocabulary transcription - use of custom language models for large-vocabulary transcription now possible

### Minor release 1.22.0 is scheduled for 1/12/2021 between 6pm and 9pm CST.

New features in this release:
* Recognition API now able to return results using websockets (previously only transcription API was using websockets for results)
* Added support for simultaneous grammar recognition and large-vocabulary transcription.  
* Offline Speech Analytics API released (**beta**)
* Phone calls made to Telephony Bot API now being processed using Speech Analytics in addition to being transcribed
* Improvements in the Language Model feature

Fixes:
* bug #rcj-182: certain short audio files (<1.5s) not being transcribed 
* bug #rcj-180: edits arrive out of order over websocket (issue with ExactTimeCorrectingWordQueue)

### Minor release 1.21.0 is scheduled for 12/18/2020 between 6pm and 9pm CST.

New features in this release:
* Telephone Bot API now supports SIP INVITE
* Transcript table caching in the UI to improve responsiveness
* Improved how asr.sensitivity is used for start-of-speech detection

Fixes:
* bug #rcj-179: Hints generating misrecognitions






































