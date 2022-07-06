### Maintenance release 1.60.3 is scheduled for 7/6/2022 between 4:40pm and 6:00pm CST

This release fixes:
* #rcj-546: DataObjects not being deleted by cleanup task. Fixes the de-referencing issue.

### Maintenance release 1.60.2 is scheduled for 6/30/2022 between 2:00pm and 6:00pm CST

This release includes:
*  Usage data now stores session Tags, so if you request from us, e.g., a monthly usage report then each session in the report will have those tags.

Issues fixed:
* #rcj-545: re-register listener whenever FirestoreException is received in FirestoreWebApiConfigCollectionEventListener -- The problem manifested itself in new JWT tokens not fully working for offline-sessions - the requests were accepted but final result was Error. The cause was Google Firestore client occasionally getting an error event from Firestore upon which no subsequent events would pass through. We implemented a workaround where the listener re-registers in case of error.

### Maintenance release 1.60.1 is scheduled for 6/22/2022 between 4:00pm and 8:00pm CST

This release includes:
* In Transcribe App: 
  * Small speed-up of the transcript loading
  * Tool-tips for prev/next buttons
* In Web Developer Console: 
  * Significantly speeds up loading of long Transcripts and Meetings
  * Private/Shared context functionality has been improved.
  * Removal of the password change reminder from the Edge Web Console - this was to support Edge deployments which are not connected to Internet.

### Minor release 1.60.0 is scheduled for 6/17/2022 between 5:30pm and 8:30pm CST

This release includes:
* Support for `sttSpeechContexts` in **AudioCodes API** - can be used to pass hints to recognition. 
  * Ability to pass additional parameters through `sttGenericData` parameter coming soon 
* Password strength check compliant with latest NIST guidelines.

### Maintenance release 1.59.2 is scheduled for 6/15/2022 between 6:30pm and 8:30pm CST

This release includes:
* Improved NLU for IVR prompt intent detection (contact support@voicegain.ai if you are interested in this feature) 

Issues fixed:
* #rcj-538: NPE in AudioCodes API when websocket closed
* #tsw-3: Default language selection in new Transcribe App project

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


Backwards incompatibility:
* the `reuse` parameter in the /data API will now be ignored - each POST request will create a new Data Object

Fixed issues:
* #ocp-777: When afterlife is 0, offline process does not submit ERROR status to asr-api (no error callback)
* #rcj-484: better error handling for Fusebill
* #rcj-496: audio redaction no longer works for mono audio


**Backwards incompatibility:**
* Certain acoustic model names are no longer available. Unless using specific custom models, it is now sufficient to just provide `languages` parameter - no need to specify acoustic model by name.
* requests to `/asr/transcribe/async` API with `portal` field value but no `portal.label` specified will fail - `portal.label` is now a required value 









































 













































