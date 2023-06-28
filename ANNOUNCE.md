### Minor release 1.85.0 is scheduled for 6/28/2023 between 7pm and 10pm CST

New functionality in the Transcribe App:
* BE-45	Add Sharing of transcripts from Transcribe App
* BE-422	In Transcribe App add Custom behavior for Help->Submit a Support Ticket option
* BE-423	In Transcribe App: Support sharing from the Transcript Detail Page
* BE-424	In Transcribe App: Add Page where the user can see all the meetings that they have shared
* BE-426	In Transcribe App added Page that shows a single shared transcript to a not logged-in user
* BE-427	In Transcribe App added Page that shows a single shared transcript to a logged-in user
* BE-449	In Transcribe App: add ability to recompute Meeting Minutes for all Meeting withing Project

New functionality in other platform components:
* BE-225	Modify the Admin Tool to show "Last Used" time
* BE-233	In Admin tool: add PCI-DSS column to the main account table display
* BE-326	In Web Console: Show SHA sum of the Edge Cluster configuration
* BE-387	In Web Console: If account is PCI compliant then show CHD Rate Limits
* BE-417	Implemented Share APIs
* BE-418	Implemented GET api for meeting data that uses shareId
* BE-425	Add sharedBy and sharedWith parameters to GET /asr/meeting query
* BE-447	Add PUT /asr/meeting/context/{contextId}/recompute method to recompute all the meetings on a context
* BE-474	In Admin Tool: Show the number of Phones
* BE-475	In Admin Tool: Add sorting by balance
* BE-476	In Admin Tool: On the Usage chart make it possible to deselect one or more lines
* BE-484	In Admin Tool: Add a "view password" feature to the login dialog
* BE-485	In Admin Tool: Add "Suspend Selected" account functionality
* BE-487	In Web Console Signup: Add confirmation of the values being submitted
* BE-489	When creating new buckets enable versioning and set lifecycle rules
* BE-514	Add Matomo to App Selector
* BE-515	In App Selector: Add support for selectable Spanish/English language in the UI
* BE-528	In Admin Tool: Add filtering on null value for Last Login and Last Used fields
* BE-539	Support a new property: minio.server.region
* BE-541	Add Region to Object Store settings for Edge Cluster

Changes related to Integrity of Processing (fixes):
* QA-183    In Transcribe App fix the link from "Manage Users"
* BE-197	Add Kubeadm API update to EZUpdate.py
* BE-411	In Web Console: Add splash loading screen
* BE-446	In Transcribe App improve prompt in the URL entry box
* BE-453	In Transcribe App fixed the "missing voice signature speaker" error
* BE-454	Configured brotli for Cloud ACP and Transcribe App
* BE-456	Fixed new-billing-utility fail to store an instance of Account in Redis due to oidcSettings
* BE-462	Fixed new-billing-utility fail to send alerts due to a missing environment variable
* BE-463	Fixed new-billing-utility fail to process storage and phone number usage periodically
* BE-466	Fixed multiple records of storage usage of an account are written to postgres
* BE-467	new-billing-utility submits the usage of a phone number to Billing System
* BE-477	In Web Console in Add User dialog fixed the User option showing twice
* BE-478	new-billing-utility fails to group the same type of ASR usage into one single record for a given interval
* BE-479	new-billing-utility derives billing_to_process from only asr usages and ignores other types of usages
* BE-480	Fixed: Account query API does not return correct values for pciDss field
* BE-483	In Admin Tool: Better names for tabs
* BE-492	new-billing-utility to ensure each quantity has up to 6 decimal places before it's sent to Fusebill
* BE-493	In Web Console: fixed issue with New User Wizard (Joyride) 
* BE-505	In Admin Tool: Make login safer by using pre-login feature
* BE-512	GET /config-cluster fails to include clusterConfigShaSum in the response
* BE-517	Fixed: EZINit issues with home directory and autossh for auto generated voicegain user.
* BE-518	rex fails to invoke SessionMeasurementUtility.commit() for some realtime ASR sessions
* BE-521	Fixed in Web Console: Transcribe+ table does not span full available width
* BE-525	Fixed Polling URL returned from POST /sa
* BE-527	Fix in Transcribe App: Download no longer downloads TXT and Audio
* BE-529	In Admin Tool: Change filtering values on Contexts, Edge, Websockets, Phone #, and Users columns
* BE-537	In Web Console: Fix user gets duplicated when adding roles
* BE-538	Fixed in Transcribe App: the request for meetings on the home page should retrieve only 20 meetings
* BE-540	Fixed in EDGE Web Console: Fallback Login is shown incorrectly
* BE-542	Fix RedisTimeoutException: Unable to acquire connection!
* BE-544	Fixed: Cloud function cannot add task to redis

Third-Party vulnerability (security) related fixes:
* BE-464	Admin Tool: Update to yarn and update packages to newer versions
* VM-79	Unimrcp docker vulnerability
* VM-81	freeswitch docker image vulnerability
* VM-133	Python package protobuf==3.20.1
* VM-135	offline-main docker image vulnerability (ffmpeg)
* VM-136	ml-svc-grpc docker image vulnerability
* VM-149	(SSO) nth-check Regular Expression Denial of Service (ReDoS)
* VM-150	(SSO) async-validator Regular Expression Denial of Service (ReDoS)
* VM-151	(SSO) word-wrap Regular Expression Denial of Service (ReDoS)
* VM-152	(SSO) css-what Regular Expression Denial of Service (ReDoS)
* VM-153	filebeat docker image vulnerability
* VM-154	elasticsearch-master docker image vulnerability
* VM-155	Triton docker image vulnerability
* VM-156	Java services Docker image vulnerability
* VM-157	httpd docker image httpd:2.4.57-alpine3.17 vulnerability
* VM-158	redocly/redoc:v2.0.0-rc.50 docker image vulnerability 
* VM-159	transmogrifier ssh and web docker container vulnerability
* VM-160	ingress-nginx==4.6.0 helm chart vulnerability
* VM-161	freeswitch 2.3.10 docker image vulnerability
* VM-162	python:3.9.16-slim@sha256:78740d6c888f2e6cb466760b3373eb35bb3f1059cf1f1b5ab0fbec9a0331a03d docker image vulnerability
* VM-163	nats:2.9.16-debian-11-r1 docker vulnerability
* VM-164	telegraf:1.26.1 docker image vulnerability 
* VM-165	mysql:5.7.30 docker image vulnerability
* VM-166	Pod container allows privilege escalation on exec
* VM-167	 Pod container is allowed to run as root
* VM-168	grafana 6.6.0 docker image vulnerability
* VM-169	single-tensorflow-serving:2.11.1 Docker image vulnerability


All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


### Maintenance release 1.84.3 is scheduled for 6/19/2023 between noon and 3pm CST

Changes related to Integrity of Processing (fixes):
* Fix several UI glitches that were introduced when updating AntD version.

Changes related to Security:
* BE-220    demo.voicegain.ai requires Content Security Policy and related Headers

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Maintenance release 1.84.2 is scheduled for 6/8/2023 between 2pm and 3pm CST

Changes related to Integrity of Processing (fixes)
* BE-448    Project transcript view shows also Home Page transcripts directly after switch from Home to Project view

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Maintenance release 1.84.1 is scheduled for 6/7/2023 between 2:30am and 3:30pm CST

Changes related to Integrity of Processing (fixes)
* BE-442    Fixed in Transcribe App: Voice Signature sample playback always plays from the beginning of audio
* BE-443    Fixed in Transcribe App: Transcription fails because unable to find the speaker

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.84.0 is scheduled for 6/6/2023 between 1am and noon CST

This release includes a significantly more accurate Spanish real-time model.

Here is a list of fixes and changes:
* BE-224	Track on each account the most recent access
* BE-242	Finalized the new style of the Browser Capture pop-up in Transcribe App
* BE-260	In Web Console: In File Transcribe Dialog add ability to enter hint misspellings and boost
* BE-279	Allow only Audio files for upload to Clip Manager
* BE-281	In Transcribe App: Added a page with Terms of Use that is reachable via the Help menu
* BE-288	Fixed in Transcribe App: Asks to setup a payment method while payment method already setup on the account
* BE-327	Show context id in the card with JWT token
* BE-336	Improved English NER
* BE-365	Voicegain SSO App updated to latest 3rd-party package versions, also switched from npm to yarn
* BE-367	Make the User Management table sortable in the Web Console
* BE-369	Generate JWT with userId and use it where needed
* BE-370	Fixed in meeting minutes: Summaries truncated mid sentence
* BE-371	Fixed: Save button not enabled on EDGE in user profile
* BE-372	In Transcribe App left-hand menu - prevent overlapping scroll bars
* BE-373	fixed in Transcribe App: Error when deleting last Device
* BE-374	Fix in Transcribe App: asr-api doesn't allow users to move a meeting session to a different context in some case
* BE-377	Library Vulnerability check for the SSO app
* BE-378	Modify EZInit and EZUpdate script to correctly set directory permissions
* BE-379	Modify /asr/transcribe/async API to support audio calbacks
* BE-380	Add report of the audioCallback in the full /asr/transcribe/async results
* BE-381	Add DMY to list of NERs that we support for redaction in asr/transcribe formatter
* BE-382	Fixed in Transcribe App: incorrect speaker names found in exported meeting transcription
* BE-384	Supports audioCallback with PI Redacted audio
* BE-388	Fix in Web Console: Transcription from URL request is missing audio.capture parameter
* BE-389	Improved Context selection dialog in the Web Console
* BE-391	In Transcribe App: trim spaces from entered URL
* BE-392	Disable Password Recovery Key page if user is logged in using SSO
* BE-394	New API to return AuthConfig by name from Context
* BE-396	Do not offer local password change to users logged in via SSO
* BE-401	In Web Console: add 'S3 Compatible' type of auth config
* BE-404	Support context.description in Context API
* BE-407	Changes to authConfig to support S3 Compatible URI
* BE-408	Fixed in Transcribe App: Wrong confirmation dialog show when deleting user from Account
* BE-412	When syncing users, avoid copying a user to edge if the user's email is found on edge
* BE-414	API for multipart/form-data for Audio Callback
* BE-415	Add GET /asr/transcribe/status/queue API
* BE-419	Add customValues to the OnPrem Cluster API
* BE-421	Fixed bug: In regex-based redaction only the first regex is being used
* BE-429	Fixed formatting anomaly: ok, let's try number 1
* BE-431	Fixed in Transcribe App: Bad URL in Advisor
* BE-435	In Web Console: When we are done creating new context - switch to the new context
* BE-436	Fixed in Web Console:  broken validation for area-code numbers
* BE-439	In Web Console: fix formatting of the Transcribe Detail page

### Minor release 1.83.0 is scheduled for 5/22/2023 between 6pm and 9pm CST

Key things that are new in the Transcribe App this release:
* Meeting summaries are generated by GPT-3.5
* Zoom Meeting Assistant now uses Device Pairing to authenticate with the Transcribe App. You will need to download and install Zoom Meeting Assistant ver 1.0.0+
* On EDGE, Transcribe App now supports OIDC SSO.

Here is a list of fixes and changes
* BE-164	Modifying Edge configuration is no longer supported - on change new configuration needs to be created
* BE-211	In Web Console - do not accept characters not needed in field values
* BE-228	Fixed Major 3rd-party vulnerabilities 
* BE-241	OIDC SSO functionality added to Transcribe App
* BE-246	Page to configure the OIDC SSO parameters in Transcribe App
* BE-247	New Login page for Transcribe App if SSO is enabled
* BE-252	Zoom Meeting assistant ver. 1.0.0 with new Device Pairing functionality
* BE-264	Invite User dialog now extended to handle SSO users
* BE-266	New welcome to Transcribe App email for the SSO invite case
* BE-267	If SSO is enabled for the Transcribe App then Forgot Password should direct to SSO
* BE-273	Meeting transcription will complete even in presence of  NATS messaging errors
* BE-275	APIs to support device pairing
* BE-282	Transcribe App now support device pairing - a new page for device management
* BE-283	New Zoom Meeting App installer now supports properties needed for device pairing
* BE-291	Fixed bug: Auth Configuration may overwrite good credential with a bad one
* BE-292	Meeting Minutes summary now generated by LLM
* BE-298	New Auth API methods to support SSO login
* BE-305	New field in /cluster API to support Edge deployments with SSO
* BE-311	CHD environment can submit measurements to local influxDB
* BE-312	New Zoom Meeting Assistant installer supported on Edge
* BE-316	Track CHD sessions for billing
* BE-319	Rate-Limit measurements are now sent from CHD environment and tagged with chd=true
* BE-324	Add CHD boolean tag to all measurements written to the influxDb
* BE-325	New Rate Limits in the Account API for CHD environment
* BE-330	Separate Rate-Limits for CHD environment
* BE-332	Apply fetchTimeout to the ffmpeg -timeout option
* BE-338	Automatically signup users from SSO if the email domain is allowed
* BE-339	Support cases where an SSO user wants to login but the domain is not allowed
* BE-340	In Transcribe App: support key sentences which are summaries as cannot be attributed to a single speaker.
* BE-341	In Transcribe App Meeting Minutes: implement speaker substitution also for key sentences
* BE-342	Fixed TTS (Google voices) fails on text like e.g. "7, 6, 2, 6, 2"
* BE-345	If OIDC is enabled for a Cluster then do not show "Signup Code" in from Account Settings
* BE-346	In Transcribe App, provide a pop-up alert if a device need pairing approval
* BE-347	GET /confgroup now accepts JWT tokens
* BE-348	Changes to how authConfig is updated using PUT/confgroup/uuid
* BE-349	In POST /asr/meeting: do not override context to null if JWT has no context
* BE-353	fixed: PUT /confgroup/uuid with languages=[null] causes NPE
* BE-356	Modify PUT /user/uuid to accept JWT tokens for authentication
* BE-357	Unable to delete values of "allow signup from domains"
* BE-359	Support DMY NER in Transcribe App project configuration
* BE-360	In Transcribe App: New user invited from SSO will set name auto populated

### Maintenance release 1.82.3 is scheduled for 5/10/2023 between 8:30am and 10am CST

This release upgrades Kubernetes to 1.25

### Maintenance release 1.82.2 is scheduled for 4/27/2023 between 5:30pm and 7pm CST

This release has the following changes:
* BE-256    Modified App Selector to properly render on mobile browsers
* BE-257    Added notice to Login Screen on Transcribe App on mobile browsers

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



**Backwards incompatibility:**
* Certain acoustic model names are no longer available. Unless using specific custom models, it is now sufficient to just provide `languages` parameter - no need to specify acoustic model by name.
* requests to `/asr/transcribe/async` API with `portal` field value but no `portal.label` specified will fail - `portal.label` is now a required value 



