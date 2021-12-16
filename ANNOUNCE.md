### Minor release 1.47.0 is scheduled for 12/16/2021 between 6:00pm and 10pm CST

This release adds:
* Ability to host more than one model per GPU - this is of importance to Edge users who no longer will have to allocate one GPU per model.
* Improved transcript paragraph splits both in the Web Console and in the downloaded TXT file
* Improved accuracy of the Spanish offline model (the real-time model is still available only upon request)
* Improved backwards compatibility of the Cloud with the Edge deployments - it mainly relates to login behavior (SSO, etc). 
* Improved EZInit script for Edge installs. Two core improvements are:
  * uses a `voicegain` user for deployment - in the past it was using one of existing user accounts on the server
  * has been adapted and tested with Ubuntu Server - although we still recommend using Ubuntu Desktop due to its better GPU support

**Backwards incompatibility:**
* requests to `/asr/transcribe/async` API with `portal` field value but no `portal.label` specified will fail - `portal.label` is now a required value 

This release fixes the following issues:
* #rcj-427: web-api should reject requests with invalid dataobject UUID
* #ocp-767: offline process throughput rate-limit checking error when ffmpeg cannot detect input audio duration

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

---
**You can vew all release notes [here](https://github.com/voicegain/platform/releases)** 





































 













































