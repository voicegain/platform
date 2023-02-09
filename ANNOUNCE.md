### Maintenance release 1.77.1 is scheduled for 2/8/2023 between 9pm and 10pm CST

This release includes:
* Back-end update of Redis to 6.2.10 which has a fix to for the issue https://github.com/redis/redis/pull/11590
* More accurate real-time model

### Minor release 1.77.0 is scheduled for 2/3/2023 between noon and 2pm CST

This release adds Zoom Meeting Assistant status display to the Transcribe App.
Due to this change this release will require Zoom Meeting Assistant version 0.3.0 at minimum.

Transcribe App issues addressed:
* #555: Automatically insert underscores into multi-word hints
* #667: Do not hide microphone and browser capture icons for old projects that have no language setting value

Admin tool has been improved in this release:
* Last Login Time and Billing Type columns have bee added.

This release addresses the following issue for the rest of the Voicegain platform:
* #211: nats-websocket fail to send messages to topic subscribers.

### Minor release 1.76.0 is scheduled for 1/24/2023 between 5pm and 8pm CST

This release has the improved Spanish Real-Time model.

Transcribe App issues addressed:
* #406: Add ability to delete a keyword in Speech Analytics settings
* #461: The downloaded audio file is mp3, but the extension is wav
* #532: In languages Project settings show if microphone transcription is not available for given language
* #610: Change the lock-out message to show the local time instead of the UTC.
* #665: Fix weird behavior in Settings if old Project has no Meeting Minutes enabled
* #666: Add a hide button for the Zoom Meeting Assistant banner

### Maintenance release 1.75.2 is scheduled for 1/26/2023 between 5:45pm and 7pm CST

This release includes:
* Fix for Issue #208 which was affecting Signup via the Developer Console
* Improved demo.voicegain.ai app with improved security

### Maintenance release 1.75.1 is scheduled for 1/25/2023 between 2pm and 4pm CST

This release fixes the following Transcribe App issue:
* #204: Occasional Error in Recomputing status

### Minor release 1.75.0 is scheduled for 1243/2023 between 5pm and 8pm CST

This release has the improved Spanish Offline model.

This release adds ability to Recompute meetings in the Transcribe App and in the /asr/meeting API. 
This means that all the NLU processing of the transcript can be redone after, e.g., change in the Project analytics settings.

Other changes to the Transcribe App:
* Info about available Zoom Meeting Assistant is shown on the home page.
* List of search results shows also topics for each transcript.
* Removed Update button on the Key Items settings. Key Items will always be updated to the latest configuration.
* Hid Key Items configuration from non-Admin users.

Transcribe App issues fixed:
* #647: If a user has no signatures and I hover over the playback icon for a signature it shows "Error" tool tip
* #656: When creating a new Project select a color by default - absence of a default selection was a bit confusing.
* #664: Logout is not working - this was only in case if the app ran out of nonces.

Other changes include:
* Improved Admin Tool - better able to handle the thousands of accounts that we have. 
* Fully tested dash-mpeg support. Will be coming soon to the Transcribe App.

This release addresses the following issues for the rest of the Voicegain platform:
* #198: Suboptimal http code returned in case of bad password reset
* #199: asr-api returns 401 for POST /asr/meeting/async, which is unsupported
* #200: Upgrade Redisson version due to a bug
* #201: When GET /sa/config is called we should update the key items to most recent version
* #203: New API method to recompute a meeting: /asr/meeting/{meetingId}/recompute

### Maintenance release 1.74.1 is scheduled for 1/17/2023 between 5:30pm and 7:30pm CST

This release fixes the following issues:
* offline task fails on re-try due to format value type mismatch
* some sessions in ERROR state not removed from session cache as soon as ERROR determined

### Minor release 1.74.0 is scheduled for 1/13/2023 between 11am and 1pm CST

This Release enables User self-signup via email on Transcribe App on Edge.

More options available in the OFFLINE /asr/transcribe API  `settings.fomatters`:
* enhanced - provides formatting for entities like: URL, EMAIL, PHONE, SSN , CC 
* redact - provides redaction for entities like: EMAIL, PHONE, SSN , CC, PERSON, ZIP
* regex - text redaction/modification using regular expression matching

EZUpdate script has been added for updating the Ubuntu packages on the Edge servers.

This release addresses the following issues in the Voicegain platform:
* #182: for sapi.voicegain.ai - limit what is accepted as values of audio.source
* #183: for sapi.voicegain.ai - do not accept the session.portal parameter
* #184: for sapi.voicegain.ai - reduced range for session.poll.persist
* #185: for sapi.voicegain.ai - reduced set of parameters for session.websocket
* #190: GET /public/monitor/asr returns HTTP 406
* #191: GET /account/uuid fails to return submissions and saDemoContext

### Maintenance release 1.73.1 is scheduled for 1/12/2023 between noon and 6pm CST

This is a dummy Release, meant to test the automated release/deployment pipeline changes.


### Minor release 1.73.0 is scheduled for 1/5/2023 between 6pm and 9pm CST

This Release enables Browser Capture in the Transcribe App on Edge.

This release also addresses the following Transcribe App issues:
* #075: Pause is behaving like mute
* #625: Add "No Microphone" option in browser Capture
* #627: (Meeting Minutes) Modifications to the KeyItems settings in Project
* #631: (Meeting Minutes) Support negative examples and regex
* #633: Cancel out of the Mic Save dialog does not work
* #634: (Meeting Minutes) Add Enabled toggle for each Key Item

This release addresses the following issues for the rest of the Voicegain platform:
* #107: Wrong content-type in response from https://console.voicegain.ai/ascalon-web-api/public/monitor/asr
* #139: If account has allowSignupsFromDomain values then allow creation of new users only with valid emails
* #144: Return simple account data from GET /account/{uuid} if no authentication provided
* #156: Make freeswitch-esl-client one of our internal libraries
* #162: Add Cache-Control: no-store to all API GET responses that may change
* #163: Implement POST /asr/meeting/search 
* #166: data-api to avoid including sosRef in the response of GET /data/uuid if its audio file is missing
* #169: Add mpdId to /asr/meeting API
* #170: Additions to formatters in the API
* #172: New `pciDss` field on account
* #173: Option to generate PCI-DSS restricted JWT token
* #174: Spelling error in JWT aud field
* #176: Add negativeExample and negativeRegex to saConfig
* #177: Secure GET /account
* #179: Add `disabled` field to saConfig Phrase
* #186: Add rejection justification for meeting key items
* #188: (Edge) negativeExample value not saved correctly
* Diarization inference reliability has been improved.

### Minor release 1.72.0 is scheduled for 12/15/2022 between 11am and 1pm CST

This release offers improved Key Items feature within the Meeting Minutes in the Transcribe App.

This release also addresses the following Transcribe App issues:
* #593: Subscribe to notifications from back-end and log the incoming messages
* #615: (Edge) make some Profile fields read-only on Edge
* #619: Add a button for applying defaults to KeyItems
* #620: Add a check for validity of regex to the Key Items Example dialog
* #621: Switch from regex to advancedRegex for key items
* #622: Show projects alphabetically sorted

This release addresses the following issues for the rest of the Voicegain platform:
* #145: Add releaseVersionDetail to response from GET /spec
* #146: Add PUT /sa/config/{saConfigId}/defaults
* #147: Return Phrases in SA Config in fixed order
* #148: Validate regex loaded from the built-in Key-Items JSON

### Maintenance release 1.71.1 is scheduled for 12/9/2022 between noon and 2pm CST

This release fixes 3 issues:
* #143: Weird clock values when on Edge and logged in as a user with role User
* #617: (Edge) New created project not visible in the project list
* #618: (Edge) New created project shows files from an older project

With this release we also support a minimal, self-contained, docker-compose deployment of MRCP ASR on GPUs.

### Minor release 1.71.0 is scheduled for 12/8/2022 between 2pm and 6pm CST

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
* Punctuation generation now runs on GPU instead of CPU

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

### Maintenance release 1.68.1 is scheduled for 11/10/2022 between 5:30pm and 8pm CDT

This release supports multiple languages choice in the `/asr/transcribe/async` and `/asr/recognize/async`. It runs recognition using all specified languages and returns the transcript with the highest confidence.

### Minor release 1.68.0 is scheduled for 10/28/2022 between 3pm and 5pm CDT

The key features in this release are:
* Improved diarization in the text areas where one speaker switches to another. 
* More accurate speaker Voice Signature matching.

This release fixes numerous small Web UI issues, mainly usability, in the Transcribe App related to the Voice Signature functionality made first available in the 2 previous releases. 

The installer for the Zoom Meeting Assistant is now signed with Extended Validation Certificate.

This release addresses the following issues for the rest of the Voicegain platform:
* #97: When deleting a Speaker we should remove references to it from Context voiceSignatureSpeakers
* #98: Orphan cleanup delete the audio clip for speaker signature



**Backwards incompatibility:**
* Certain acoustic model names are no longer available. Unless using specific custom models, it is now sufficient to just provide `languages` parameter - no need to specify acoustic model by name.
* requests to `/asr/transcribe/async` API with `portal` field value but no `portal.label` specified will fail - `portal.label` is now a required value 



