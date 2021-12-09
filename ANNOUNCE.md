### Maintenance release 1.46.1 is scheduled for 12/9/2021 between 6:00pm and 10pm CST

This release fixes the following issues:
* #rcj-419: POST /sa sessions failing (stuck in PROCESSING)
* #rcj-418: account login API returns fields incompatible with older Edge versions
* #rcj-417: first callback always fails after idle

### Minor release 1.46.0 is scheduled for 12/3/2021 between 7:00pm and 10pm CST

This release starts to **enforce rate limiting**. 
For details of about rate limiting, including the default values, 
please see this [knowledge base article](https://support.voicegain.ai/hc/en-us/articles/4411882926868-Rate-Limiting).

This release adds:
* ability to disable punctuation and capitalization in the output (rcj-411)
* session specific diarization settings for transcription (rcj-398)
* `longPersist` parameter to POST /data API (rcj-397)
* Second real-time model (faster but less accurate): `VoiceGain-rho-en-us`

This release fixes the following issues:
* rcj-414: Remove archaic words from British English dictionary
* rcj-396: Polling request is slow when there are multiple web-api instances

### Maintenance release 1.45.3 is scheduled for 11/15/2021 between 7:00pm and 10pm CST

This release includes the following changes:
* Results of speech recognition which get assigned the `__garbage__` semantic tag will now be returned as NOMATCH irrespective of the confidence value w.r.t threshold.
* Diarization has been made more memory efficient
* API documentation includes info about rate limiting 

### Maintenance release 1.45.2 is scheduled for 11/12/2021 between 6:00pm and 10pm CST

This release fixes the following issues:
* #rcj-393: New session takes few extra msec to start after a longer pause between request 
* #rcj-379: customer reports that Expired transcripts are still visible (Edge deployment)

### Maintenance release 1.45.1 is scheduled for 11/9/2021 between 6:00pm and 10pm CST

This release fixes the following issues:
* #rcj-386: multiple callback requests are sent for a given request
* #rcj-385: occasionally responses from recognition take extra long (incompleteTimeout) - incompleteTimeout was not behaving as per spec
* #rcj-384: Realtime session takes 1-2s to start - requests to billing were not being cached efficiently
* #rcj-383: Audio from AIVR transcription shows in the Portal under normal Transcribe 

### Minor release 1.45.0 is scheduled for 11/5/2021 between 6:00pm and 10pm CST

This release has these main changes:
* Introduces a uniform way to handle kubeconfg in Edge deployments. This makes it easy to deploy Voicegain Edge to various Cloud Platforms.
* For Edge: moved to a different GPU runtime framework which uses GPU resource more efficiently. Allows to run more recognition sessions on same hardware.
* Optimized offline task queue - significantly higher throughput is now possible (more hours of audio transcribed in the same period of time). 
* The latency of the callback response in real-time transcription has been reduced to better support voicebot scenarios.
* Polling now goes via load-balancer URL instead of directly to individual services in order to better support rolling deployments. 
* Microphone capture in web browser applications moved away from deprecated methods

This release fixes the following issues:
* #rcj-368: callback from recognition not working (introduced when adding redis:// callback method)
* #rcj-365: Transcripts of Telephony Bot Session cannot be viewed in Web Console
* #rcj-359: Reduce delay between end of recognition and call-back response 

Known issue that is not fixed in this release:
* #rcj-380: polling requests fail to return transcript after poll.afterlife -- the workaround is to make sure that content.full includes both ["transcript", "words"]
* #rcj-377: if content.full is only ["transcript"] then the callback will not have the transcript -- it is necessary to specify ["transcript", "words"] to get any transcript in the callback 

It also provides these enhancements:
* #vgp-822: naming changes in Edge management ACP pages - uses less ambiguous names in Web Console

Additional announcements:
* We now offer advanced monitoring for Edge deployments (for a slight per-port price premium).



































 













































