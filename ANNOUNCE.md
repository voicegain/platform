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

### Minor release 1.20.0 is scheduled for 12/14/2020 between 6pm and 9pm CST.

New features in this release:
* improved Edge related web UI
* improved Transcribe UI
* improvements to API around websockets (performance and resource use)
* fix to ulaw decoding (bug rcj-164)
* admin tool improvements

.





































