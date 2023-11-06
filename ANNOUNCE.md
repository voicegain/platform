### Minor release 1.93.0 is scheduled for 11/2/2023 between 9:00pm and 11:59pm CST

New functionality in the Transcribe App:
* BE-1100	TA: In large Video view put the Transcript (CC) in a frame that can be moved around the screen.
* BE-1135	TA: Better copy-to-clipboard of the Meeting Minutes components
* BE-1147	TA: Show "This Meeting has no video" in the large-video view if meeting has video
* BE-1152	TA: In tag editor enable Save button only if something has changed

New functionality in other platform components:
* BE-1032	Add GET /zoom/oauth and DELETE /zoom/oauth APIs
* BE-1039	AIVR: Support DTMF in output actions
* BE-1040	AIVR: Re-design for prompt playback - now using events instead on single audio stream
* BE-1044	POST /auth-svc/device to return api URL in the QR code
* BE-1068	Support misspellings in hints in REAL-TIME mode
* BE-1159	Increase the number of allowed audio files in POST /asr/meeting to 25

Changes related to Integrity of Processing (fixes):
* BE-1099	TA: Fix - Specified date format is not being used
* BE-1110	TA: Modify NSIS Installer use proper setting of REINSTALLMODE
* BE-1126	TA: Fix - Large-video chat popup captures focus and icons become not clickable
* BE-1142	TA: Fix - When Zoom upload contains a video file we should set the "video" tag on this meeting
* BE-1145	TA: Add beta label over the DOCX selector
* BE-1146	TA: Fix - Remove UUID tool tips in the large-video view
* BE-1162	Fix - Failure in sa-recompute on Edge
* QA-545	TA: Now not be allowed to play multiple voice signature at the same time.
* QA-567	TA: Fix - Files under processing status shouldn't get option for (Re-Compute, Move or Delete)
* QA-630	TA: Fix - Transcripts on Homepage are not updating after changing Projects.
* QA-631	TA: Fix - Unable to edit Download permission after changing role from admin to user in one go.
* BE-1166	In offline task, if we can't download video, we generate audio-only dash-mpeg
* QA-629	Console: Fix - Unable to download in JSON format in Download options in Transcribe under Transcribe+(beta)

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.92.0 is scheduled for 10/19/2023 between 4pm and 6pm CST

New functionality in the Transcribe App:
* BE-779	TA: Show chat messages in Right-Hand pane
* BE-856	TA: Fix - Login - not showing the locked until information
* BE-883	TA: Zoom OAuth Handshake page added
* BE-999	TA: Include video in the manual Zoom folder upload
* BE-1003	TA: Implemented large video view
* BE-1004	TA: New design for the Audio Source selector
* BE-1010	TA: Add export in Docx format
* BE-1014	TA: Better error massage in case of Recaptcha related Error
* BE-1015	TA: Fixed the +tag message and added hover text
* BE-1022	TA: Added a tag editor
* BE-1053	TA: Edge: If SSO is enabled make login automatic if user hits /login url
* BE-1055	TA: Show both installed version and available version of Zoom Meeting Assistant if newer version available
* BE-1061	TA: Ability to Control Download permissions
* BE-1063	TA: Ability to set a download permission on a User
* BE-1082	TA: Meeting Chat now being shown
* BE-1086	TA: Add Copy-to-Clipboard feature on the Overview page
* BE-1087	TA: Add new download option for docx files
* BE-1101	TA: Prevent entering regex that can match too much text
* QA-488	TA: Make Meta Description Tags SEO friendly
* QA-538	TA: Show message after user delete successfully 

New functionality in other platform components:
* BE-832	Implemented GET /asr/meeting/search/fields
* BE-852	Digits formatter for real-time sessions
* BE-862	Add new field AUDIO_SRC to meeting search API
* BE-932	Use Google secret manager to manage credentials on GCP cloud
* BE-974	In offline task, create gRPC channel to ml-svc on demand
* BE-980	Ensure that Advanced Search queries only Projects/Contexts the User has access to
* BE-988	App Selector: Add links to Privacy Policy and Terms of Use
* BE-993	The video that is stored under videoId on a meeting now has audio removed
* BE-1008	Console: Align Left and Right audio charts for the Telephony Bot Sessions
* BE-1009	Console: Improve the look of the ASR settings forms
* BE-1030	AIVR API: Add authToken to first Callback and use it in PUT /aivr/{ivrSid}/vars
* BE-1031	AIVR API: Add ani parameter to GET /aivr/, add sorting, add endTime field
* BE-1037	Configure MongoDB memory limit and cacheSizeGB
* BE-1045	Add tags field to PUT /asr/meeting/{meetingId}
* BE-1046	Modifications to GET and HEAD /data/{uuid}/file/{fnameWithExt} APIs
* BE-1065	Enforce "download" permission in GET /asr/meeting/{meetingId}/transcript
* BE-1069	Console: Show error if API to create new Edge Cluster fails
* BE-1071	Support chat.msg in the response of GET /asr/meeting/uuid/data
* BE-1079	Smarter match of chat speakers to the speakers in the Zoom Meeting (if there is no speaker timeline)
* BE-1083	Add docx format option to GET /asr/meeting/{meetingId}/transcript
* BE-1102	Prevent text redaction regex from matching too long patterns
* BE-1103	Support smarter partial redacting PERSON if a name has no space

Changes related to Integrity of Processing (fixes):
* BE-966	TA: Fix - Weird pause and play behavior on the Voice Signatures page
* BE-967	TA: Fix - Missing Users step in new Project Wizard on Edge
* BE-1078	TA: Fix - Password reset by admin does not work
* BE-1080	TA: Fix - Unable to play audio/video in certain Edge deployments
* QA-537	TA: Fix - Current Project is not picking correctly while move

* BE-920	Fix - Meeting Search API exposes database structure in the error messages
* BE-991	Fix - Meeting Search - Gt, Le Terms always returning empty results
* BE-1012	Console: Fix Listen button from the Telephony Both Session view
* BE-1034	Console: On Edge environments without HTTPS provide a workaround for copy to clipboard
* BE-1038	Fix mongodb rolling deployment
* BE-1056	Fix - Session gets stuck on certain corrupted audio files
* BE-1076	Fixed: ascalon-cleanup fails to remove any orphan data object if persist=true is found in every data object in the first page
* BE-1085	Fix - Search API shows meetings from projects that User has no access to 
* BE-1098	Fix - Modified meeting tags are not passed to the data in postgresql
* QA-531	Console: Fix - On deleting the JWT success message is showing incorrect


All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Maintenance release 1.91.1 is scheduled for 10/3/2023 between 3pm and 6pm CST

Changes:
* BE-1013  Log invalid patterns found in RegexFormatters instead of throwing exceptions

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


### Minor release 1.91.0 is scheduled for 9/30/2023 between 5pm and 9pm CST

New functionality in the Transcribe App:
* BE-71	Transcribe App: Show Meeting VIdeo
* BE-709	Transcribe App: New meeting submitted by ZoomMA shows up on the home page automatically
* BE-886	Transcribe App: Support new guides for Zoom Meeting Assistant Use
* BE-961	Transcribe App: Remove Recompute button from Project settings - we can now select multiple Transcripts and recompute them
* BE-975	Transcribe App: Save latest project opened by a user in clientSideProperties
* BE-977	Transcribe App: Show Project info on the list of Shares
* BE-986	Transcribe App: Re-enable API Security settings
* BE-990	Transcribe App: Show Privacy Policy same way we show Terms of Service

New functionality in other platform components:
* BE-739	Web Console: Log audit events
* BE-778	In /ASR/meeting API add ability to upload meeting video and chat
* BE-819	New Kappa Real-TIme model trained on IVR data
* BE-901	Support more than one JWT per context
* BE-925	Prepare fluentbit configuration for writing audit log to Grafana Loki
* BE-945	Web Console: Show description for Edge Configurations
* BE-946	Web Console: Show Model and Language information in the Context Dash
* BE-956	Web Console: In Context Settings support multiple JWT
* BE-987	Web Console: Change the text about available languages (now that we support Whisper)
* BE-989	Web Console: Show privacy policy similar to how we show terms of service
* BE-992	Handle MPD files in SegmentTemplate format
* QA-490	Web Console (Edge): Launch Cloud Console in new tab
* QA-516	App Selector: Update features list now that we have Video support

Changes related to Integrity of Processing (fixes):
* BE-855	Web Console: Fixed transcript download in Transcribe+
* BE-969	Web Console: Fix weird layout in Telephony App settings
* BE-983	Fixed: REX tries to reserve Whisper model when diarization enabled
* QA-310	Transcribe App: Fixed - Features and Usage are not being translated in selected language instead of English language
* QA-467	Transcribe App: Fixed - Taking any URL as audio URL.
* QA-505	Transcribe App: Fixed - Mouse hovering on the upload/ upload type always showing microphone recording.
* QA-510	Transcribe App: Fixed - Editing any shared link changing its scope to public.
* QA-511	Transcribe App: Fixed - After audio finish play icon should be paused.
* QA-514	Transcribe App: Fixed - Hindi translation is on Recomputing the multiple transcription

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

Upload of video to the Transcribe App requires Voicegain Zoom Meeting Assistant version 1.2.1 or higher.


### Maintenance release 1.90.1 is scheduled for 9/22/2023 between 6pm and 11pm CST

Changes related to Integrity of Processing (fixes)
All these apply to the Transcribe App:
* QA-497  Fix: Accepting anything in tag, also taking space as tag.
* BE-790  Fix: At the end of project wizard sometimes have to click Done twice to get the new project saved
* BE-957  Fix: Not accepting MP4 file for transcription
* BE-964  Fix: Calling Invoice API on Edge

Other changes in Transcribe App:
* BE-955  Disable API Security Page

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.90.0 is scheduled for 9/20/2023 between 1pm and 6pm CST

New functionality in the Transcribe App:
* BE-669	Transcribe App: Added audit log
* BE-681	Transcribe App: Implement Person obfuscation in Meetings after a set time threshold
* BE-824	Transcribe App: Add ability to select multiple transcripts from the table an perform selected Action on them
* BE-843	Transcribe App: Add ability to specify Regex Redaction on the Project/Account Settings Text Redaction
* BE-873	Transcribe App: Added multi-selector delete on the Shares list
* BE-888	Transcribe App: Improve message on Zoom Meeting Assistant status
* BE-894	Transcribe App: Change name of the exe file in installer bundle to install.exe
* BE-909	Transcribe App: Make the digit formatting a default enabled option on creating new Project
* BE-910	Transcribe App: Store collapsed status of home page elements in ClientSide Properties on a User
* BE-915	Transcribe App: Add settings for Archival Text Redaction
* BE-919	Transcribe App: Tweak behavior of the 4 selectors on Transcripts on Home Page
* BE-929	Transcribe App: On Devices page - add a button to pair a Phone App

New functionality in other platform components:
* BE-124	(EDGE) Make InfluxDB available for querying by customers
* BE-778	In /ASR/meeting API add ability to upload meeting video and chat
* BE-812	(SSO) Modify password reset page to match the style that is used in Web Console
* BE-860	Support audio redaction also on DASH-MPEG audio
* BE-872	Generate video dash-mpeg file in offline meeting task
* BE-874	Support Accept-Ranges in the data presigned URL that returns mp3 audio
* BE-877	Make sure the redacted audio for meeting sessions is mp3
* BE-887	Modify POST /auth-svc/device to return QR code and also support new device type
* BE-891	Add long-term redaction settings to the Account API
* BE-892	Modify Meeting PERSON NER redaction to include speaker names
* BE-893	Add internal meeting recompute API that runs recompute on the entire account
* BE-904	Change how Context Regex and Account Regex are processed if both present
* BE-905	Automatically enable digit formatting if any redaction is turned on
* BE-912	Add fluentbit external helm chart to env-tracking
* BE-916	Create a cronjob to call internal meeting recompute API on the entire account
* BE-922	Update ingress and support basic-auth in influxdb helm chart
* BE-933	OfflineMeetingWordsGrouper in ml-svc to use timestamp to group words if punc is missing
* BE-937	Return raw transcription results if there is any error in formatter code
* BE-942	Validate model and language in offline requests before submitting to offline queue
* QA-458	Web Console: Add a button to delete a transcript under transcript beta.

Changes related to Integrity of Processing (fixes):
* QA-469	Transcribe App: Fix multiple translation issues
* QA-482	Transcribe App: Fix - Inactivity timout set on zero hrs and zero is showing out of the box, when toggle is disabled no value should show.
* QA-497  Transcribe App: Fix for accepting anything in tag, also taking space as tag.
* BE-870	Transcribe App: Fix - jumping to time in MP3 audio playback does not work
* BE-890	Transcribe App: Fix for being logged out when accessing Speakers page with many voice signatures
* BE-899	Transcribe App: Fix - Meeting audio redaction only works on the first 3 speakers in a meeting session
* BE-935	Transcribe App: Fixed - incorrectly imposing share limit on Edge
* BE-655	Fix for onprem-cluster-deployment task stuck when pods are in unexpected status
* BE-735	Fixed: Recompute does not reapply PII Redaction
* BE-895	Web Console: Fix - Regex redact options are saved but not displayed
* BE-907	Admin Tool: Fix - When I suspend some account it is my account that gets suspended
* BE-921	Fix: Dates with 'the'/'of' in the phrase don't get classified as DMY NER
* BE-928	Fix: Installer fails to apply settings to registry
* BE-936	Fixed - List index out of range error when formatting certain Spanish results
* BE-943	Fix weird output in case of multiple recompute with redaction and placeholder fill
* BE-950	Fix bug in Spanish formatter : int() argument must be a string, a bytes-like object or a number, not 'NoneType'

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Maintenance release 1.89.2 is scheduled for 9/10/2023 between 8pm and 10pm CST

Changes related to Integrity of Processing (fixes)
* BE-882  TWIML sessions not closed if no TWIML Stop message sent on websocket

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Maintenance release 1.89.1 is scheduled for 9/7/2023 between noon and 3pm CST

Changes related to Integrity of Processing (fixes)
* QA-477 Transcribe App: Sharing (public) a transcript and when try to play this transcript page refreshing all the time.
* QA-483 Transcribe App: Not able to play the old transcripts

Additions:
* BE-865  Add presigned url to response from GET /asr/meeting/shared/{shareId}/data

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.89.0 is scheduled for 9/5/2023 between 1pm and 6pm CST

New functionality in the Transcribe App:
* BE-168	Transcribe App: Add ability to upload a directory with Zoom meeting recordings
* BE-777  Transcribe App: Remove Project Transcripts page and show project transcripts on home page
* BE-837	Transcribe App: Use GET /asr/meeting/search API on the home page
* BE-845	Transcribe App: Show tags in full if just 1 or 2

New functionality in other platform components:
* BE-785	Demo App: Now running on Firefox
* BE-792	API: Allow audio data that is retrieved from url to use local settings similar to AuthConfig
* BE-800	Return "lang" in Get Meeting Data API
* BE-816	Web Console: Improve Contexts Card on the Context dash

Changes related to Integrity of Processing (fixes):
* BE-794	Transcribe App: Fixed Word Cloud in Spanish
* BE-799	Transcribe App: Fixed - summary and key items generated by recompute are always in English
* BE-809	Transcribe App: Fixed - Enabling full masking (*****) caused Meeting Minutes to not be generated
* BE-813	Transcribe App: Fixed - Wrong text shown if no Speakers shown on page
* QA-418	Transcribe App: Fixed - While creating new project "Profanity Masking" tabs are showing hidden at 100% screen resolution
* QA-426	Transcribe App: Fixed some missing German translations in the UI
* QA-444	Transcribe App: Fixed - User detail is missing on the delete confirmation pop up, In case user delete the account from edit user popup
* QA-448	Transcribe App: Fix - For multiple file uploads, no speakers show a difference even after selecting a range of speakers.

* BE-774	Fix: Incorrect MPEG-DASH mpd format file generated
* BE-786	Web Console: Fix color of buttons in Microphone Capture dialog
* BE-798	Fixed: GET /asr/meeting/search assumes fromAllContexts is always true
* BE-826	Web Console: Fixed - MRCP experiment page should be 100% wide
* BE-827	Automatically delete REX pods in Unknown and UnexpectedAdmissionError status
* BE-836	Fixed: /asr/meeting/search API should match all documents in textQuery parameter is missing
* QA-423	Web Console: Fixed - Add Context window closing when trying an add context with a name that already exist.
* QA-432	Web Console: Fixed in MRCP ASR - Create Grammar is not working and also the file format is not defined
* QA-433	Web Console: Fixed in MRCP ASR - On the experiment How to Upload video is not playing

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

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


**Backwards incompatibility:**
* Certain acoustic model names are no longer available. Unless using specific custom models, it is now sufficient to just provide `languages` parameter - no need to specify acoustic model by name.
* requests to `/asr/transcribe/async` API with `portal` field value but no `portal.label` specified will fail - `portal.label` is now a required value 



