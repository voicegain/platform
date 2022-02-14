### Minor release 1.50.0 is scheduled for 2/14/2022 between 4:00pm and 10pm CST

This release addresses the following issues and enhancements:
* #rcj-461: the body of a callback request with callback.format=text is empty
* #rcj-460: better handling of billing system rate-limiting errors
* #rcj-459: new audio selector for call center calls to be processed offline

### Maintenance release 1.49.3 is scheduled for 2/4/2021 between 8:00pm and 10pm CST

This release fixes the following issues:
* #rcj-457: Missing influxDB entries due to identical timestamp
* #rcj-456: Long audio files (e.g. 24 hours) cause OOM
  * Max audio file duration has been limited to 8 hours
* #rcj-455: Offline session time reported to billing as real-time session

### Maintenance release 1.49.2 was deployed on 2/3/2021 between 6:00pm and 6:45pm CST

This release modified how offline transcription billing information is submitted to Billing in order to:
* make it more efficient,
* correct underbilling. 

### Maintenance release 1.49.1 is scheduled for 1/28/2021 between 6:00pm and 10pm CST

This release upgrades the Redis server and clients to a newer version and makes changes to their configuration to prevent certain issues affecting High Availability.

### Minor release 1.49.0 is scheduled for 1/27/2022 between 6:00pm and 10pm CST

This release has numerous back-end changes to improve Voicegain platform ability to handle large loads.

This release fixes the following issues:
* #rcj-448: User logs not available.

### Maintenance release 1.48.4 is scheduled for 1/20/2021 between 6:00pm and 10pm CST

This release adds the following features:
* vadMode "disabled" is now supported - this turns off the VAD and may give higher accuracy where there is constant speech in presence of high volume background noise/hum
* offline processor configuration has been modified to handle more offline requests

This release includes the latest offline model. For info about improved accuracy see update on this [blog post](https://www.voicegain.ai/post/speech-to-text-accuracy-benchmark-october-2021).

### Maintenance release 1.48.3 is scheduled for 1/20/2021 between 6:00pm and 10pm CST

This release fixes the following issues:
* #rcj-447: New Language Model build not working due to Cloud Function issue/change
* #ocp-768: offline process cannot transcribe mlp and truehd file because of rate limiting bug
   * This applies also to other formats which do not provide audio duration information. In addition to these files not being transcribed, other files were delayed in processing.
* #rcj-445: NullPointerException while processing sync /asr/recognize and /asr/transcribe requests with dataStore as audio

### Maintenance release 1.48.2 is scheduled for 1/18/2021 between 6:00pm and 10pm CST

This release fixes the following issue:
* #rcj-444: Unnecessary check for audio file format

### Maintenance release 1.48.1 is scheduled for 1/13/2021 between 6:00pm and 10pm CST

This release fixes the following issues (which impacted Edge deployments with no Internet connection):
* #rcj-442: Consider empty context model name same as null
* #rcj-441: Web Console goes blank if unable to obtain status info

### Support for ACH Payments

ACH payments are now available.

**Backwards incompatibility:**
* requests to `/asr/transcribe/async` API with `portal` field value but no `portal.label` specified will fail - `portal.label` is now a required value 

---
**You can view all release notes [here](https://github.com/voicegain/platform/releases)** 



































 













































