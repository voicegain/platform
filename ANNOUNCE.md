### Maintenance release 1.97.2 is scheduled for 1/18/2023 between 3pm and 9pm CST

Changes related to Integrity of Processing (fixes):
* BE-1443 Fix endpointing of low confidence recognitions in Telephony Bot API
* BE-1476 TA: Fix - Something Went Wrong page not loading correctly on Edge
* BE-1477 Fix - Invalid value: null error when retrieving transcript in Web Console
* QA-858  Web Console: Fix -Showing no transcript when click on the view for any transcription. 
* QA-859  Demo: Fix - Getting white screen in demo when trying to upload a file or trying to do doing mic capture

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Maintenance release 1.97.1 is scheduled for 1/17/2023 between 7pm and 8pm CST

Changes related to Integrity of Processing (fixes):
* BE-1473  Fix - NPE in Meeting Search if any account context does not have type set

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.97.0 is scheduled for 1/17/2024 between 1:00pm and 3:00pm CST

IMPORTANT Note for Edge users: If you update from any prior release to 1.97.0 and you need to roll-back please contact 
Voicegain for support with the rollback process. This is because the compatibility setting on the Mongo DB has been changed in 1.97.0.

New functionality in the Transcribe App:
* BE-1186	TA: Meeting search fields API returns intermediate values
* BE-1377	TA: In Advanced Search filters use the intermediate values returned from the fields API
* QA-421	TA: Improved inactivity timeout functionality
* QA-660	TA: Transcript caption popup window now is resizable in full-screen video player

New functionality in other platform components:
* BE-1249	Added logicConnectMethod field to AIVR App API
* BE-1353	Update Node version app-selector: 16.10.0 → 18
* BE-1355	Web Console: Show the SHA and description of the currently deployed Edge configuration
* BE-1356	Web Console: Show the history of deployed Edge configurations (incl SHA sums)
* BE-1359	Web Console: Make password expire time configurable
* BE-1360	Web Console: Make number of old remembered passwords configurable
* BE-1367	Migration from InfluxDB v1.8.10 to v2.7.x
* BE-1376	Add joinedMeetingEvent(s) field to the /asr/meeting API for meetings that were joined using meeting bot
* BE-1379	Web Console: Add ability to set logicConnectMethod for AIVR App
* BE-1397	In account API make number of old remembered passwords configurable
* BE-1398	In account API - new min, max, and default values of inactivityLogoutThreshold
* BE-1399	Add passwordExpirationDays to the Account API
* BE-1400	In MRCP, support defining large vocabulary grammar using buildin grammar in DEFINE-GRAMMAR request
* BE-1403	Web Console: Added option to control which Edge configurations will be shown
* BE-1405	Add deploymentHistory field to /cluster API
* BE-1422	A utility that creates user/org/bucket in InfluxDBv2 for each existing account in the db
* BE-1434	Support storing orgId and userId under account.influxDB
* BE-1435	Support hostAliases in offline task
* BE-1441	Support acoustic model with only model config file and a reference to another model
* BE-1442	Create a telephony bot specific acoustic model configuration in REX with new sensitivity setting
* BE-1444	Log any occurrence of "Something Went Wrong" page to Sentry
* BE-473	2FA for Web Console
* BE-503	Web Console: In the user profile add ability to configure 2FA
* BE-504	In Authentication Client modify login to handle cases if MFA is enabled for a user

Changes related to Integrity of Processing (fixes):
* BE-1252	TA: Fix - After Submit on Zoom Upload still staying on the same page
* BE-1383	TA: Fix - The User avatar is currently saved to the currently selected context - we need to save it to another bucket
* BE-1385	TA: Fix - Password reset link incorrect on some Edge deployments
* QA-509	TA: Fix - Incorrect behavior if User tries to use Share "within account" while not being logged in
* QA-594	TA: Fix - On uploading the zoom folder getting the status as error
* QA-703	TA: Fix - Shares is not showing under My Shares (on accounts with many transcripts)
* QA-709	TA: Fix - Filter by Phase/Status not working in advanced search.
* QA-756	TA: Fix - Zoom App Page is not loading for some new users
* QA-799	TA: Fix - For new users "Something went wrong" error page shown instead of a First Project Wizard
* QA-802	TA: Fix - Save button is not getting enabled after updating the settings.
* QA-809	TA: Fix - Advanced Search Filter is not working on Status Filter
* QA-811	TA: Fix - Advanced search: Searching for the error transcripts filter not working.
* QA-820	TA: In Advanced Search now able to enter duration manually (in addition to slider)
* QA-829	TA: Fix - For new User Search Page is coming blank
* QA-833	TA: Fix - After changing the profile picture "Hide Project Language Reminder" checkbox automatically gets unchecked.
* BE-1363	Fix - Hints with misspellings sometimes do not work correctly in real-time mode
* BE-1387	Fix - VAD classifies Beep as Speech
* BE-1389	Fix - Limit of 3 pending pairing devices should be per User and not per Account
* BE-1391	Fix - Edge data backup cronjob has wrong minio password
* BE-1401	Fix - Some vars are ignored in AIVR callback
* BE-1436	Fix - Recognition doesn't work in AIVR sessions if influxDB is down
* BE-1447	Fix - MaxAskExceedException in llm-svc is not captured
* QA-796	Web Console: Fix - Signup error message in XML format
* QA-823	Web Console: Fix - Ascending DNIS and ANI sorting not working for call sessions table.
* QA-824	Web Console: Fix - Delete functionality is not working Properly for 90% page zoom.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


### Minor release 1.96.0 is scheduled for 1/02/2024 between 8:30pm and 10:00pm CST

New functionality in the Transcribe App:
* BE-1158	TA: In Advanced Search show Headlines in the list of search results
* BE-1172	TA: Identify currently paired Zoom Meeting Assistant
* BE-1193	TA: In Advanced Search - Add filter on transcript language
* BE-1258	TA: Add a filter on creator in Advanced Search
* QA-350	TA: Upload button is now disabled when max allowed minutes are exceeded for the basic plan. 
* QA-671	TA: Revised search location of the Home page
* QA-726	TA: Voice signature status is shown in specific colors like green for "Ready" and blue for processing.
* QA-729	TA: Added special page for 500 errors
* QA-773	TA: Tags have their own specific alert message on Editing (Adding and Deleting).
* QA-778	TA: Improved login behavior if accessing a meeting shared within Account

New functionality in other platform components:
* BE-1084	AVIR: Added Telephony Bot Websocket API
* BE-1175	Upload large files via a pre-signed URL to S3 (including Google Storage in S3 mode)
* BE-1192	Support the new lang column in the GET fields method for search
* BE-1222	Add `intermediateValues` field to the GET /asr/meeting/search/fields API
* BE-1285	Add headline to response from the Advanced Meeting Search API
* BE-1325	Rewritten built-in grammars to avoid repeat when it's not in an <item> scope
* BE-1350	Update Node version for customer-portal: 14.21.3 -> 18
* BE-1351	Web Console: Comment out Language Model which is no longer needed for Audio Sending Daemon
* BE-1361	Support tempCode in the AIVR API
* BE-1362	Configure ingress for wss://host:port/n/ws/aivr/uuid/session/uuid
* BE-1381	In MRCP ASR - in Large Vocab Transcription return combination of 2 language recognition
* BE-1384	Web Console: Add filtering AIVR call sessions by App Name
* QA-779	Web Console: Better error messages if phone number not found
* QA-813	Web Console: Added TTML download option

Changes related to Integrity of Processing (fixes):
* BE-1333	TA: Fix - Mute/Unmute gets confused if we press the mute/unmute button too fast in a seqeunce several times
* BE-1336	TA: Fix - Refresh icon gets squished when we open search box
* QA-669	TA: Fix - Various issues on Advanced search feature
* QA-672	TA: Fix - Unable to choose the folder directory in Zoom upload
* QA-710	TA: Fix - Page behavior is unusual after URL upload.
* QA-718	TA: Fix -Search for transcript on the home page is not working if searching by transcript name
* QA-752	TA: Fix - Owner account should not show while creating a project and adding users to the project.
* QA-768	TA: Fix - Advanced search page is going blank.
* QA-770	TA: Fix - Filters are getting reset, when user open any transcript through advanced search.
* QA-772	TA: Fix - Load more button the Advance search not working properly it respond after 3 to 4 clicks
* QA-774	TA: Fix - Save button shouldn't get enable if inactivity timeout field is empty.
* QA-780	TA: Fix - Tags, Speakers, Participants filters associated with zoom upload are not searchable in Advanced search.
* QA-781	TA: Fix - Sometimes Word Cloud gets broken for some random transcripts.
* QA-782	TA: Fix - All 5 languages should be mentioned under language filter.
* QA-792	TA: Fix - "May Download" checkbox getting automatically enable after adding the project in user setting
* QA-794	TA: Fix - No error or alert msg on login page, when login with incorrect password.
* BE-1340	Multiple 3rd-party Vulnerabilities fixed
* BE-1342	Web Console: Fix - Error messages mixed up after purchasing a phone number
* BE-1349	Fix: asr-api doesn't have to check if a websocket exists for known topics
* BE-1370	Web Console: Fix - Right channel of the Telephony Bot recording is not getting shown
* QA-767	Web Console: Fix - Shortcut keys are not working properly.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.



### Maintenance release 1.95.1 is scheduled for 12/20/2023 between 1pm and 3pm CST

Changes:
* BE-1343  Add property builtin.grammar.output.flavor to dynamic grammar

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.95.0 is scheduled for 12/07/2023 between 3:00pm and 6:00pm CST

New functionality in the Transcribe App:
* BE-1255	TA: After new content is loaded by clicking "Load More" the page should scroll to the same place as before
* BE-1256	TA: Do not truncate meeting names if not needed
* BE-1274	TA: Check sizes of all Zoom folder files before starting upload and not during
* BE-1276	TA: Add our own controls over the small video window of Shaka Player
* QA-719	TA: Now, after search the page scrolls past "Get Started" and "Actions" to results
* QA-720	TA: Share link now does proper redirect back to the share link if login is required

New functionality in other platform components:
* BE-996	App Selector: Tweaks on the Signup page
* BE-1143	Upgrade from GCP container registry to artifact registry
* BE-1176	A method to stream words to ml-svc and get SA results
* BE-1197	Web Console: Show an error if phone number purchase fails
* BE-1209	Web Console: Show any error that occurs when creating a context
* BE-1233	Web Console: In edge deployments view make the number of rows per page configurable
* BE-1262	add /opt/voicegain/bin and /home/voicegain mounts to a k8s containe
* BE-1288	Support semicolons as query string separators in dynamic-grammar
* BE-1289	Support returning SWI_literal in dynamic-grammar
* BE-1290	Updated Grafana in edge deployment task
* BE-1291	Configure Sentry on Edge
* BE-1292	Create security policy for sentry.io on Transcribe App
* BE-1318	Web Console: Add more voices to AIVR App selection
* BE-1321	Deploy llm-svc to qa and prod
* BE-1323	Report llm-svc gpt cost for each session
* BE-1326	Support both builtin grammar:digits and grammar:digit

Changes related to Integrity of Processing (fixes):
* BE-1221	TA: Fix - Uncaught TypeError: Cannot read properties of null
* BE-1257	TA: Fix - For Duration the sorting toggle is placed weird
* BE-1259	TA: Fix - Keywords and tags displayed are missing spaces between them
* BE-1261	TA: Fix -Show correct color for each project in Project filter
* BE-1277	TA: Fix - Sometimes the Zoom Meeting Assistant page show stale value of the installed version
* BE-1299	TA: Fix - When searching for text in meetings on home page, the API request should not contain any sort parameters
* BE-1304	TA: Fix - POST /auth-svc/auth/login/openid fails if the User account exists but is only in the CREATED state
* BE-1313	TA: Fix - weird behavior of Project search
* BE-1314	TA: Fix - Weird logic for showing Move button on multiple selects
* BE-1317	TA: Fix - On Edge the option to add users to project is not visible to the Project Owner
* QA-651	TA: Fix - Date formats should not get translated in other languages.
* QA-657	TA: Fix - File submit fails if we change project after upload and before submit.
* QA-677	TA: Fix - Show current month in the right pane of the calendar
* QA-698	TA: Fix - Project search by name is not working properly.
* QA-699	TA: Fix - At the time save Transcript if we change the project then getting error
* QA-700	TA: Fix - User is able to update the email in update payment but updated mail is not showing after saved
* QA-701	TA: Fix - Add user- There should be words limit for entering the name
* QA-705	TA: Fix - Tag for the voice signature showing like a single word not showing any gap between them.
* QA-706	TA: Fix - Overlapping text in Download option when Spanish or German language is selected
* QA-716	TA: Fix - If the chat is long then White blank screen showing after the Video
* QA-717	TA: Fix - On large Chat video view -closed captioning, Video minimize buttons is not working
* QA-721	TA: Fix -  My Shares page stuck on loading after we Edit a share.
* QA-725	TA: Fix - User should only able to delete the voice signature by clicking on the delete icon.
* QA-727	TA: Fix - mouse hover on the Regenerate button showing in English when Hindi language is selected.
* QA-732	TA: Fix - There should be a limit for max allowed char for the project name.
* QA-733	TA: Fix - My shares table - tags should be separated.
* QA-735	TA: Fix - Restart when adding a new voice signature is not working properly.
* QA-736	TA: Fix - On the archival text reduction page, unable to save the updated time as the save button not enabled when changing days.
* QA-741	TA: Fix - On Advance search Project check box is not showing similar for all project
* QA-743	TA: Fix - On Changing the setting of "Start of the calendar week" from Sunday to Monday and vice versa getting the error of enter valid data
* QA-744	TA: Fix - Invited user is able to move the transcript of Admin project But the Admin is not able to move the transcribe to User project and also the error message is not showing on the Frontend
* QA-749	TA: Fix - Project creation page-users page is missing
* QA-753	TA: Fix - Re-Upload option is showing for Recording and Browser.
* QA-757	TA: Fix - On navigating back from the browser arrow from the large video mode then left menu disappear from the screen
* BE-1200	Admin Tool: Fix - Duplicated Search button label
* BE-1280	Fix - RexServerLauncher bean should start before all controllers
* BE-1296	Fix - Rate-limit cleanup cronjob is not created on CHD environment
* BE-1305	Fix - meta.<rule_name>.text should also include text in its reference rules
* BE-1316	Fix - audio-server fails to start on Edge
* BE-1319	Fix - audio-server fails to compute duration of down-sampled audio generated by maryTTS
* BE-1327	Fix - dtmf currency grammar doesn't work
* BE-1329	Fix - Missing Content-Length header in the response of GET /private/synthesis
* BE-716	Fix - Grafana image rendering in version 8
* QA-708	Web Console: Fix - Incorrect pop-up msg when updating company address in account settings.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


### Maintenance release 1.94.1 is scheduled for 11/28/2023 between noon and 2pm CST

Changes:
* BE-1282  Fix - offline task can't process 7.1 channel audio

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.94.0 is scheduled for 11/26/2023 between 6:00pm and 11:00pm CST

New functionality in the Transcribe App:
* BE-1054	TA: Avatar image can now be edited (cropped)
* BE-1104	TA: Better reporting of file size errors on upload (413 error)
* BE-1167	TA: Show Project settings only to Project owners and Admins
* BE-1168	TA: Add user Profile Setting: "Show advanced Project settings"
* BE-1170	TA: Any text redaction Settings (Account, Project) visible only to Account Owner and Admins
* BE-1171	TA: Menu actions in the Advanced Search results list work now the same as on the Home Page
* BE-1174	TA: Added "Re-upload" that opens Zoom Upload form
* BE-1190	TA: Show countdown on the modal that shows the QR code.
* BE-1196	TA: Prompt user to reload if there is a new version (also invalidate any open session)
* BE-1234	TA: Do not show Analytics settings on a Project unless user has enabled advanced settings
* BE-1236	TA: Upgrade to Node version 18
* BE-1254	TA: For Admins the "Show advanced Project settings" is now enabled by default
* BE-1264	TA: Added more logs around the login process
* QA-602	TA: Cleaned up the Inactivity Timeout setting
* QA-619	TA: Remove settings in Shaka Player
* QA-642	TA: Similar Date formats are now together in Settings under Account in Profile menu.

New functionality in other platform components:
* BE-984	Update helm to the latest version
* BE-1114	Move feature extraction to Triton to reduce CPU load in ASR 
* BE-1115	New Date Format enum for Account and Context
* BE-1127	Move from tfs to triton for VAD models
* BE-1144	Extract audio features using Triton
* BE-1191	Meeting search API: Add new field: LANG - to store the main language of the transcript
* BE-1203	End-to-end flow for meeting recorder using Puppeteer (Webex)
* BE-1213	Hardened core ASR when the model is not available
* BE-1219	Use UTF-8 encoding in telephony bot callback requests
* BE-1223	Web Console: Add column sorting on the phone management page plus variable page size
* BE-1224	Add debug meetingPlatform value to POST /asr/meeting/join
* BE-1240	Support prompt response in llm-svc (in addition to question, transfer, disconnect)
* BE-1246	Support custom mrcp configuration using helm chart
* QA-654	Demo: Show message confirming copy to clipboard


Changes related to Integrity of Processing (fixes):
* BE-875	TA: Fix -Warning about a too large file is not being shown
* BE-1105	TA: Fix - Submit button gets enabled too early while uploading zoom recording folders
* BE-1128	TA: Fix - "walkThroughWizardSeen" gets set to True even if user has not done the Wizard
* BE-1156	TA: Fix - In Advanced Search Filters should be remembered
* BE-1157	TA: Fix - In Advanced Search show Project icon as the first column
* BE-1169	TA: Fix - Show error message when hovering over the Error in Transcript list (was broken)
* BE-1180	TA: Fix - When SSO user gets logged out from TA they see normal login page for a few seconds
* BE-1182	TA: Fix - Weird behavior after clicking back button on detail page opened from Advanced search
* BE-1217	TA: Fix - Advanced Search API should return al the values if body is not passed.
* BE-1220	TA: Fix - Missing translations
* BE-1265	TA: Fix - First Project wizard not running is new user was invited to some projects
* BE-1269	TA: Fix - On a new account the My Shares page hangs forever with a spinner
* BE-1270	TA: Fix - GET /asr/meeting sharedBy returns meetings for a brand new user that has not shared anything
* BE-1272	TA: Fix - Getting incorrect error "cannot transcribe audio from video file" while uploading zoom folder
* BE-1273	TA: Fix - Checking for file size in Zoom Upload is broken (looks at files that will not be uploaded)
* QA-537	TA: Fix - Current Project is not picking correctly while move
* QA-613	TA: Fix - On uploading zoom folder- chat not uploaded correctly
* QA-643	TA: Fix - Search is not working on Homepage
* QA-644	TA: Fix - Do not show tag edit option in Shared transcripts
* QA-655	TA: Fix - Submit button shouldn't get enable until all selected files are uploaded.
* QA-670	TA: Fix - Right outline of the box is missing the speaker popup
* QA-674	TA: Fix - After deleting the project still showing name on homepage and setting icon, and clicking on setting no result showing.
* QA-686	TA: Fix - Project Invited user is able to access the project setting by URL
* QA-688	TA: Fix - Search user is not working on the Add User(s) to Project setting popup and its redirecting to the General Project Settings
* QA-695	TA: Fix - Advanced search button stays there on the page even after search collapsed.
* BE-1026	Fix - azure default voice amber doesn't work
* BE-1212	Fix - Telephony bot API does not support some symbols in Spanish
* BE-1227	Fix - In telephony bot API, we should send START-INPUT-TIMER request only after the prompt is played fully.
* BE-1229	Fix - In telephony bot, DTMF detection has very long delay
* BE-1239	Fix - Audio server does not support prompt with email address
* BE-1245	Fix - Bot logic does not get authToken in POST callback

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Maintenance release 1.93.1 is scheduled for 11/8/2023 between 9am and noon CST

Changes:
* BE-1207  Reject ASR requests if the default model doesn't support languages specified in requests. 

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


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

