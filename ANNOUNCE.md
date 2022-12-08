### Minor release 1.71.0 is scheduled for 12/7/2022 between 8pm and 11pm CST

This release adds configurability of the Key Items of the Meeting Minutes in the Transcribe App.

This release also addresses the following Transcribe App issues:
* #556: Prepopulate the Name with the file name
* #599: Show project name on transcript detail view
* #602: Show avatar if Speaker is a User
* #605: In Overview view, clicking on the times in the Summary should scroll to relevant Section
* #607: Remove the front-end bolding of keywords in key sentences (done in back-end now more accurately)

This release addresses the following issues for the rest of the Voicegain platform:
* #128: Add justification fields in meetingMinutes
* #129: Support json-mc in GET /asr/transcribe/{sessionId}/transcript
* #130: Speed up GET /asr/meeting
* #131: Add metatada to PUT /asr/meeting
* #132: Prepopulate SA Config with Meeting Minutes phrases
* #133: Meeting Minutes defaults for existing projects
* #136: Change the lock-out duration for user sign-in

Other changes in this release are:
* Updated EZ-Init script
* CallHome License Server

### Maintenance release 1.70.2 is scheduled for 11/23/2022 between 3:30pm and 6pm CST

This release fixes one issue:
* #126: Add project filtering to meeting search for normal Users

### Maintenance release 1.70.1 is scheduled for 11/22/2022 between 4pm and 6pm CST

This release has only two changes:
* Diarization processing has been moved to GPU which is of interest to Edge users because it will reduce the CPU resource requirements.
* In Transcribe App, the default setting of Meeting Minutes on existing Projects has been changed to make it less confusing.

### Minor release 1.70.0 is scheduled for 11/21/2022 between 4pm and 7pm CST

This release addresses the following Transcribe App issues:
* #595: Highlight the topics/keywords in the key sentences in Meeting Minutes
* #596: Add audio playback and transcript text links to the sentences in Overview and Key Items
* #600: In Profile: Separate Account from User settings
* #601: In New Project Wizard set the toggle for Meeting Minutes to enabled by default
* #603: (Edge only) disable Download if transcribeAppSettings has disableDownload:true

This release addresses the following issues for the rest of the Voicegain platform:
* #103: CC number marking in logs
* #111: `sttGenericData` in AudioCodes API now supports maxAlternatives 
* #112: `sttGenericData` in AudioCodes API now supports interpretation 
* #123: Added POST /data/audio/ws method to data API
* #124: Use Content-Type: text/plain; charset=utf-8 for all text/plain responses
* #125: Added transcribeAppSettings to OnPrem Cluster

Moreover the following improvements were done in the ML back-end.
* Punctuation generation now runs on GPU insted of CPU

### Minor release 1.69.0 is scheduled for 11/16/2022 between 4pm and 7pm CST

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


**Backwards incompatibility:**
* Certain acoustic model names are no longer available. Unless using specific custom models, it is now sufficient to just provide `languages` parameter - no need to specify acoustic model by name.
* requests to `/asr/transcribe/async` API with `portal` field value but no `portal.label` specified will fail - `portal.label` is now a required value 









































 













































