## Release 1.111.0

This release prepares for upgrade to Mongo 6 in 1.112.0

New or changed functionality in other platform components:
* BE-3136	Copilot: Acknowledge all messages received via Pusher back to Voicegain.
* BE-3130	Copilot: Added "Mark Call Transferred" button.
* BE-3082	Implement mechanism to delete recordings from FreeSWITCH after they have been uploaded for processing
* BE-3135	Implement POST /public/aircall/user/message-ack
* BE-3086	Implemented trace field on the AIVR session.
* BE-3123	New API that can be invoked from Copilot that Agent can use to indicate transferred calls, so that Call Notes are generated and pushed.
* BE-3126	SA: Added the JWT token generation/management features as we have in Developer Web Console.
* QA-1847	SA: Agents should not be allowed to edit PII Redaction in settings.
* BE-2950	SA: Enhance the visibility of un-selectable rows for the user in both dark and light modes.
* BE-3068	SA: Improve tag entry/edit - show existing tags already used within project.
* BE-3125	SA: New SA project type - Generic Project
* BE-3078	SA: Showing DTMF words in a distinct way in the Call audio timeline view.
* BE-2863	Separate fav-icons for each product.
* QA-1914	Web Console: Made Business Configuration UI user-friendly, so that users can manually enter the start and closing times.

Changes related to Integrity of Processing (fixes):
* BE-3145	Fix - Hints with apostrophes should be allowed to be set on a context
* BE-3114	SA: Fix - App may get into a loop
* QA-1908	SA: Fix - Checkboxes are overlapping on advanced search filter pop-up.
* BE-3035	SA: Fix - Credit card numbers are not being masked out in spite of NER redaction being turned on
* QA-1787	SA: Fix - Demo calls are not generating for Demo projects.
* QA-1909	SA: Fix - DNIS search is not working on calls page.
* QA-1910	SA: Fix - Getting "Sorry, there was an error." when using DNIS search.
* QA-1822	SA: Fix - Password reset button were not responding.
* BE-3113	SA: Fix - Sentry Integration for SA app as source-maps are not working for recent events.
* QA-1809	SA: Fix - The agent created during the upload is not appearing on the Agents page.
* QA-1813	SA: Fix - The owner is unable to edit their first and last name on the user page.
* QA-1935	SA: Fix - The save button should stay disabled until changes are made on configuration page.
* QA-1778	SA: Fix - Unable to access Demo calls getting "Sorry, there was an error! We were unable to download the call audio.
* QA-1934	SA: Fix - Unable to edit project configuration name in settings.
* QA-1927	SA: Fix - User is able to access integration page for Generic projects through left menu.
* QA-1921	SA: Fix - When the keywords field is empty, it overlaps with 'Average Handle Time'.
* BE-2973	TA: Enhance the visibility of un-selectable rows (User table).
* QA-1917	TA: Fix - 'Continue' button shouldn't be enabled if project name is empty at first time login after signup. 
* QA-1901	TA: Fix - Delete Device text is not translated in German, Spanish and Hindi languages.
* QA-1912	TA: Fix - Getting error while meeting Bot joining Webex meetings, "failed to join the meeting" even when the bots are present in the meeting.
* QA-1906	TA: Fix - If a user tries to forget the meeting, the message 'The Bot is not in the meeting' should also be translated into languages other than English.
* QA-1886	TA: Fix - Showing something went wrong page for the account setting.
* QA-1913	Web Console: Fix - New User Wizard were not working properly.
* BE-3131	Web Console: Fix - Removed hardcoded sensitivity setting from mic capture.
* QA-1915	Web Console: Fix - When the user tries to explore the left menu for the telephone bot API, the business configuration text is overlapping and hidden.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.110.0

**Key changes related to the core APIs**
* Multiple improvements and fixes to the Speech Analytics App

**Key changes related to Transcribe APP**
* Improvements to the Webhook functionality
* UI improvements

New or changed functionality in the Transcribe App:
* BE-3075	TA: Added time-to-live (TTL) setting for the webhook JWT.
* BE-2983	TA: Check the Error Boundary implementation and catch all errors
* QA-1760	TA: Improved Profile page layout.
* QA-1721	TA: Provide way to identify Zoom, MS Teams or Webex meeting. 
* QA-1821	TA: Removed Edit Tag functionality for the shared transcript for both public and account share pages.
* QA-1851	TA: The password menu is available under the profile settings, so removed it from the "My Profile" menu.
* BE-2940	TA: Updated Transcribe App styles.


New or changed functionality in other platform components:
* BE-3074	Added jwtTTL parameter to Webhook API.
* BE-2966	Allow Managers to get results of advanced search POST /sa/call/search and GET /sa/call/search/fields
* BE-3101	Implement API to get all tags attached to /sa/calls in a given Context.
* BE-3086	Implemented trace field on the AIVR session.
* BE-2964	In the confGroup API throw Bad Request if someone tries to create a new confGroup without a name or with empty name.
* BE-2986	Made SpeechAnalyticsCallDao optional so that asr-api can start without it in CHD environment.
* BE-2978	Play audio while AIVR is making an outbound call triggered by warm-transfer.
* BE-3052	SA: Added "Resend Invite" in menu under account Users.
* BE-3039	SA: Added a cancel button in profile page.
* BE-3088	SA: Added dailyRepeatCalls to API - /sa/calls
* BE-3102	SA: Added filter for DNIS and a search for ANI.
* BE-3073	SA: Added hours:minutes to the date filter in Advanced Search.
* QA-1881	SA: In the login page, "Email Address" text is overlap on error message or pending approval message.
* QA-1854	SA: Introduced option to delete "Examples", "Keywords" and "Entity".
* BE-2938	SA: On Users table added filtering by Role.
* QA-1766	SA: The status filter should function like the role filter, using predefined values instead of working like email filter on the Users page.
* BE-3077	SA: Time-query to the back-end from the Advanced Search should use UTC.
* BE-2863	Separate fav-icons for each product.
* QA-1852	Web Console: Added maximum length limit validation for Business Configuration name.
* QA-1827	Web Console: Added pop-up/ alert message appears when edit a user in User Management.
* BE-2976	Web Console: In Phone number table, added a filter on Status column. 
* BE-2981	Web Console: In the AIVR App list, if the App has many phone numbers, then wrap them over multiple lines.
* BE-3049	Web Console: In the Call Sessions page, DNIS column is now sorted in ascending order.
* QA-1839	Web Console: Prevent Duplicate Shortcut Keys to Avoid Interference with Audio Playback.

Changes related to Integrity of Processing (fixes):
* QA-1768	Admin Portal: Fix - Special characters and numbers are accepted in the "First Name" field.
* BE-3096	Fix - Newly created Contexts from Web Console get type Transcription.
* BE-3093	Fix - Syntax error in tsquery
* BE-2944	Fix/Modify how we match names of meeting participants to the names obtained from Zoom API.
* QA-1765	SA: Fix - Agents and Manager are able to access Users and Time setting page via URL manipulation.
* QA-1802	SA: Fix - All demo calls are failing in processing and returning an error.
* QA-1739	SA: Fix - ANI and DNIS fields in upload file should not accept characters as inputs.
* QA-1840	SA: Fix - Call ID icon is overlapping with filter selector on Advanced search page.
* QA-1888	SA: Fix - Call Time Breakdown in Call Overview is not showing for uploaded call with single channel.
* QA-1855	SA: Fix - Calls tables column header and cell data are not aligned properly [1920 X 1080]
* QA-1873	SA: Fix - Color inconsistency in delete project modal.
* QA-1789	SA: Fix - Debug page is not clearly visible in Dark theme in call details.
* QA-1850	SA: Fix - Direction filter shows is not working properly.
* BE-3083	SA: Fix - Filter dates are reported in wrong format.
* QA-1804	SA: Fix - PII Redaction feature not working.
* BE-3100	SA: Fix - PII redaction in /sa/offline does not redact audio.
* QA-1849	SA: Fix - Resolution field column is missing from calls table.
* QA-1825	SA: Fix - The agent created during the upload is not appearing in the Agent filter on Advanced search page.
* QA-1880	SA: Fix - The country flag icons are not showing up in the ANI and DNIS fields during call uploads.
* BE-3095	SA: Fix - The date range component doesn't work in Chrome.
* QA-1857	SA: Fix - User should not be allowed to create two projects with same name.
* BE-3006	SA: Fix - Weird chars on the Calls list pagination.
* QA-1836	SA: Fix - Wrong pop-up msg on copying Voicebot ID.
* BE-3103	TA Edge: Fix -  Webhook page refresh is taking time and render page with no web-hook defined even there is existing web-hook.
* QA-1791	TA: Fix -  Cancel icon visibility is low in dark theme.
* QA-1846	TA: Fix - "Title" field should be editable for Admin account user in profile.
* QA-1780	TA: Fix - A type error page is showing on the advanced search page when the user tries to apply a filter.
* QA-1826	TA: Fix - advanced search - The selected start and end dates are not populated in the UI, but they appear when saved in Date filter.
* QA-1805	TA: Fix - Allowed domain settings are now visible for the Cloud version, whereas they were previously exclusive to Edge.
* QA-1819	TA: Fix - An "unexpected character" error is displayed during signup on Transcribe Cloud
* QA-1773	TA: Fix - An unexpected error page appears when a user tries to delete a device after changing its status to "Rejected."
* QA-1823	TA: Fix - Basic user should not be allowed to create share.
* BE-2994	TA: Fix - Does not allow entry of valid hints.
* QA-1812	TA: Fix - If the user is on the basic plan, the allowed email domain settings should not be displayed, as users on the basic plan cannot invite new users.
* QA-1845	TA: Fix - In Dark theme input field text is not visible.
* QA-1781	TA: Fix - Meeting Bot: If a user fails to join the meeting, they are unable to leave the meeting.
* QA-1783	TA: Fix - Missing "Allow signup with the domain" field
* QA-1833	TA: Fix - Partial translation when join a meeting by meeting bot.
* QA-1797	TA: Fix - PDF Download: The meeting details table should be properly sized to fit the screen.
* QA-1764	TA: Fix - Text was not translated based on selected language.
* QA-1883	TA: Fix - The 'Click here' hyperlink appears on the login page immediately after entering the email.
* QA-1856	TA: Fix - The user is able to add a Webhook without providing any details.
* BE-3104	TA: Fix - Webhook jwtTTL information weren't consistent.
* QA-1869	Web Console [Edge]: Fix - Showing Transcribe App projects as context on the customer portal and user can also delete the projects.
* QA-1700	Web Console: Fix - A vague error occurs when trying to upload files with long names.
* QA-1870	Web Console: Fix - Creating a new context and switching to the other context shows a type error page on the customer portal.
* QA-1859	Web Console: Fix - Creating a new context on the customer portal displays a type error and shows a blank page.
* QA-1853	Web Console: Fix - 'Open' and 'Close' time can't be same time of 'Normal Opening Hours' in Business Configuration.
* BE-2980	Web Console: Fix - Sorting of the Phone Numbers by App name does not work.
* QA-1897	Web Console: Fix - The Change Password page UI has layout and alignment issues.
* QA-1882	Web Console: Fix - User is unable to select a time for "Open time" if "Close time" is not set
* QA-1904	Web Console: Fix - When a user hover at billing label in header section, no cursor:pointer


All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


## Release 1.109.1

New or changed functionality in other platform components:
* BE-3088	Add dailyRepeatCalls to /sa/calls
* BE-3011	Add dtmfEvents field to /sa/call
* BE-2968	Add fallback in case of Azure TTS issues
* BE-2877	Added new variable in /sa/call that stores the type of transfer - Internal, Agency, None.
* BE-3087	Additional fields added to the Pusher messages to be sent to Copilot
* BE-2966	Allow Managers to get results of advanced search POST /sa/call/search and GET /sa/call/search/fields
* BE-3065	API for text redaction POST /text/redact
* BE-2961	API introduced to get Zoom Server API access_token.
* BE-1820	Ascalon-cleanup to support removing expired sa_offline sessions.
* BE-2957	At the end of the AIVR session, set language field of the /sa/call based on the language of the AIVR session.
* BE-2959	Copilot: If not logged in show message about need to login.
* BE-2974	Copilot: Implementation for updating co-pilot extension for Edge/Chrome browser. 
* BE-2985	Copilot: Improvements in settings page.
* BE-3016	If a call came from a provider then prepend to the GPT Call Notes the info about provider from Voicebot
* BE-3012	In /sa/offline obtained from /sa/call add DTMF values into the words returned
* BE-2958	In POST /sa/offline/call/{callId} use the language specified in /sa/call unless overridden by settings.asr
* BE-2944	Modify how we match names of meeting participants to the names obtained from Zoom API.
* BE-3015	New API method to modify sa call tags
* BE-2902	Poll URL returned from POST /asr/transcribe/async is a sticky url.
* BE-3010	Record DTMF detected in AIVR session
* BE-3023	SA: Add a direction column to call tables
* BE-3040	SA: Add Regex formatter to the PII Redaction settings
* BE-3064	SA: Add search functionality in Filters
* BE-2945	SA: Added ANI and DNIS to the Call table and Advanced Search table
* BE-2941	SA: Added callCenterCallId to /sa/call and set it from aivr session aircallId.
* BE-2956	SA: Added language field to /sa/call.
* QA-1730	SA: Added spinner when deleting admin user to show admin user is being deleted.
* BE-2936	SA: Added status of the Users in the Users Table.
* QA-1732	SA: Added user's role in the profile section.
* BE-3000	SA: Browser-specific text on the extension download page
* BE-3057	SA: Change the number of calls retrieved on the Calls page to max 1000
* BE-3022	SA: Consistent ANI/Dialed Number and CLI/DNIS naming
* BE-2939	SA: If no sentiment value is returned from the API we are showing "N/A" along with icon/emoji.
* QA-1751	SA: Improved design for Agents & Agents Detail page.
* BE-2954	SA: In Call Details added a Debug page that is visible to the Admins.
* BE-3070	SA: Increase the limit for number of calls in the Export query from 1000 to 2000
* QA-1752	SA: Made company details in profile read-only for Manager 
* BE-2962	SA: New design introduced for Agent pages.
* BE-3044	SA: Remember number of items per page setting till user modify.
* BE-2999	SA: Show callCenterCallId in the Call in Calls list
* BE-3013	SA: Show DTMF words in a distinct way in the Call transcript view
* BE-3014	SA: Show tags and allow adding new or editing existing ones
* BE-3027	SA: Show the next/prev buttons also on a call details page that is in processing right now
* BE-2652	Sync AIVR session with Aircall callId at transfer
* QA-1693	TA: If the number of speakers exceeds the expected amount, providing a scroll bar. This will not affect the transcript view.
* BE-3017	Web Console: Add a refresh button on the AIVR Call Session Details page
* BE-3004	Web Console: In AIVR session list, remove Version column, and add IVR Sid and FS UUID columns - both searchable
* BE-3048	Web Console: In the Call Sessions page, On the ANI column, instead of a Selection Filter we will have Search option.

Changes related to Integrity of Processing (fixes):
* QA-1734	Demo: Fix - For Long transcripts- text were overlapping with buttons.
* QA-1735	Demo: Fix - Typography issue on the demo healthcare call details page.
* BE-3043	Fix - Bad Event Bus configuration causing some events being dropped
* BE-3041	Fix - Did not report Queue and Agent in /sa/call
* BE-2991	Fix - Enforce non-empty name on Contexts in a correct way
* BE-3045	Fix - GET /aivr-app/uuid/jwt fails to return JWT tokens using authToken in some cases
* BE-2996	Fix - GET /asr/transcribe/uuid/transcript returns 500
* BE-2987	Fix - Glitch in business operating hours/days
* BE-3024	Fix - Issue with ascalon-asr-api starting on Edge deployment (specifically smopqa)
* BE-2780	Fix - netty.io Buffer leak in Java FreeSWITCH ESL library
* BE-3061	Fix - NPE when reading IvrSession.Recordings from Firestore
* BE-2943	Fix - NullPointerException in Aircall webhook
* BE-3058	Fix - Phone number formatter StringIndexOutOfBoundsException
* BE-3003	Fix - PII redaction does not work for /sa/offline transcript
* BE-3009	Fix - Real-time transcript possibly available too late for Call Notes
* BE-1366	Fix - RedisConnectionException: Issues with Redis Marshalling Codec
* BE-3020	Fix - Some Voicebot calls that get transferred end up in Disconnect instead of Hangup
* BE-3060	Fix - START-INPUT-TIMERS is sent to Rex right after RECOGNITION-COMPLETE is received
* BE-3050	Fix - The Users that we create when saving /sa/calls that have Agent data, do not have accountId
* BE-3066	Fix - Voicebot to Aircall call transfer handshake error.
* BE-2953	Fix - Voicegain call incorrectly matched to data from Aircall.
* QA-1784	SA: Fix - Admin account user is able to change Owner account user's role.
* BE-3047	SA: Fix - Advance search is not working for ANI/Dialed Number
* QA-1740	SA: Fix - After successfully deleting a user through the checkbox, another user gets selected. 
* QA-1761	SA: Fix - Agents and Manager should not delete project created by Admin.
* BE-3018	SA: Fix - Download from Advanced Search does not use the same max calls setting as the search
* BE-3037	SA: Fix - If we are using a 12 hour format we should show AM/PM in the time displayed
* BE-3046	SA: Fix - Need to access next/previous call transcript, if there is no call audio available.
* QA-1753	SA: Fix - No calls are showing on Advanced search page getting 500 (Internal Server Error).
* QA-1769	SA: Fix - Placeholder text does not disappear when the user enters data.
* QA-1831	SA: Fix - Sorting is not working for ANI and DNIS fields on Calls and Advanced search page.
* QA-1698	SA: Fix - The Call's Overview page is not responsive when zoomed in, causing text to overlap.
* QA-1706	SA: Fix - The Queue option in the file upload under Integration displays duplicate entries.
* BE-3076	SA: Fix - The search query in the Advanced Search Page should by default include sort by date so that most recent calls are retrieved first
* QA-1738	SA: Fix - Unable to delete multiple users when there are admin users among them.
* QA-1528	SA: Fix - When a user uploads a corrupted audio file, an error message repeatedly appears.
* QA-1157	TA Edge: Fix - For some audio URL showing something went wrong issue.
* QA-1800	TA Edge: Fix - Meeting Minutes missing
* BE-2951	TA Edge: Fix - Projects returned from the back-end are ignored. 
* QA-1723	TA: Fix - "Meeting Minutes" string  should not appear two times.
* QA-1708	TA: Fix - [Dark Theme] When the owner attempts to rename the transcript, the cancel icon is not visible.
* QA-1717	TA: Fix - After file uploading, the 'File uploaded' text weren't translated. 
* QA-1757	TA: Fix - Edit transcript icon overlapping with the transcripts name.
* QA-1701	TA: Fix - Hindi translation in "Delete Transcribe" pop-up.
* QA-1707	TA: Fix - Made Phrases visible for the dark theme.
* QA-1716	TA: Fix - Meeting Bot Placeholder text translation according to selected language.
* QA-1709	TA: Fix - No space between "Timezone" text and the dropdown box border.
* QA-1702	TA: Fix - Time zone pop-up was hiding the left menu.
* QA-1724	TA: Fix - When owner unable to join meeting bot receive "Failed to join meeting" string was not translated as per selected language.
* QA-1663	TA: Fix - When the Hindi language is selected, the 'Apply' button overlaps with the participants dropdown on the advanced search page.
* BE-2984	Web Console: Fix - Timezone prompt not taking spaces as input
* QA-1685	Web Console: Fix - When admin try to create "Add broadcast websocket" receive 400 bad request error.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.109.0

**Key changes related to the core APIs**
* Added Webhook API (phase 1)
* UI redesign for the Speech Analytics App
* Speech Analytics app now supports Warm Transfer scenario
* Copilot Browser Extension for Agent Assist

**Key changes related to Transcribe APP**
* Support Webhook API (phase 1)
* Added third set of LLM service settings and add model name field to all 3 LLM services.
* Including transcript metadata together with transcript when using LLM to generate meeting minutes items.
* Improved reliability of the Meeting Bot on longer meetings

New or changed functionality in the Transcribe App:
* BE-2798	TA: Added new LLM Prompts for Meeting Minutes.
* BE-2855	TA: Added third set of LLM service settings and add model name field to all 3 LLM services.
* BE-2805	TA: Added user's status column in users lists
* BE-2860	TA: Added Webhook settings page.
* BE-2857	TA: Addition to the LLM Prompts Settings.
* QA-849	TA: Consistent password complexity requirements.
* BE-2812	TA: Enforced LLM token limit.
* BE-2850	TA: Including transcript metadata together with transcript when using LLM to generate meeting minutes items.
* BE-2874	TA: Introduced fallback error page for Loading Chunk Issue.
* BE-2875	TA: Introduced fallback page for error boundary case.
* QA-1228	TA: Sorting given for users by name, for the Login all session table.

New or changed functionality in other platform components:
* BE-2856	Add Korean (ko) as one other possible value of switchLanguage in AIVR callback response.
* BE-1043	Add secure SIP and RTP to freeswitch.
* BE-2450	Added ability to obtain temporary JWT token from AIVR session using authToken
* BE-2891	Added metadata value to the speakers field in API /sa/offline
* BE-2714	Added new Group of items sent to Aircall as Caller Insight.
* BE-2843	Added originatingCallId and spawnedCalls to API - /sa/call
* BE-2819	Added processing status to API -  /sa/call
* BE-2226	Added Webhook Notification APIs.
* BE-2896	Adding in API - /sa/call an Agency tag, If AIVR inbound call is an Agency call (warm transfer bridged).
* QA-1633	Admin Tool: Updated Terms and Conditions page.
* BE-2832	API - /public/aircall/user-check used to check if user info matches data in Aircall.
* BE-2904	Copilot: Create a web interface to host the .crx download links
* BE-2884	Copilot: Implemented override of the Intent by Agent.
* BE-2861	Copilot: Implemented the Login.
* BE-2888	Copilot: Remove the dev/qa/prod selector and /dev/qa indicators.
* BE-2847	Copilot: Show Intent card with Agency Transfer data.
* BE-2876	Edge: If Action Items LLM prompt is not defined, then do not generate Action Items at all.
* BE-2897	For real-time transcription sending metadata over results websocket, also every time metadata is added/modified.
* BE-2886	Generate full call notes for the agency call that was bridged to the caller (not transferred to Aircall)
* BE-2826	Handling 2x2 audio channels from warm transfer call in API - /sa/offline.
* BE-2824	Improved design of Copilot.
* BE-2825	In AIVR session allowing for caller id to be any of the secondary phone numbers attached to the AIVR App.
* BE-2889	Included aivr_authToken and aivr_sessionId variables when pushing the AIVR Voicebot variables to the Copilot.
* BE-2787	INVALID_ARGUMENT: Sample rate must be empty or 24khz for this voice.
* BE-2929	Log the response payload from the Zoom API method that gets info about Zoom Meeting participants
* BE-2320	Make AIVR Sessions expire (use expiry period from AIVR App)
* BE-2928	Make sure that all calls in SA Demo project have progressPhase=DONE
* BE-2775	make sure that user deletion does not fail if context deletion takes too much time
* BE-2854	Modifications to llmSettings field (introduced premiumLlmService) on the onPrem cluster API.
* BE-2710	New version of the Sidepanel (Copilot Browser Extension) that integrates with Aircall.
* BE-2892	Populate speaker metadata in API - /sa/offline/call/{callId}
* BE-2844	POST /sa/offline/call/{callId} need to be able handle calls with spawnedCalls (from warm transfer).
* BE-1366	RedisConnectionException: Unable to init enough connections amount! Only 0 of 24 were initialized. 
* BE-2829	Return 400 Bad Request if someone tries to create a new AIVR App or assign a phone to existing App if the phone is not available.
* QA-1695	SA : Highlighting any calls that had error in processing
* BE-2885	SA: Added a Export button for the Advanced Search Results.
* QA-1623	SA: Added limit of 1024 characters against description under General settings. 
* BE-1796	SA: App should be customisable per account.
* BE-2808	SA: Enabled currency formatting for /sa/offline in AIVR sessions.
* QA-1587	SA: Enhancement - Downloaded call transcript should have Call ID as name instead of timestamp.
* BE-2933	SA: For call overview, render in processing page rather error page if call is in progress.
* BE-2704	SA: For the call sessions that are being processed, adding a subtle overlay that says processing
* QA-1695	SA: Highlighting any calls that had error in processing
* QA-1533	SA: Optimized call page & made fields small enough to fit all data without scrolling.
* QA-1690	SA: Provide correct information for Aircall Integration
* BE-2818	SA: Redesign of Speech Analytics App UI
* BE-2916	SA: Show first and last name in the user table
* BE-2862	SA: Showing more than 2 channels in the SA Call Detail view if present.
* BE-2907	SA: UI changes to implement the new design
* BE-2879	Setting ANI correctly on calls coming from AIVR Voicebot to Aircall.
* BE-2881	Submitting tags to Aircall when doing the call handshake between AIVR and Aircall.
* BE-2728	support auto-reconnect if fssk loses connection to Freeswitch
* BE-2836	Supporting Korean Prompt in telephony bot and in audio server.
* BE-2883	Taking the Voicebot intent and insert it into /sa/offline and /sa/call.
* BE-2880	Updated Advanced Search API - /sa/call/search  to return results in CSV format.
* BE-2859	Use premium LLM Service with the new LLM Query logic and use standard with the old LLM Query logic.
* QA-1536	Web Console: Added popup after adding or deleting a user under User management.
* QA-1540	Web Console: Added popup for deleting a WebSocket under Live Broadcasting.
* BE-2001	Web Console: Notify about inability to to microphone capture on HTTP urls.
* BE-2830	Web Console: Remember last items per page setting on the Call Sessions page.
* BE-2831	Web Console: Remember the last value of items-per-page setting on the Phone Apps page.

Changes related to Integrity of Processing (fixes):
* QA-1635	TA: Fix - "MINE/SHARED/ALL" option should not be visible to Basic account on LLM Query page.
* QA-1225	TA: Fix - Clicking on backward icon of any transcript results in value of time getting negative.
* QA-1665	TA: Fix - Clicking on microphone capture save recording page showing, it should show the start recording pop-up page.
* BE-2842	TA: Fix - Dialog to reset password.
* QA-1485	TA: Fix - Error page when opening rediarized transcript (partial fix)
* BE-2906	TA: Fix - error when searching for a phrase with an apostrophe 
* QA-1604	TA: Fix - Footer of Document should not overlap with transcript in downloaded PDF.
* QA-1689	TA: Fix - For longer meetings, after it ends, the transcript isn't processing properly.
* BE-2900	TA: Fix - If a Zoom meeting is long and is eventually ended by the host the bot does not notice that meeting has ended.
* QA-1605	TA: Fix - In share meeting pop -up , month name is not translating and always show in default language.
* QA-1497	TA: Fix - Invalid date and year showing for the last active under account users.
* QA-1672	TA: Fix - LLM Query not working and returning 500 error (Internal Server Error).
* QA-1718	TA: Fix - Meeting bot icon should also show as disabled when the maximum allowed minutes limit is exceeded.
* QA-1490	TA: Fix - Meeting Bot were unable to join Webex meeting.
* BE-2845	TA: Fix - Meeting platform selection tiles were too indistinct.
* QA-1677	TA: Fix - Some old transcripts still showing the queued status and user can not delete or remove them.
* BE-2195	TA: Fix - Stuck on login.
* QA-1662	TA: Fix - The error message should be displayed in the selected language after the maximum allowed minutes have been exceeded.
* QA-1667	TA: Fix - The walkthrough wizard is not functioning properly for new users.
* QA-1600	TA: Fix - Unable to join the webex meeting by meeting bot.
* BE-2834	TA: Fix - Unexpected Application Error! Loading chunk failed.
* QA-1609	TA: Fix - Voicegain logo is not fully visible in the 100% zoom.
* QA-1668	TA: Fix - When a user selects more than 12 speakers, the submit button becomes disabled however we have limit for 20 speakers.
* QA-1560	TA: Fix - When user try to invite user, it shows an invalid email address error but when user re-click on the save button it showing "User already exists".
* BE-2809	Fix - Bad currency formatting for thousands plus
* BE-2722	Fix - Bot logic doesn't get input callback if the caller hangup immediately after saying something.
* BE-2436	Fix - In meeting Join if the pod/puppeteer leaves the meeting because it is not progressing there is no info about that event
* BE-2814	Fix - MS-Teams puppet bot were not terminating if the meeting gets ended.
* BE-1354	Fix - NatsEndpoint fails to reconnect to NATS when its connection is lost
* BE-2869	Fix - Not working error prompt in telephony-bot LUA
* BE-2927	Fix - Pusher sending DNIS instead of the ANI
* BE-2663	Fix - Several calls where the merged meeting audio is missing a speaker.
* BE-2923	Fix Demo Prod
* BE-2913	SA: Fix - Agent and Caller labels are incorrect
* BE-2918	SA: Fix - Call Transcript page failing in case of single speakers
* QA-1699	SA: Fix - Exports in advanced search is not working with filters.
* QA-1686	SA: Fix - Getting error on Call's Transcript page.
* QA-1733	SA: Fix - Issues when Agent/Manager user try to edit/delete Admin user.
* BE-2915	SA: Fix - New User Dialog starts with values of the previously created user
* BE-2917	SA: Fix - Save button not activated for all values on Profile page
* QA-1729	SA: Fix - Selected duration is not shown in applied filters in advanced search page.
* BE-2898	SA: Fix - Spinning forever if the /sa/call has no saSesisonId.
* BE-2898	SA: Fix - Spinning forever if the /sa/call has no saSesisonId.
* QA-1719	SA: Fix - The added user role changes to "User" even if a different role was assigned while inviting.
* QA-1725	SA: Fix - The calls continue to load and display an error icon when hovered over, but the call itself is still accessible.
* QA-1622	SA: Fix - Timestamp interval dropdown have values that are more than transcript runtime.
* BE-2914	SA: Fix - Unable to add Admin Users
* QA-1710	SA: Fix - Unable to edit role of user under Profile users.
* BE-2926	SA: Fix - User Edit dialog has just First Name and it does not even populate it
* QA-1596	SA: Fix - User is unable to modify AIVR app getting "400 Bad Request".
* QA-1687	SA: Fix - User is unable to upload file under Integration section.
* QA-1528	SA: Fix - When a user uploads a corrupted audio file, an error message repeatedly appears.
* QA-1535	Web Console: Fix - Audio URL field box is too small.
* QA-1625	Web Console: Fix - For Phone Management, clickable area is too small. 
* QA-1571	Web Console: Fix - Logs - When a user tries to filter logs, filter not working.
* BE-2908	Web Console: Fix - Phone number deletion from AIVR App does not work
* BE-2813	Web Console: Fix - Playback timeline cut off after the last word.
* QA-1509	Web Console: Fix - 'Speed and Audio' control panels should be in proper size.
* QA-1392	Web Console: Fix - When we click the back button more than once, the time interval goes to minus and after that the video pauses.


All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.108.0

**Key changes related to the core APIs**
* More accurate offline transcription model
  * Removed artifacts from training data
  * Added additional Call Center data to training set
* Finalized warm transfer support in Telephony Bot API
* Support for pushing Voicebot data and Call Notes to Copilot

**Key changes related to Transcribe APP**
* Cloud only: Major improvement to capabilities of LLM Query
* Major makeover of the look of the UI
* Added UI dark mode
* Added Configurable Meeting Minutes (via LLM prompt)
* Added tracking of LLM tokens (in the Cloud)
* On Edge: Added ability to retrieve speaker data (incl. email) using Zoom API


New or changed functionality in the Transcribe App:
* BE-2798	TA: Added new LLM Prompts for Meeting Minutes
* BE-2811	TA: Added Purple project color (instead of black).
* QA-1003	TA: Add option to rename transcripts.
* BE-2668	TA: Change Key Items to Meeting Minutes : Add more categories in addition to Action Items
* BE-2762	TA: Change naming from Key Items to Meeting Minutes.
* BE-2786	TA: Changed border radius on avatars.
* BE-2718	TA: Dark mode is enabled for transcribe app.
* BE-2763	TA: On LLM Settings have two tabs - one for Prompts and one for Services
* BE-2797	TA: Post signup to Transcribe App, sending signup email.  
* QA-1515	TA: Show creator avatar on the transcript detail page
* BE-2781	TA: Show usage of LLM Tokens
* BE-2789	TA: Showing email icon next to the speaker/participant if there it an email field for that speaker/participant.
* BE-2810	TA: Switch Black Project color to Purple (for dark mode)
* BE-2329	TA: Track LLM token use in Transcribe App Cloud
* BE-2739	TA: Tracking used time on Transcribe App.
* BE-2791	TA: Update look and feel of transcribe app

New or changed functionality in other platform components:
* BE-2758	Add codec restrictions to the dial string for outbound
* BE-2045	Add to AIVR API subReturn action.
* BE-1782	Added Copilot Call Notes support.
* BE-2777	Added info about LLM tokens to GET account new-billing method.
* BE-2698	Added information regarding Member being Verified to the Call Notes
* BE-2695	Added realTimeTranscriptText to AIVR Session and store the transcript from real-time transcription in it.
* BE-1757	Added required features for Inbound Bot.
* BE-2821	Added secondary voice connector id to AIVR App api.
* BE-2768	Added speaker email value in the meeting data (ASR Meeting API)
* BE-2404	Added support for language switching in telephony bot.
* BE-1761	Added to AIVR API warmTransfer action.
* BE-2767	Added to Edge Configuration parameters for connecting to Zoom Service.
* QA-1319	Admin Tool: Added email validation on add account page.
* BE-2657	Admin Tool: Convert API Use chart to chart-js
* BE-2114	Check if we are within phone number quota on AWS before creating a new one
* BE-2749	Check Voice Connector number against quota before creating a new one.
* BE-2765	Demo: Collect events to Matomo from the voicebot part of the demo
* BE-2761	For confGroups of type other than Transcription do not delete them if the creator is deleted
* BE-2726	Get available information about participants of the specified Zoom meeting.
* BE-2776	Grouping segments by meeting and attaching meeting metadata for /asr/meeting/llm/query
* BE-2712	If the rex sessions are stuck (in error) do not count them towards the live session count during shutdown
* BE-2759	If user deletion fails for any reason, we should still audit log it.
* BE-2737	In AIVR, send vg::sub-return Event to Lua script (Freeswitch)
* BE-2799	Introduced wew llmSettings.prompts for Meeting minutes.
* BE-2733	Push data from Aircall Integration to the Copilot.
* BE-2754	SA: Add extra confirmation before deleting a user who has the Admin role.
* BE-2678	SA: Added API - GET /sa/offline/{id}/transcript 
* BE-2713	SA: Added context to the return values from GET /sa/call/agent
* BE-2703	SA: Added contextId to the request for /sa/call
* BE-2677	SA: Added download ability to the transcript view.
* QA-1427	SA: Added search feature to transcript page.
* BE-2689	SA: Addedd contextId to the GET /sa/call/{callId}
* QA-1534	SA: New project gets default time settings from the Account.
* BE-2774	SA: Supporting accounts with INVOICE billing on first login.
* BE-2697	SA: When submitting /sa/offline request to as part of SA AIVR Integration set correct formatting parameters.
* BE-2572	Send Caller Insight to Aircall as part of handling call.created webhook
* BE-2790	Set the non-Speaker email value in the meeting data.
* BE-2670	Transcribe App Client can get notified over websocket of any meeting join events instantaneously.
* BE-2732	Using Pusher to push information to the Copilot Browser Extension.
* BE-2736	Web Console: Added editable description to Edge Cluster
* BE-2622	Web Console: AIVR Sessions table show which sessions have SA integration.
* BE-2755	Web Console: Do not allow spaces in the names of AIVR Apps.
* BE-2696	Web Console: Show real-time transcript text in the AIVR session detail view
* BE-2747	Web Console: Showing AIVR App Id on the AIVR App detail drawer.
* QA-1472	Web Console: Unable to add second URL in logic when its name is same as first.

Changes related to Integrity of Processing (fixes):
* BE-2822	Fix - Can't play audio from URL in bot logic callback
* BE-2741	Fix - Duplicate data in meeting_vector database on Edge
* BE-2727	Fix - Error when leaving a meeting (meeting join API).
* BE-2721	Fix - Large vocabulary BUILT-IN grammar is not working in telephony bot
* BE-2760	Fix - Origination data is not properly set for a new Voice Connector.
* BE-2753	Fix - Outbound calling does not work anymore.
* BE-2204	Fix - Percolator stop request ignored if sent immediately after start
* BE-2806	Fix - The hidden checkbox stops working on ascalon TranscribeApp in some cases
* BE-2817	Fix - Voice Connector quota check is not working OK
* BE-2752	Fix - voiceConnectorId is not set on AIVR App if a phone gets added to AIVR App that did not have any phone
* BE-2700	Fix - Weird Agent Composite values for the Demo Project /sa/calls
* BE-2766	Fix prompt for Action Items.
* BE-2729	Fix the shutdown of ascalon-asr-api
* BE-2773	SA: Fix - Clicking on Terms of Service during SA Signup messes up signup
* BE-2550	SA: Fix - Incorrect default time in file upload.
* BE-2595	SA: Fix - JWT is not automatically inserted into the selected AIVR App.
* QA-1475	SA: Fix - Pagination on Users page looks weird.
* QA-1531	SA: Fix - Queue filter in Advanced search is not working for Uploaded file.
* QA-1474	SA: Fix - Score filter is still available in advanced search even when score has been removed.
* QA-1373	SA: Fix - The Continue button should remain disabled until all mandatory fields have been filled out.
* QA-1541	SA: Fix - The login button should remain disabled until all required fields are filled.
* QA-1437	SA: Fix - The role "Coach" is displayed as "QA" after being saved in Users.
* QA-1480	SA: Fix - Unable to clear the description in General settings.
* BE-2701	SA: Fix - undefined:undefined on the Topic chart
* QA-1476	SA: Fix - User deletion is not working properly.
* QA-1467	SA: Fix - User is able to set Persistence time more than 365 days in AIVR app.
* QA-1446	SA: Fix - When a user goes back, they are redirected to the calls page instead of the Advanced Search.
* BE-2699	SA: Fix - When I add a new keyword the dialog opens prepopulated with the name of the previous keyword I created
* QA-1525	TA: Fix - Accepting only digits in the domain name for the "Allow signup with emails from the following domains:" field.
* QA-1443	TA: Fix - Error message is wrong for the password reset page.
* QA-1638	TA: Fix - Getting 500 server error when Users use Special characters in search bar on Advanced search page.
* BE-1388	TA: Fix - Getting identical values of confidence when running transcript/{session-id} REAL-TIME
* QA-1493	TA: Fix - HTML element showing in overview section on production.
* QA-1613	TA: Fix - In Advance search Filter, tag is not working.
* BE-2756	TA: Fix - List of transcripts on Home page loads twice
* QA-1511	TA: Fix - LLM prompt box on transcript should not be available for shares.
* QA-910	TA: Fix - Search by numbers is not working properly.
* QA-1454	TA: Fix - Text "Undefined" populate when user left blank while signup
* QA-1593	TA: Fix - The Advanced Search functionality breaking on searching more than one word.
* QA-1461	TA: Fix - There should be a limit for the expiry time limit for shared transcript.
* QA-1481	TA: Fix - There should be warning Dialog when user click on Back Button or Close Browser
* BE-2330	TA: Fix - Transcribe is showing one-line per word.
* QA-1636	TA: Fix - Unable to check the creator on the advanced search filter.
* QA-1462	TA: Fix - Walk through wizard breaks when user switch language between walkthroughs.
* QA-764	TA: Fix - When a whole sentence entered in search box, it is not working and overlapping with close icon.
* BE-2828	Web Console: Fix - AIVR App creation allows you to pick phone numbers that are not yet ready for use.
* QA-1425	Web Console: Fix - Double error showing when phone number purchase.
* BE-2716	Web Console: Fix - Error page when trying to open AIVR session details.
* QA-1513	Web Console: Fix - Transcript play time exceeds than actual time when playback speed increases.
* QA-1575	Web Console: Fix - User is unable to Logout properly.
* QA-1483	Web Console: Fix - User Management Search - When user searches with leading or trailing whitespace with email then no results come.
* QA-1526	Web Console: Fix - When user switch context on Profile page then 2FA pop-up keeps showing each time context is changed.



## Release 1.107.0

**Key changes related to the core APIs**
* Changes in AIVR API to support Aircall integration
* Changes in AIVR API to support multiple languages
* Agents and Queues now correctly handles in SA APIs and SA App
* Improved Advanced Search in SA App
* Ability to use single session on websocket receiving server for both left and right transcription channels.
* Ability to add external UUID to any transcription session
* Full HA setups for FreeSWITCH and Kamailio

**Key changes related to Transcribe APP**
* Meeting metadata used in LLM Playground
* LLM Query uses history of previous Q and As
* More detail for the relevant meeting display in LLM Query
* Enhancements to text file download

New or changed functionality in the Transcribe App:
* BE-2633	TA: Add metadata information to LLM Playground query
* BE-2724	TA: Add option to include header in the downloaded text file
* BE-2651	TA: Add Project information to the relevant-meeting list in LLM Query page
* BE-2687	TA: API Key entry boxes should be set to not remember history
* BE-2634	TA: For text transcript download, add configurable transcript timestamp
* BE-2725	TA: Improve the rules to show the speakers and non-speaking participants
* BE-2577	TA: Indicate the relevance of the relevantMeetings returned from /asr/meeting/llm/query
* BE-2717	TA: Make sure that the transcript submitted to LLM Playground has timestamps (interval parameter)
* BE-2601	TA: Remember sorting on home page when returning to it from open meeting details
* BE-2589	TA: Replace HighCharts WordCloud with another library
* BE-2570	TA: Show the scope of the LLM query in the Answer

New or changed functionality in other platform components:
* BE-2673	Web Console Add search by email to user management page
* BE-2617	Web Console: Add 3 new Aircall parameters to the AIVR App settings
* BE-2605	Web Console: Add language to the logic settings on the AIVR App
* BE-2604	Web Console: In AIVR App settings - support multiple voices (one per language)
* BE-2598	Web Console: Make number of rows per page in the Phone Apps table configurable
* BE-2667	Web Console: New Voice Connector status column in AIVR App view
* BE-2666	Web Console: Shortcuts from Phone Management page plus modified status field
* BE-2669	Web Console: Show event metadata (if present) for AIVR Session Events
* BE-2012	Web Console: Transcribe+ now uses /sa/offline API
* BE-2649	Web Console: When querying AIVR (telephone) session set the limit parameter to 500
* BE-2675	SA: Add a refresh button to the page with the list of Calls
* BE-2635	SA: Add Description to Project
* BE-2631	SA: Add tooltips on 1D, 7D, 30D
* BE-2607	SA: Improvements to AIVR App selector
* BE-2608	SA: Make the selected Project indicator have 2 instead of 1 letter
* BE-2380	SA: On project general settings highlight the color and show time settings preview
* BE-2606	SA: Preselect time settings on the page where we create new project
* BE-2621	SA: Show headline in /sa/call search results if the search included text search
* BE-2636	SA: Show project name on the Integration settings page
* BE-2590	SA: Show the integration Icon on the Project selection list
* BE-2647	SA: Use the new GET /sa/call/agent to map agent_user_id to the name of the Agent
* BE-2646	SA: Use the new GET /sa/call/queue method to provide names for queues in the Advanced Search Queue filter
* BE-2645	SA: When querying fields for advanced search pass the contextId for the current Project
* BE-2611	Admin Tool: Convert Account Activity chart to Chart.js
* BE-2664	Add a verify query parameter to GET/account/{uuid}/phone-number
* BE-2643	Add contexId parameter to GET /sa/call/search/fields
* BE-2650	Add contextId to the content of the relevantMeetings returned from GET /asr/meeting/llm/query
* BE-2603	Add default TTS/ASR language for logic in AIVR App
* BE-2623	Add externalSaSession flag to AIVR Session
* BE-2648	Add limit parameter to the API that returns AIVR sessions
* BE-2660	Add metadata field to the AIVR Event
* BE-2665	Add new verify query parameter to GET /aivr-app
* BE-2720	Add optional metadata parameter to method that GETs meeting transcript
* BE-2614	Add to AIVR App: aircallApiUsername and aircallApiPassword
* BE-1783	AIVR API now can enable real-time transcription on transferred leg
* BE-2221	Allow the AIVR logic to send an alternative callback url in the response
* BE-2503	Associate and external ID to transcribe session on post in order to be able to retrieve the session using that ID later
* BE-2618	DAO for a database that will be storing data about recordings from S3 that need to be transcribed
* BE-2602	Define default voice for each language supported by AIVR App
* BE-2559	Delete embedding vectors if meeting is deleted.
* BE-2296	Deploy HA Kamailio Setup in Cloud
* BE-2644	Implement GET /sa/call/agent
* BE-2642	Implement GET /sa/call/queue
* BE-2571	In FreeSwitch transcribe proxy remove REDIRECT_URI and create SIP uri used in deflect from SIP URI name and DESTINATION DOMAIN
* BE-2715	More accurate control over the number of tokens submitted to LLM Service with all the embeddings
* BE-2563	Move meeting-join docker image from public repo to private repo
* BE-2526	New settings for voiceconnector origination and termination
* BE-2482	Pass intents from AIVR Session to /sa/offline via topics in /sa/call
* BE-1366	RedisConnectionException: Unable to init enough connections amount! Only 0 of 24 were initialized. 
* BE-2627	Remove xml:lang from the SSML template in audio-server
* BE-2641	Report Aircall Agent to the /sa/call
* BE-2640	Report Aircall Queue to the /sa/call
* BE-2620	Return headline as part of the /sa/call search results
* BE-2573	Send Call Notes to Aircall when AIVR call ends
* BE-2572	Send Caller Insight to Aircall as part of handling call.created webhook
* BE-2531	Send multiple asr session results to a single websocket receiver server session
* BE-2659	Split post-processing of AIVR sessions into immediate step and the delayed step
* BE-1786	Store copilot notes in /sa/call
* BE-2579	Store meeting speaker timeline in the database
* BE-2676	Support follow up queries in the /asr/meeting/llm/query - add history parameter and use it
* BE-2406	Support language switching setting in telephony bot logic callback
* BE-2652	Sync AIVR session with Aircall callId at transfer
* BE-2583	Use meeting.join.puppeteer.imagePullSecret property to pull puppeteer docker image

Changes related to Integrity of Processing (fixes):
* BE-2034	Admin Tool: Fix - failed to decode request body: organization name "telegraf" not found"
* BE-2600	Fix - Aircall webhook is unable to find an AIVR session
* BE-2674	Fix - Error when saving queue field data in /sa/call API
* BE-2705	Fix - fail to get fsPodName from the db for outbound calls
* BE-2628	Fix - In case of AIVR/SA integration the saConfig is retrieved from AIVR App context instead of from the SA Project
* BE-1354	Fix - NatsEndpoint fails to reconnect to NATS when its connection is lost
* BE-2637	Fix - realTimeAsrTranscribeSession is set on AIVR Session, but processing after the call terminates claims that "no RT asr transcribe session"
* BE-2629	Fix - Still seeing default text in the sa_call table
* BE-2638	Fix - Transcript text is not being saved into text field in sa_call
* BE-2592	Fix filebeat logging on cloud
* BE-2594	SA: Fix - Incorrect message shown after Voicebot Integration Project created
* BE-2373	SA: Fix - Name validations for project settings are required. 
* BE-2691	SA: Fix - Swapped channels in SA AIVR Integration
* BE-2560	TA: Fix - After latest change the Meeting Bot does not distinguish between progress Processing or Done
* BE-2630	TA: Fix - Meeting search seems to not always return the newest first
* QA-1485	TA: Fix - Error page when opening rediarized transcript (partial fix)
* BE-2692	Web Console: Fix - Error when listing some sessions Call Session view
* BE-2693	Web Console: Fix - Filter on the App Name in the Call Sessions table does not work
* BE-2525	Web Console: Fix - Label validation issues in Transcribe+
* BE-2534	Web Console: Fix - Provide correct value of the SIP URI on QA


All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


## Release 1.106.0

**Key changes related to the core APIs**
* Offline model (omega) trained on additional data from call center calls (health insurance, retail customer support)
* Improved diarization
* Improvements in /asr/meeting/join API (for Meeting Bot)
* Improvements to /asr/meeting/llm/query API (return relevant meetings)
* Outbound dialing needs to be enabled per account (it is a compliance feature)
* Added AIVR (Voicebot) Integration to Speech Analytics App
* Added webhook to Aircall integration
* Added HA Freeswitch support
* Collecting TTS character and LLM token usage
* Fixed a configuration issue where Grafana was not available on Edge

**Key changes related to Transcribe APP**
* Added Meeting Bot that can join a meeting and record/transcribe it (beta)
* Added Rediarize option
* LLM Playground and LLM Query available on Cloud
  * Note there is a limit of 16K tokens - about 1.5h of audio
* LLM Query results now show which transcripts were used in answering the query
* Added LLM Service authorization header settings
* Improved Action Items LLM query
* Show which users have Zoom Meeting Assistant installed

New or changed functionality in the Transcribe App:
* BE-2468	TA: Add a meeting_bot tag to meetings recorded using Bot
* BE-2470	TA: Add BOT selector on the home page
* BE-2345	TA: Add Meeting Bot
* BE-2412	TA: Add Re-diarize option for a meeting
* QA-766	TA: Added search to time-zone selector
* QA-1281	TA: Better error message when inviting user with invalid domain
* BE-2545	TA: Do not hide LLM Playground on the Cloud
* BE-2546	TA: Do not hide LLM Query on the Cloud
* QA-1377	TA: Fix after-login redirect URL on Edge
* BE-2508	TA: For first time login, after creating first project, we should take user to the page with the Zoom Meeting Assistant
* BE-2529	TA: Handle 429 response from /llm/chat API and /asr/meeting/llm/query
* BE-2467	TA: Identify Meeting Bot recordings as such in Transcribe App
* BE-1998	TA: Improved 404 Error handling
* BE-2394	TA: Improvements to LLM Playground UI
* BE-2495	TA: In LLM settings add Authorization header settings
* BE-1094	TA: Information about the use of Shared links is displayed
* BE-2514	TA: Make the request for Action Items be similar to the request made from the LLM Playground
* BE-2487	TA: Modify the LLM Query page to have the same look and feel as the new LLM Playground
* BE-2392	TA: New widgets to set number of speakers for Saving microphone recording
* BE-2391	TA: New widgets to set number of speakers for Upload
* QA-1416	TA: Remove language selector on Project Settings page on Edge
* BE-2339	TA: Show on Users page if the user has Zoom Meeting Assistant installed
* BE-2486	TA: Show relevant meetings if they are returned by the /llm/query API
* BE-2207	TA: Show share usage
* QA-321	TA: When a new user creates his first project there is now an option for change language for page translation

New or changed functionality in other platform components:
* BE-2524	Add a failsafe to all meeting bots
* BE-2481	Add aircallId field to AIVR Session
* BE-2480	Add aircallWebhookToken to AIVR App
* BE-2367	Add audio websocket URL to response from POST aivr logic callback
* BE-2494	Add authHeader parameter to llmSettings in /cluster API methods
* BE-2343	Add avirAppId and aivrSessionId to /sa/call API
* BE-2469	Add BOT value to AUDIO_SRC in meeting search API
* BE-2520	Add date field to relevantMeetings
* BE-2383	Add diarization parameter to re-run meeting API
* BE-2477	Add fsPodName to the POST /aivr
* BE-2368	Add read-only field llmCopilotNotesPrompt to saConfig
* BE-2444	Add relevantMeetings to the response from GET /asr/meeting/llm/query
* BE-2439	Add reviewNotes field to /sa/call API
* BE-2351	Add to GET /sa/call API ability to query by AIVR App Ids
* BE-2400	Add to storage measurement an explicit multiply column
* BE-2452	Allow Outbound Dialing only of OutboundDialing is set on the account
* BE-1785	At end of call, AIVR to submit real-time transcript to GPT to generate copilot notes
* BE-2232	Better handling of ServiceUnavailableException from cloud Influxdb
* BE-2338	Collect LLM statistics in InfluxDB
* BE-2042	Collect TTS statistics in InfluxDB
* BE-2516	Do not launch new /meeting/join if there are already N running meeting join K8s tasks
* BE-2466	Enforce Meeting Join limits on Transcribe App Cloud accounts
* BE-2458	For all AIVR sessions use POST /sa/offline/call/{callId}
* BE-2437	Generate call summary using llmSummaryPrompt setting in saConfig (offline)
* BE-2536	If the underlying LLM service behind /asr/meeting/llm/query API returns 429 error, the API should also return 429
* BE-2479	Implement POST /public/awebhook/aircall
* BE-2362	Implemented PUT /asr/meeting/{meetingId}/leave
* BE-2270	Improved AIVR Session Start Time
* BE-2358	Increase diarization.maxSpeakers from 12 to 20
* BE-2548	Increase max number audio on meeting API from 25 to 35
* BE-2438	Increase SA shortSummary length to 2048
* BE-2533	Make cleanup property configurable
* BE-2390	Modifications to how we configure Voice Connectors in Telco Service
* BE-2352	Modify GET /account/{uuid}/new-billing to obtain usage data from influx DG rather than from the account
* BE-2411	Modify pagination style for GET /sa/call
* BE-2433	New debug event and tweaks to the existing events in meeting join API
* BE-2482	Pass intents from aIVR Session to /sa/offline via topics in /sa/call
* BE-2549	POST /llm/chat now works in Cloud as well as Edge
* BE-2213	Removed Prompt Manager from audio server API
* BE-2501	Request to /llm/chat should use the authHeader settings from llmSettings
* BE-2502	Request to compute action items and any other llm requests for the transcript should use authHeader from llmSettings
* BE-2500	Request to Embeddings API should use the new authHeader parameter
* BE-2463	Return different 404 error code in case "No pods found for job: meeting-join-krxuobktp3kyez2uuqo3"
* BE-2371	SA: Add filtering by Agents
* BE-2422	SA: Add filtering on Call List page for Agent, Queue, and Resolution
* BE-2374	SA: Added a placeholder image for default profile avatar.
* BE-2228	SA: Added AIVR (Voicebot) Integration
* QA-1289	SA: Added success/alert notification after settings are updated or saved.
* BE-2370	SA: After selecting a custom date, show it on the page
* QA-1316	SA: Highlight Project name while deleting project.
* BE-2423	SA: Improve the Date Picker (e.g. on the Call List Page)
* BE-2380	SA: On project general settings highlight the color and show time settings preview
* BE-2420	SA: Remove the search box from the Call list page
* BE-2455	SA: Show notes about the Call
* BE-2378	SA: Show preview of Time Settings
* BE-2507	Set aivrSessionId and AivrAppId on /sa/call when we create it at the end of the aivr session even if there is no AIVR Integration
* QA-1390	Set the correct text on sa/call at the end of /sa/offline processing
* BE-2377	Support for multiple FreeSWITCH services
* BE-2506	Switch to new sentence embedding model in ml-svc
* BE-1557	Track use of /asr/meeting API for billing
* BE-2526	Two new settings for voiceconnector origination and termination
* BE-2519	Update the omega model to the latest version
* BE-2543	Use the weighted average on the similarity scores on agent detection
* BE-2440	Voicebot logic to start real-time transcription sessions and submit audio WS URL and asr session IDs in response
* BE-2429	Voicebot: Detect intents using examples
* BE-2409	Voicebot: Translate prompt on the fly and store to firestore
* BE-2344	Web Console: Add Calls page to Telephony Bot mode
* BE-2297	Web Console: Add filter by name to the list of Edge Configurations
* BE-2307	Web Console: Add view like 'kubectl get pods'
* QA-1042	Web Console: Added an option for Log out from all devices under account settings.
* BE-2454	Web Console: In the list of phone Apps mark those that have SA Project integration

Changes related to Integrity of Processing (fixes):
* BE-2478	Address issue where some users end up in Main Org. in Grafana
* BE-2385	Admin Tool: Fix - CMP user get 401 error when retrieving user data from some other account
* BE-2427	Fix - Cannot store some data in sa_call table
* BE-2456	Fix - GET /asr/transcribe/{sid}/transcript?format=text" hangs is many hints are used and audio is over 30 minutes
* BE-2498	Fix - Meeting join is not working on Edge
* BE-2204	Fix - Percolator stop request ignored if sent immediately after start
* BE-2415	Fix - Sentiment values have now narrower range than they used to be
* QA-1388	Fix Grafana on Edge
* BE-2457	Fix: Bot cannot join meeting in multiple participant scenario
* BE-2280	Remove speakers field from POST /sa/offline/call/{callId} method
* BE-2474	SA: Fix duration filter
* QA-1206	SA: Fix - Advanced Search is not working
* BE-2381	SA: Fix - Agent statistics page needs a spinner as soon as one of the time periods get selected
* BE-2348	SA: Fix - Call duration has wrong values
* BE-2418	SA: Fix - Cancel on Edit use simply closes the window without restoring the state
* BE-2379	SA: Fix - Configuring of Silence and Overtalk thresholds is messed up
* BE-2419	SA: Fix - Double loading of the call details page
* QA-1318	SA: Fix - Duration filter is not working in Advanced search.
* BE-2416	SA: Fix - Icons and Letters are getting cut off in the Call List view
* BE-2373	SA: Fix - Name validations for project settings are required. 
* BE-2346	SA: Fix - Next button works only on the 1st call loaded
* QA-1309	SA: Fix - Pagination on Agents page have Chinese letters instead of "per page".
* BE-2369	SA: Fix - Style issue on number of pages selection in modal.
* QA-1275	SA: Fix - Unknown symbols instead of "Next" and "Back" buttons
* QA-1066	SA: Fix - User is unable to change profile photo
* BE-2372	SA: Fix - When using current time as default time, if I don’t change the value it gives me the error: ‘Start Time is required’, it should be set as current date by default.
* QA-1298	TA: Fix - Admin User is unable to update the LLM setting.
* QA-1277	TA: Fix - After submitting a microphone recording, no success or upload message is shown. It should display a success message.
* BE-2331	TA: Fix - Browser Capture Pop-Up seems to load bunch of stuff that it does not need
* QA-1304	TA: Fix - For browser share and microphone capture recording, the Success message is not displaying after saving the recording.
* QA-1357	TA: Fix - LLM Query is not working
* QA-1359	TA: Fix - Redux is not clearing up in case of session logout
* QA-1196	TA: Fix - Sometimes, the login process gets stuck on the login page.
* QA-1384	TA: Fix - Three dot menu are not visible for the account users table.
* QA-965	TA: Fix - Within account share is not working properly.
* QA-1286	Web Console: Fix - "Create" button for Context should be disabled after first click and loader should show
* QA-1280	Web Console: Fix - Edit issues on API Secrets page
* BE-2322	Web Console: Fix - Error when I modify AIVR APP (Change CSID Callback from Path to Query)
* QA-1282	Web Console: Fix - Getting error message when user starts recoding but does not save it
* QA-1181	Web Console: Fix - GREG: When users try to filter True column of Interpretation and Review Status getting blank page
* QA-1358	Web Console: Fix - Pagination Control/Sessions per page is not working under Account management.
* QA-1178	Web Console: Fix - Text "Undefined" coming in "Main DNIS" dropdown
* QA-1180	Web Console: Fix - Unable to Edit AIVR App Settings getting 500 error
* BE-2461	Web Console: Fix - Unable to log into grafana on Edge on dev and QA
* QA-1272	Web Console: Fix - When user logout and login again, get Authorization error and login failed

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


## Release 1.105.0

**Key changes related to the core APIs**
* Offline model (omega) trained on additional data from call center calls (health insurance, retail customer support)
* Telephony Bot API now supports outbound calling and setting ANI caller id on transfer
* Added a parameter that controls language detection in offline transcribe API
* Added ability to send real-time transcription results to a websocket server (previously only supported websocket client)
* Web Console now shows all login sessions and supports forced logout.

**Key changes related to Transcribe APP**
* Added basic LLM Query over data stored in vector database
* User-level time settings (previously time settings were only account-wide)
* Korean transcription should now be less likely to shift to translation
* Summary LLM prompts are customizable on Edge

New or changed functionality in the Transcribe App:
* QA-1230	TA: Active login sessions now displayed and highlighted at the top by default.
* BE-2276	TA: Add 3 more LLM prompts to LLM settings
* BE-2224	TA: Add 'copy to clipboard' for action items
* BE-2278	TA: Add time settings also on User Profile
* QA-1237	TA: Added an option for Logout from all devices on My Login sessions.
* BE-2217	TA: Added basic Vector LLM Query
* BE-2284	TA: Apply MD formatting to the section summaries
* BE-2314	TA: If a user clicks the LLM Query button on the home page - take them to the LLM settings if needed
* BE-2240	TA: Implement page for Vector based querying - Edge Only
* BE-2196	TA: Make sure that whenever we discard the login session in the browser we do call logout API
* BE-2218	TA: Provide immediate feedback of the Start mic capture button being clicked
* BE-2282	TA: Use the customer overrides (if specified) for the summary prompts

New or changed functionality in other platform components:
* BE-2198	Web Console: Add login sessions view in Account Profile page
* BE-2197	Web Console: Make sure that whenever we discard the login session in the browser we do call logout API
* BE-2001	Web Console: Notify about inability to to microphone capture on HTTP urls
* QA-1274	Web Console: Removed Prompt and TTS Settings
* BE-2233	Web Console: Show the list of languages sorted
* BE-2229	Web Console: Use the new change password API
* BE-2199	SA: Added created date and UUID to the page with Project details
* BE-2200	SA: Added name of the project to the Delete dialog
* BE-2256	SA: Contact Support now opens in a new browser tab
* BE-2290	SA: Implement AIVR Integration (configuration)
* BE-2206	SA: Improve PII Redaction Config page
* BE-2255	SA: Use the Account Time settings as the time defaults when creating a new Project
* BE-2254	SA: Use the new change password API in SA App
* BE-2252	SA: Hide (comment out) the setting for Age detection
* BE-2299	Demo: Add a note about the models used in the Voicebot Demo
* BE-2300	Demo: Copy to clipboard icons need tool-tip and there needs to be confirmation after copy
* BE-2211	Admin Tool: Add tab/page to control SA activation
* BE-2301	Add languageDetection parameter to asr settings in the transcribe API
* BE-1749	Add Outbound Calling to AIVR API
* BE-2277	Add to cluster API new LLM Settings for the Embeddings
* BE-2177	Added support for 11labs voices in TTS
* BE-2225	Added transfer to extension option in the AIVR transfer action
* BE-2291	AIVR Transfer should give option to use DNIs or Original ANI for the caller id for the transferred call
* BE-2312	Better handling of HTTP 502 from Fusebill
* BE-2279	Changes on agent field in request to POST /sa/call
* BE-2085	Do not return "user not found" from the forgot password API
* BE-1972	Hide/Show features of the Speech Analytics App based on the settings on the account
* BE-2239	Implement POST /asr/meeting/llm/query
* BE-2286	Improve (speedup) lookup of AIVR App by DNIS
* BE-2216	Improve diarization sentence boundary
* BE-2209	Language detection for offline sessions using Omega model
* BE-2273	LLM meeting section summary now returned raw
* BE-2193	Modified GET /greg/experiment to return only the experiments that are from the specified Context
* BE-673	Modify password change API to encrypt password parameters
* BE-2081	Move caching of TTS prompts from memory to redis
* BE-2185	Move mod_xml_curl service to fssk
* BE-1791	Omega model trained on Health Insurance Call Center data
* BE-2230	Speedup the response time of POST /asr/transcribe/async
* BE-2191	Support 'external' websocket mode for /asr/transcribe/async and /asr/recognize/async
* BE-2192	Support new returned Content type - metadata
* BE-2261	Tie AIVR App and Context to form AIVR Integration (Context side)
* BE-1680	Update jdk version to 17 in docker images

Changes related to Integrity of Processing (fixes):
* QA-1185	TA Edge: Fix - Unable to recognize transcript's project on homepage. 
* QA-1252	TA Edge: Fix - Port Number is missing in invitation link
* BE-2269	TA: Fix - Action Items are no longer included in the PDF and Docx
* QA-1198	TA: Fix - Advanced Search View does not update after clicking ReRun.
* QA-1263	TA: Fix - After deleting any share, it still shows in the table until the user performs a hard refresh of the page
* QA-1240	TA: Fix - Downloaded pdf for Korean transcript does not open in Acrobat Reader
* QA-1248	TA: Fix - Duplicate transcripts are showing in advance search.
* BE-2275	TA: Fix - Korean sometimes being translated in addition to transcribed
* BE-2274	TA: Fix - LLM Playground needs to be able to get transcript even if user is User role and has no Download permission
* QA-1279	TA: Fix - Microphone recording and browser share menu should not be shown under actions for languages that do not have permissions for browser capture and microphone recording.
* QA-1126	TA: Fix - Null projects displayed for some meetings.
* QA-1199	TA: Fix - Some transcripts are missing a options under the 3-dot menu.
* QA-1232	Ta: Fix - Sorting is not working on MY Login sessions page.
* QA-1219	TA: Fix - The 'Incorrect Password' message should appear when a user tries to download the password recovery key with the wrong password.
* BE-838	TA: Fix - Tracking of time used does not seem to work anymore
* QA-1242	TA: Fix - User gets stuck on Upload page after submitting a file.
* QA-912	TA: Fix - User is able to upload the audio file even when the allotted storage is fully used.
* BE-2313	TA: Fix - User unable to move recording from one project to another
* QA-1205	TA: Fix - Warning not showing for upload of large file.
* BE-2169	Web Console: Fix - Clicking on the date range in Logs page triggers an error in the console
* QA-1220	Web Console: Fix - New user Account getting error on log search
* BE-2271	Web Console: Fix - Output AIVR prompts are not expanding
* BE-2219	Web Console: Fix - recorded audio chart should start from 0:00
* QA-1243	Web Console: Fix - Unable to edit 'App Name'
* QA-1273	Web Console: Fix - When user click on the No. of node of 'No edge deployments loaded' table getting blank page
* QA-1258	SA: Fix - Audio forward/backward buttons are not working as expected.
* BE-2316	SA: Fix - Avatar not getting saved
* BE-2250	SA: Fix - Back Button should take us back to Settings overview and not to main page
* QA-1226	SA: Fix - Fails to show the new project wizard if there are not Projects on account
* BE-2260	SA: Fix - Missing parameters for uploaded Call
* QA-1159	SA: Fix - User is unable to select the time and time dropdown text is overlap.
* QA-1068	SA: Fix - User unable to update location , Company Position, and Name, as save button disabled.
* QA-1133	SA: Fix - Weird behavior on the configurations page.
* BE-2288	Fix - AIVR stopped listening in the middle of a my answer
* BE-2208	Fix - asr-api fails to submit DEL callback request after disconnect is processed
* BE-2181	Fix - ml-svc performance degradation since release 103 after we upgrade to python 3.11
* BE-2214	Demo: Fix - Getting 401 error when trying to send a link from the demo app
* QA-1213	Admin Tool: Fix - Showing a blank page when the admin user tries to check the API usage.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.104.0

**Key changes related to the core APIs**
* Add diarization to Whisper model in offline task
* Autoscale real-time REX on GCP
* Automatically detect agent channel in offline SA API
* Improved Kappa (real-time) model trained on additional call-center data (health insurance domain)
* Switch Analytics App from /sa API to /sa/offline APIs
* Extend the use of allowSignupsFromDomain to allowed user invites

**Key changes related to Transcribe APP**
* Add Korean Language option for Edge
* Enhanced LLM Playground to support temperature setting and markdown rendering
* Added "Automatic" setting for number of speakers in diarization
* In Advanced Search added Relative Time filter
* Add pages with list of login sessions (for user and for all account)

New or changed functionality in the Transcribe App:
* BE-2133	TA: Add "Go to Home" button on "Something Went Wrong" page
* BE-2202	TA: Add a 3 second timeout on the request to ipfy
* BE-2134	TA: Add Korean Language option for Edge
* BE-2078	TA: Add page with list of all logged-in sessions on the account
* BE-2182	TA: Add support for m4a files in file upload
* BE-2155	TA: Add temperature to LLM Settings
* QA-680	TA: Better reporting of Recompute in progress on Advanced Search page
* BE-2125	TA: LLM playground able to render markdown format in LLM responses
* BE-2190	TA: Modify message template used LLM Playground to work with Mixtral
* BE-2141	TA: Modify the number of speakers selector for diarization on Upload
* BE-2184	TA: Remove diarization from Live Microphone recording preview
* BE-2118	TA: Remove previous error message from the login screen as soon as the user clicks the login button
* QA-848	TA: Show all login sessions of the current user
* BE-2136	TA: Show PC Name when hovering over Installed-Connected
* BE-2164	TA: Support Relative Time search filter on Start Time in Advanced Search
* BE-1885	TA: Use Mixtral for Summarization on Edge

New or changed functionality in other platform components:
* BE-2142	Add ability to save Meeting Search queries
* BE-1698	Add diarization to Whisper model in offline task
* BE-2062	Add percolatorThreshold to the output response in AIVR callback
* BE-2139	Add regex syntax and group references to the url prefix matching in grammar fetcher
* BE-2137	Add RelTimeTerm query term to Advanced Meeting Search API
* BE-2138	Add RelTimeTerm query term to Call Search API
* BE-2144	Add temperature parameter to llmSettings in the /cluster API
* BE-2092	Admin Tool: Show login error messages to user
* BE-1601	API to email link to the results of Voicebot Demo session - make the link url configurable
* BE-2127	Autoscale real-time REX on GCP
* BE-2120	Demo Voicebot: Show the page with trancript/audio/sidepanel immediately after the end of the call
* BE-2158	Demo Voicebot: Support Spanish version of Casey demo
* BE-2187	Demo: Use the new urlLink parameter in the API used to send the link
* BE-2089	Detect agent channel in offline SA API
* BE-2175	Extend the use of allowSignupsFromDomain to user invites
* BE-2135	Improve /llm/chat API to handle transcript longer than the token limit
* BE-1792	Improved Kappa (real-time) model trained on additional call-center data (health insurance domain)
* BE-2041	Limit maximum number of nonces that can be active for a login session at any time
* BE-1678	Migrate Java Applications from Java 11 to Java 17
* BE-2172	Modify the GET method for the Business Config API which takes Auth Token
* BE-2108	Monitor and restart asr container if it loses GPU
* BE-2126	Retire old billing-utility
* BE-2117	Return a specific http error response if we get ResourceLimitExceededException when creating new Voice Connector.
* BE-2149	SA: Add filter on User Role
* BE-2129	SA: Add JWT token generation to SA
* BE-2157	SA: Add option to Delete a user
* BE-2156	SA: Add option to Edit the User
* BE-2057	SA: Invoke correct new APIs when uploading single file on SA App
* BE-1712	SA: New Advanced Search Page
* BE-1794	Switch Analytics App from /sa API to /sa/offline APIs
* BE-1997	Tie collecting storage information to activity on account
* BE-2109	Upgrade openai package to version 1.*
* QA-1165	Web Console: Add a filter for the 2FA enabled on the user management page.
* QA-1188	Web Console: Add Calendar to date selection in Business Config
* BE-2080	Web Console: Add sorting on columns showing available Edge configurations
* BE-2121	Web Console: Edge deployment filter - bring the search box in focus as soon as I open the filter
* BE-2075	Web Console: Show telcoData.fsUUID on the AIVR session details page
* BE-2176	Web Console: Show value of allowSignupsFromDomain in account profile

Changes related to Integrity of Processing (fixes):
* BE-98	Fix - Bug in telco service with Apps that are sip-only and we try add a phone number
* BE-2170	Fix - Float overflow issue in rex RNNT search
* BE-2166	Fix - Incorrect column count: expected 1, actual 38 in getCallCount in /sa/call API
* BE-1971	Fix - NoSuchFieldError: LUCENE_7_7_3
* BE-2167	Fix - Speakers merged into streaks of other speaker utterances in /sa/offline API
* QA-1133	SA: Fix - Weird behavior on the configurations page.
* QA-1200	TA Edge: Fix - Invitation email is not coming to the provided email address.
* QA-1236	TA: Fix - After editing any expired shared transcript to Never Expire, the save button is not working.
* QA-1223	TA: Fix - Back button is not working on Walkthrough Wizard
* QA-1153	TA: Fix - Blank page is showing for the login for one account.
* QA-1211	TA: Fix - Hover msg over Never share Expiry status is wrong.
* BE-1989	TA: Fix - Inconsistent Project membership as shown in the UI
* QA-1076	TA: Fix - Personal projects are not showing in the destination projects while moving any transcript.
* QA-1122	TA: Fix - Resend invites to bad email address throwing the something went wrong issue.
* BE-2146	TA: Fix - Right-click not working on Edge
* QA-1227	TA: Fix - Showing the American flag for all project language projects.
* QA-1197	TA: Fix - Specific No. of Speakers field is accepting blank inputs.
* BE-1987	TA: Fix - Stuck on Import/Upload page after Submit
* QA-1231	TA: Fix - There is no limit given for the Time range in advanced search.
* QA-1209	TA: Fix - Walkthrough wizards not working properly on 90% page zoom.
* QA-586	TA: Fix - When a user clicks on “edit” of a Share it automatically increases its “Expires in” time by a day.
* QA-1174	Web Console: Fix - On Experiment Browser section- ‘Apply filter' button is not working, user getting ‘e.preventDefault’ is not a function.
* QA-1191	Web Console: Fix - Only one success message should be displayed when adding a 'Business Configuration'.
* QA-1186	Web Console: Fix - Past date entry should not allowed in adding Business Config records.
* BE-2148	Web Console: Fix - Unable to save the URL of the outbound AIVR logic
* QA-1176	Web Console: Fix - User getting blank page, either clicked on True text or ascending- descending filter or when searching something.
* QA-1177	Web Console: Fix - When a user click on copy icon under A of Utterance, he does not get any copied data but getting Type Error
* QA-1179	Web Console: Fix - When users try to delete ID’s under Interpretation column by clicking on delete icon, it’ s not getting deleted.
* QA-1175	Web Console: Fix - When users try to edit any ID under True column, since at the time of editing Reset and Save button is disable but still it is clickable.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


## Release 1.103.1

New or changed functionality in the Transcribe App:
* BE-2143: (TA) Show Recompute option also if status Error under certain conditions

Changes related to Integrity of Processing (fixes):
* BE-2163: Fix - Incorrect nginx routing for auth-svc from admin app

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.103.0

**Key changes related to the core APIs**
* Support for url rewrite and HTTP proxy for grammar fetching for /asr/recognize API and for MRCP ASR.
* Switch Speech Analytics App from old /sa api to new /sa/offline API
* New APIs to manage user login sessions
* New API to define business specific settings for a Voicebot

**Key changes related to Transcribe APP**
* LLM Playground for Edge Deployments - ask a LLM any questions about the transcript.
* Fix for negative duration of words which was impacting recomputing data from transcripts.

New or changed functionality in the Transcribe App:
* BE-2068	TA: Add LLM Playground page to Transcribe App (on Edge only)
* QA-1054	TA: Add validator for keyword group names
* BE-2060	TA: Option to set share within account to not expire

New or changed functionality in other platform components:
* BE-2101	/sa/offline API - generate talk and overtalk data for each speaker
* BE-2076	Add AIVR API method to reserve rex for already started outbound aivr session
* BE-1953	Add AIVR Business Config API with opening-hours information and other info
* BE-2036	Add aivrAppId to the initial callback for the AIVR session (also the websocket version)
* QA-1071	Add API to logout user from some/all login sessions
* QA-1070	Add API to show User's all login sessions
* BE-2061	Add audioOffset option to audio in /sa/offline
* BE-1878	Add localization in llm-svc
* BE-2044	Add parent AIVR session to POST /aivr/dial/{destination}
* BE-1917	Add to Account a read-only field to store customization settings for SA App
* BE-1974	Add to Account API saAppHiddenFeatures
* BE-2020	Add version field to /sa/call
* BE-2033	Associate Business Config with AIVR App
* BE-1850	Casey Demo Voicebot in Spanish
* BE-2058	Configure demoPhoneNumber for demo app on dev qa and prod environments
* BE-2011	Convert auth-svc from tomcat+war to SpringBoot
* BE-1985	Enhancements to grammar fetcher (http proxy, url rewrite)
* BE-1972	Hide/Show features of the Speech Analytics App based on the settings on the account
* BE-1909	Hook up Speech Analytics App to Sentry
* BE-1954	Implement API to query existing login sessions
* BE-2035	Implement GET /aivr-app/{aivrAppId}/business
* BE-1992	Implement GET and DELETE /auth/login/{sessionId}
* BE-1497	Implement getContextStats method on SearchableMeetingDao that returns statistics for contexts
* BE-2074	Implement POST /llm/chat API
* BE-1598	Implement proper queue priority for transcription
* BE-2003	Implement safe shutdown for freeswitch/fssk pod
* BE-2031	Improve nonce handling in Customer Management Portal (Admin Tool)
* BE-2030	Improve nonce handling in Customer Portal
* BE-2032	Improve nonce handling in Speech Analytics App
* BE-2116	In Share APIs -- make expires value of 0 mean that the share never expires
* BE-2052	Modify REX to stop storing usages in Redis
* BE-2051	Move sentryEnvironment to global setting in onprem-cluster-deployment task
* BE-1073	New API: POST /asr/meeting/{meetingId}/rerun
* BE-1520	Stop storing usages in Redis after billing-utility is no longer needed on production
* BE-1981	Support cluster specific service account key in onprem-cluster-deployment task
* BE-1794	Switch Analytics App from /sa API to /sa/offline APIs
* BE-1966	Update k8sNodes in firestore automatically when changing cluster setup
* BE-2069	Web Console: add "outbound" option to pull-down for logic
* BE-1994	Web Console: Add audio download button to AIVR call audio page
* BE-2038	Web Console: Add page to configure Business settings for use in AIVR
* BE-2006	Web Console: include ;transport=tcp in the sip URI shown in Telephony Bot App
* BE-2002	Web Console: Place cursor and focus on the highlighted textbox right after the context dialog is shown
* BE-1492	Web Console: Show Edge configuration in the table that shows all Edge deployments
* BE-1951	Web Console: Telephony Bot mode in Call Session table - make it remember previous state when returning from the detailed session view

Changes related to Integrity of Processing (fixes):
* QA-1111	TA: Fix - "ID to Clipboard" option is missing in Advanced Search.
* QA-1125	TA: Fix - After deleting any transcript, success message not showing.
* BE-2022	TA: Fix - bad http request URLs in Edge deployments 
* QA-1140	TA: Fix - Project numbers going blank after filtering role in Users under Account.
* QA-1081	TA: Fix - Proper translation should be there for mouse hovering on error.
* BE-2021	TA: Fix - running out of nonces in some scenarios
* BE-2027	TA: Fix - Sentry errors when sending to Glitchtip
* QA-1184	TA: Fix - Shared transcript page getting refresh continuously(Public share)
* QA-1141	TA: Fix - Sorting in Users under Account section is not working properly.
* QA-1143	TA: Fix - The duration filter is not working as intended, having issues setting it up manually, and also not showing the transcripts.
* QA-1167	TA: Fix - The owner is unable to log in to below mentioned IP addresses and the "Failed to fetch" error is being received.
* QA-786	TA: Fix - Transcripts with no duration are not available in advanced search.
* QA-1117	TA: Fix - Unable to edit "Users" when creating a new project.
* QA-685	TA: Fix - Updated User name is not showing on the admin Speaker screen
* QA-1116	TA: Fix - Walkthrough wizard not working properly, back button not working when user tries to go back from the transcripts.
* BE-2013	TA: Fix - When inviting the user to the account, if we provide an invalid email it throws a 500 error and goes to the "Something went wrong" page
* QA-1114	TA: Fix back button from transcript opened from Advanced Search results
* BE-2084	Web Console: Fix - Audio is fresh-uploaded GREG experiment not playing
* BE-2119	Web Console: Fix - certain Edge Configurations showing blank page instead
* QA-1142	Web Console: Fix - Context dash filter by status is not working properly.
* BE-1955	Web Console: Fix - In user Profile show permissions and not the Role
* BE-2007	Web Console: Fix - Narrow window does not render transcript text in telephony call detail view
* BE-2077	Web Console: Fix - Requests for GREG audio stuck in "pending" and then failing
* BE-2087	Web Console: Fix - Showing Training mode even though account does not have Training enabled
* BE-2053	Fix - Glitchtip cannot handle larger headers (cookies)
* BE-1982	Fix - NPE found in new-billing-utility logs on voicegain
* BE-2103	Fix - Queue info is not getting saved and/or returned from /sa/call API
* BE-2083	Fix for negative duration of words
* BE-655	Fix for onprem-cluster-deployment task stuck when pods are in unexpected status

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


## Release 1.102.0

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


## Release 1.101.1

New or changed functionality:
* BE-1877: Enable VAD on Whisper
* BE-1886: Make node affinity configurable in offline-whisper
* BE-1889: Deploy whisper model to the edge cluster without internet connection
* BE-1938: Initial whisper prompt to ensure punctuation is generated  

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.101.0

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



## Release 1.100.0

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


## Release 1.99.0

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


## Release 1.98.0

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

## Release 1.97.3

Updates:
* BE-1455   Upgrade cloud function runtime from python 3.7 to 3.9

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.97.2

Changes related to Integrity of Processing (fixes):
* BE-1510   Fix - SnippetAnnotations is not working

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.97.1

Changes related to Integrity of Processing (fixes):
* BE-1412   Fix - uhhuh recognition with low confidence messing up the flow (early barge-in) 
* BE-1443   Fix endpointing of low confidence recognitions in Telephony Bot API
* BE-1473   Fix - NPE in Meeting Search if any account context does not have type set
* BE-1476   TA: Fix - Something Went Wrong page not loading correctly on Edge
* BE-1477   Fix - Invalid value: null error when retrieving transcript in Web Console
* BE-1479   TA: Fix - missingKey translation "Uploaded File" logged in a loop
* BE-1487   Web Console: Fix - Unable to sign-up without providing Company Name
* QA-858    Web Console: Fix - Showing no transcript when click on the view for any transcription. 
* QA-859    Demo: Fix - Getting white screen in demo when trying to upload a file or trying to do doing mic capture

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.97.0

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

## Release 1.96.0

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


## Release 1.95.1

Changes:
* BE-1343  Add property builtin.grammar.output.flavor to dynamic grammar

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.95.0

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


## Release 1.94.1

Changes:
* BE-1282  Fix - offline task can't process 7.1 channel audio

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.94.0

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

## Release 1.93.1

Changes:
* BE-1207  Reject ASR requests if the default model doesn't support languages specified in requests. 

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.93.0

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

## Release 1.92.0

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

## Release 1.91.1

Changes:
* BE-1013  Log invalid patterns found in RegexFormatters instead of throwing exceptions

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


## Release 1.91.0

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

## Release 1.90.1

Changes related to Integrity of Processing (fixes)
All these apply to the Transcribe App:
* QA-497  Fix: Accepting anything in tag, also taking space as tag.
* BE-790  Fix: At the end of project wizard sometimes have to click Done twice to get the new project saved
* BE-957  Fix: Not accepting MP4 file for transcription
* BE-964  Fix: Calling Invoice API on Edge

Other changes in Transcribe App:
* BE-955  Disable API Security Page

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.90.0

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


## Release 1.89.2

Changes related to Integrity of Processing (fixes)
* BE-882  TWIML sessions not closed if no TWIML Stop message sent on websocket

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


## Release 1.89.1

Changes related to Integrity of Processing (fixes)
* QA-477 Transcribe App: Sharing (public) a transcript and when try to play this transcript page refreshing all the time.
* QA-483 Transcribe App: Not able to play the old transcripts

Additions:
* BE-865  Add presigned url to response from GET /asr/meeting/shared/{shareId}/data

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.89.0

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

## Release 1.88.1

Known Issues:
* BE-809 Enabling full masking (*****) caused Meeting Minutes to not be generated - If you enable Full Text Redaction for some category then Meeting Minutes may not be generated. A work-around is to disable Word Cloud on the Project.

Changes related to Integrity of Processing (fixes)
* BE-774	Fix: Incorrect MPEG-DASH mpd format file generated
* BE-802	(TA) Fix: Account redacting formatters are saved to Projects
* BE-803	Fix: Formatters defined on account are not being used in POST /asr/meeting
* BE-806	(TA) Fix: When generating a pdf, NullPointerException is thrown if meetingMinutes is not enabled
* QA-405	Fix: Demo app has incorrect recaptcha key

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.88.0

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


## Release 1.87.1

Changes related to Integrity of Processing (fixes)
* BE-722    Recognizer does not send RECOGNIZE-COMPLETE if no audio has been sent to Recognizer

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


## Release 1.87.0

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

## Release 1.86.5

This release enables higher number of replicas for autoscaling.

It is just a configuration change.

## Release 1.86.4

Changes related to Integrity of Processing (fixes)
* BE-662    Temporary fix for "ASR-API kills REX session if there is no activity for 5 minutes" - timeout extended to 15 minutes
* BE-663    Fix for: asr-api on CHD environment rejects derived session because callback url is redis
  * this was introduced by: BE-615 Enable TWILIO protocol in CHD environment (sapi.voicegain.ai) 

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.86.3

Changes related to Integrity of Processing (fixes)
* BE-631    Remove punctuation between two digits in En BERT punctuation model

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.86.2

This release includes an improved real-time English model delivering higher accuracy of speech recognition.

Changes related to Integrity of Processing (fixes)
* BE-622    (SSO) Fix issue with Spinner that does not stop if login failed (no error message was shown)

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.86.1

This release has several improvements in the PDF export in the Taanscribe App (Meeting API)

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

## Release 1.86.0

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


## Release 1.85.2

Changes related to Integrity of Processing (fixes)
* BE-549    Public Transcribe App share from EDGE cycles non-stop if used without login

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


## Release 1.85.1

Changes related to Integrity of Processing (fixes)
* BE-548    Do not send multipart/form-data parameters as files in audio.callback. Only audio data should be sent as file.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.85.0

New functionality in this release in the Transcribe App:
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


## Release 1.84.3

Changes related to Integrity of Processing (fixes):
* Fix several UI glitches that were introduced when updating AntD version.

Changes related to Security:
* BE-220    demo.voicegain.ai requires Content Security Policy and related Headers

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.84.2

Changes related to Integrity of Processing (fixes)
* BE-448    Project transcript view shows also Home Page transcripts directly after switch from Home to Project view

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.84.1

Changes related to Integrity of Processing (fixes)
* BE-442    Fixed in Transcribe App: Voice Signature sample playback always plays from the beginning of audio
* BE-443    Fixed in Transcribe App: Transcription fails because unable to find the speaker

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

## Release 1.84.0

This minor release includes a significantly more accurate Spanish real-time model.

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


## Release 1.83.0

Key things that are new in the Transcribe App this minor release:
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

## Release 1.82.4

This release allows for use of the /confgroup API with JWT token.

## Release 1.82.3

This release upgrades Kubernetes to 1.25

## Release 1.82.2

This maintenance release has the following changes:
* BE-256    Modified App Selector to properly render on mobile browsers
* BE-257    Added notice to Login Screen on Transcribe App on mobile browsers

## Release 1.82.1

This maintenance release has the following changes:
* BE-243 Fix for not getting any transcriptions from the Telephony Bot sessions
* BE-244 Fix for erratic recognition in the Telephony Bot

This release also fixes several 3rd-party vulnerabilities.

## Release 1.82.0

This minor release chas the following changes:
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

## Release 1.81.0

This minor release has the following fixes and improvements in the Transcribe App:

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

## Release 1.80.2

This maintenance release has the following fixes:
* BE-106 SMU is using a lot of Redis memory

## Release 1.80.1

This maintenance release has the following fixes
* BE-51	Fix for WS/WSS protocol for Audio Streaming is not working
* BE-54	Fix session_duration set to 0 for each offline ASR session measurement in influxDB
* BE-58	Add missing insecure websocket url to Ingress

## Release 1.80.0

This minor release has back-end improvements that will eventually give better monitoring more precise billing/usage data. It also includes a model that is more accurate on call-center audio.
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

## Release 1.79.0

This minor release has several back-end improvements to the core Voicegain Platform:
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

## Release 1.78.1

This maintenance release includes the following for the Transcribe App:
* Keyword and phrase highlighting in the transcript text
* Bug #671 fixed: home/login page loop in all the nonces somehow are removed from the indexedDB

## Release 1.78.0

In this minor release the throughput of the offline transcription in two-channel mode has been significantly improved.

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

## Release 1.77.1

This maintenance release includes:
* Back-end update of Redis to 6.2.10 which has a fix to for the issue https://github.com/redis/redis/pull/11590
* More accurate real-time model

## Release 1.77.0

This release adds Zoom Meeting Assistant status display to the Transcribe App.
Due to this change this release will require Zoom Meeting Assistant version 0.3.0 at minimum.

Transcribe App issues addressed:
* #555: Automatically insert underscores into multi-word hints
* #667: Do not hide microphone and browser capture icons for old projects that have no language setting value

Admin tool has been improved in this release:
* Last Login Time and Billing Type columns have been added.

This release addresses the following issue for the rest of the Voicegain platform:
* #211: nats-websocket fail to send messages to topic subscribers.

## Release 1.76.0

This minor release has the improved Spanish Real-Time model.

Transcribe App issues addressed:
* #406: Add ability to delete a keyword in Speech Analytics settings
* #461: The downloaded audio file is mp3, but the extension is wav
* #532: In languages Project settings show if microphone transcription is not available for given language
* #610: Change the lock-out message to show the local time instead of the UTC.
* #665: Fix weird behavior in Settings if old Project has no Meeting Minutes enabled
* #666: Add a hide button for the Zoom Meeting Assistant banner

## Release 1.75.2

This maintenance release includes:
* Fix for Issue #208 which was affecting Signup via the Developer Console
* Improved demo.voicegain.ai app with improved security

## Release 1.75.1

This maintenance release fixes the following Transcribe App issue:
* #204: Occasional Error in Recomputing status

## Release 1.75.0

This minor release has the improved Spanish Offline model.

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

## Release 1.74.1

This maintenance release fixes the following issues:
* offline task fails on re-try due to format value type mismatch
* some sessions in ERROR state not removed from session cache as soon as ERROR determined

## Release 1.74.0

This Minor Release enables User self-signup via email on Transcribe App on Edge.

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

## Release 1.73.1

This is a dummy maintenance Release, meant to test the automated release/deployment pipeline changes.

## Release 1.73.0

This minor release enables Browser Capture in the Transcribe App on Edge.

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

## Release 1.72.0

This minor release offers improved Key Items feature within the Meeting Minutes in the Transcribe App.

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

## Release 1.71.1

This maintenance release fixes 3 issues:
* #143: Weird clock values when on Edge and logged in as a user with role User
* #617: (Edge) New created project not visible in the project list
* #618: (Edge) New created project shows files from an older project

With this release we also support a minimal, self-contained, docker-compose deployment of MRCP ASR on GPUs.

## Release 1.71.0

This minor release adds configurability of the Key Items of the Meeting Minutes in the Transcribe App.

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

## Release 1.70.2

This maintenance release fixes one issue:
* #126: Add project filtering to meeting search for normal Users

## Release 1.70.1

This maintenance release has only two changes:
* Diarization processing has been moved to GPU which is of interest to Edge users because it will reduce the CPU resource requirements.
* In Transcribe App, the default setting of Meeting Minutes on existing Projects has been changed to make it less confusing.

## Release 1.70.0

This minor release addresses the following Transcribe App issues:
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

## Release 1.69.0

This minor release adds two major new features in the Transcribe App:
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

## Release 1.68.1

This maintenance release supports multiple languages choice in the `/asr/transcribe/async` and `/asr/recognize/async`. It runs recognition using all specified languages and returns the transcript with the highest confidence.

## Release 1.68.0

The key features in this minor release are:
* Improved diarization in the text areas where one speaker switches to another. 
* More accurate speaker Voice Signature matching.

This release fixes numerous small Web UI issues, mainly usability, in the Transcribe App related to the Voice Signature functionality made first available in the 2 previous releases.

The installer for the Zoom Meeting Assistant is now signed with Extended Validation Certificate.

This release addresses the following issues for the rest of the Voicegain platform:
* #97: When deleting a Speaker we should remove references to it from Context voiceSignatureSpeakers
* #98: Orphan cleanup delete the audio clip for speaker signature

## Release 1.67.0

This minor release addresses these specific Transcribe App issues:
* #546: Older projects do not generate topics
* #547: Saving a project switches it to a different one
* #550: Assign transcript speaker to a known Speaker (with or without voice signature) - also create new Speaker if needed
* #551: Add page for managing Speakers

The release addresses these specific Speech Analaytics App issues:
* #12: Turn off pagination in the Calls page in Speech Analytics App - this is temporary measure before switching to new pagination style
* #14: Upload file should use short-lived JWT

This release addresses the following issues for the rest of the Voicegain platform:
* #81: Enhance logging for AIVR sessions
* #86: When creating a new User let's create a corresponding Speaker entry (for Transcribe App accounts)
* #88: Add support for vsConf and originalName (meeting API)
* #91: Add mustHaveSignature parameter to GET /speakers API

## Release 1.66.1

This maintenance release includes improved punctuation for the English Offline transcription.

## Release 1.66.0

This minor release provides an improved model for Offline English transcription - you will notice about 1% higher accuracy

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

## Release 1.65.0

This minor release addresses the following Transcribe App issues:
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

## Release 1.64.1

This maintenance release includes an improved model for diarization which will provide better diarization accuracy.

The release also fixes these issues in the ML Services:
* #1: Words that should be stop words appear in the Topic results
* #2: Topic extraction should be case insensitive.


## Release 1.64.0

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

## Release 1.63.0

This minor release addresses the following Transcribe App issues:
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

## Release 1.62.1

This maintenance release fixes the following issue:
* #rcj-555: fail to copy asr transcription result files to a new context - affects SA App Demos

## Release 1.62.0

This minor release addresses the following Transcribe App issues:
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

Known issue in Trancribe App:
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

## Release 1.61.0

This minor release includes a major overhaul of the Transcribe App:
* Transcribe App now supports Zoom Meeting Assistant App which can submit all your local Zoom Meeting recordings for transcription to the Transcribe App.
* New Transcript Detail display that no longer requires paging and supports transcript from overlapping speech.
* Transcribe App is now available on Edge - this way you can deploy it to all users in an Enterprise and keep all your confidential data local.

Other minor changes include:
* Decrease playout of the Telephony Bot prompts. Latency of actions following a prompt has been reduced by about 800ms.
* Built-in number grammar has a fix for a minor issue.

This release includes improved offline speech-recognition model with about 1.5% improvement in accuracy.

## Release 1.60.4

This maintenance release changes 2 things relevant for MRCP users:
1. The content on NLSML returned in MRCP results - We now return `<nomatch/>` element within `<result><interpretation>` in case of `Completion-Cause: 001 no-match`. In the past `<nomatch/>` was not included, instead an NLSML corresponding to a normal recognition was returned even in case of `Completion-Cause: 001 no-match`
1. GRXML grammars with `scope=private` attribute now parse without an error. Note, however, that the private scope is still not enforced. That will be fixed in future releases.

## Release 1.60.3

This maintenance release fixes:
* #rcj-546: DataObjects not being deleted by cleanup task. Fixes the de-referencing issue.

## Release 1.60.2

This maintenance release includes:
*  Usage data now stores session Tags, so if you request from us, e.g., a monthly usage report then each session in the report will have those tags.

Issues fixed:
* #rcj-545: re-register listener whenever FirestoreException is received in FirestoreWebApiConfigCollectionEventListener -- The problem manifested itself in new JWT tokens not fully working for offline-sessions - the requests were accepted but final result was Error. The cause was Google Firestore client occasionally getting an error event from Firestore upon which no subsequent events would pass through. We implemented a workaround where the listener re-registers in case of error.

## Release 1.60.1

This maintenance release includes:
* In Transcribe App: 
  * Small speed-up of the transcript loading
  * Tool-tips for prev/next buttons
* In Web Developer Console: 
  * Significantly speeds up loading of long Transcripts and Meetings
  * Private/Shared context functionality has been improved.
  * Removal of the password change reminder from the Edge Web Console - this was to support Edge deployments which are not connected to Internet.

## Release 1.60.0

This minor release includes:
* Support for `sttSpeechContexts` in **AudioCodes API** - can be used to pass hints to recognition. 
  * Ability to pass additional parameters through `sttGenericData` parameter coming soon 
* Password strength check compliant with latest NIST guidelines.

## Release 1.59.2

This maintenance release includes:
* Improved NLU for IVR prompt intent detection (contact support@voicegain.ai if you are interested in this feature) 

Issues fixed:
* #rcj-538: NPE in AudioCodes API when websocket closed
* #tsw-3: Default language selection in new Transcribe App project

## Release 1.59.1

This maintenance release includes:
* Ability to configure external document and object storage for Edge deployment
* Maximum persist time for meeting transcripts on Cloud has been increased from 7 to 31 days (this is in /asr/meeting API)
* Added password view toggle in the Web Console Login
* Multiple upgrades to 3rd-party dependencies to remove known vulnerabilities

## Release 1.59.0

Issues fixed in this minor release:
* #358: (Transcribe App) Login not working if email is not lower case
* #ocp-780: Topic generation for SA not working

This release also changes the logging library used by our back-end code.

## Release 1.58.1

This maintenance release adds in Transcribe App:
* Ability to set the transcript expiry to "Never expire"
* Improved pop-up preview for transcript in browser-capture mode.

## Release 1.58.0

This minor release includes:
* Even more accurate offline transcription
* New "rho" model which gives accurate, low latency real-time transcription (meant for API use, enabled using `"acousticModelRealTime" : "VoiceGain-rho"`).
* Custom profanity list feature - please contact us if the default profanity list does not work for your use case.
* Expired-item cleanup code - starting from June invoice you may see charges for storage - previously they were not included because cleanup code was not 100% tested.

Issues fixed:
* #rcj-536: Stop users from logging into a different application from account.type
* #rcj-534: handling unknown speaker it transcript export

## Release 1.57.0

This minor release includes:
* More accurate offline transcription.
* Improved language selection in Transcribe App.
* Private Contexts in Web Console

Issues fixed:
* #rcj-532: Microphone capture transcript in Transcribe App occasionally does not load (No Data)
* #rcj-527: Text export from Transcribe App does not have modified speaker names
* #rcw-6: (Transcribe app) An exception shows up in the console when Settings is clicked

## Release 1.56.0

This minor release includes:
* More accurate offline/batch model. Accuracy is improved in particular in lecture/zoom meeting/podcast type of audio.
* Hints in large-vocabulary continuous recognition via MRCP.
* For MRCP customers using large-vocabulary continuous recognition - we now can deliver custom intent recognition using NLU.

Issues fixed:
* Transcribe App
  * #346: Word Cloud is now shown even though the data is there 
  * #347: Named entities (NER) are not highlighted correctly 

## Release 1.55.1

This maintenance release fixes the following issue:
* #ocp-779: offline process returns NOINPUT for audio shorter than 1.25s

## Release 1.55.0

This minor release includes:
* Web Console now supports Meeting view - for viewing transcripts from /asr/meeting API
* Alpha version of the Zoom Recorder utility is available upon requests - it captures individual audio of each Zoom Meeting participant and submits it for transcription to /asr/meeting API. It works both with Voicegain Cloud and Edge.
* Improvement to internal ml-svc request routing - previously in certain scenarios the requests to ml-svc service might end up going to just a subset of available pods thus reducing performance. 

Issues addressed:
* #rcj-522: GET /asr/transcribe/{uuid}/transcript fails intermittently
* #rcj-520: support replacing acoustic model(s) with languages
  * this is in place to accommodate older pre-1.53.0 style requests which reference names of acoustic models that no longer exists (have been merged into model bundles)
  * new style requests should use `languages` parameter which is sufficient in most cases

## Release 1.54.1

This maintenance release partially addresses the following issue:
* #rcj-517: old/expired data cleanup inefficiency

## Release 1.54.0

This minor release includes:
* Edge deployment improvements:
  * Support for external S3-compatible object storage
  * Support for SSL Certificates
  * Support for Kubernetes clusters with no GPU
  * Configurable Grafana Dashboard for visualizing API use 
* Other improvements:
  * Beta version of new /asr/meeting API suitable for transcribing per-speaker audio from e.g. a Zoom Meeting 
  * Beta version of encryption for the /data API
  * Faster offline transcribe, including optimized pipeline for audio coming from S3 (or other external URL)
  * Improved English acoustic model (offline mode) - about 1.5% better accuracy on meeting / lecture type of audio
  * Beta version of a German offline acoustic model
  * Language settings in the Web Console improved - only acoustic models compatible with a selected language are shown
  * Added profanity masking option to the Transcribe Dialog

Backwards incompatibility:
* the `reuse` parameter in the /data API will now be ignored - each POST request will create a new Data Object

Fixed issues:
* #ocp-777: When afterlife is 0, offline process does not submit ERROR status to asr-api (no error callback)
* #rcj-484: better error handling for Fusebill
* #rcj-496: audio redaction no longer works for mono audio

## Release 1.53.3

This maintenance release adds:
* improved food-kappa model 

This release fixes the following issue:
* #rcj-488: spanish offline transcription ignores languages defined in the associated context

## Release 1.53.2

This release adds:
* Choice of 4 high quality TTS voices in Indian English (en-IN)

This release fixes the following issue:
* #rcj-486: support using context.asrSettingsRecognition.acousticModelRealTime for Rex resource reservation for AIVR sessions if present

## Release 1.53.1

This maintenance release addresses the following issue:
* #TranscribeApp-338: Fix countries images icon at Transcribe App - Acoustic model selection

## Release 1.53.0

This minor release includes:
* Telephony Bot API uses a more efficient method to stream audio to the recognizer. The response latency has been reduced a bit.
* Model selection mechanism has been changed. A single Acoustic Model can now support multiple languages; therefore, we added a extra language parameter that can be provided together with a model name.
* MRCP ASR now supports a dual language mode - it is possible to do recognition not knowing what language is spoken. Currently, only en/es combination is available.
* Profanity masking has been added to the Transcribe API
* In Web Console - the audio display now shows milliseconds in tooltip and when zoomed in.

## Release 1.52.0

This minor release includes:
* Browser Capture feature available in the transcribe app. This allows you to capture full audio of e.g. Zoom or MS Teams meetings.

This release addresses the following issues:
* #rcj-477: AIVR - attempt to play empty questionPrompt results in error (was re-opened)
* #rcj-475: Unable to listen to recordings of Telephone Bot API sessions

## Release 1.51.0

This minor release provides the following more accurate models:
* English real-time (streaming)
* Spanish off-line

This release addresses the following issues:
* #rcj-477: AIVR - attempt to play empty questionPrompt results in error
* #rcj-476: AIVR -the last prompt in disconnect is not being played and the hangup is not done
* #rcj-474: REX returns incorrect long result for certain utterances in recent benchmark
* #vgp-833: The startTime field datatype is "String in the spec, but web-api returns integer
* #rcj-472: Get exception when submit silence to SA
* #rcj-470: Cannot GET SA transcript
* #vgp-830: DEL SA session and DEL SA config need to be in the public API spec
* #ocp-773: offline-process occasionally return empty result
* #vgp-831: "name" field should be required when creating SA config
* #rcj-469: attempt to get /sa results returns INTERNAL_SERVER_ERROR
* #ocp-770: diarization is not returned when audio is short

Two enhancements:
* Old and/or orphan data cleanup has been moved to separate task and made faster
* Time filter has been added to the GET /data query method  

## Release 1.50.1

This maintenance release fixes the following issue:
* #rcj-463: call duration reported from offline transcription to billing is 1/1000th of what it should be

## Release 1.50.0

This minor release addresses the following issues and enhancements:
* #rcj-461: the body of a callback request with callback.format=text is empty
* #rcj-460: better handling of billing system rate-limiting errors
* #rcj-459: new audio selector for call center calls to be processed offline

## Release 1.49.3

This maintenance release fixes the following issues:
* #rcj-457: Missing influxDB entries due to identical timestamp
* #rcj-456: Long audio files (e.g. 24 hours) cause OOM
  * Max audio file duration has been limited to 8 hours
* #rcj-455: Offline session time reported to billing as real-time session

## Release 1.49.2

This maintenance release modified how offline transcription billing information is submitted to Billing in order to:
* make it more efficient,
* correct underbilling. 

## Release 1.49.1

This maintenance release upgrades the Redis server and clients to a newer version and makes changes to their configuration to prevent certain issues affecting High Availability.

## Release 1.49.0

This minor release has numerous back-end changes to improve Voicegain platform ability to handle large loads.

This release fixes the following issues:
* #rcj-448: User logs not available.

## Release 1.48.4

This maintenance release adds the following features:
* vadMode "disabled" is now supported - this turns off the VAD and may give higher accuracy where there is constant speech in presence of high volume background noise/hum
* offline processor configuration has been modified to handle more offline requests

This release includes the latest offline model. For info about improved accuracy see update on this [blog post](https://www.voicegain.ai/post/speech-to-text-accuracy-benchmark-october-2021).

## Release 1.48.3

This maintenance release fixes the following issues:
* #rcj-447: New Language Model build not working due to Cloud Function issue/change
* #ocp-768: offline process cannot transcribe mlp and truehd file because of rate limiting bug
   * This applies also to other formats which do not provide audio duration information. In addition to these files not being transcribed, other files were delayed in processing.
* #rcj-445: NullPointerException while processing sync /asr/recognize and /asr/transcribe requests with dataStore as audio

## Release 1.48.2

This maintenance release fixes the following issue:
* #rcj-444: Unnecessary check for audio file format

## Release 1.48.1

This maintenance release fixes the following issues (which impacted Edge deployments with no Internet connection):
* #rcj-442: Consider empty context model name same as null
* #rcj-441: Web Console goes blank if unable to obtain status info

## Release 1.48.0

This minor release adds or changes:
* Punctuation/capitalization and digit formatting for Spanish Transcription is now available.
* Rate limit for Edge offline queue throughput is now expressed per hour rather than per day.
* Modifications were made to allow for transcription on Edge without connection to Internet.

This release fixes the following issues:
* #rcj-439: responses of polling requests don't include word.spk for diarized requests
* #rcj-435: NullPointerException when polling a transcription session

## Release 1.47.1

This maintenance release fixes the following issues:
* #rcj-434: web-api throws LowAccountBalanceException in an **Edge** environment with a port-based license
* #rcj-433: endTimeOfCurrentBillingPeriod is found in some Developer-only accounts in prod and dev environments
* #rcj-432: NoHttpResponseException: some callbacks failing - old http library
* #rcj-431: ConverterNotFoundException: No converter found capable of converting from type [java.lang.Integer] to type [java.time.Instant]
* #rcj-430: An offline SA session (mono, no diarization) is not showing up in Dev Console
* #rcj-428: ACH payments not working

## Release 1.47.0

This minor release adds:
* Ability to host more than one model per GPU - this is of importance to Edge users who no longer will have to allocate one GPU per model.
* Improved transcript paragraph splits both in the Web Console and in the downloaded TXT file
* Improved accuracy of the Spanish offline model (the real-time model is still available only upon request)
* Improved backwards compatibility of the Cloud with the Edge deployments - it mainly relates to login behavior (SSO, etc). 
* Improved EZInit script for Edge installs. Two core improvements are:
  * uses a `voicegain` user for deployment - in the past it was using one of existing user accounts on the server
  * has been adapted and tested with Ubuntu Server - although we still recommend using Ubuntu Desktop due to its better GPU support

**Backwards incompatibility:**
* requests to `/asr/transcribe/async` API with `portal` field value but no `portal.label` specified will fail - `portal.label` is now a required value 

This release fixes the following issues:
* #rcj-427: web-api should reject requests with invalid dataobject UUID
* #ocp-767: offline process throughput rate-limit checking error when ffmpeg cannot detect input audio duration

## Release 1.46.1

This maintenance release fixes the following issues:
* #rcj-419: POST /sa sessions failing (stuck in PROCESSING)
* #rcj-418: account login API returns fields incompatible with older Edge versions
* #rcj-417: first callback always fails after idle

## Release 1.46.0

This minor release starts to **enforce rate limiting**. 
For details of about rate limiting, including the default values, 
please see this [knowledge base article](https://support.voicegain.ai/hc/en-us/articles/4411882926868-Rate-Limiting).

This release adds:
* ability to disable punctuation and capitalization in the output (rcj-411)
* session specific diarization settings for transcription (rcj-398)
* `longPersist` parameter to POST /data API (rcj-397)
* Second real-time model (faster but less accurate): `VoiceGain-rho-en-us`

This release fixes the following issues:
* rcj-414: Remove archaic words from British English dictionary
* rcj-396: Polling request is slow when there are multiple web-api instances

## Release 1.45.3

This maintenance release includes the following changes:
* Results of speech recognition which get assigned the `__garbage__` semantic tag will now be returned as NOMATCH irrespective of the confidence value w.r.t threshold.
* Diarization has been made more memory efficient
* API documentation includes info about rate limiting 

## Release 1.45.2 

This maintenance release fixes the following issues:
* #rcj-393: New session takes few extra msec to start after a longer pause between request 
* #rcj-379: customer reports that Expired transcripts are still visible (Edge deployment)

## Release 1.45.1

This maintenance release fixes the following issues:
* #rcj-386: multiple callback requests are sent for a given request
* #rcj-385: occasionally responses from recognition take extra long (incompleteTimeout) - incompleteTimeout was not behaving as per spec
* #rcj-384: Realtime session takes 1-2s to start - requests to billing were not being cached efficiently
* #rcj-383: Audio from AIVR transcription shows in the Portal under normal Transcribe 

## Release 1.45.0

The release has these main changes:
* Introduces a uniform way to handle kubeconfg in Edge deployments. This makes it easy to deploy Voicegain Edge to various Cloud Platforms.
* For Edge: moved to a different GPU runtime framework which uses GPU resource more efficiently. Allows to run more recognition sessions on same hardware.
* Optimized offline task queue - significantly higher throughput is now possible (more hours of audio transcribed in the same period of time). 
* The latency of the callback response in real-time transcription has been reduced to better support voicebot scenarios.
* Polling now goes via load-balancer URL instead of directly to individual services in order to better support rolling deployments. 
* Microphone capture in web browser applications moved away from deprecated methods

The release fixes the following issues:
* #rcj-368: callback from recognition not working (introduced when adding redis:// callback method)
* #rcj-365: Transcripts of Telephony Bot Session cannot be viewed in Web Console
* #rcj-359: Reduce delay between end of recognition and call-back response 

Known issue that is not fixed in this release:
* #rcj-380: polling requests fail to return transcript after poll.afterlife -- the workaround is to make sure that content.full includes both ["transcript", "words"]
* #rcj-377: if content.full is only ["transcript"] then the callback will not have the transcript -- it is necessary to specify ["transcript", "words"] to get any transcript in the callback 

It also provides these enhancements:
* #vgp-822: naming changes in Edge management ACP pages - uses less ambiguous names in Web Console

Additional announcements:
* We now offer advanced monitoring for Edge deployments (for a slight per-port price premium).

## Release 1.44.1

This maintenance release provides:
* Further improved accuracy of the real-time/command model.

## Release 1.44.0

This minor release provides:
* New versions of the models used for real-time and offline transcription. They provide improved accuracy. This improvement in accuracy is particularly noticeable for short real-time transcripts, like e.g. encountered in voice-bots.
* The hints feature provides new misspellings capability. 
For more info about hints see [this Knowledge Base article](https://support.voicegain.ai/hc/en-us/articles/4407993206548-Using-Hints)

This release fixes the following issues:
* #rcj-358: web-api returns "missing websocket name" by mistake
* #rcj-355: ContentType.word-tree was serialized as WordTree by mistake

## Release 1.43.6

This maintenance release fixes the following issue:
* #vgp-821: availableFeatureDetails field not retrieved properly by Edge Web Console

## Release 1.43.5

This maintenance release fixes the following issues:
* #rcj-353: completeTimeout not working in SEMI-REAL-TIME mode
* #rcj-351: submitting an offline SA session with stereo audio ended up with mono audio - this bug was introduced in release 1.42.0
* #vgp-820: allow : in hint names - new weight property

## Release 1.43.4

This maintenance release fixes the following issues:
* Certain fields not saved on a transcription record due to NPE
* Uploaded LM corpus files incorrectly reported as having wrong format/encoding
* Edge Web Console not showing all Application Modes correctly

## Release 1.43.3

This release fixes issues:
* #rcj-349: Acoustic model setting in context is not used in offline transcribe

For Transcribe App released fixes for the following:
* Issue with navigating away from microphone capture which would break the recording
* Not able to upgrade in a single step from monthly to annual and to a higher Plan
* Computation of remaining days till usage reset
* Minor issues in password entry for a new password
* Several small UI issues 

## Release 1.43.2

This release fixes issues:
* #rcj-345: On ACP, Edge configuration selection is not filtered by selected version
* #rcj-347: Invalid value for `persist`, must be a value less than or equal to `604800000`

For Transcribe App:
* Fixed several small UI issues 
* Fixed pricing values shown on Billing Plans page - was reporting price/user/month as price/month
* Fixed double counting usage for microphone transcriptions.
* Fixed error when doing transcription with Expiry set to longer than 1 Week.

## Release 1.43.1

This maintenance release:
* Changes signup text for Developer Web Console from "300 free monthly minutes available" to "$50 one-time credit available" 

## Release 1.43.0

This minor release:
* Significantly improves Hint and Language Model functionality. You can now achieve much higher accuracy using Hints and/or Language Model
* Available configurations for Edge deployments now are annotated with the compatible release range - the Web UI ensures that you can apply to your Edge cluster only compatible configurations
* New accounts get $50 credit instead of the monthly 300 minutes allowance. Old accounts retain 300 minutes allowance.

Two new Applications are being released:
* Speech Analytics App - analyze call-center calls
* Transcribe App - transcribe audio from meetings and other audio files

See [www.voicegain.ai](https://www.voicegain.ai) for how to signup.

Issues fixed:
* Memory issue affecting Offline transcription which occasionally would cause the transcription to be stuck in Processing

## Release 1.42.1

This maintenance release:
* Reduces the amount of memory used by the offline transcription tasks leaving more space that may be used for transcoding audio files. Should reduce chance of failed offline transcription.

Edge specific notes:
* It is recommended to apply this release to your Edge deployment if you are doing offline-transcription.
* This release is not relevant to Edge users using only MRCP ASR or only real-time transcription.

## Release 1.42.0

This minor release adds the following:
* OFFLINE transcription now uses ffmpeg to transcode audio - see [the list of supported audio formats](https://support.voicegain.ai/hc/en-us/articles/360050477331-Supported-Audio-Formats)
* Edge Deployment UI now shows all available versions and allows deployment of any one of them onto an Edge Cluster. Version rollback is also possible using this feature.
* data-api has been split off from the web-api - this improves robustness of the platform 
* Digit formatter has been added to transcript returned from polling real-time transcription session
* In the Cloud, added ability to increase data persistence time for individual accounts. In the past persistence was capped at 7 days.

Edge specific notes:
* data-api has been split off from web-api - it is recommended that you Rebuild to this version if you are doing a lot of audio file uploads. Overloading data-api with too many concurrent large file uploads will not longer affect speech recognition sessions in progress.

**Backwards incompatibility**:
* We have changed the `result.incrementalTranscript` field in the response from `GET  https://api.voicegain.ai/v1/asr/transcribe/{sessionId}` - the new design will better support the changing hypotheses, in particular in commbination with digit and other formatters.

This release fixes the following issues:
* #rcj-339: v1/asr/transcribe/{}/transcript?format=text API does not behave like spec w/o interval parameter
* #rcj-338: Exception in data-api when upload multiple files concurrently on Edge

## Release 1.41.0

This minor release adds the following:
* MRCP server's 3rd-party dependencies get updated to their latest versions
* Offline transcription tasks get optimized to increase the throughput
* Ability to enable digit formatting as default for a Context
* Ability to enable audio capture for all transcriptions in a Context 

## Release 1.40.2

This maintenance release:
* fixes a small bug in EZInit script
* improves diarization algorithm
* adds alerts in the recognizer 

## Release 1.40.1

This maintenance release:
* fixes issue #rcj-319: diarization setting of minSpeakers:1 and maxSpeakers:2 results in only 1 speaker identified
* adds better error handling of invalid request parameters

## Release 1.40.0

This minor release adds the following features:
* New format parameter to control payload of /asr API callbacks 
* Test button for quick check of the functionality of an Edge Deployment

## Release 1.39.0

This minor release adds the following features:
* SIP INVITE for Telephony Bot API supports now also UDP protocol in addition to TCP
* Announcements API now supports html format in addition to Markdown (md)
* Added ability to download invoices from the Web Console

## Release 1.38.0
This minor release adds the following features:
* `authConf` setting for callback authentication
* support for new mechanism to specify configuration of services deployed on Edge
* invoice API added
* changes to user-group API to support attaching groups to Contexts

The release also provides improvements in ML algorithms used for Speech Analytics.

Finally, the release fixes the following issues:
* #rcj-315: Missed packet timestamps from dual RTP stream not handled correctly
* #rcj-314: user.role is set to User by mistake

## Release 1.37.1

This maintenance release:
* improves the internal thread Executor setup to make it more resilient
* improves on the alerting service to better notify Voicegain support of production issues

## Release 1.37.0

This minor release improves the Speech Analytics App.
* We added a new type of construct that can be detected in a call. It is called Criteria and allows to conditionally combine NERs, Keywords, Phrases, etc.
* Improvements to Call Review view 

Our STT API now supports Pause and Mute for real-time transcription.

An improved offline Acoustic Model for English language is also part of this release. 

This release addresses the following issues:
* #rcj-308: A mic transcription is terminated after 10 minutes
* #rcj-305: improve handling for invalid values of fetchTimeout

## Release 1.36.3

This maintenance release adds various improvements to the Speech Analytics App (beta).

The release also adds the following enhancements to the API:
* max fetchTimeout for getting audio from a URL has been increased from 60 to 90 seconds
* it is now possible to set a diarization speaker range starting at 1
* GET /sa?detailed=false now returns numIncidents, numChannels, and numSpeakers

## Release 1.36.2

This maintenance release fixes one issue and adds one enhancement
* #rcj-303: 'missing websocket name' error in audiocodes API 
* #rcj-304: flush RT SA data faster if hypotheses allow it

## Release 1.36.1

This maintenance release switches the new account email to AWS SES and it fixes 1 issue:
* #rcj-293: differential word cloud empty on Voicegain

## Release 1.36.0

This minor release improves the Speech Analytics App.

This release addresses the following issues:
* #rcj-288: currentSentiment is all 0 for 30D period
* #rcj-286: Call resolution seems to be not calculated correctly
* #rcj-285: average Agent Score is incorrect
* #rcj-284: latest demo integration gives us empty Differential Word Cloud 
* #rcj-283: changes to sentiment in the response of GET /sa/call-stats
* #rcj-282: changes to how we show sentiment for dashboard
* #rcj-281: ensure that output from GET /sa/call-stats uses the subperiod definitions 
* #saa-13: something wrong with how the sentiment is displayed on the dash
* #saa-11: show the value of the sentiment next to smiley on call details page
* #saa-10: something wrong with the incident count
* #saa-9: tweaks to QA Form read-only view
* #saa-8: show Phrases on the analytics page
* #saa-7: show tooltip with the Phrase Tag when hovering over highlighted phrase
* #saa-6: show PROFANITY keyword in red font
* #saa-5: add values of sentiment to the Calls table
* #saa-3: Highlight Demo Information part about accuracy
* #saa-2: Edited Call Review questions do not persists
* #saa-1: wasted space on SA dashboard - 3 bottom cards

## Release 1.35.0

This minor release has the following changes:
* POST /sa now supports notifying subscribers to a STOMP topic
* Added lightweight GET /sa/{saSesId}/status polling method
* Added `detailed` query parameter to GET /sa query method

## Release 1.34.0

This minor release has the following changes:
* We are releasing a beta of an API compatible with **AudioCodes Voice AI Gateway**. Once it is in prod we will do integration testing and once AudioCodes confirms compatibility we will make an official announcement about availability.
* A `completeTimeout` setting has been added to the Context settings. This is needed for AudioCodes.
* We have added a file upload functionality to the Speech Analytics App. Now you can upload and process your own files in addition to exploring the demo content. You can find the file upload under Settings -> Integrations
* We have added a digit formatter to our transcription engine.
* The NER accuracy has been improved.
* A change to the CC-App which improves usability on mobile phones. 

This release also fixes the following issues:
* #vgp-793: Ensure that SA config does not allow use of the same tag for a Keyword and a KeywordGroup
* #rcj-236: gap value present in the json transcript export
* #rcj-261: in phrase detection - location.channel setting not working ok

## Release 1.33.0

This minor release has the following changes:
* We are switching to AWS SES as our provider for outbound emails. This should makes Password Reset and other emails more reliable.
* The Named Entity Recognition (NER) model has been improved.
* The beta Speech Analytics App adds: Account time and profile settings, users table and add new users to accounts, full time-zones list.

This release also fixes the following issues:
* #rcj-265: validate each email address for POST /user
* #rcj-260: in phrase detection - location.time setting should be in seconds
* #rcj-259: PII Redaction enhancement (defaults)

## Release 1.32.3

This maintenance release has fixes for:
* bug #rcj-262: Word Cloud has no content on Demo Integration Dash

Our mail provider has an issue that forces us to temporarily switch to a very simple forgot-password email.

## Release 1.32.2

This maintenance release adds two small improvements:
* A demo token has been added to control access to Demo Integration in Speech Analytics.
* API documentation for Speech Analytics section has been improved.

## Release 1.32.1

This maintenance release updates the SSL certificates and also fixes the following issues:
* issue #vgp-798: show the incidents on the small audio bar same way as they are shown on the detailed view 
* bug #rcj-258: Sometimes incidents count not showing on call analysis page
* bug #rcj-253: PII Redacted entities shown in audio player view

## Release 1.32.0

Limited access Beta release of the Speech Analytics App. To learn more email us at info@voicegain.ai 

## Release 1.31.1

This release fixes the following issues:
* bug #rcj-238: concurrent offline transcription fails due to VAD issue
* bug #rcj-237: submitting very short files for diarization fails with ERROR

It also adds a new offline acoustic model with higher accuracy.

## Release 1.31.0

New features in this minor release:
* Real-time Speech Analytics API - results are provided real-time via websocket 
* Improved accuracy of the main English language real-time acoustic model
* Second English language real-time acoustic model: optimized for use in IVR - provides improved accuracy on long sequences of digits
* asr.speechContext parameter to provide hint to the recognizer if a lot of digits are expected
* sessions.vadMode parameter to control music rejection - meant to be used mainly for call-center audio to reject music-on-hold
* adjusted behavior of the asr.sensitivity parameter - 0 value now corresponds to -40dbFS

This release fixes the following issues:

* bug #vgp-775: handle transcript results with no spk assigned to words
* bug #rcj-236: gap value present in the json transcript export
* bug #rcj-234: Web Console hangs soon after one opens a mic transcription

## Release 1.30.1

This maintenance release fixes the following issues:
* bug #rcj-228: Noise detected as speech
* bug #rcj-227: Real-time transcription of stereo audio files from Amazon S3 fails  

## Release 1.30.0

New features in this release:
* Improved accuracy of the acoustic models - offline and real-time
* Improved accuracy of the recognizer in Voicebot scenarios
* Ability to set default sensitivity settings from Console Web UI
* Returning ERROR instead of NOINPUT if no bytes were received by the recognizer. This makes troubleshooting of RTP streaming easier. 

## Release 1.29.0

New features in this release:
* Support for 2-channel audio streaming via RTP. This is intended mainly for telephony applications where 1 channel is e.g. caller and the 2nd channel is e.g. agent.  
An example script that demonstrates this new functionality is on our [github](https://github.com/voicegain/platform/tree/master/examples/RTP-streaming#ffmpeg-2chn-testpy).
* Added support for MRCP Recognition-Timeout parameter.

## Release 1.28.0

New features in this release:
* real-time diarization - in addition to off-line diarization which has been supported since October 2020, Voicegain transcribe now support real-time diarization
* German language is supported for offline and semi-real-time transcription and recognition 
* Built-in creditcard grammar supports Luhn check for higher accuracy. Also added Diners Card support.

This release fixes the following issues:
* vgp-773 - Incorrect NOMATCH audio zone shown in Transcribe+ for file 4490_pcm_stereo.wav
* vgp-773 - Call Metrics broken in Transcribe+
* vgp-772 - Female label attached to incorrect speaker
* vgp-771 - Left/RIght labels on Transcribe+ (virtual stereo) incorrect
* rcj-225 - Review Answers with autopopulated answer choices are not set to the answerValue of the question
* vgp-770 - Update NER list
* rcj-224 - Comparison method violates its general contract!
* rcj-223 - NullPointerException related to a /asr/transcribe request
* rcj-222 - Diarization and speaker result in virtual dual channel session displayed on UI is wrong

## Release 1.27.1

This maintenance release fixes the following issues:
* bug #vgp-769: show informative error message when submitting audio in unsupported/bad format
* bug #rcj-219: deleted user account difficult to recover
* bug #rcj-218: gaps in audio being played in Telephony Bot API
* bug #rcj-216: Call transcripts from Call Sessions not being shown sometimes

## Release 1.27.0

New features in this release:
* The signup process has been switched from using 2 emails (one from billing and one for the password set link) to using just a single email - it will contain both the info about the billing account created and the link to set the password. This will make the process simpler and reduce the number of password set emails going to a Spam folder. 

## Release 1.26.0

New features in this release:
* Support for "stereo" audio in TWIML audio streaming protocol. This allows for real-time transcription of calls made to Twilio Platform - inbound and outbound channels are transcribed individually. Audio capture (recording) for this audio format is also supported.

## Release 1.25.2

This maintenance release fixes the following issue:
* bug #rcj-212: Creating new account results in NPE. This resolves the sign-up issue reported earlier.

## Release 1.25.1

This maintenance release has fixes for the following issues:
* bug #rcj-208: Long audio prompts not played completely in AIVR (Telephone Bot API)
* bug #rcj-205: TTS preview not working in Web Console

## Release 1.25.0

New features in this release:
* New Signup - we have simplified the form
* Improved WordCloud - we are using smarter algorithm to generate words and two-word phrases for it. It also now draws faster. 

## Release 1.24.0

New features in this release:
* Spanish language support for off-line transcription. This is beta. Please email us at support@voicegain.ai if you would like Spanish recognizer to be enabled on your account.
* PII Redaction has been added to Speech Analytics API. Can be used to remove any chosen Named Entities from the audio and the transcript.
* Added support for 3 more new Named Entities that are recognized: ADDRESS, CC (credit card), and SSN. 

This release has fixes for the following issues:
* bug #vgp-766: Links to Transcript from Context Dash do not work
* bug #rcj-196: Microphone transcribe from Web Console is not working on Edge

## Release 1.23.1

This maintenance release has fixes for the following issues:
* bug #rcj-195: Some short speech audio not being recognized in OFFLINE mode
* bug #rcj-194: RTP streaming in 8-bit format fails intermittently

In this release also the accuracy of the real-time and offline acoustic models has been improved.

## Release 1.23.0

New features in this release:
* Support for RTP streaming fully tested and working - includes ulaw and L16 audio formats
* Improved support for simultaneous grammar recognition and large-vocabulary transcription - use of custom language models for large-vocabulary transcription now possible

## Release 1.22.0

New features in this release:
* Recognition API now able to return results using websockets (previously only transcription API was using websockets for results)
* Added support for simultaneous grammar recognition and large-vocabulary transcription.  
* Offline Speech Analytics API released (**beta**)
* Phone calls made to Telephony Bot API now being processed using Speech Analytics in addition to being transcribed
* Improvements in the Language Model feature

Fixes:
* bug #rcj-182: certain short audio files (<1.5s) not being transcribed 
* bug #rcj-180: edits arrive out of order over websocket (issue with ExactTimeCorrectingWordQueue)

## Release 1.21.0

New features in this release:
* Telephone Bot API now supports SIP INVITE
* Transcript table caching in the UI to improve responsiveness
* Improved how asr.sensitivity is used for start-of-speech detection

Fixes:
* bug #rcj-179: Hints generating misrecognitions
* bug #rcj-178: AWS Exception when creating new AIVR app

## Release 1.20.0

New features in this release:
* improved Edge related web UI
* improved Transcribe UI (#vgp-759 -  multiple enhancements)
* improvements to API around websockets (performance and resource use)
* admin tool improvements

#### Bug Fixes and Enhancements
* bug #rcj-164: Certain WAV files with ulaw encoding not being transcribed
* bug #vgp-757: Show message when refill attempt fails
* enhancement #vgp-761: Enable Delete on expired transcription sessions
* enhancement #rcj-158: Terminate sessions which have not received any audio within 30 seconds of being created
* enhancement #rcj-157: Terminate real-time sessions with an audio gap of more than 30 seconds

## Release 1.19.2

This maintenance release fixes the following bug:
* bug #vgp-758: Error when trying to transcribe audio from URL via portal

It also adjusts the CPU and memory settings for a couple of services in order to be able to handle larger loads.

## Release 1.19.1

This maintenance release fixes the following bug:
* bug #rcj147: Async transcribe result cannot be viewed in cc-app

## Release 1.19.0

New features in this release:
* Keyword and profanity detection in Transcribe+ page (beta)
* Ability to choose real-time or off-line acoustic models for single-GPU Edge deployments
* Delete function added to Transcribe page
* More accurate real-time acoustic model

#### Bug Fixes 
* bug #779: Audio receiving websocket closed too late

## Release 1.18.2

This maintenance release fixes the following bug:
* bug #768: Problems with accounts with business name containing comma.

and ads the following enhancement:
* enhancement #770: add `builtin:speech/transcribe` as another option to specify transcription in MRCP 

The release also includes a higher accuracy offline Acoustic Model

## Release 1.18.1

This maintenance release provides fixes for the following bugs:
* bug #766: Websocket that returns recognition results is incompatible with OkHttp3

The release also improves the look of transcripts on Transcript+ (beta) page

## Release 1.18.0

### Major Features and Improvements
Features in this release:
* Transcribe+ page (beta)
* Switching main url from https://portal.voicegain.ai to https://console.voicegain.ai

### Breaking Changes
* Old portal url https://portal.voicegain.ai is now a redirect to new url https://console.voicegain.ai

#### Bug Fixes 
* bug #764: API requests to incorrect URLs sometimes did not return 404
* bug #755: The account without billing permission cannot see transcript result

### Known Issues
* bug #751: If voice is omitted from `<Connect><Stream>` request then the audio will play garbled

## Release 1.17.0

### Major Features and Improvements
* Added support for large vocabulary transcription over MRCP
* Websocket that returns transcription results is now configurable to be either: a plain websocket, or a websocket that uses STOMP protocol.

### Breaking Changes
* none

### Bug Fixes and Other Changes
since Release 1.16.0
* bug #741: Programmable IVR does not wait with start timers till prompt finishes playing to human
* enhancement #742: remove underscore from variable values inserted into TTS prompts

## Release 1.16.0

### Major Features and Improvements
* Support for transcription on Twilio Media Streams - provides `TwiML <Gather>` like functionality
* Ability to select different audio channel per session
* RTC-API supports large vocabulary transcription
* RTC-API supports prompt playback from external URLs
* RTC-API `input` action supports non-bargeinable intro prompt and bargeinable main question prompt 
* added continuous recognition option

### Breaking Changes
* `audio.channel` parameter has been deprecated  in /asr/recognize and /asr/transcribe APIs

### Bug Fixes and Other Changes
since Release 1.15.1
* bug #738: Unable to create accounts starting on digit  
* bug #736: 'vars' not returned when using literal tags in grammar
* bug #735: Creating a new broadcast websocket makes the old ones temporarily disappear
* bug #733: Prompt text field not returned in events for AIVR Sessions
* enhancement #729: Add question.audioResponse.questionPrompt to AIVR Callback response
* enhancement #728: Allow AIVR App to send csid either in path or in query or in the body
* enhancement #727: add support for start timers in /asr/transcribe
* enhancement #726: add DTMF support for JJSGF grammars
* enhancement #723: add support for large vocabulary transcription to AIVR
* enhancement #722: add to AIVR support for prompts where text is an http URL to the audio to be used
* enhancement #721: add support for start timers in AIVR processing loop
* enhancement #718: JJSGF tweak - do not require rule names on the left side to be <>
* enhancement #716: allow timeout to control the stop of transcription

## Release 1.15.1

This maintenance release provides fixes for the following bugs:
* #711: Failed to play audio in RTC-API
* #709: Adding a clip to clipstore fails on production
* #707: Occasional IllegalStateException in Twilio Media Stream 

It also is a beta release of the speaker diarization feature.

## Release 1.15.0

### Major Features and Improvements
* Support for speech recognition on Twilio Media Streams via TwiML `<Connect><Stream>` command
  * [Voicegain Speech-to-Text integrates with Twilio Media Streams](https://www.voicegain.ai/post/announcing-twilio-twiml-connect-stream-support) blog post
  * [How to use Voicegain with Twilio Media Streams](https://www.voicegain.ai/post/how-to-use-voicegain-with-twilio-media-streams) blog post
* Prompt Manager for dynamic concatenation for prerecorded prompts - can be combined with TTS - currently available only from TwiML `<Connect><Stream>`
* Offline transcription supports output of [music] labels
* Improved accuracy from ASR through enhancements to the search algorithm 
* DTMF detection from audio stream

### Breaking Changes
* none

### Bug Fixes and Other Changes
since Release 1.14.
* enhancement #693: Limit duration of microphone transcription to 100 minutes - prevents runaway transcription if someone leaves the microphone on.
* enhancement #692: Support externally controlled start of timers on ASR
* enhancement #691: Add password strength check to Portal password change page
* enhancement #683: Signup will auto-approve all requests for RTC-API feature

## Release 1.14.0

### Major Features and Improvements
* Significantly reduced time for recognition and transcription session setup.
* JJSGF now supports tags - both semantics/1.0-literals and semantics/1.0 formats.
* Improved accuracy for both offline and real-time acoustic models.

### Breaking Changes
Size of inline audio submitted to /asr/recognize or /asr/transcribe has been limited to 4MB


## Release 1.13.1

This maintenance release provides fixes for the following bugs:
* #661: User logs not accessible
* #654: Callback URLs do not support {sessionId}
* #651: Microphone transcription on Firefox not working - note: there is still a delay before the first words of the transcript appear in preview


Following enhancements are added:
* #657: Account lookup time has been reduced
* #656: Log all callback failures to Elastic Search so that users are able to see them

This release includes **latest acoustic models with significant improvements to accuracy**.

This release also adds minor UI improvements on Transcripts page.

## Release 1.13.0

This Minor release focuses on improving websocket streaming.

### Major Features and Improvements
* Websocket streaming now supports multiple formats, including u-Law 8000 Hz 
* Added support for PCM Floating-Point 32-bit audio
* Added control for recording and transcription to RTC Apps

### Breaking Changes
None

### Known issues
* JJSGF grammar does no support tags yet.
* issue #651: Microphone transcription on Firefox not working 
* issue #607: some customers reported problem uploading some mp3 files


### Bug Fixes and Other Changes
since Release 1.12.1
* bug #631: No callback received from /asr/recognize
* bug #630: Wrong Content-type returned from /data/{uuid}/file 
* bug #629: Irrelevant parameters returned for audio stream WEBSOCKET
* bug #617: Final DELETE callback has the event from previous sequence
* bug #616: Transfer reported in RTC Callback misses prompt payback event
* bug #573: Websocket streaming locks up due to issues inside 3rd-party library
* enhancement #626: Pass value of default vice to RTC Callback
* enhancement #625: Set the value of audio.channel in transcription result 
* enhancement #624: Values of callIsBeingRecorded and toBeTranscribed passed to RTC Callback
* enhancement #620: Add to AIVRApp two new fields: recordCalls and percentCallsToTranscribe


## Release 1.12.1

This maintenance release provides fixes for following bugs plus provides 2 enhancements:
* issue #610: Issues with Listen access to recording and transcript of just ended call
* issue #609: Phone number deletion failing
* enhancement #613: Disable Delete button for phone numbers used in app - delete would fail anyway
* enhancement #611: Provide info about time needed for new RTC App to become active

## Release 1.12.0

This Minor release fixes some bugs in the RTC Callback API release last week plus provides some usability enhancements

### Major Features and Improvements
* TTS preview added - you can no listen to the sound of the TTS voices before making a choice
* API Spec document open in full frame - improves navigation within the Spec
* Improved usability of User Management

### Breaking Changes
None

### Known issues
* JJSGF grammar does no support tags yet.
* issue #607: some customers reported problem uploading some mp3 files
* issue #582: Microphone transcription on Firefox gets stuck (never completes)

### Bug Fixes and Other Changes
since Release 1.11.1
* bug #606: Failed user add was silently ignored
* bug #601: Two DELETE callbacks in one session
* bug #600: error termination value now supported
* enhancement #606: Call Sessions table is by default now sorted in descending order
* enhancement #604: Base `user` role is not explicitly present
* enhancement #602: Add sanity stop for runaway RTC session

## Release 1.11.0

This Minor release introduces the RTC Callback API for telephony applications of speech recognition.

### Major Features and Improvements
* New RTC API Application mode -- provides tools and APIs to build speech-enabled telephone applications
  * purchase phone numbers
  * attach phone numbers to RTC Apps
  * control flow of you RTC App using Web Callback API
* Guide, Help, and API Spec information has been improved. 

### Breaking Changes
* Not really a breaking change but names of two Application Modes have changed:
  * Dev API -> STT API (to differentiate from new RTC API)
  * ASR -> MRCP ASR 

### Known issues
* JJSGF grammar does no support tags yet.
* issue #582: Microphone transcription on Firefox gets stuck (never completes)

### Bug Fixes and Other Changes
since Release 1.10.1
* bug #566: Link to Terms of Service not visible in Portal
* enhancement #585: Alphabetical sorting of contexts
* enhancement #583: Direct link to support ticket 
* enhancement #567: Separate Guide Card for each App

## Release 1.10.0

### Major Features and Improvements
* Added basic JJSGF grammar support (no tags yet)
* Changes to Transcription Mode UI
* Microphone capture has better compatibility with different browsers
* Only a single session is billed if running multiple sessions on same audio input

### Breaking Changes
* none

### Known issues
* JJSGF grammar does no support tags yet.

## Release 1.9.0

### Major Features and Improvements
* New API to generate short-lived JWT authentication tokens. 
* Ability to set `allowedOrigins` for web API requests to allow cross-origin  requests (CORS)
* More responsive TTS - part of IVR functionality coming in 2.0.0
* Real-time Speech-to-Text price is now 1.25 cent/minute

### Breaking Changes
* none

## Release 1.8.1

This maintenance release provides fixes for following bugs:
* #534: Transcript Review page stops spinner before the audio file has finished loading
* #530: Last part of incremental word-tree content missing in web api response
* #528: GREG chart tool-tip showing incorrect values

## Release 1.8.0

### Major Features and Improvements

* New `word-tree` format for delivering incremental transcription results.
* GREG test grammars can be uploaded in addition to being retrieved from a URL.

### Known issues
* Audio Sender Daemon does not support encryption yet. 
* Grafana Dashboards configurations are very basic

### Breaking Changes
* Preemptible flag is now reserved/internal use.

### Bug Fixes and Other Changes
since Release 1.7.1
* bug #518: Details of tiered pricing not being shown
* bug #515: Under-billing for long offline transcriptions
* bug #513: In transcript review - speech audio is colored as if it was mere sound
* enhancement #524: Allow to set the number of rows on one page for GREG experiment view
* enhancement #523: Better GREG Data Upload instruction video

## Release 1.7.1

This maintenance release provides fixes for following bugs:
* bug #506: Frequency of timestamps in TXT transcript export too high.
* bug #505: minimimumDelay setting for Live Transcription websocket has no effect.

With this release the free $1.25 credit for new accounts has been reduced to $0.25 but **all accounts now get 600 free speech-to-text minutes monthly**. 

## Release 1.7.0

### Major Features and Improvements

* Signup has been opened to gmail and other non-business email addresses 
* Improved acoustic model for offline transcription. 
* Improved efficiency of the core ASR recognizer.
* Many fixes and enhancements around Live Transcription.

### Known issues
* Audio Sender Daemon does not support encryption yet. 
* Grafana Dashboards configurations are very basic

### Breaking Changes
* none

### Bug Fixes and Other Changes
since Release 1.6.3
* bug #499: (and related) Session gets stuck in load testing.
* bug #492: Unable to enter person's names with dashes.
* bug #488: OutOfMemory error when processing many large requests with inline audio
* bug #487: Stopped Live Transcription stuck in Online-Starting state
* bug #485: Running Live Transcription with audio.capture flag does not result in working Transcript Preview
* bug #481: Secondary output websocket shows controls enabled even though it is not a control websocket
* bug #479: Unable to change delay for websocket
* bug #474: Unable to change context for websocket
* bug #473: "missing websocket name" error when running REAL-TIME together with SEMI-REAL-TIME sessions
* bug #469: 504 error when submitting file for transcription - timeout
* enhancement #503: IVR-Proxy will now work behind HTTP Proxy. 
* enhancement #483: Add a label to each Live Transcription session
* enhancement #482: Improve archives of Live Transcription
* enhancement #478: Improve response of adding a new Websocket 


## Release 1.6.3
  This maintenance release provides an improved acoustic model for off-line transcription. 


## Release 1.6.2
  This maintenance release fixes bug #467 

### Bug Fixes and Other Changes
  * bug# 467: Offline transcription of long files sometimes does not report completion - remaining issues have been fixed


## Release 1.6.1
  This maintenance release fixes the two Issues reported after Release 1.6.0 

### Bug Fixes and Other Changes
  * bug# 468: IVR-Proxy not starting. 
  * bug# 467: Offline transcription of long files sometimes does not report completion.


## Release 1.6.0

Minor release that adds a much faster offline transcription and a more accurate acoustic model.

### Major Features and Improvements

* Offline transcription in Edge deployments has been sped up by approximately a factor of 10x.  
* New acoustic model for offline transcription has significantly improved accuracy. 
* Previous IVR product has been renamed ASR to better reflect its core functionality. A new product supporting complete end-to-end functionality will be release in June/July.

### Known issues
* Audio Sender Daemon does not support encryption yet. 
* Grafana Dashboards configurations are very basic

### Breaking Changes
* none

### Bug Fixes and Other Changes
since Release 1.5.1
* bug #459: Fixed issue that prevented Edge transcription when connection to Cloud was not possible.
* bug #450: Fixed issue with resetting expired password.
* bug #443: Fixed resource use issue for user log collection.
* bug #442: Fixed logout issue from Edge portal.
* bug #439: Resolved occasional failure of ASR resource reservation on Edge.
* enhancement #460: Cache current balance on Edge to reduce number requests. 


## Release 1.5.1

Maintenance release that fixes several bugs.

### Major Features and Improvements
Added in version 1.5.0:
* Web portal is now organized into Voicegain Apps (Transcribe, IVR, etc.) making it easier to navigate the many options by hiding those not applicable to the currently selected App. 
* Changed New Account Signup form to a wizard style with better explanation of choices available. 
* Edge deployment now has its own influxDb and Grafana instance.

### Known issues
* Audio Sender Daemon does not support encryption yet. 
* Grafana Dashboards configurations are very basic

### Breaking Changes
* none

### Bug Fixes and Other Changes
Only bugs present in the previous 1.5.0 release are listed.
* bug #441: Links from Guide Card to support articles fail to login into Zendesk
* bug #435: Training mode not supported correctly on Edge Portal
* bug #433: New User Wizard (joyride) not reflecting changes in the UI
* bug #432: Language Model selection now showing LMs published from other Contexts 
* bug #431: Billing not tracking all the usage
* enhancement #437: Added "Training" option to signup wizard
* enhancement #430: Improved icons in Transcribe View playback controls 
* enhancement #428: Grafana login - auto click OAuth button 

## Release 1.5.0

Minor release that modifies the Web Portal UI and updates the versions of some core 3rd party libraries.

### Major Features and Improvements
Added in version 1.5.0:
* Web portal is now organized into Voicegain Apps (Transcribe, IVR, etc.) making it easier to navigate the many options by hiding those not applicable to the currently selected App. 
* Changed New Account Signup form to a wizard style with better explanation of choices available. 
* Edge deployment now has its own influxDb and Grafana instance.

### Known issues
* Audio Sender Daemon does not support encryption yet. 
* Grafana Dashboards configurations are very basic

### Breaking Changes
* none

### Bug Fixes and Other Changes
Only bugs present in the previous 1.4.1 release are listed.
* bug #413: Logs query not respecting date range selection.
* bug #393: Insufficient resources allocated to ElasticSearch node.
* bug #388: Audio Daemon JVM stats sending to influxdb fails on prod.
* enhancement #392: CC-App viewer embedded into Websocket control page.

## Release 1.4.1

Maintenance release that fixes several issues and adds minor enhancements.

### Major Features and Improvements
Added in version 1.4.0:
* Core Functionality
  * Web portal now has a built-in log viewer.
  * Configurable inactivity timeout has been added.
* Web UI
  * Many small UI changes improving usability  
* IVR-Proxy
  * Encryption option has been added. Efficiency has been improved. It also now reports version, which makes it easy to spot when you are running an older version and need to update.
* Edge Deployment has now been tested and is out of Alpha status.

### Known issues
* Audio Sender Daemon does not support encryption yet. 
* Grafana Dashboards configurations are very basic

### Breaking Changes
* none

### Bug Fixes and Other Changes
Only bugs present in the previous 1.4.0 release are listed.
* bug #385: Log query error messages not shown in the Web UI
* bug #380: Filtering by service name in log query not working
* bug #379: MRCP chart not showing data for IVR-Proxy sessions
* bug #374: Edge portal has link to MRCP Proxy page
* bug #373: Some Edge portal Cloud links point to dev
* enhancement #378: Refresh button for MRCP proxy page.


## Release 1.4.0

Minor release adding features and improvements as well as bug fixes.

### Major Features and Improvements
Added in this version:
* Core Functionality
  * Web portal now has a built-in log viewer.
  * Configurable inactivity timeout has been added.
* Web UI
  * Many small UI changes improving usability  
* IVR-Proxy
  * Encryption option has been added. Efficiency has been improved. It also now reports version, which makes it easy to spot when you are running an older version and need to update.
* Edge Deployment has now been tested and is out of Alpha status.

### Known issues
* Audio Sender Daemon does not support encryption yet. 
* Grafana Dashboards configurations are very basic

### Breaking Changes
* none

### Bug Fixes and Other Changes
Only bugs present in the previous 1.3.3_beta release are listed.
* bug #357: https://portal.voicegain.ai/billing url fixed
* bug #338: Unable to control certain broadcast websockets
* bug #337: Websocket detail page blank for certain websockets
* bug #336: Audio Sender link downloads incorrect configuration if name mistyped
* enhancement #367: SSO sends directly to destination if only one destination available
* enhancement #362: Format of "My Status" card has been improved
* enhancement #349: MRCP chart shows data specific to Context in which it is viewed
* enhancement #342: Broadcast Websockets can now be deleted
* enhancement #335: Add option to choose encryption for IVR Proxy at download link


## Release 1.3.3_beta

Maintenance release that fixes several issues and adds minor enhancements.

### Major Features and Improvements
(Info carried over from 1.3.0_beta)
* Core Functionality
  * Support for multiple Acoustic models - may be configured in ASR Settings for Contexts and for each API request
* IVR
  * Added to GREG Tool ability to run Experiments on external ASR. (1.3.1_beta adds preview of new GREG interface)
  * Added downloadable IVR-Proxy for interfacing local MRCP Clients to Voicegain ASR in the Cloud.
* Transcription
  * Redesigned the Transcript Review UI.
  * Added highlighting of non-speech sound and unrecognized speech.
  * Added microphone input capture.
* Other
  * Added Voicegain sign-up dialog form (previously new accounts had to be created using Admin tool).
* Speech.Works 
  * Transcript Review page has been changed to be the same as the new page in Voicegain Portal

### Known issues
* Edge deployment is still in Alpha status. It is functional for Trial use. Can be enabled upon Customer request.
* Audio Sender Daemon does not support encryption yet. 
* Grafana Dashboards configurations are very basic
* issue #322: OAuth sign-in to Grafana does not work if a session has been open for a while

### Breaking Changes
* none

### Bug Fixes and Other Changes
Only bugs present in the previous 1.3.2_beta release are listed.
* bug #321: Error when creating a new account with business name containing a hyphen
* bug #317: Deleting user via Admin Console does not work
* bugs #314,316: Grafana - uses can see the main dashboard, but cannot see their Account dashboards
* enhancement #320,325: Modifications for Sign-Up form and page (incl. email validation)
* enhancement #318: Add IVR chart for MRCP messages


## Release 1.3.2_beta

Maintenance release that fixes several issues and adds minor enhancements.

### Major Features and Improvements
(Info carried over from 1.3.0_beta)
* Core Functionality
  * Support for multiple Acoustic models - may be configured in ASR Settings for Contexts and for each API request
* IVR
  * Added to GREG Tool ability to run Experiments on external ASR. (1.3.1_beta adds preview of new GREG interface)
  * Added downloadable IVR-Proxy for interfacing local MRCP Clients to Voicegain ASR in the Cloud.
* Transcription
  * Redesigned the Transcript Review UI.
  * Added highlighting of non-speech sound and unrecognized speech.
  * Added microphone input capture.
* Other
  * Added Voicegain sign-up dialog form (previously new accounts had to be created using Admin tool).
* Speech.Works 
  * Transcript Review page has been changed to be the same as the new page in Voicegain Portal

### Known issues
* Edge deployment is still in Alpha status. It is functional for Trial use. Can be enabled upon Customer request.
* Audio Sender Daemon does not support encryption yet. 
* Grafana Dashboards are not configured yet

### Breaking Changes
* none

### Bug Fixes and Other Changes
Only bugs present in the previous 1.3.1_beta release are listed.
* bug #312: Wrong URL returned for Audio Sender bootstrap download link
* bug #311: Expiry time for Audio Sender bootstrap download link is shown in UTC
* bug #309: Wrong websocket url returned for real-time transcription on Prod
* bug #306: Stop words shown in word cloud for Transcript Review page
* bug #305: After sign-up from the form account web name is derived from owner name instead of company name
* bug #304: No ASR settings visible if account has no premium features
* enhancement #320: Sign-up form has been modified 
* enhancement #313: Redeploy button has been added to Edge Deployment page
* enhancement #307: Refresh button added to ASR Availability card
* enhancement #301: Improved Wizard for EZSetup of Edge Deployment
* enhancement #298: In new GREG show audio hash instead of id and allow copy of either
* enhancement #295: Better file names for downloaded transcripts


## Release 1.3.1_beta

Maintenance release that fixes several issues and adds minor enhancements.

### Major Features and Improvements
(Info carried over from 1.3.0_beta)
* Core Functionality
  * Support for multiple Acoustic models - may be configured in ASR Settings for Contexts and for each API request
* IVR
  * Added to GREG Tool ability to run Experiments on external ASR. (1.3.1_beta adds preview of new GREG interface)
  * Added downloadable IVR-Proxy for interfacing local MRCP Clients to Voicegain ASR in the Cloud.
* Transcription
  * Redesigned the Transcript Review UI.
  * Added highlighting of non-speech sound and unrecognized speech.
  * Added microphone input capture.
* Other
  * Added Voicegain sign-up dialog form (previously new accounts had to be created using Admin tool).
* Speech.Works 
  * Transcript Review page has been changed to be the same as the new page in Voicegain Portal

### Known issues
* Audio-Sender bootstrap download not fully configured yet. Will make an announcement when it is ready.
* Edge deployment is still in Alpha status. It is functional for Trial use. Can be enabled upon Customer request.
* Audio Sender Daemon has to be deployed manually. It also does not support encryption yet. 

### Breaking Changes
* none

### Bug Fixes and Other Changes
Only bugs present in the previous 1.3.0_beta release are listed.
* bug #280: Prevent opening transcription viewer in transcription is in error state
* bug #283: SSO to Grafana analytics dashboard does not work
* bug #284: MRCP and IVR-Proxy suffer packet loss under concurrent load
* bug #286: Web-api in on-prem environment should not attempt to talk to Billing API directly 
* bug #292: Data usage not monitored propertly due to missing Cloud Function Permission
* enchancement #270: Modified text of the Billing emails to add clarity
* enchancements #275,277, 278: Add Corpus dialog specifies expected file type, size, storage cost, and prevents upload of files that are too large
* acoustic model: VoiceGain-rt-ivr-en-us:13 (reduced error from 0.0857 to 0.0831)


## Release 1.3.0_beta

Minor release that adds extra IVR and Transcription functionality.

### Major Features and Improvements
* Core Functionality
  * Support for multiple Acoustic models - may be configured in ASR Settings for Contexts and for each API request
* IVR
  * Added to GREG Tool ability to run Experiments on external ASR.
  * Added downloadable IVR-Proxy for interfacing local MRCP Clients to Voicegain ASR in the Cloud.
* Transcription
  * Redesigned the Transcript Review UI.
  * Added highlighting of non-speech sound and unrecognized speech.
  * Added microphone input capture.
* Other
  * Added Voicegain sign-up dialog form (previously new accounts had to be created using Admin tool).
* Speech.Works 
  * Transcript Review page has been changed to be the same as the new page in Voicegain Portal

### Known issues
* Audio-Sender bootstrap download not fully configured yet. Will make an announcement when it is ready.
* Edge deployment is still in Alpha status. It is functional for Trial use. Can be enabled upon Customer request.
* Audio Sender Daemon has to be deployed manually. It also does not support encryption yet. 

### Breaking Changes
* none

### Bug Fixes and Other Changes
Only bugs present in the previous 1.2.2_beta release are listed.
* bug #190: Incorrect parsing of urls with websocket names containing dot '.'
* bug #203: Gateway timeout when creating a Language Model
* bug #206: Offline transcription does not report certain Errors (stuck on Fetched)


## Release 1.2.2_beta

Maintenance release in order to fix 2 breaking bugs.

### Major Features and Improvements
None in this maintenance Release.

### Known issues
* Edge deployment is still in Alpha status. Disabled by default. Can be enabled per Customer Account upon request.
* Cloud IVR has not passed full test suite yet. Disabled by default. Can be enabled per Customer Account upon request.
* Audio Sender Daemon does not support encryption yet.

### Breaking Changes
* Broadcast Websocket functionality not longer part of the default set of features.

### Bug Fixes and Other Changes
* bug #185: Unable to generate JWT from Portal (Context Web Settings not visible in Web UI)
* bug #181: Websockets control page not visible in Web UI (even for accounts with the websocket broadcast feature)

## Release 1.2.1_beta

Maintenance release in order to fix issues with Preemptible GPU instances. 

### Major Features and Improvements
* Flexible mechanism to allocate various types of GPUs to ASR instances. Circumvents the problem with certain GPUs temporarily not being available in the Cloud.

### Known issues
* Edge deployment is still in Alpha status. Disabled by default. Can be enabled per Customer Account upon request.
* Cloud IVR has not passed full test suite yet. Disabled by default. Can be enabled per Customer Account upon request.
* Audio Sender Daemon does not support encryption yet.

### Breaking Changes
* Broadcast Websocket functionality not longer part of the default set of features.

### Bug Fixes and Other Changes
* bug #178: NullPointerException caused by an invalid request for /asr/recognize
* bug #177: Fixed incorrect Uptime computation for Voicegain ASR
* enhancement #176: Added Announcements on home page

## Release 1.2.0_beta

This release adds fine-grained control of features available to various types of accounts.

### Major Features and Improvements
* More convenient Billing status info and control from within the Portal.
* Fine-grained control of features enabled for each account.  This allows Voicegain to control access to features that still are still in limited relase to certain accounts only.
* Enhanced Admin/Account Provisioning Portal - password reset, referrer/referral, premium features, etc.

### Known issues
* Edge deployment is still in Alpha status. Disabled by default. Can be enabled per Customer Account upon request.
* Cloud IVR has not passed full test suite yet. Disabled by default. Can be enabled per Customer Account upon request.
* Audio Sender Daemon does not support encryption yet.

### Breaking Changes
none

### Bug Fixes and Other Changes
* bug #167: Release Notes not being displayed.
* bug #170: Fixed slow redraw of modified words in CC-App
* bug #171: Login failing due to case difference is user email
* enhancement #173: Favicons different between various apps and prod/QA/dev
* enhancement #174: CC-App supports Account landing page

## Release 1.1.0_beta.2

This release adds functionality that did not make it into the initial release. It also fixes several bugs.

### Major Features and Improvements
* Added ASR engine resource status monitoring to Voicegain Portal UI
* Added Password strength checking
* Added Release Notes info to Voicegain Portal UI
* All three billing styles (manual-refill, auto-refill, invoice) now supported for Enterprise Voicegain customers. Speech.Works customers are created with manual-refill style.
* Provisioning&Admin Portal shows 3 new account fields: referrer, referral, billingStyle.

### Known issues
* Edge deployment is still in Alpha status - please contact us before attempting Edge Deployments
* Cloud IVR has not passed full test suite yet. Also, it lacks documentation. Please contact us if you would like to test Cloud IVR.
* Audio Sender Daemon does not support encryption yet.

### Breaking Changes
none

### Bug Fixes and Other Changes
Most of the bugs fixed in this release are related to login/authentication and to working with Language Models.
* bug #142: Provisioning Portal times out after login.
* bug #143: ASR resets occasionally in the middle of transcription. Was due to empty request to NLM.
* bug #144: Password lockout was mistakenly set to occur only after one mistake. Has been increased to 5.
* bug #145: 401 errors when logging in after a period of inactivity
* bug #147: Service name at the end of the URL in the password (re)set email incorrect.
* bug #148: New Language Models not shown unless user has Manager role
* bug #149: Language Model created as Built-in shows up as User model
* bug #153: Bad redirect from Password Set Dialog
* bug #158: Language Model card for a Context is not showing all the models
* bug #160: Building a Built-In model fails
* bug #161: Ensure correct results are returned from Language Model Query (built-in models, etc.)
* bug #162: Transcription with built-in Language Models fails at initial checks
* bug #163: Offline transcription with built-in Language Model not working
* minor bugs #150, #157

## Release 1.0.0_beta.1

This is a first public release of Voicegain Speech-to-Text Platform.

### Major Features and Improvements
This being a first public release, here is a list of key features of the Voicegain platform:
* Cloud based Speech-to-Text API supporting both Transcription (large vocabulary) and Recognition (limited context-free grammars)
* MRCP/VXML/GRXML compatible ASR - tested with Dialogic and Aspect (Voxeo) VXML platforms
* Real-Time transcription - core Real-Time Speech-to-Text engine plus tools like: Audio Sender, Web UI for managing multiple transcription channels, Web based client for displaying live transcriptions
* Voicegain Enterprise Web Portal
* Simplified Transcription only Web Portal (Speech.Works)

### Known issues
* Edge deployment is still in Alpha status - please contact us before attempting Edge Deployments
* Cloud IVR has not passed full test suite yet. Also it lacks documentation. Please contact us if you would like to test Cloud IVR.
* Audio Sender Daemon does not support encryption yet.

### Breaking Changes
* none

### Bug Fixes and Other Changes
* We will begin reporting bug fixes starting from the next release

