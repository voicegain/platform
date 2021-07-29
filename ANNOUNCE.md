### Minor release 1.38.0 is scheduled for 7/29/2021 between 6pm and 11pm CST

This release adds the following features:
* `authConf` setting for callback authentication
* support for new mechanism to specify configuration of services deployed on Edge
* invoice API added
* changes to user-group API to support attaching groups to Contexts

The release also provides improvements in ML algorithms used for Speech Analytics.

Finally the release fixes the following issues:
* #rcj-315: Missed packet timestamps from dual RTP stream not handled correctly
* #rcj-314: user.role is set to User by mistake

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












 




































 





