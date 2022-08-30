### Maintenance release 1.62.1 is scheduled for 8/30/2022 between 5:00pm and 7:00pm CST

This release fixes the following issue:
* #rcj-555: fail to copy asr transcription result files to a new context - affects SA App Demos

### Minor release 1.62.0 is scheduled for 8/26/2022 between 1:00pm and 4:00pm CST

This release addresses the following Transcribe App issues:
* #380: only positive (>0) values of speakers should be allowed
* #398: on Zoom download page add info about needed Zoom settings
* #407: add ability to delete a Keyword example
* #424: (Edge) Cannot see the projects I created
* #436: A wrong value is assigned to user.memberOf
* #440: I am an Admin user and in Projects settings I do not see the icon for Users
* #449: Project->Settings->Users page show a "no users in project" page briefly before showing that there are users
* #450: deleted project still visible in the project menu
* #451: American English is highlighted instead of Spanish which is the actual setting on the Context
* #452: (Edge) Not able to save changes to file name
* #453: Show error message as a tooltip over Error
* #454: Cannot select other languages on Cloud Transcribe App
* #457: (Edge) New URL to the Knowledge Base for Transcribe App on Edge
* #459: selection of a column for sorting a table cannot be undone
* #460: sorting by storage size is as if storage size was a string not a number
* #463: back button does not take you back
* #464: on projects settings - move NER to bottom of page
* #467: modify logic for checking validity of Labels
* #469: Allow max number of speakers for diarization to be 12 instead of 10
* #472: (Edge) The latest sessions are not on the home page
* #474: no way to add another user to project

Known issue in Transcribe App:
* Uploading files larger than 128MB may fail in the Web Browser.

This release addresses the following issues for the rest of the Voicegain platform:
* #39: number formatting is not working on meeting transcripts
* #40: Some sessions are on the second column when there is only one speaker
* #41: fail to read formatters from MongoDB
* #42: create a new project if user logs in from=TranscribeApp and there are no private contexts with type=Transcription for that user
* #46: queue size rate-limit being exceeded
* #47: Increase audio file size for upload to 256MB
* #48: increase maxspeakers for diarization to 12
* #49: add nonSpeakingParticipants to /asr/meeting API
* #50: change in allowed format for Labels
* #51: new GET /spec API

### Minor release 1.61.0 is scheduled for 8/17/2022 between 6:30pm and 10:30pm CST

This release includes a major overhaul of the Transcribe App:
* Transcribe App now supports Zoom Meeting Assistant App which can submit all your local Zoom Meeting recordings for transcription to the Transcribe App.
* New Transcript Detail display that no longer requires paging and supports transcript from overlapping speech.
* Transcribe App is now available on Edge - this way you can deploy it to all users in an Enterprise and keep all your confidential data local.

Other minor changes include:
* Decrease playout of the Telephony Bot prompts. Latency of actions following a prompt has been reduced by about 800ms.
* Built-in number grammar has a fix for a minor issue.

This release includes improved offline speech-recognition model with about 1.5% improvement in accuracy.

### Maintenance release 1.60.4 is scheduled for 8/10/2022 between 7:00pm and 9:00pm CST

This release changes 2 things relevant for MRCP users:
1. The content on NLSML returned in MRCP results - We now return `<nomatch/>` element within `<result><interpretation>` in case of `Completion-Cause: 001 no-match`. In the past `<nomatch/>` was not included, instead an NLSML corresponding to a normal recognition was returned even in case of `Completion-Cause: 001 no-match`
1. GRXML grammars with `scope=private` attribute now parse without an error. Note, however, that the private scope is still not enforced. That will be fixed in future releases.

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


**Backwards incompatibility:**
* Certain acoustic model names are no longer available. Unless using specific custom models, it is now sufficient to just provide `languages` parameter - no need to specify acoustic model by name.
* requests to `/asr/transcribe/async` API with `portal` field value but no `portal.label` specified will fail - `portal.label` is now a required value 









































 













































