### Minor release 1.45.0 is scheduled for 11/5/2021 between 6:00pm and 10pm CST

This release provides these main changes:
* Introduces a uniform way to handle kubeconfg in Edge deployments. This makes it easy to deploy Voicegain Edge to various Cloud Platforms.
* The latency of the callback response in real-time transcription has been reduced to better support voicebot scenarios.
* Polling now goes via load-balancer URL instead of directly to individual services in order to better support rolling deployments. 

This release fixes the following issues:
* #rcj-368: callback from recognition not working (introduced when adding redis:// callback method)
* #rcj-365: Transcripts of Telephony Bot Session cannot be viewed in Web Console
* #rcj-359: Reduce delay between end of recognition and call-back response 

It also provides these enhancements:
* #vgp-822: naming changes in Edge management ACP pages - uses less ambiguous names in Web Console

### Maintenance release 1.44.1 is scheduled for 10/25/2021 between 6:00pm and 10pm CST

This release provides:
* Further improved accuracy of the real-time/command model.

### Minor release 1.44.0 is scheduled for 10/21/2021 between 6:00pm and 11pm CST

This release provides:
* New versions of the models used for real-time and offline transcription. They provide improved accuracy. This improvement in accuracy is particularly noticeable for short real-time transcripts, like e.g. encountered in voice-bots.
* The hints feature provides new misspellings capability. 
For more info about hints see [this Knowledge Base article](https://support.voicegain.ai/hc/en-us/articles/4407993206548-Using-Hints)

This release fixes the following issues:
* #rcj-358: web-api returns "missing websocket name" by mistake
* #rcj-355: ContentType.word-tree was serialized as WordTree by mistake

### Maintenance release 1.43.6 is scheduled for 10/7/2021 between 6:00pm and 10pm CST

This release fixes the following issue:
* #vgp-821: availableFeatureDetails field not retrieved properly by Edge Web Console

### Maintenance release 1.43.5 is scheduled for 10/4/2021 between 6:00pm and 10pm CST

This release fixes the following issues:
* #rcj-353: completeTimeout not working in SEMI-REAL-TIME mode
* #rcj-351: submitting an offline SA session with stereo audio ended up with mono audio - this bug was introduced in release 1.42.0
* #vgp-820: allow : in hint names - new weight property

### Maintenance release 1.43.4 is scheduled for 9/30/2021 between 6:30pm and 10pm CST

This release fixes the following issues:
* Certain fields not saved on a transcription record due to NPE
* Uploaded LM corpus files incorrectly reported as having wrong format/encoding
* Edge Web Console now showing all Application Modes correctly

### Maintenance release 1.43.3 is scheduled for 9/28/2021 between 8:00pm and 10pm CST

This release fixes issues:
* #rcj-349: Acoustic model setting in context is not used in offline transcribe

For Transcribe App released fixes for the following:
* Issue with navigating away from microphone capture which would break the recording
* Not able to upgrade in a single step from monthly to annual and to a higher Plan
* Computation of remaining days till usage reset
* Minor issues in password entry for a new password
* Several small UI issues 






























 













































