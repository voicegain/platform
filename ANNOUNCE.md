### Maintenance release 1.48.4 is scheduled for 1/20/2021 between 6:00pm and 10pm CST

This release add the following feature:
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


### Minor release 1.48.0 is scheduled for 1/12/2022 between 6:00pm and 10pm CST

Known Issue:
* Custom Language Models in the Cloud cannot be generated. This will soon be fixed in 1.48.1 

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

**Backwards incompatibility:**
* requests to `/asr/transcribe/async` API with `portal` field value but no `portal.label` specified will fail - `portal.label` is now a required value 









































 













































