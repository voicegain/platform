### Maintenance release 1.59.1 is scheduled for 6/9/2022 between 5:00pm and 8:00pm CST

This release includes:
* Ability to configure external document and object storage for Edge deployment
* Maximum persist time for meeting transcripts on Cloud has been increased from 7 to 31 days (this is in /asr/meeting API)
* Added password view toggle in the Web Console Login
* Multiple upgrades to 3rd-party dependencies to remove known vulnerabilities


### Minor release 1.59.0 is scheduled for 5/31/2022 between 7:00pm and 10:00pm CST

Issues fixed:
* #358: (Transcribe App) Login not working if email is not lower case
* #ocp-780: Topic generation for SA not working

This release also changes the logging library used by our back-end code.

### Maintenance release 1.58.1 is scheduled for 5/24/2022 between 5:00pm and 8:00pm CST

In Transcribe App:
* Ability to set the transcript expiry to "Never expire"
* Improved pop-up preview for transcript in browser-capture mode.

### Minor release 1.58.0 is scheduled for 5/23/2022 between 5:00pm and 8:00pm CST

This release includes:
* Even more accurate offline transcription
* New "rho" model which gives accurate, low latency real-time transcription (meant for API use, enabled using `"acousticModelRealTime" : "VoiceGain-rho"`).
* Custom profanity list feature - please contact us if the default profanity list does not work for your use case.
* Expired-item cleanup code - starting from June invoice you may see charges for storage - previously they were not included because cleanup code was not 100% tested.

Issues fixed:
* #rcj-536: Stop users from logging into a different application from account.type
* #rcj-534: handling unknown speaker it transcript export

### Minor release 1.57.0 is scheduled for 5/12/2022 between 7:00pm and 8:00pm CST

This release includes:
* More accurate offline transcription.
* Improved language selection in Transcribe App.
* Private Contexts in Web Console

Issues fixed:
* #rcj-532: Microphone capture transcript in Transcribe App occasionally does not load (No Data)
* #rcj-527: Text export from Transcribe App does not have modified speaker names
* #rcw-6: (Transcribe app) An exception shows up in the console when Settings is clicked

### Minor release 1.56.0 is scheduled for 4/28/2022 between 4:00pm and 8:00pm CST

This release includes:
* More accurate offline/batch model. Accuracy is improved in particular in lecture/zoom meeting/podcast type of audio.
* Hints in large-vocabulary continuous recognition via MRCP.
* For MRCP customers using large-vocabulary continuous recognition - we now can deliver custom intent recognition using NLU.

Issues fixed:
* Transcribe App
  * #346: Word Cloud is now shown even though the data is there 
  * #347: Named entities (NER) are not highlighted correctly 

### Maintenance release 1.55.1 is scheduled for 4/22/2022 between 11:00am and 3:00pm CST

This release fixes the following issue:
* #ocp-779: offline process returns NOINPUT for audio shorter than 1.25s

### Minor release 1.55.0 is scheduled for 4/19/2022 between 7:00pm and 10:00pm CST

This release includes:
* Web Console now supports Meeting view - for viewing transcripts from /asr/meeting API
* Alpha version of the Zoom Recorder utility is available upon requests - it captures individual audio of each Zoom Meeting participant and submits it for transcription to /asr/meeting API. It works both with Voicegain Cloud and Edge.
* Improvement to internal ml-svc request routing - previously in certain scenarios the requests to ml-svc service might end up going to just a subset of available pods thus reducing performance. 

Issues addressed:
* #rcj-522: GET /asr/transcribe/{uuid}/transcript fails intermittently
* #rcj-520: support replacing acoustic model(s) with languages
  * this is in place to accommodate older pre-1.53.0 style requests which reference names of acoustic models that no longer exists (have been merged into model bundles)
  * new style requests should use `languages` parameter which is sufficient in most cases

### Maintenance release 1.54.1 is scheduled for 4/18/2022 between 11:15am and 2:00pm CST

This release partially addresses the following issue:
* #rcj-517: old/expired data cleanup inefficiency

### Minor release 1.54.0 is scheduled for 4/11/2022 between 4:00pm and 10:00pm CST

This release includes:
* Edge deployment improvements:
  * Support for external S3-compatible object storage
  * Support for SSL Certificates
  * Support for Kubernetes clusters with no GPU
  * Configurable Grafana Dashboard for visualizing API use 
* Other improvements:
  * Beta version of new /asr/meeting API suitable for transcribing per-speaker audio from e.g. a Zoom Meeting 
  * Beta version of encryption for the /data API
  * Faster offline transcribe, including optimized pipeline for audio coming from S3 (or other external URL)
  * Improved English acoustic model (offline mode) - about 1.5% better accuracy on meeting / lecture type of audio
  * Beta version of a German offline acoustic model
  * Language settings in the Web Console improved - only acoustic models compatible with a selected language are shown
  * Added profanity masking option to the Transcribe Dialog

Backwards incompatibility:
* the `reuse` parameter in the /data API will now be ignored - each POST request will create a new Data Object

Fixed issues:
* #ocp-777: When afterlife is 0, offline process does not submit ERROR status to asr-api (no error callback)
* #rcj-484: better error handling for Fusebill
* #rcj-496: audio redaction no longer works for mono audio


**Backwards incompatibility:**
* Certain acoustic model names are no longer available. Unless using specific custom models, it is now sufficient to just provide `languages` parameter - no need to specify acoustic model by name.
* requests to `/asr/transcribe/async` API with `portal` field value but no `portal.label` specified will fail - `portal.label` is now a required value 









































 













































