### Maintenance release 1.82.1 is scheduled for 4/25/2023 between 5pm and 7pm CST

This release has the following changes:
* BE-243 Fix for not getting any transcriptions from the Telephony Bot sessions
* BE-244 Fix for erratic recognition in the Telephony Bot

This release also fixes several 3rd-party vulnerabilities.


### Minor release 1.82.0 is scheduled for 4/20/2023 between 2pm and 5pm CST

This release chas the following changes:
* BE-73	Add info about language to Mic Recording and File Upload dialogs
* BE-74	Improved Project Move dialog
* BE-76	Improved Zoom Meeting Assistant download page
* BE-80	Improved/Simplified Browser Capture Preview in Transcribe App
* BE-81	New Project Wizard in Transcribe App upon first login
* BE-109	Fixed: Issue with saving meeting with certain commas in the name
* BE-110	Option to send transcription results back over the audio websocket
* BE-113	EZInit Script disable Leader Election on NFS Provisioner
* BE-114	EZInit updated for Containerd
* BE-115	Upgrade minio to highest backwards-compatible version
* BE-119	Improved the throughput for Kappa model when using web-socket to stream audio
* BE-130	Clarified that only Screen and Browser Tab audio capture works
* BE-133	AccountUsage generation complete in new-billing-utility
* BE-135	New Billing Utility writes to postgresql the same data that would be written to Fusebill
* BE-138	Fixed old portal URL still referenced from within Grafana
* BE-143	Fixed incorrect ERROR tooltip visible for new uploaded Voice Signatures
* BE-146	Fix concurrency issue in mrcp_rex plugin history
* BE-148	The Zoom App download page is now correctly reporting the App version
* BE-150	Disabled Automatic creation of a New Transcribe App project upon first login
* BE-151	every GET data API request decreases rate limit by 1 (instead of 10)
* BE-153	Google Storage bucket creation now works in the QA environment
* BE-154	Remove confusing Logs option from LH menu in Edge mode
* BE-155	In Web Console on EDGE: Remove all Log options from the LH menu
* BE-162	Fix Terms of Service it highlight on the LH menu
* BE-163	Offer First Project Wizard when user logs in and has no Projects
* BE-165	Updated Content-Security-Policies for QA Environment
* BE-170	Usability improvements to App Selector (reduce mouse clicks)
* BE-172	Add ability to turn off the current language reminders in Mic and Upload dialogs
* BE-174	Ensure that returned items from the Extended Summary (topics) are unique
* BE-175	Improve reliability of Browser Capture
* BE-178	Show tooltip with Creator name when hovering over avatar
* BE-182	In Transcribe App: Remove diarization from the Browser Capture preview
* BE-184	Better location for the close-search-box icon
* BE-188	In Web Console: Make email on the Phone Management Page clickable link
* BE-193	Fixed: Unable to go from Apps page direct to Project Transcripts page
* BE-194	Support Statefulset uniMRCP deployment (for Cloud)
* BE-200	Fixed upload of corpus files for Language Model
* BE-202	Fixed uploading an audio file on demo.voicegain.ai 
* BE-207	In Demo App: Allow more audio file types for Upload
* BE-209	Add back button to Pricing Plans page in Transcribe App
* BE-212	In Transcribe App: show creator name tooltip when hovering over creator avatar
* BE-213	Made email in balance details clickable (mailto:)
* BE-214	In Demo App: Remove FFW and REV buttons
* BE-219	In Web Console: Move password reset link to the first step
* BE-227	Added a link to submit a support ticket in Transcribe App
* BE-229	Added new field "complianceType" to Account

### Minor release 1.81.0 is scheduled for 3/20/2023 between 9pm and 10pm CST

This release has the following fixes and improvements in the Transcribe App:

* BE-21	Fix expanded left-hand menu obscuring page content if frozen
* BE-24	In user Profile add a setting to hide language flags on Project icons
* BE-26	New Project design for the Transcribe App (mainly left-hand menu)
* BE-27	Add Search within transcript in the detail view in Transcribe App
* BE-52	Flags on Projects are inconsistent
* BE-59	Back button doesn't work
* BE-63	Transcribe from URL not working in Transcribe App
* BE-64	Upgrade on home page of the Transcribe App takes you to Password Reset
* BE-65	Plan Upgrade page working off stale billing data
* BE-66	Walk-Through Wizard cannot be launched
* BE-68	Hide expanded LH menu upon a click
* BE-112	None or not all Projects are visible on Edge
* BE-126	Clicking on the Downgrade button has no effect
* BE-127	Show a Tool Tip for Project Settings
* BE-128	Sending password confirmation in clear-text
* BE-140	Modify behavior of the expandable LH menu - do not expand when I merely move the mouse across it
* BE-141	Show tooltip when hovering over project icon in the transcript list on home page

This release has the following fixes and improvements in the rest of the Voicegain Platform:

* BE-48	Issue with AccountUsage collector query
* BE-53	Issue with AccountUsage collector query (2)
* BE-56	Duplicate/Triplicate Projects visible in Transcribe App
* BE-62	Text formatter occasionally throws an Exception
* BE-117	Increase the limit for the number of concurrent websockets
* BE-118	Remove duplicate Transcribe App projects on Edge
* BE-129	Reduce real-time delay in case of many concurrent sessions
* BE-146	Fix concurrency issue in mrcp_rex plugin history

### Maintenance release 1.80.2 is scheduled for 3/13/2023 between 1pm and 2pm CST

This release has the following fixes:
* BE-106 SMU is using a lot of Redis memory

### Maintenance release 1.80.1 is scheduled for 3/10/2023 between 3:45pm and 6:45pm CST

This release has the following fixes
* BE-51	Fix for WS/WSS protocol for Audio Streaming is not working
* BE-54	Fix session_duration set to 0 for each offline ASR session measurement in influxDB
* BE-58	Add missing insecure websocket url to Ingress

### Minor release 1.80.0 is scheduled for 3/9/2023 between noon and 3pm CST

This release has back-end improvements that will eventually give better monitoring more precise billing/usage data. It also includes a model that is more accurate on call-center audio.
We also made changes to support new Billing Plans in the Transcribe App.

* BE-1	Fixed number formatting in multi-speaker transcripts
* BE-2	Fixed error connecting to Redisson caused by 3rd-party lib
* BE-3	Fix issues where in some cases mixed meeting audio was missing some channels
* BE-6	Fix measurements not written to influxDB due to field format mismatch
* BE-7	Fix measurements not written to influxDB due to field format mismatch
* BE-9	Fix issue where measurements with identical timestamp would overwrite
* BE-15	Resolve issue with field type being inconsistent with old data
* BE-30	Fix service startup problem due to invalid character in authorization value
* BE-39	Configure production-ready log levels on classes that write to influxDB
* BE-17	Configure Cloud influxDB connection parameters for all environments
* BE-18	Configure influxDB writing classes correctly for deployment on Edge
* BE-19	MeasurementWriter to be able to distinguish if it is running in Cloud or on Edge
* BE-20	Add diarization and channel_selector tags to api_session_asr measurements
* BE-33	AccountUsage generator should use longer query interval if run for the very first time
* BE-36	Deploy latest offline model VoiceGain-omega-x - trained on additional call-center audio
* BE-38	Changed pricing and time limits on Transcribe App plans

### Minor release 1.79.0 is scheduled for 2/19/2023 between 3pm and 6pm CST

This release has several back-end improvements to the core Voicegain Platform:
* The rate limits use is now logged to the influxDB and can be queried from Grafana. 
You can configure alerts in Grafana so that you can know if you are getting close to the rate limits.
* The throughput in the offline mode has been further improved. 
Edge deployments have been tested to 1200 hours transcribed per hour for extended periods of time.
* Cause for the spike in redis use under extreme loads has been identified and removed.
This will result in better stability due to much lower use of the redis resource.
* Edge deployments to GCP VPC now require smaller set of permissions to use Google Storage.
* In Edge deployment, MongoDB indexes are created on startup. The set of indexes used has been optimized.
* Removed `permessage-deflate` support on websocket connections used by real-time transcription. 
This in order to reduce the latency.

### Maintenance release 1.78.1 is scheduled for 2/15/2023 between 6pm and 9pm CST

This release includes the following for the Transcribe App:
* Keyword and phrase highlighting in the transcript text
* Bug #671 fixed: home/login page loop in all the nonces somehow are removed from the indexedDB

### Minor release 1.78.0 is scheduled for 2/14/2023 between 6pm and 9pm CST

In this release the throughput of the offline transcription in two-channel mode has been significantly improved.

This release addresses the following issue for the rest of the Voicegain platform:
* #82: (ACP) Add matomo to Web Console (dev and prod)
* #86: (CMP) the Detail option takes me to the Login page instead of the Account Detail page
* #212: ascalon-asr-api cannot start on CHD environment
* #214: Get error when running offline transcribe on CHD
* #216: Add code that logs the measurements for usage of rate-limits per account
* #217: Log usage of the offlineQueueSizeLimit
* #220: Edge deployments to GCP VPC now support Google Storage via S3 adapter
* #223: Add language to the result of Transcription
* #225: Random text output from real-time transcription in some cases after long silence

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



**Backwards incompatibility:**
* Certain acoustic model names are no longer available. Unless using specific custom models, it is now sufficient to just provide `languages` parameter - no need to specify acoustic model by name.
* requests to `/asr/transcribe/async` API with `portal` field value but no `portal.label` specified will fail - `portal.label` is now a required value 



