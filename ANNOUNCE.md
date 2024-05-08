### Minor release 1.103.0 is scheduled for 5/7/2024 between 9:30pm and 11:30pm CDT

**Key changes related to the core APIs**
* Support for url rewrite and HTTP proxy for grammar fetching for /asr/recognize API and for MRCP ASR.

**Key changes related to Transcribe APP**
* LLM Playground for Edge Deployments - ask aLLM any questions about the transcript.

TBD...


### Minor release 1.102.0 is scheduled for 4/16/2024 between 6:00pm and 10:00pm CDT

**Key changes related to the core APIs**
* MRCP ASR now supports GARBAGE grammars (Nuance syntax)
* Removal of Prompt Manager in Web Console - not used due to popularity of TTS
* /sa/offline API is now available in beta - this is for Offline Transcription and Speech Analytics
* Telephony Bot API supports A/B testing using multiple logic URLs
* Improvements to accuracy of the whisper model

**Key changes related to Transcribe APP**
* Cloud version uses whisper:small for English (it already used whisper:medium for foreign languages)
* Generating just one Action Items table per entire transcript instead of one per Section.
* Fixed errors in PDF and DOCX generation for some meetings

New or changed functionality in the Transcribe App:
* BE-1595	TA: Improve the User Edit Dialog - project selection
* BE-1699	TA: Better message if there are no other users on the Project
* BE-1870	TA: Improve the User Delete dialog
* BE-1871	TA: Make the Avatar icons larger
* BE-1881	TA: Display Release Version in the app.
* BE-1893	TA: Upload Zoom files using POST/data/s3 API
* BE-1913	TA: Add option to copy session id to Clipboard
* BE-1936	TA: Add browser client info to login request
* BE-1975	TA Cloud: Enable whisper:small on English language
* QA-1036	TA: Show allowed characters when entering a tag
* QA-1041	TA: Added 365 days time limit for expiry of shared transcript.
* QA-1089	TA: Added sorting by email to Users table

New or changed functionality in other platform components:
* BE-1842	Web Console: Changes to API Security setting
* BE-1843	Web Console: Better text in Settings -> Speech Recognition
* BE-1844	Web Console: Hide Tools-> Prompt Manager menu option
* BE-1882	Web Console: Display Release Version in the app.
* BE-1896	Web Console: Switch Telephony Bot Call Audio+Transcript view from old /sa to new /sa/offline style
* BE-1928	Web Console: Add configuration for multiple URLs to AIVR App Settings
* BE-1929	Web Console: Add support for logic event in AIVR session
* BE-506	Support removing objects with multiple versions in Google Storage
* BE-857	Add `key-match` option to Query Terms in Advanced Search
* BE-858	Add `key` field to Query Term in Advanced Search
* BE-1150	Implement Offline SA Task in offline task project (Python)
* BE-1406	Improvements to prvention of SQL injection in the Advanced Meeting Search API
* BE-1514	Add to each of our API methods optional X-Request-ID header
* BE-1550	Freeswitch: discontinue using modified mod_shout file
* BE-1560	Update Freeswitch to use latest Debian 12
* BE-1579	Collect session_duration for realtime ASR sessions
* BE-1718	Implement POST /sa/offline/call/{callId}
* BE-1719	Implement POST /sa/call
* BE-1742	Mobile: Add extra parameter to /asr/transcribe/async request used in Microphone transcription
* BE-1788	Switch AIVR recording processing from /sa to /sa/offline
* BE-1789	AIVR to create /sa/call records if requested
* BE-1816	As of Redis version 6.2.0, ZRANGEBYSCORE is regarded as deprecated
* BE-1828	Add roles parameter to GET /user API method
* BE-1848	(Demo-Voicebot) Convert voicebot demo details view to use /sa/offline
* BE-1861	MRCP ASR: Add support for GARBAGE rule
* BE-1862	Add initialPrompt to POST /asr/transcribe/async
* BE-1867	For some internal APIs - ignore unknown fields, and not return 400 error, instead return X-Warning header
* BE-1883	SSO: Display Release Version in authentication-client app.
* BE-1884	Demo: Display Release Version in the app.
* BE-1888	Add X-Request-ID to all API requests from all Web Apps
* BE-1891	Support llm-svc rolling deployment -- websocket sessions
* BE-1903	Add version field to the AIVR session
* BE-1904	Store the GCP service account key in edge cluster document in firestore
* BE-1908	Add read-only offlineQueuePriority field to Account
* BE-1910	Support POST /auth-svc/zendesk/jwt
* BE-1912	Increase the size of concurrent websocket connections in asr-api
* BE-1914	Add Client Params to the login API
* BE-1919	Add numAudioChannels and numSpkChannels to POST /sa/call and GET
* BE-1927	Add support for multiple call-back URL in AIVR App
* BE-1940	Use default init prompt on Whisper if initPrompt is not set
* BE-1942	In Meeting API, generate action items from entire meeting transcript
* BE-1944	Add keySentencesByType to PUT /internal/asr/meeting/{meetingId}
* BE-1956	Admin Tool: Add support for login using 2FA
* BE-1959	Report license expiration time in edge-debugger
* BE-1983	Improve the efficiency of relation extraction algorithm for IVR Prompt NLU to support long input
* BE-2019   Modify sip settings of unimrcp server

Changes related to Integrity of Processing (fixes):
* BE-1585	TA: Inspect all cases of using "dangerouslySetInnerHTML"
* BE-1724	TA: Fix - SyntaxError: The string did not match the expected pattern, during fetchVersion in AppReloadModal
* BE-1725	TA: Fix - TypeError: Failed to fetch version.json
* BE-1727	TA: Fix - TypeError: c is not a function at handleDelete in components/ProjectsList/DeleteMultiSelectDialog
* BE-1835	TA: Fix - Try Again button has no effect after a failed upload
* BE-1841	TA: Fix - Unable to select audio files for upload on iPad
* BE-1857	TA: Fix - Generated Avatar not working ok for single user account where use has no avatar picture uploaded
* BE-1932	TA: Fix - Bad content security policy for GlitchTip
* BE-1937	TA: Fix - After logging in, the home page initially loads but then suddenly goes blank
* BE-1941	TA: Fix - TypeError: Cannot read properties of undefined (reading 'includes')
* BE-1945	TA: Fix - TypeError: Cannot read properties of undefined (reading 'value') on Settings page
* QA-1027	TA: Fix - Close Icon is missing on "Pair Voicegain Phone App" pop up
* QA-1031	TA: Fix - User is able to set value above 365 days on Archival Text Redaction.
* QA-1039	TA: Fix - User is able to set blank or invalid names as external speakers names.
* QA-1044	TA: Fix - bad link in the guide
* QA-1069   TA: Fix - Errors in PDF and DOCX generation for some meetings
* QA-1083	TA: Fix - Inconsistent Upload success message on upload page
* QA-1088	TA: Fix - Sorting indicators are broken for the Owned Projects and Shared Projects
* QA-1092	TA: Fix - Projects with same names getting automatically selected in Advanced Search project filter.
* QA-1093	TA: Fix - Player disappear when user clicks on anywhere near to the play button.
* QA-1100	TA: Fix - Assigning a role for invited user should be a must required filed.
* QA-1113	TA: Fix - Do not allow a tag with only underscores 
* QA-1114	TA: Fix back button from transcript opened from Advanced Search results
* QA-641	TA: Fix - Account Owner should be irremovable for any the project under Account Users.
* QA-800	TA: Improve behavior of resize on browser-share pop-up window
* BE-1703	Web Console: Fix - Wrong error message in GREG
* BE-1869	Web Console Edge: Fix - failed to decode request body: organization name \"api_test\" not found"
* BE-1872	Web Console: Fix - TypeError: Cannot read properties of undefined (reading 'ac')
* BE-1920	Web Console: Fix - Loss of filtering info in AIVR view
* BE-1943	Web Console: Fix - context switcher does not correctly support duplicate-named project
* BE-1962	Web Console: Fix -  Error on Edge management page (properties of undefined)
* QA-997	Web Console: Fix - Transcript is not getting skip by specified seconds as expected and onClick function is also not a function as in console tab.
* QA-1086	Web Console: Only CMP users may modify CMP permissions
* QA-1063	App Selector: Fix - Language selector should not be transparent.
* QA-1066	SA: Fix - User is unable to change profile photo
* BE-1478	Fix - Failed to execute 'decodeAudioData' on 'BaseAudioContext': Unable to decode audio data
* BE-1840	Fix - PUT /sa/call/review/answers/{crAnswersId} Spec and Implementation are different
* BE-1854	Fix - AIVR - prompt playback of audio from http url not working
* BE-1902	Fix - llm-svc does not handle SIGTERM properly
* BE-1907	Fix - uuid_vg_tap_ws at CLI not showing UUIDs to be started
* BE-1925	Fix - AIVR playback of audio from an HTTPs URL stops after 30 seconds
* BE-1999	Fix - Exception in case of many failed logins
* BE-926	Fix - EqTerm is not properly handled in meeting search for some fields

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Maintenance release 1.101.1 is scheduled for 4/4/2024 between 5:00pm and 7:00pm CDT

New or changed functionality:
* BE-1877: Enable VAD on Whisper
* BE-1886: Make node affinity configurable in offline-whisper
* BE-1889: Deploy whisper model to the edge cluster without internet connection
* BE-1938: Initial whisper prompt to ensure punctuation is generated  

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.101.0 is scheduled for 3/25/2024 between 6:00pm and 10:00pm CDT

IMPORTANT Note for Edge users: 
If you update from any prior release to 1.98.0 and you need to roll-back please contact Voicegain for support with the rollback process. 
This is because the compatibility setting on the Mongo DB has been changed in 1.97.0 and influxDB version has changed in 1.98.0

**Key changes related to the core APIs**
* Revised User deletion logic - will retain deleted User info so that any remaining references can be resolved.
* Added ability to enforce 2FA account-wide via a Web Console setting
* Connected Web Console to Sentry service for error tracking
* Improved session logs
* Websocket version of the Telephony Bot API
* Improved NLU model for understanding IVR prompts

**Key changes related to Transcribe APP**
* Improved User deletion logic functionality.
* Added LLM Settings to Account profile
* Action Items tables now correctly rendered in PDF and DOCX
* Upload audio data directly to storage without sending data through data API service
* Improved tables with lists of Shared transcripts (User and Admin view)


New or changed functionality in the Transcribe App:
* BE-1189	TA: Add option for Admins to see what others have shared
* BE-1271	TA: Support a workflow for the Admin to delete a user account and take over the user's project
* BE-1536	TA: Improved Splash page after login which shows the different stages
* BE-1646	TA: If there are no devices we show 2 options: download and phone app setup
* BE-1708	TA: On All Shares table, added sorting and filter on the Creator column, and filters on the Scope and Expires columns
* BE-1709	TA: In account users show Own Projects and Shared Projects columns in place of the current single Projects column
* BE-1713	TA: Modify the PDF output to render markdown tables
* BE-1714	TA: Modify the DOCX output to render markdown tables
* BE-1721	TA: Improved error message on the Zoom directory upload
* BE-1733	TA: Generate avatar based on user name if they have not uploaded a picture for avatar
* BE-1741	TA: Add extra parameter to /asr/transcribe/async request used in Microphone transcription
* BE-1744	TA: Upload files using the POST /data/s3 API
* BE-1807	TA: Add LLM Settings to Account profile
* BE-1810	TA: More functional user delete
* BE-1818	TA: Show info of users that have been deleted
* BE-1823	TA: Add Polish language transcription
* BE-1834	TA: Remove "Sync From Cloud" button
* QA-1009	TA: Increase max number of transcripts shown on home page from 100 to 250
* QA-1010	TA: Show the Upgrade button only to the Owner role
* QA-1017	TA: Better error message in case of an error resetting password
* QA-1021	TA: When user is deleted all user sessions will be invalidated.

New or changed functionality in other platform components:
* BE-1194	Advanced Search: Add new column `bucket` to the meeting_session table
* BE-1579	Collect session_duration for realtime ASR sessions
* BE-1663	Web Console: When deleting Users in the Cloud and if there are Edge deployments warn that also users on the Edge will be deleted
* BE-1687	Websocket version of AIVR API: support question.audioResponse.streaming
* BE-1693	Support Zoom Breakout Rooms in Meeting Join
* BE-1695	New /sa/call/search API
* BE-1697	New /sa/call/search/fields API
* BE-1691	Web Console: Add internal refresh to the page with Edge Deployment details
* BE-1705	Web Console: Add ability to enforce 2FA account-wide
* BE-1706	Add to Account API a field that controls 2FA enforcement
* BE-1707	Web Console: Better error message in case of creating a GREG experiment with duplicate name
* BE-1715	Support model_name measurement for offline sessions (offline transcribe, offline meeting, offline SA)
* BE-1716	Add session ID to all log messages in offline-task
* BE-1722	Web Console: Improved inactivity timeout processing
* BE-1728	Update code to use the latest Azure OpenAI Service preview API
* BE-1732	Web Console: Connect to Sentry
* BE-1739	Connect authentication-client to Sentry
* BE-1743	Add llmSettings to /cluster/ API
* BE-1809	Add deleteUserContexts parameter to DELETE /user
* BE-1817	New inclDeleted parameter on GET /user API method
* BE-1822	Support inclDeleted for GET /account/uuid/users
* BE-814	Improved NLU model for IVR prompts
* BE-978	Removed contextId and fromAllContexts parameters from the Advanced Meeting Search API method
* QA-1046	Demo: Improved error message in case of internal issues.

Changes related to Integrity of Processing (fixes):
* BE-1629	TA: Fix - It is impossible to share a project with an Owner of the account
* BE-1734	TA: Fix - Sorting of devices by date broken if any device is deleted
* BE-1802	TA: Fix - Search for creator by name in Advanced Search filter
* QA-1012	TA: Fix -  Project setting- Save button enabled when there is no change
* QA-1022	TA: Fix - In some rare cases Voice Signature page is showing white page.
* QA-887	TA: Fix - Walk through wizard should get automatically initiated when new user logs in for the first time.
* QA-929	TA: Fix -  Project (number) information is confusing
* QA-967	TA: Fix - User is able to add invalid keywords under project setting.
* BE-1672	Web Console: Fix - Sliders too small at console.ascalon.ai/specific/meetings
* QA-992	Web Console: Fix - User is able to play the audio when no voice is selected while creating a phone app.
* QA-993	Web Console: Fix - After clicking on view button of call session, it's showing blank page.
* QA-997	Web Console: Fix - Transcript is not getting skip by specified seconds as expected and onClick function is also not a function as in console tab.
* QA-999	Web Console: Fix - When User click on Cancel button of add context it should be close.
* BE-1735	Mobile App: Fix - order of projects in the list
* BE-1736	Mobile App: Fix - My project returns transcripts from other projects
* BE-1812	AIVR: Fix - getting MATCH but no recognized utterance
* BE-1831	ASR API: Fix - ValueError: Invalid value for `type` (), must be one of ['ner', 'regex']
* QA-1005	SA App: Fix - use the correct time format enum values

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


### Minor release 1.100.0 is scheduled for 3/4/2024 between 7:00pm and 10:00pm CST

IMPORTANT Note for Edge users: 
If you update from any prior release to 1.98.0 and you need to roll-back please contact Voicegain for support with the rollback process. 
This is because the compatibility setting on the Mongo DB has been changed in 1.97.0 and influxDB version has changed in 1.98.0

New functionality in the Transcribe App:
* BE-1559	TA: Automatically update the currently installed Zoom App version
* BE-1582	TA: Add "Mine | Shared | All" selector to the home page
* BE-1625	TA: Add a logout confirmation dialog.
* BE-1642	TA: Show avatars on Account Users table
* BE-1659	TA: Support action items using GPT for cloud Transcribe App
* BE-1665	TA: Support action items using custom LLM for Edge 
* BE-1669	TA: Advance Search  - Type filters populated dynamically from audio_src in fields api.
* BE-1671	TA: Hide the project settings for the Key Items

New functionality in other platform components:
* BE-1315	Move rexConfig from xml to properties file in Rex
* BE-1348	After password reset in AuthenticationClient provide link(s) to the correct App(s) for a given user
* BE-1527	Switch to yaml rex configuration file on K8s
* BE-1567	Web Console Edge: Add splash page after login and before home page shows up
* BE-1578	Changes to get app.voicegain.ai score A on https://securityheaders.com
* BE-1593	Web Console: Remove Clouds from ACP Header on Cloud
* BE-1628	Meeting Join API - add parameter to control which js script is run (zoom, teams, etc)
* BE-1638	Changes to the Voicebot Demo Instructions page
* BE-1648	Web Console: Disable old MRCP Experiment Analyze - the new will become the only one

Changes related to Integrity of Processing (fixes):
* BE-1596	TA: Fix - Zoom Device Approvals pop up on wrong accounts
* BE-1629	TA: Fix - It is impossible to share a project with an Owner of the account
* BE-1649	TA: Fix - When the delete button is clicked in advanced search, it triggers an incorrect API, leading to inaccurate transcript result, Furthermore, post-deletion, filtered and searched data fail to display accurately.
* BE-1652	TA: Fix - Reload button does not work on Firefox
* BE-1664	TA: Fix - deleting a project should also remove its meetings from databases
* BE-1702	TA: Fix - Advanced Search page goes blank with TypeError: Cannot read properties of undefined (reading 'split')
* QA-822	TA Edge: Fix - User (Role) is able to access Account settings.
* QA-853	TA: Fix - No options to select under "creator" filter in advanced search.
* QA-856	TA: Fix - Alert msg of "maximum allowed minutes exceeded" is not translating in other languages.
* QA-888	TA: Fix - In Advanced search deleted transcript are not getting removed from list, unless we refresh the page.
* QA-892	TA: Fix - partial Translation is there while uploading a file
* QA-903	TA: Fix - There should be proper translation on the share pop-up page.
* QA-913	TA: Fix - Walk through wizard gets hidden after few steps, when left menu is locked.
* QA-920	TA: Fix - For a single project, the move should be disabled 
* QA-931	TA: Fix - User is able to de-select all filters on home page for shared.
* QA-938	TA: Fix - Different loading screens when deleting a single share in compared to deleting multiple shares.
* QA-940	TA: Fix - User is unable to "generate " the JWT token.
* QA-944	TA: Fix - Owner should not be allowed to delete all of its project if any user have shared any project with him.
* QA-946	TA: Fix - Unable to Invite user after we edit a user in account section.
* QA-947	TA: Fix - Voicegain splash screen showing when project user adds other users to a project.
* QA-949	TA: Fix - Unable to close the dialog pop-up for added phrase.
* QA-950	TA: Fix - Project setting- save button overlaps with text when Spanish language is selected.
* QA-953	TA: Fix - Account with only user access can invite other account.
* QA-961	TA: Fix - While creating the first project(new project wizards) Word cloud toggle not showing properly.
* QA-962	TA: Fix - User with Admin role is not able to update address in profile section
* QA-963	TA: Fix - Language reminder- Close icon not showing properly cutting with boundary of the pop-up.
* QA-964	TA: Fix - During Signup user given company name and title, after login title missing under profile section
* QA-970	TA: Fix - Date filter is not working on advanced search page.
* QA-972	TA: Fix - Invited User is able to change "May Download" setting in account.
* QA-973	TA: Fix - Language filter under advanced search should show full language name
* QA-985	TA: Fix - Save button not working properly under profile setting.
* BE-1512	Fix - Occasionally k8s lost gpu and we need to restart nvidia-device-plugin-daemonset
* BE-1591	Web Console: Fix - Audio display in Meeting Detail page messed up
* BE-1641	Web Console: Fix - GREG is not showing recognition results
* BE-1644	Fix - Something wrong with keyword advanced search 
* BE-1650	Fix - accounts are getting revoked on QA even though the setting is 0 which means do not revoke
* BE-1654	Fix - Misleading error response of POST API asr/meeting/join
* BE-1668	Fix - Zoom Meeting join api cannot handle a case where the waiting room is disabled
* BE-1674	Fix -  NullPointerException from JoinedMeetingEvent
* BE-1675	Fix - NullPointerException is thrown from ascalon-cleanup
* QA-748	Demo: Fix - Double confirmation is required to browse audio file in the upload demo file
* QA-797	Web Console: Fix - On Websocket Details on live broadcasting getting the blank page
* QA-894	Web Console: Fix - Page is not responsive enough for the 90% zoom, all the pop-up are vibrating.
* QA-943	Web Console: Fix - Unable to set "Disable inactive users" as Not Enabled.
* QA-983	Web Console: Fix - After reset password- Web console button is not clickable

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.99.0 is scheduled for 2/13/2024 between 7:00pm and 10:00pm CST

IMPORTANT Note for Edge users: 
If you update from any prior release to 1.98.0 and you need to roll-back please contact Voicegain for support with the rollback process. 
This is because the compatibility setting on the Mongo DB has been changed in 1.97.0 and influxDB version has changed in 1.98.0

New functionality in the Transcribe App:
* BE-1258	TA: Add a filter on creator in Advanced Search
* BE-1472	TA: Better order of columns in the transcript table on home page
* BE-1532	TA: Record in clientSideProperties when a user downloads Zoom Meeting Assistant
* BE-1582	TA: Add "Mine | Shared | All" selector to the home page

New functionality in other platform components:
* BE-1300	Meeting Search API: new ctxSelect parameter with values "mine", "mineAndShared", "all"
* BE-1301	Meeting Search Fields API: new ctxSelect parameter with values "mine", "mineAndShared", "all"
* BE-1361	Support tempCode in the AIVR API
* BE-1408	Modify the Password Reset API to return login URLs for all the Apps for which the password works
* BE-1446	Return 400 Bad Request rather then 500 Internal Server Error if the query parameters in Meeting Search API are missing or invalid
* BE-1458	Web Console Edge: Add check for email relay and do not offer emailed OTP if that email relay is not configured
* BE-1488	Configure Edge to have GlitchTip
* BE-1499	Add API that Revokes a user and transfers all projects to the Admin or some other designated User
* BE-1517	Convert /sa/call API to use Postgres instead of Firestore to store data
* BE-1522	API to email link to the results of Voicebot Demo session
* BE-1524	Deploy GlitchTip using onprem-cluster-deployment
* BE-1526	Reduce silence padding of Azure TTS prompts to minimum
* BE-1533	Add persist setting to AIVR app API
* BE-1534	Web Console: Add persist setting for Telephony Bot App
* BE-1538	Hookup Demo App to Sentry
* BE-1541	Cache account data daily using the /recache api
* BE-1544	Web Console: Do not allow smaller than 30 days values of "Disable inactive users after days"
* BE-1545	Web Console: Add a close (x) to the notice about 2FA setup
* BE-1546	Web Console: Add a spinner when saving account settings
* BE-1565	For accounts that are INVOICE and do not have billingAccountId we should not submit anything to fusebill
* BE-1572	AIVR Callback API method to interrupt prompt being played
* BE-1575	Utility that copies all calls - reads using Firestore Calls DAO and writes using Postgres Calls DAO
* BE-1580	Add jingleUrl field to the AIVR App
* BE-1581	Web Console: Add ability to configure Jingle and percolator URLs in AIVR APP
* BE-1588	Add percolatorUrl field to the AIVR App API
* BE-1589	Use the AIVR App Jingle in Freeswitch script
* BE-1592	Web Console: Make it possible to disable the "Disable inactive users after days" feature
* BE-1594	Web Console: Make the Account Settings card pretty
* BE-1599	Demo: Support copy paste of the Code
* BE-1604	Demo: Change tooltips
* BE-1615	When creating Users using POST /user, if we exceed max users on account we should not return 500 code but 429

Changes related to Integrity of Processing (fixes):
* BE-1621	TA: Fix - User Profile Setting Save button stays permanently disabled after saving once
* BE-1629	TA: Fix - It is impossible to share a project with an Owner of the account
* QA-641	TA: Fix - Project Owner should be irremovable for any the project under Account Users.
* QA-760	TA: Fix - The re-upload menu again shows for the normal uploaded file, it should only show for the zoom uploaded file. 
* QA-822	TA Edge: Fix - User (Role) is able to access and edit Account settings.
* QA-843	TA: Fix - When the user tries to share the transcript as a public share and delete the transcript from the owner account, something went wrong error is showing when login in from the sign-in link on the share.
* QA-860	TA: Fix - Mouse hovering on error, message information should show
* QA-863	TA: Fix - "May Download" checkbox getting automatically disable after adding/removing a project for user (role).
* QA-875	TA: Fix - After processing URL upload blank space showing on home page.
* QA-881	TA: Fix - Clicking on the filter button on advanced search page, showing blank page.
* QA-885	TA: Fix - Voicegain splash screen showing even when deleting a transcript.
* QA-890	TA: Fix - Due to new languages added, profanity maskimg menu not showing properly on 100% zoom screen.
* QA-891	TA: Fix - In Profile deleted Shares are not getting removed, unless we refresh the page.
* QA-899	TA: Fix - Expired shared transcripts showing expiry date in negative.
* QA-906	TA: Fix - Various problems with saving edited user data from Account Settings
* QA-917	TA: Fix - Text-redaction and Archival Text-redaction crashes the app
* QA-922	TA: Fix - Blank page showing when user clicks in Profile on the "Archival text reduction".
* QA-923	TA: Fix - If no Download permission selected on user invite, getting wrong permission error
* QA-925	TA: Fix - Getting blank screen on Users page under account section.
* QA-932	TA: Fix - Voicegain splash screen showing when user save the mic capture recording.
* BE-1484	Web Console: Fix - On Live Transcribe: Websocket Delay resets to 0 upon page refresh
* BE-1485	Web Console: Fix - Misaligned UI on the Live Transcribe Websockets
* BE-1576	Web Console: Fix Content Security Policy to the cc app iFrame
* BE-1577	Web Console: Fix - /restricted/page API returns 500 Internal Server Error
* BE-1586	Web Console: Fix  - Wrong request to retrieve AIVR sessions
* BE-1603	Fix - Microphone demo needs to provide also completeTimeout
* BE-1624	Fix - User REVOKE can be undone by a user by doing a simple Password Reset
* QA-847	Web Console: Fix - After uploading a file, the label field should be automatically filled.
* QA-889	Web Console: Fix - Walk through wizard should get automatically initiated when new user logs in for the first time.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.98.0 is scheduled for 2/1/2024 between 4:00pm and 6:00pm CST

IMPORTANT Note for Edge users: 
If you update from any prior release to 1.98.0 and you need to roll-back please contact Voicegain for support with the rollback process. 
This is because the compatibility setting on the Mongo DB has been changed in 1.97.0 and influxDB version has changed in 1.98.0

New functionality in the Transcribe App:
* BE-1395	TA: Improvements on the Share dialog											
* BE-1494	TA: Add Splash page on login											
* BE-1507	TA: Support French, Dutch, Portuguese, Italian languages using the whisper:medium model (Cloud only)											
* BE-1508	TA: Hide the Key-Items configuration in settings of Projects with language other than English											

New functionality in other platform components:
* BE-1006	Collect lastConnectedEpoch time for device											
* BE-1226	Send logs and errors from Voicegain Flutter app to Sentry											
* BE-1358	Web Console: Inactive Users are disabled after 90 days of inactivity - add ability to set disableInactiveUsersDays value											
* BE-1365	Remove default sort by meeting_id from the GET and POST /asr/meeting/search											
* BE-1371	Extend default persistence of Telephony Bot calls to 42 days											
* BE-1380	In the SSO UI add ability to mark the browser safe (i.e. no longer requiring TOTP)											
* BE-1404	Add new field to account API - disableInactiveUsersDays											
* BE-1431	Support Influxdb V2 on Edge											
* BE-1438	Edge: Write sizes of minio and mongo backups as influxDb measurements											
* BE-1457	Web Console: Show time in the deployment history in the time zone of the browser and in a nicer format											
* BE-1460	Add a 'generic' joined meeting event and annotate the zoom meeting with such events for various steps performed											
* BE-1461	Add joinedMeetingEvents to the Meeting API poll method response											
* BE-1462	Modify login API to return information if emailing OTP is possible											
* BE-1470	Add image to the url/QR that is used in TOTP setup											
* BE-1474	Modify the existing login API to take secureBrowserToken											
* BE-1475	Implement internal API to write sizes of backups to influxDB											
* BE-1481	Web Console: Turn the nagging 2FA dialog to a message that auto disappears											
* BE-1482	Web Console: Improvements to the 2FA setup dialog											
* BE-1483	Modify the share APIs to track usage of shares											
* BE-1493	Show number of currently open MRCP and RTSP sessions in the unimrcp log											
* BE-1506	Web Console: Allow for selection of multiple languages plus base, small, and medium whisper model											
* BE-1513	Deploy prometheus to edge cluster using onprem-cluster-deployment task											
* BE-1516	Autoscaling Offline transcription on Edge deployed on GCP											
* BE-1522	API to email link to the results of Voicebot Demo session											
* BE-1523	Disable returning meeting topic generation for languages other than English and Spanish											
* BE-1525	Change max value of poll.persist to an equivalent of 365 days											
* BE-1551	Increase Project limit to 1000 and change the corresponding error from 500 to 429											
* BE-502	Modify User PUT API and add ability to add secureBrowserToken											
* BE-776	Upgrade unimrcp to 1.8.0											
* QA-563	Admin Tool: Remove Register page											

Changes related to Integrity of Processing (fixes):
* BE-1440	TA: Fix - Different Users not able to create Projects with the same name.											
* BE-1549	TA: Fix - For Zoom dir upload the size check should be performed only on files that actually are going to be uploaded											
* QA-723	TA: Fix - First time Login- All the links should be hyperlinked.											
* QA-760	TA: Fix - The re-upload menu again shows for the normal uploaded file, it should only show for the zoom uploaded file. 											
* QA-828	TA: Fix - New User First Login - Zoom App page is coming blank											
* QA-834	TA: Fix - Hint message is missing below Tag input field											
* QA-864	TA: Fix - Error after new login if the Project user used last has been deleted											
* QA-865	TA: Fixes in the speaker number range selection UI											
* QA-887	TA: Fix - Walk through wizard should get automatically initiated when new user logs in for the first time.											
* BE-1278	Fix - If no sort order in specified then the advanced text search results should be ordered by rank											
* BE-1334	Fix - results from the GET /asr/meeting/search API are not sorted by rank if no sorting is specified											
* BE-1436	Fix - Recognition doesn't work in AIVR sessions if influxDB is down											
* BE-1490	Fix - AIVR should start recognition only after the non-bargineable text prompt					
* BE-1563	Fix - Missing `<instance>` value in the result of `builtin:speech/transcribe` (and all lvoc "grammars")	
* QA-847	Web Console: Fix - After uploading a file, the label field should be automatically filled.											

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Maintenance release 1.97.3 is scheduled for 1/24/2023 between 3pm and 4pm CST

Updates:
* BE-1455   Upgrade cloud function runtime from python 3.7 to 3.9

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Maintenance release 1.97.2 is scheduled for 1/22/2023 between 10pm and 11pm CST

Changes related to Integrity of Processing (fixes):
* BE-1510   Fix - SnippetAnnotations is not working

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Maintenance release 1.97.1 is scheduled for 1/18/2023 between 3pm and 9pm CST

Changes related to Integrity of Processing (fixes):
* BE-1412 Fix - uhhuh recognition with low confidence messing up the flow (early barge-in) 
* BE-1443 Fix endpointing of low confidence recognitions in Telephony Bot API
* BE-1473 TA: Fix - NPE in Meeting Search if any account context does not have type set
* BE-1476 TA: Fix - Something Went Wrong page not loading correctly on Edge
* BE-1477 Fix - Invalid value: null error when retrieving transcript in Web Console
* BE-1479 TA: Fix - missingKey translation "Uploaded File" logged in a loop
* BE-1487 Web Console: Fix - Unable to sign-up without providing Company Name
* QA-858  Web Console: Fix - Showing no transcript when click on the view for any transcription. 
* QA-859  Demo: Fix - Getting white screen in demo when trying to upload a file or trying to do doing mic capture

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


### Minor release 1.93.0 is scheduled for 11/2/2023 between 9:00pm and 11:59pm CDT

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

### Minor release 1.92.0 is scheduled for 10/19/2023 between 4pm and 6pm CDT

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


