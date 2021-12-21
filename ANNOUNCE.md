### Support for ACH Payments

ACH payments are now available.

### Maintenance release 1.47.1 is scheduled for 12/21/2021 between 6:00pm and 10pm CST

This release fixes the following issues:
* #rcj-434: web-api throws LowAccountBalanceException in an **Edge** environment with a port-based license
* #rcj-433: endTimeOfCurrentBillingPeriod is found in some Developer-only accounts in prod and dev environments
* #rcj-432: NoHttpResponseException: some callbacks failing - old http library
* #rcj-431: ConverterNotFoundException: No converter found capable of converting from type [java.lang.Integer] to type [java.time.Instant]
* #rcj-430: An offline SA session (mono, no diarization) is not showing up in Dev Console
* #rcj-428: ACH payments not working

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



---
**You can vew all release notes [here](https://github.com/voicegain/platform/releases)** 



































 













































