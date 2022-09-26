### Minor release 1.65.0 is scheduled for 9/17/2022 between 1:00pm and 3:00pm CST

This release addresses the following Transcribe App issues:
* #364: Add option to move transcript to a different project
* #466: run GET /data/{data-object-id} before submitting microphone recording for offline - this ensures that mic recording is available
* #505-506: better tooltips regarding Project
* #508: different behavior when user selects project while on Home page
* #509: on all of the Project Settings pages show the Project name the same way we do it on e.g. Transcripts page
* #510-512: (Edge only) add ability to reset a password using Password Recovery Key (PRK)
* #513: Front-end should allow apostrophe in the Project name
* #515: change the "data not found" text to "No transcripts"
* #516: Changes on the Apps Download page

This release addresses the following Developer Web Console issues:
* #74: Add info about Rate Limits on the Account
* #78: Password is encrypted even on HTTP connections (relevant to Edge only) 

This release addresses the following issues for the rest of the Voicegain platform:
* #63: new /speaker API
* #64: small changes to /asr/meeting API to take account new Speaker objects
* #66: add voiceSignatureSpeakers to POST /asr/meeting
* #67: add voiceSignatureSpeakers to context APIs
* #68: Allow DataObject to be associated with an Account

### Minor release 1.64.1 is scheduled for 9/19/2022 between 5:00pm and 7:00pm CST

This release includes an improved model for diarization which will provide better diarization accuracy.

The release also fixes these issues in the ML Services:
* #1: Words that should be stop words appear in the Topic results
* #2: Topic extraction should be case insensitive.

NOTE: Gender estimation feature is not working starting from version 1.64.1. This feature will be restored in future versions.

### Minor release 1.64.0 is scheduled for 9/15/2022 between 1:00pm and 3:00pm CST

This release addresses the following Transcribe App issues:
* #469: Added options for profanity masking and digits formatting
* #488: "My Transcripts" Project has no Creator value set
* #487: Add owner information on Project Settings page
* #489: On the Cloud, for Basic Account, do not show User setting for a Project
* #490: Creator avatars vanish when I do search
* #491 through #498: All these make it easier to identify current Project and create a distinction between a Home page and a Project Transcript List page
* #499: Show non-speaking participants on the Transcript Details page - Requires Zoom Meeting Assistant ver 0.2.11 or higher
* #501: First project for a new user should not be called "My Transcripts" but "{firstname}'s Transcripts"

Zoom Meeting Assistant installer is now digitally signed.

This release addresses the following Developer Web Console issues:
* #76: New Auth Configuration type - support for Twilio encrypted recordings

This release addresses the following issues for the rest of the Voicegain platform:
* #58: New field in authConfig on Context - support for Twilio encrypted recordings
* #59: Add support for authConf in POST and PUT /data/audio (twilio-rec-encrypted type)
* #60: NPE in REAL-TIME transcribe session is no audio has been received at all over websocket

### Minor release 1.63.0 is scheduled for 9/6/2022 between 5:00pm and 7:00pm CST

This release addresses the following Transcribe App issues:
* #382: (re-opened) wrong (previous) audio being played
* #403: reduce spacing in the Keyword dialog
* #404: Tags are not displayed
* #447: add a password view icon to Transcribe App login
* #456: App download page does not show on Chrome on Mac
* #462: in Project settings - if switching the project, the settings do not switch to reflect the selected project
* #468: Increase max file size for upload to 256MB
* #473: change of terminology when removing user from Project
* #476: Lag in switching between audio being played
* #477: Add Role setting to Edit User dialog
* #478: Add to user Profile a toggle that makes the account discoverable
* #480: change header: Latest Activity => Latest activity across all Projects
* #483: Allow someone with role=User to share their own Projects with other users
* #484: handle a case where words are empty
* #485: change wording on the transcript delete form

Note: This release requires Zoom Meeting Assistant version **0.2.3** or higher.

This release addresses the following Developer Web Console issues:
* #72: modify file upload to use JWT in the POST /data/file API
* #72: change refill amounts

This release addresses the following issues for the rest of the Voicegain platform:
* #47: Increase audio file size for upload to 256MB
* #52: New discoverable field on User
* #53: APIs to support for Password Recovery Key
* #54: data-api rejects a request when a context doesn't have any allowedOrigins
* #56: add minRequiredZoomMAVersion to /spec API

### Maintenance release 1.62.1 is scheduled for 8/30/2022 between 4:30pm and 5:00pm CST

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


**Backwards incompatibility:**
* Certain acoustic model names are no longer available. Unless using specific custom models, it is now sufficient to just provide `languages` parameter - no need to specify acoustic model by name.
* requests to `/asr/transcribe/async` API with `portal` field value but no `portal.label` specified will fail - `portal.label` is now a required value 









































 













































