### Minor release 1.31.0 is scheduled for 5/28/2021 between 6pm and 9pm CST

New features in this release:
* Real-time Speech Analytics API - results are provided real-time via websocket 
* Improved accuracy of the main English language real-time acoustic model
* Second English language real-time acoustic model: optimized for use in IVR - provides improved accuracy on long sequences of digits
* asr.speechContext parameter to provide hint to the recognizer if a lot of digits are expected
* sessions.vadMode parameter to control music rejection - meant to be used mainly for call-center audio to reject music-on-hold
* adjusted behavior of the asr.sensitivity parameter - 0 value now corresponds to -40dbFS

This release fixes the following issues:
* bug #vgp-775: handle transcript results with no spk assigned to words
* bug #rcj-236: gap value present in the json transcript export
* bug #rcj-234: Web Console hangs soon after one opens a mic transcription


### Maintenance release 1.30.1 is scheduled for 5/14/2021 between 6pm and 9pm CST

This release fixes the following issues:
* bug #rcj-228: Noise detected as speech
* bug #rcj-227: Real-time transcription of stereo audio files from Amazon S3 fails  

### Minor release 1.30.0 is scheduled for 5/10/2021 between 6pm and 9pm CST

New features in this release:
* Improved accuracy of the acoustic models - offline and real-time
* Improved accuracy of the recognizer in Voicebot scenarios
* Ability to set default sensitivity settings from Console Web UI
* Returning ERROR instead of NOINPUT if no bytes were received by the recognizer. This makes troubleshooting of RTP streaming easier. 

### German and Spanish language available

Voicegain Speech-to-Text Platform now supports German and Spanish languages in addition to English.
If you would like to enable either of those languages on your account please email us at support@voicegain.ai


 




































 





