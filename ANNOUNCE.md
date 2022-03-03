### Minor release 1.51.0 is scheduled for 3/3/2022 between 5:00pm and 10pm CST

This release provides the following more accurate models:
* English real-time (streaming)
* Spanish off-line

This release addresses the following issues:
* #rcj-477: AIVR - attempt to play empty questionPrompt results in error
* #rcj-476: AIVR -the last prompt in disconnect is not being played and the hangup is not done
* #rcj-474: REX returns incorrect long result for certain utterances in recent benchmark
* #vgp-833: The startTime field datatype is "String in the spec, but web-api returns integer
* #rcj-472: Get exception when submit silence to SA
* #rcj-470: Cannot GET SA transcript
* #vgp-830: DEL SA session and DEL SA config need to be in the public API spec
* #ocp-773: offline-process occasionally return empty result
* #vgp-831: "name" field should be required when creating SA config
* #rcj-469: attempt to get /sa results returns INTERNAL_SERVER_ERROR
* #ocp-770: diarization is not returned when audio is short

Two enhancements:
* Old and/or orphan data cleanup has been moved to separate task and made faster
* Time filter has been added to the GET /data query method  

### Maintenance release 1.50.1 is scheduled for 2/16/2021 between 11:00am and noon CST

This release fixes the following issue:
* #rcj-463: call duration reported from offline transcription to billing is 1/1000th of what it should be

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


### Support for ACH Payments

ACH payments are now available.

**Backwards incompatibility:**
* requests to `/asr/transcribe/async` API with `portal` field value but no `portal.label` specified will fail - `portal.label` is now a required value 

---
**You can view all release notes [here](https://github.com/voicegain/platform/releases)** 



































 













































