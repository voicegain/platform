### Maintenance release 1.37.1 is scheduled for 7/22/2021 between 6:00pm and 10pm CST

This release:
* improves the internal thread Executor setup to make it more resilient
* improves on the alerting service to better notify Voicegain support of production issues

### Minor release 1.37.0 is scheduled for 7/19/2021 between 6pm and 11pm CST

This release improves the Speech Analytics App.
* We added a new type of construct that can be detected in a call. It is called Criteria and allows to conditionally combine NERs, Keywords, Phrases, etc.
* Improvements to Call Review view 

Our STT API now supports Pause and Mute for real-time transcription.

An improved offline Acoustic Model for English language is also part of this release. 

This release addresses the following issues:
* #rcj-308: A mic transcription is terminated after 10 minutes
* #rcj-305: improve handling for invalid values of fetchTimeout

### Maintenance release 1.36.3 is scheduled for 7/9/2021 between 6:00pm and 10pm CST

This release adds various improvements to the Speech Analytics App (beta).

The release also adds the following enhancements to the API:
* max fetchTimeout for getting audio from a URL has been increased from 60 to 90 seconds
* it is now possible to set a diarization speaker range starting at 1
* GET /sa?detailed=false now returns numIncidents, numChannels, and numSpeakers

### Maintenance release 1.36.2 is scheduled for 7/6/2021 between 7:30pm and 10pm CST

This release fixes one issue and adds one enhancement
* #rcj-303: 'missing websocket name' error in audiocodes API 
* #rcj-304: flush RT SA data faster if hypotheses allow it

### Maintenance release 1.36.1 is scheduled for 6/30/2021 between 6:30pm and 11pm CST

This release switches the new account email to AWS SES and it fixes 1 issue:
* #rcj-293: differential word cloud empty on Voicegain

















 













































