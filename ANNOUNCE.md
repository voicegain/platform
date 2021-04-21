### Minor release 1.28.0 is scheduled for 4/21/2021 between 6pm and 9pm CST.

New features in this release:
* real-time diarization - in addition to off-line diarization which has been supported since October 2020, Voicegain transcribe now support real-time diarization
* German language is supported for offline and semi-real-time transcription and recognition 
* Built-in creditcard grammar supports Luhn check for higher accuracy. Also added Diners Card support.

This release fixes the following issues:
* vgp-773 - Incorrect NOMATCH audio zone shown in Transcribe+ for file 4490_pcm_stereo.wav
* vgp-773 - Call Metrics broken in Transcribe+
* vgp-772 - Female label attached to incorrect speaker
* vgp-771 - Left/RIght labels on Transcribe+ (virtual stereo) incorrect
* rcj-225 - Review Answers with autopopulated answer choices are not set to the answerValue of the question
* vgp-770 - Update NER list
* rcj-224 - Comparison method violates its general contract!
* rcj-223 - NullPointerException related to a /asr/transcribe request
* rcj-222 - NullPointerException related to a /asr/transcribe request


### German and Spanish language available

Voicegain Speech-to-Text Platform now supports German and Spanish languages in addition to English.
If you would like to enable either of those languages on your account please email us at support@voicegain.ai

### Maintenance release 1.27.1 has been rescheduled to 3/29/2021 between 6:00pm and 9pm CST.

This release fixes the following issues:
* bug #vgp-769: show informative error message when submitting audio in unsupported/bad format
* bug #rcj-220: recordings of long Telephony Bot API calls not playable
* bug #rcj-219: deleted user account difficult to recover
* bug #rcj-218: gaps in audio being played in Telephony Bot API
* bug #rcj-216: Call transcripts from Call Sessions not being shown sometimes

### Minor release 1.27.0 is scheduled for 3/19/2021 between 6pm and 9pm CST.

New features in this release:
* We are switching the signup process from using 2 emails (one from billing and one for the password set link) to using just a single email - it will contain both the info about the billing account created and the link to set the password. This will make the process simpler and reduce the number of password set emails going to a Spam folder. 

### Minor release 1.26.0 is scheduled for 3/16/2021 between 6pm and 9pm CST.

New features in this release:
* Support for "stereo" audio in TWIML audio streaming protocol. This allows for real-time transcription of calls made to Twilio Platform - inbound and outbound channels are transcribed individually. Audio capture (recording) for this audio format is also supported.

### Maintenance release 1.25.2 is scheduled for 3/12/2021 between 6:30pm and 9pm CST.

This release fixes the following issue:
* bug #rcj-212: Creating new account results in NPE



 













































