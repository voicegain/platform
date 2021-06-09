### Maintenance release 1.32.2 is scheduled for 6/8/2021 between 8pm and 11pm CST

A demo token has been added to control access to Demo Integration in Speech Analytics.

API documentation for Speech Analytics section has been improved.

### Maintenance release 1.32.1 is scheduled for 6/7/2021 between 6pm and 9pm CST

This release updates the SSL certificates and also fixes the following issues:
* issue #vgp-798: show the incidents on the small audio bar same way as they are shown on the detailed view 
* bug #rcj-258: Sometimes incidents count not showing on call analysis page
* bug #rcj-253: PII Redacted entities shown in audio player view

### Minor release 1.32.0 is scheduled for 6/4/2021 between 8pm and 11pm CST

Limited access Beta release of the Speech Analytics App. To learn more email us at info@voicegain.ai 

### Maintenance release 1.31.1 is scheduled for 6/1/2021 between 8pm and 11pm CST

This release fixes the following issues:
* bug #rcj-238: concurrent offline transcription fails due to VAD issue
* bug #rcj-237: submitting very short files for diarization fails with ERROR

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


### German and Spanish language available

Voicegain Speech-to-Text Platform now supports German and Spanish languages in addition to English.
If you would like to enable either of those languages on your account please email us at support@voicegain.ai


 




































 





