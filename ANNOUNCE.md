### Maintenance release 1.88.1 is scheduled for 8/23/2023 between 6pm and 9pm CST

Known Issues:
* BE-809 Enabling full masking (*****) caused Meeting Minutes to not be generated - If you enable Full Text Redaction for some category then Meeting Minutes may not be generated. A work-around is to disable Word Cloud on the Project.

Changes related to Integrity of Processing (fixes)
* BE-774	Fix: Incorrect MPEG-DASH mpd format file generated
* BE-802	(TA) Fix: Account redacting formatters are saved to Projects
* BE-803	Fix: Formatters defined on account are not being used in POST /asr/meeting
* BE-806	(TA) Fix: When generating a pdf, NullPointerException is thrown if meetingMinutes is not enabled
* QA-405	Fix: Demo app has incorrect recaptcha key

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.88.0 is scheduled for 8/22/2023 between 5pm and 7pm CST

**Backwards incompatibility** : 
This release removes `sentences` parameter from session.content in /asr/transcribe API.
It gets replaces with `segments`.

New functionality in the Transcribe App:
* BE-416	(TA) Login from Transcribe App to Freshdesk
* BE-640	(TA) Support renaming existing Speaker
* BE-685	(TA) Admin (Account level) controlled PII redaction
* BE-699	(TA) more options for PII Redaction (add full and partial masking)
* BE-703	(TA) Implement https://transcribe.voicegain.ai/freshdesk/login
* BE-704	(TA) Change the URL for Help->Submit a Support Ticket
* BE-721	(TA) Add PII Redaction page inside Account settings
* BE-732	(TA) Add x to cancel a search for transcript within project
* BE-751	(TA) Support upload of multiple files for transcription
* BE-752	(TA) Add two filter toggles on the Speakers list
* BE-755	(TA) On home page show selected Project together with Home
* BE-756	(TA) Allow change of name of an External Speaker
* BE-757	(TA) Show email for User Speaker
* BE-759	(TA) Modify the list of entities to redact (ZIP, DMY)
* BE-764	(TA) Show only current project on the LH menu
* BE-793	(TA) 3 distinct URLs for "Submit Support Ticket" link depending on environment
* QA-369	(TA) Improved Error message if user tries to sign-up second time with same email
* QA-373	(TA) Improved title of page with Account Users
* QA-400	(TA) Disable Save button if no new users have been selected

New functionality in other platform components:

* BE-666	Return information about what parts of the transcript were redacted and by what rule
* BE-688	Better end-of-segment detection for real-time sentence-by-sentence (segment-by-segment) mode
* BE-707	Enable keepalive ping also on the websocket used for the audio
* BE-710	Add formatters field to the Account API
* BE-728	Presigned URLs for Data Object files
* BE-729	In the API remove "sentences" as content and replace with new "segments"
* BE-738	Partial redaction of PERSON NER -> generate Initials
* BE-749	Add defaultContext to User data in User API
* BE-769	Make  GET `/data/{uuid/file/{fnameWIthExt)` return special output if contentType is application/dash+xml

Changes related to Integrity of Processing (fixes):
* BE-708	(TA) Fix: Cannot delete a device that is shown in the device list
* BE-715	(TA) Fix: At larger zoom levels Left-Hand menu unusable
* BE-761	(TA) Fix: Project Transcript list shows meeting from home page after auto refresh due to STOP message
* BE-791	(TA) Fix: We are not generating Meeting Minutes in German if the Project is German
* BE-795	(TA) Fix: Weird long topics for Spanish Meetings
* QA-365	(TA) Fix: Next Audio button not responding on Single Click (or with delay)
* QA-368	(TA) Fix: Search and Project Name is overlapping over each other
* QA-370	(TA) Fix: Trying to recompute any file, resulting all files showing across all projects.
* QA-372	(TA) Fix: Transcripts table-Table sorting by "Name" and "Created on" is not working.
* QA-374	(TA) Fix: My shares table-Table sorting not working for name, transcription date, and scope.
* QA-377	(TA) Fix: Search text should reset on Project switch
* QA-401	(TA) Fix: Other users table- Sorting by last active is not working.
* QA-403	(TA) Fix: other accounts users table- Sorting by name is not working.
* QA-410	(TA) Fix: Left menu is breaking down when selecting it rapidly.
* QA-417	(TA) Fix: Account Text redaction/project setting- When placeholder is selected fields should be required fields.
* BE-720	Fix issue with UUID on Oracle MongoDB
* BE-723	Fix: ex-autoscaler cronjob is not working when there are more than 9 rex instances
* BE-742	Fix: asr-api sends hypothesis msg of the next sentence to websocket before the recognition msg of the current sentence
* BE-746	Fix: Some words are included in two recognition results
* BE-750	Fix: In some case, asr-api does not send recognition websocket msg when getting EOS
* BE-753	Logic fix in EZInit kubelet configuration
* BE-754	Fix: audio redaction is not working in meeting API
* BE-762	Fix: Redaction.originalValue is returned with default debug level
* BE-763	Fix: Prevent storing duplicate formatters
* BE-797	Fix: Incorrect decimal formatting if currency
* QA-363	(Web Console) Fix: New User Wizard step4
* QA-379	(Web Console) Fix: In Experiments sections, input fields overlapping with close icon
* QA-380	(Web Console) Fix: IVR Proxy status is not showing properly
* QA-392	(Web Console) Fix: Properly notify about attempt to create duplicate name Context
* QA-398	(Web Console) Fix: textboxes are not cleaned up when I try to create a second context

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Maintenance release 1.87.1 is scheduled for 8/10/2023 between 2:30pm and 6pm CST

Changes related to Integrity of Processing (fixes)
* BE-722    Recognizer does not send RECOGNIZE-COMPLETE if no audio has been sent to Recognizer

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.87.0 is scheduled for 8/7/2023 between 8pm and 11pm CST

New functionality in the Transcribe App:
* BE-603	Transcribe App: Automatically refresh status of the transcripts
* BE-621	Transcribe App: Hide invalid transcript move project destinations
* BE-623	Transcribe App: Improved Error message in case of transcript move error
* BE-626	Transcribe App: Limit Basic Plan user to only 5 shares
* BE-628	Transcribe App: Enhanced Project selection
* BE-638	Transcribe App: PII Redaction placeholder validators allow non-ASCII characters
* BE-651	Transcribe App: Add Table of Contents in the exported PDF
* BE-657	Transcribe App: Add Metadata in the exported PDF
* BE-668	Transcribe App: Zoom Meeting Assistant Download name now has version included
* BE-671	Transcribe App: Add ability to completely disable Download on Edge
* BE-675	Transcribe App: Update content of Home Page if there are no transcripts
* BE-680	Transcribe App: Add ability to completely disable transcript copy to clipboard on Edge
* BE-693	Transcribe App: Update content of Home Page if there are no transcripts
* BE-694	Transcribe App: Add Login and SignUp buttons to the Share Expired/Invalid page
* BE-695	Transcribe App: Do not show the Move option for transcripts in a project that does not belong to a user and has not been shared with the user

New functionality in other platform components:
* BE-574	Web Developer Console upgrade to latest AntD
* BE-641	Disabled deprecated support for the Language Models in the Developer Console
* BE-667	Admin Tool: Allow modification of Rate-Limits
* BE-678	Easy scaling for real-time transcription supported
* BE-687	Add noAudioTimeout option to asr API

Changes related to Integrity of Processing (fixes):
* BE-620	Transcribe App fix: Sorting shares by Expiry time
* BE-635	Fixed issues in Walk-Through Wizard in the Developer Console
* BE-637	Transcribe App fix: Prevent invalid PII Redaction placeholders in Project settings during creation 
* BE-639	Fix access to a transcript from a Developer Console Context Dash
* BE-672	Transcribe App fix: Prev/Next buttons not working correctly
* BE-674	Fix missing audio charts in Transcribe+ in Web Console
* BE-691	GET /user/sync API checks user existence based on user.email
* QA-261  Transcribe App fix: Make transcript not clickable if status is Queued
* QA-357  Fix weird behavior of Web Console if the current context is deleted
* QA-362  Transcribe App fix: Sorting by transcript Status

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Maintenance release 1.86.5 is scheduled for 8/2/2023 between 3:30pm and 4:30pm CST

This release enables higher number of replicas for autoscaling.

It is just a configuration change.

### Maintenance release 1.86.4 is scheduled for 7/28/2023 between noon and 2pm CST

Changes related to Integrity of Processing (fixes)
* BE-662    Temporary fix for "ASR-API kills REX session if there is no activity for 5 minutes" - timeout extended to 15 minutes
* BE-663    Fix for: asr-api on CHD environment rejects derived session because callback url is redis
  * this was introduced by: BE-615 Enable TWILIO protocol in CHD environment (sapi.voicegain.ai) 

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Maintenance release 1.86.3 is scheduled for 7/21/2023 between 5pm and 6pm CST

Changes related to Integrity of Processing (fixes)
* BE-631    Remove punctuation between two digits in En BERT punctuation model

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Maintenance release 1.86.2 is scheduled for 7/18/2023 between 1pm and 4pm CST

This release includes an improved real-time English model delivering higher accuracy of speech recognition.

Changes related to Integrity of Processing (fixes)
* BE-622    (SSO) Fix issue with Spinner that does not stop if login failed (no error message was shown)

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Maintenance release 1.86.1 is scheduled for 7/14/2023 between 5pm and 6pm CST

This release has several improvements in the PDF export in the Transcribe App (Meeting API)

Changes related to Integrity of Processing (fixes)
* QA-301    Transcribe App: Removed recompute option from transcripts in Error state.
* QA-308    Transcribe App: Fixed getting blank screen on My Shares
* QA-323    Transcribe App: Fixed project flag indicators not working as expected on Homepage (also BE-611)
* QA-324    Transcribe App: Fixed unable to move transcript between projects (also BE-616)
* BE-612    Transcribe App: Incorrect area outlines on the Home Page

Fixes in other components:
* BE-614    Web Console: In Edge Config prevent selection of configuration not matching the version
* BE-615    Enable TWILIO protocol in CHD environment (sapi.voicegain.ai)

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.86.0 is scheduled for 7/13/2023 between 9pm and 11pm CST

New functionality in the Transcribe App:
* BE-550	Transcribe App: Usability improvement in share creation.
* BE-458	Transcribe App: Add a checkmark to indicate among the matching Speakers the one that is assigned to the Speaker from transcript
* BE-494	Transcribe App: Added validation for values entered in the text redaction fields
* BE-555	Added support for multiple languages to the UI of the Transcribe App.
* BE-568	Transcribe App: Delete all devices belonging to a User when a User is being deleted
* BE-570	Transcribe App: Improvements to the projects view in the Left-Hand menu
* BE-571	Transcribe App: Add new Zoom Icon (with status) in left-hand Menu
* BE-576	Transcribe App: Add name of the user to be deleted to the User Deletion confirmation dialog
* BE-582	Transcribe App: Modified text on the Signup page for EDGE if OIDC SSO is enabled on the account
* BE-596	Transcribe: Add support for Hindi language for transcription.
* BE-605	Transcribe App: Improved instructions on ZoomMA download page
* BE-598	Transcribe App: Added PDF export option (beta)
* BE-569	Transcribe App: Change the Home Page Plan info to a new format
* BE-575	Transcribe App: Replace Browser Capture Icon with Google Meet Icon
* BE-580	Transcribe App: Move Latest News to a separate page that in accessible from the Help Menu

New functionality in other platform components:
* BE-561	Admin tool: Added ability to change the account Billing Style
* BE-563	Added API to add credit to an account
* BE-558	Implemented a static method that generates PDF from a meeting JSON
* BE-564	Make it possible to modify billing style on the Account using Admin tool
* BE-565	Added pdf format to GET /asr/meeting/{meetingId}/transcript API
* BE-546	Support stopping billing-utility from processing anything
* BE-547	new-billing-utility to store usage of each TranscribApp account in Firestore
* BE-554	new-billing-utility supports auto-refill

Changes related to Integrity of Processing (fixes):
* BE-440	Web Console: fix missing waveform in the microphone capture preview
* BE-591	Make sure no account information is revealed by password reset API.
* BE-514	Added Matomo to App Selector with correct IDs for dev and prod
* BE-567	GET /user/{userId} returns 404 if the specified user does not exist
* BE-581	prevent new-billing-utility from processing multiple hourly storage requests
* BE-560	EZ Script fixes for K8s 1.27 and deprecated config
* BE-572	App Selector: Update text on Signup page
* BE-587	Reject with 400 (Bad Request) all requests to sapi endpoint which have audio.capture=true
* BE-590	Accept WSS streaming protocol on PCI/CHD environment

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


### Maintenance release 1.85.2 is scheduled for 6/29/2023 between 9pm and 11pm CST

Changes related to Integrity of Processing (fixes)
* BE-549    Public Transcribe App share from EDGE cycles non-stop if used without login

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Maintenance release 1.85.1 is scheduled for 6/29/2023 between 3pm and 6pm CST

Changes related to Integrity of Processing (fixes)
* BE-548    Do not send multipart/form-data parameters as files in audio.callback. Only audio data should be sent as file.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

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



**Backwards incompatibility:**
* Certain acoustic model names are no longer available. Unless using specific custom models, it is now sufficient to just provide `languages` parameter - no need to specify acoustic model by name.
* requests to `/asr/transcribe/async` API with `portal` field value but no `portal.label` specified will fail - `portal.label` is now a required value 



