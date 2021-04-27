### Minor release 1.29.0 is scheduled for 4/27/2021 between 6pm and 9pm CST

New features in this release:
* Support for 2-channel audio streaming via RTP. This is intended mainly for telephony applications where 1 channel is e.g. caller and the 2nd channel is e.g. agent.  
An example script that demonstrates this new functionality is on our [github](https://github.com/voicegain/platform/tree/master/examples/RTP-streaming#ffmpeg-2chn-testpy).
* Added support for MRCP Recognition-Timeout parameter.

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
* rcj-222 - Diarization and speaker result in virtual dual channel session displayed on UI is wrong

### German and Spanish language available

Voicegain Speech-to-Text Platform now supports German and Spanish languages in addition to English.
If you would like to enable either of those languages on your account please email us at support@voicegain.ai


 




































 





