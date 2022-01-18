### Maintenance release 1.48.2 is scheduled for 1/18/2021 between 6:00pm and 10pm CST

This release fixes the following issue:
* #rcj-444: Unnecessary check for audio file format

### Maintenance release 1.48.1 is scheduled for 1/13/2021 between 6:00pm and 10pm CST

This release fixes the following issues (which impacted Edge deployments with no Internet connection):
* #rcj-442: Consider empty context model name same as null
* #rcj-441: Web Console goes blank if unable to obtain status info

### Minor release 1.48.0 is scheduled for 1/12/2022 between 6:00pm and 10pm CST

This release adds or changes:
* Punctuation/capitalization and digit formatting for Spanish Transcription is now available.
* Rate limit for Edge offline queue throughput is now expressed per hour rather than per day.
* Modifications were made to allow for transcription on Edge without connection to Internet.

This release fixes the following issues:
* #rcj-439: responses of polling requests don't include word.spk for diarized requests
* #rcj-435: NullPointerException when polling a transcription session

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


---
**You can view all release notes [here](https://github.com/voicegain/platform/releases)** 



































 













































