### Minor release 1.69.0 is scheduled for 11/16/2022 between 4pm and 5pm CST

This release adds two major new features in the Transcribe App:
* Meeting Minutes - an AI generated overview of the meeting including key sections with topics/keywords and key sentences in 4 categories: Actions, issues, Risks, Requirements. Meeting Minutes can be enabled from Project Settings.
* Text search of transcripts - from the Home page find transcripts containing the specified words.

Other Transcribe App issues addressed in this release:
* #530: Fix confusing text in the confirmation dialog for user deletion
* #560: Fixed a scroll issue where the last line of transript was only partially visible.
* #578: Do not allow Phrase example sensitivity values outside the 0-1 range
* #580: Fixed a glitch in multi-column formatting
* #584: Made user email not editable - the User dialog incorrectly was allowing it to be modified
* #585: Added scroll shortcuts to the right pane in the Transcript Detail view
* #588: (Edge only) Added `Sync from Cloud` button which can be used to sync all the user info from Cloud to the Edge.
* #589: (Edge only) Added `Send Test Email` button. This is in preparation of the rollout of the SMTP email support on Edge.

This release addresses the following issues for the rest of the Voicegain platform:
* #104: New setting for transcription and recognition APIs that controls logging of results
* #117: Add localOnly parameter to GET /model/acoustic

### Maintenance release 1.68.1 is scheduled for 11/10/2022 between 5:30pm and 8pm CST

This release supports multiple languages choice in the `/asr/transcribe/async` and `/asr/recognize/async`. It runs recognition using all specified languages and returns the transcript with the highest confidence.

### Minor release 1.68.0 is scheduled for 10/28/2022 between 3pm and 5pm CDT

The key features in this release are:
* Improved diarization in the text areas where one speaker switches to another. 
* More accurate speaker Voice Signature matching.

This release fixes numerous small Web UI issues, mainly usability, in the Transcribe App related to the Voice Signature functionality made first available in the 2 previous releases.

The installer for the Zoom Meeting Assistant is now signed with an Extended Validation Certificate.

This release addresses the following issues for the rest of the Voicegain platform:
* #97: When deleting a Speaker we should remove references to it from Context voiceSignatureSpeakers
* #98: Orphan cleanup delete the audio clip for speaker signature

### Minor release 1.67.0 is scheduled for 10/25/2022 between 10am and 1pm CDT

The release addresses these specific Transcribe App issues:
* #546: Older projects do not generate topics
* #547: Saving a project switches it to a different one
* #550: Assign transcript speaker to a known Speaker (with or without voice signature) - also create new Speaker if needed
* #551: Add page for managing Speakers

The release addresses these specific Speech Analytics App issues:
* #12: Turn off pagination in the Calls page in Speech Analytics App - this is temporary measure before switching to new pagination style
* #14: Upload file should use short-lived JWT

This release addresses the following issues for the rest of the Voicegain platform:
* #81: Enhance logging for AIVR sessions
* #86: When creating a new User let's create a corresponding Speaker entry (for Transcribe App accounts)
* #88: Add support for vsConf and originalName (meeting API)
* #91: Add mustHaveSignature parameter to GET /speakers API

### Maintenance release 1.66.1 is scheduled for 10/21/2022 between 1pm and 2pm CDT

This release includes improved punctuation for the English Offline transcription.

### Minor release 1.66.0 is scheduled for 10/17/2022 between 8:00am and 9:00am CDT

This release provides an improved model for Offline English transcription - you will notice about 1% higher accuracy

The release provides these overall improvements to the Transcribe App:
* Voice Signature support. Users can now create voice signatures and be automatically recognized in transcripts. Next release will add support for creating Voice Signatures for other speakers based on audio.
* Phrase detection in transcript is now suported.
* Topic detection has been improved. Still a beta feature.

The release addresses these specific Transcribe App issues:
* #514: use /auth/login/pre to get the key to encrypt password for login
* #519: tweak space around arrows pointing to other speakers text
* #521: do not show the expiry info if the expiry time is "Never"
* #540: browser capture - same text in both channels
* #542: sometimes getting a blank page when opening transcript (Cannot read properties of undefined (reading 'name'))

The current version of the Zoom Meeting Assistant going with this release is 0.2.17

This release addresses the following issues for the rest of the Voicegain platform:
* #69: Changes to pagination of API results (/calls API)
* #70: add mine and sharedWithMe fields to context
* #71: fail to persist AbstractGrammar.type in MongoDB
* #76: Add new style pagination to GET /asr/meeting
* #77: support PII Redaction in Meeting API
* #78: new auth API: /auth/prk/filename
* #79: add format parameter to GET /sa/calls (to support CSV export)
* #80: MeetingSession.sizeInStorage includes the size of each original audio file by mistake


### Minor release 1.65.0 is scheduled for 9/27/2022 between 1:00pm and 3:00pm CDT

This release addresses the following Transcribe App issues:
* #364: Add option to move transcript to a different project
* #466: run GET /data/{data-object-id} before submitting microphone recording for offline - this ensures that mic recording is available
* #505-506: better tooltips regarding Project
* #508: different behavior when user selects project while on Home page
* #509: on all of the Project Settings pages show the Project name the same way we do it on e.g. Transcripts page
* #510-511: (Edge only) add ability to reset a password using Password Recovery Key (PRK)
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

### Minor release 1.64.1 is scheduled for 9/19/2022 between 5:00pm and 7:00pm CDT

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


**Backwards incompatibility:**
* Certain acoustic model names are no longer available. Unless using specific custom models, it is now sufficient to just provide `languages` parameter - no need to specify acoustic model by name.
* requests to `/asr/transcribe/async` API with `portal` field value but no `portal.label` specified will fail - `portal.label` is now a required value 









































 













































