### Minor release 1.115.0 is scheduled for 2/10/2025 between 11:00pm and 12:00am US Central Time

TBD...


### Minor release 1.114.0 is scheduled for 1/20/2025 between 11:00pm and 12:00am US Central Time

This release updates Edge deployments from Mongo version 6 to 7.

New or changed functionality in the Transcribe App:
* QA-2183	TA: Advanced Search - Improve filter for selecting languages
* QA-2190	TA: Advanced Search - Improve filter for selecting participants
* QA-2189	TA: Advanced Search - Improve filter for selecting speakers
* QA-2181	TA: Advanced Search - Improve filter for selecting tags
* QA-2130	TA: The speakers table under account settings now has sorting functionality by Email.
* BE-2874	TA: Introduced fallback error page for Loading Chunk Issue
* QA-2137	TA: Show 'Copy to clipboard' message when hovering the mouse over the copy icon for the project ID
* QA-2083	TA: Until a profile picture is updated by the user, display the avatar image in the profile settings
* QA-2142	TA: When no group is available for the keyword to merge, display the option to create a new group

New or changed functionality in other platform components:
* BE-3274	Add clientParams to openId Login API
* BE-3273	Add languageDetection parameter to /sa/offline API
* BE-3317	Add support for new CVV NER in our APIs
* BE-2449	Added account API methods to add/remove Grafana support to account
* BE-3311	Enable MRCP by default on all new Developer accounts
* BE-3277	In Add Meeting Audio API method add email field to speaker or participant
* BE-3280	In response from Login API return account Grafana setting if account has Grafana enabled
* BE-3279	In Webex Meeting Bot obtain email from the participants and store it
* BE-3090	Redesign the sso.voicegain.ai 
* QA-2198	Return from login API correct set of permissions for the user even if passwordChangeRequired is true
* BE-3255	SA: Add a card that shows time distribution of various parts of the call
* BE-3287	SA: Add a filter on Direction to the Calls table
* BE-3266	SA: Add a set of fast filters for date selection to advanced search
* QA-2053	SA: Add Save button for add/edit tags
* BE-3306	SA: Better check for correct Keyword settings before saving them
* QA-2184	SA: Better indication for case when sentiment has not been computed.
* BE-3299	SA: Better read-only view of the AIVR integrations
* BE-3298	SA: Increase size of Sentiment Icons
* QA-2201	SA: Use the same rules on the call details page for considering an error as we use in the calls table
* BE-3032	Support async writes to influxdb
* BE-3292	Support CVV redaction in formatter in ASR API (transcribe, meeting and offline SA api)
* QA-2099	Web Console: Copy to clipboard info shows when user mouse hover on copy icon
* QA-2018	Web Console: Improved Edge logout behavior
* QA-2006	Web Console: Improved transcript highlight efficiency so that pagination could be removed
* QA-2082	Web Console: In user profile make clear that email field is read-only
* BE-2448	Web Console: Only select accounts show Grafana option
* QA-1867	Web Console: Show audio graph also for whisper models
* MST-332 Train Kappa model using customer data
* MST-357 Review and release the latest gpt-4o integration in llm-svc
* MST-364 Improve billing intents routing
* MST-380 Integrate new CVV feature in offline-main and ml-svc
* MST-382 Support whisper-large-v3-turbo in APIs, and decide the default model for each use case
* MST-409 Disable previous NER context when entering new context

Changes related to Integrity of Processing (fixes):
* QA-2194	Fix for section formatting in Meeting API for certain cases
* QA-2127	SA: Fix - Call Time Breakdown chart flickers when call is played.
* QA-2234	SA: Fix - Date filter in Advanced search is not working when "Include current partial period" is un-selected.
* QA-2165	SA: Fix - Keywords hidden on mouse over in advanced filter selection when a large number of keywords are selected
* BE-3291	SA: Fix - Usage in Keywords must be optional
* QA-2182	SA: Fix - Word cloud gets broken when user play call on overview page and then move to transcript page
* QA-2138	SA: Fix - Word cloud toggle is missing in Confirm Configuration pop-up.
* QA-1498	TA Edge: Fix  - Unable to detect the Browser OS Device IP for all login sessions.
* QA-2113	TA: Fix - Advanced Search: Project filter having extra white space that is covering whole page
* QA-2129	TA: Fix - behavior of the tag entry box
* QA-2110	TA: Fix - Duplicate tags shouldn't be allowed
* QA-2209	TA: Fix - Meeting Bot - Displaying 'Forgot Meeting' instead of 'Leave Meeting' for a Webex call."
* QA-2204	TA: Fix - Occasional unable to join Zoom meeting bot - Error: “Failed to join meeting"
* QA-2120	TA: Fix - Project names should not be allowed to start with spaces
* QA-2163	TA: Fix - Properly handle Projects with missing saConfig
* QA-2160	TA: Fix - Unable to move multiple files across all projects, as the pop-up page displays differently and does not allow selecting the destination.
* QA-2115	Web Console: Fix -  New User Wizard: The header menu location is incorrect; it should be highlighted in the top right corner of the page.
* QA-2013	Web Console: Fix - Alignment issue in the 'Word Cloud'
* QA-2122	Web Console: Fix - Column names e.g. Languages, Non-Real Time Models appear duplicated due to each 'ASR Transcription' and 'ASR Recognition' widget having an associated column
* QA-2124	Web Console: Fix - Context filter should either have unique column names or provide a way to distinguish between the 'ASR Transcription' and 'ASR Recognition' widgets
* QA-2216	Web Console: Fix - Edge Portal Logout is not working properly for Cloud Login.
* QA-2105	Web Console: Fix - Fields names are different in table and column on call session page.
* BE-3288	Web Console: Fix - In Phone number table, filtering by number does not work and/or is super slow
* QA-1967	Web Console: Fix - 'Level' filter is not working as expected
* QA-1953	Web Console: Fix - Log Filter is not working
* QA-1404	Web Console: Fix - Logs filter is not working
* QA-2170	Web Console: Fix - 'Max Alternatives' textbox of 'Real-Time Acoustic Model' section shouldn't accept 0 as it's value should be between 1-100
* QA-1966	Web Console: Fix - 'Services' filter is not working as expected
* QA-2097	Web Console: Fix - Sorting for Duration is not working properly on calls page.
* QA-2098	Web Console: Fix - Sorting for Events is not working properly on call sessions page.
* QA-2104	Web Console: Fix - Sorting is not working for ANI and FS UUID on call sessions page.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.113.0 is scheduled for 1/4/2025 between 11:00pm and 12:00am US Central Time

This release prepares Edge deployments for Mongo upgrade from version 6 to 7.

New or changed functionality in the Transcribe App:
* BE-3226	TA: Add a title and heading to LLM Page.
* BE-3229	TA: Disable invoices button if there are no invoices available
* QA-2045	TA: When no speaker is present, the dropdown now displays the text 'No speaker present' under project creation

New or changed functionality in other platform components:
* BE-3220	Add comfort noise to AIVR lua app
* BE-3137	Added consecutive mode to GET /sa/call
* BE-3240	ASR API now return urls with local host names and ports for internal requests
* BE-3186	Populate fields in the markers field after a call is completed
* BE-3188	Remove inactive login sessions faster
* BE-3206	SA/TA: Better design for PII Redaction settings
* BE-3255	SA: Add a card that shows time distribution of various parts of the call
* QA-2052	SA: Add a search box for selecting the time zone under account settings.
* BE-3215	SA: Add search on Time Zone selector
* BE-3269	SA: Add sorting to the lists of values in Filters for Advanced Search
* BE-3230	SA: Implement the call-section marking - audio line
* BE-3258	SA: In the Call Detail view on Debug page show the date when the call will expire
* BE-3253	SA: Mark sections of the call also on the timeline of the expanded audio view
* BE-3233	SA: New icons for Inbound Call and Outbound Call
* BE-3234	SA: On Call Detail Debug page show a link to the AIVR Session in Web Console
* QA-1989	SA: On Calls page - improved data range selector
* BE-3201	SA: Replace Topic Cloud with a pie/bar chart showing topics
* BE-3283	SA: Support for phrase text queries in Advanced Search
* BE-3237	Speed up the agent stats API
* BE-3286	Web Console: Added clarification about formatter applicability to different transcription modes
* QA-2004	Web Console: Added success message when creating a GREG Grammar
* BE-3235	Web Console: Changes on AIVR session page: 1) obtain name from session, 2) add link to SA call details
* BE-3243	Web Console: Improved ASR settings
* BE-3146	Web Console: Improve look of the User profile page
* BE-3254	Web Console: On the Context page make the languages the 1st column under ASR Transcription/Recognition grouping
* QA-1982	Web Console: Remember selected column fields so that they survive page refresh
* QA-2028	Web Console: Validate IP Address entered for IVR Proxy download

Changes related to Integrity of Processing (fixes):
* BE-3250	Copilot: Fix - Refresh of the Pusher button does not work - but logout and login back works
* BE-3252	Fix - Call-stats method sometimes fails with 500 error
* QA-1999	SA: Fix - Call Center ID filter is not working in advanced search filters.
* QA-1919	SA: Fix - Demo Calls are not generating in Demo calls in PROD.
* BE-3214	SA: Fix - Gender and Word Cloud toggles do not work
* BE-3212	SA: Fix - Mood selection does not work
* BE-3259	SA: Fix - Sorting Calls by VB Transfer does not work
* BE-3213	SA: Fix - Tooltip on NER behavior weird
* QA-2011	TA: Fix - Downloading audio file with text file issue
* QA-2046	TA: Fix - Microphone capture: The transcript scrollbar is overlapping with the start time.
* QA-2064	TA: Fix - Zoom Meeting Bot is not working properly as it is failing even after joining a Zoom meeting.
* BE-3261	TA: Fix speaker activity detection in Webex Meeting Bot if screen is being shared
* QA-1952	Web Console: Fix - "Clear Filters" button is missing in Console log Filter section
* BE-3185	Web Console: Fix - Collapsed LH menu icons are identical for many items
* QA-2058	Web Console: Fix - Password Change button should disable after first click it should not invoke two calls
* QA-1958	Web Console: Fix - Sorting of 'Business Configuration' is not working as expected
* QA-2017	Web Console: Fix - Unable to change the speed of the transcript.
* QA-2065	Web Console: Fix - Unable to download transcript under Transcribe+(beta) getting 403 (Forbidden) error.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.112.0 is scheduled for 12/06/2024 between 12:00am and 1:00am US Central Time

This release upgrades Mongo on Edge from version 5 to 6.

**Key changes related to the core APIs**
* Improver Web Console UI.
* /sa/call API supports call event marking which is utilized in the SA App to highlight various parts of the call
  * NOTE: there is a known issue with the offset for the markers being somewhat off - this will be fixed in a patch
* API for outbound calling that is used by Copilot
* Copilot User may request Call Notes generation after internal transfer

New or changed functionality in the Transcribe App:
* QA-1628	TA: Search functionality provided for Admin users when they delete any other user and transfer their projects to another user.
* BE-2934	TA: Improved design of the Webhook Settings.

New or changed functionality in other platform components:
* BE-3173	Add markers field to /sa/call
* BE-3199	Added ignore_early_media parameter to POST /aivr/dial/{destination}
* BE-2320	AIVR sessions will expire (using expiry period from AIVR App).
* BE-3149	API that will be used to launch outbound call from the Copilot
* BE-3197	Avoid storing null values under trace in each ivr_session document
* BE-3204	Flag as error sa calls that will never recover from pending status
* BE-3189	Implement the call-section marking
* BE-3117	Improve performance of /sa/call-stats
* BE-3202	In redaction, modify partial masking algorithm to always do a full mask if we have 4 or fewer digits total
* BE-3161	Mark Meetings stuck in Processing as Error within 6 hours
* BE-3109	Migrated Mongo 5 to Mongo 6 on Edge.
* BE-3156	Modify account creation code to not create grafana org if type=SPEECH-WORKS
* BE-3123	New API that can be invoked from Copilot that Agent can use to indicate transferred calls, so that Call Notes are generated and pushed.
* BE-3021	Outbound Calling from Copilot with call submitted to SA App Project
* BE-3186	Populate fields in the markers field after a call is completed
* BE-3159	SA: Add "VB Transfer" column
* BE-3203	SA: Add indicator for Fields data still loading
* BE-3163	SA: Added a filter on Call Center Call Id
* BE-3164	SA: Added more quick time period selectors for the calls
* BE-3165	SA: Do not set sorting on the search query if query includes TxtSearchTerm
* BE-3205	SA: Improved Tag editing
* QA-1874	SA: More compact columns in the Calls table
* BE-3154	SA: New design for the Keyword settings
* BE-3125	SA: New SA project type - Generic Project
* BE-3162	SA: On Call Details page show the time of the call including seconds
* BE-3158	SA: Reduce the width of columns by shrinking displayed content and headers
* BE-3201	SA: Replace Topic Cloud with a pie/bar chart showing topics
* BE-3176	SA: Show playback position and total time in audio player
* BE-3178	SA: Show Word Cloud
* BE-3193	Store only top 100 words for WordCloud on the /sa/call
* BE-2899	User records that have never been activated are actually deleted by DELETE api
* BE-3184	Web Console: Added "Last Deployment Date" column to table of Edge deployments
* BE-3198	Web Console: Added shortcut from app name in call session to the app definition
* BE-3181	Web Console: Added UUID column to the table with Contexts
* QA-1942	Web Console: Allowed User to enter time manually rather bound to select 'Open' and 'Close' time from clock selection in Business Configuration
* QA-1988	Web Console: Better error messages in case of uploading bad grammar to GREG
* BE-3216	Web Console: Improved Mode Switcher
* QA-1984	Web Console: Improvements to Create GREG Question dialog
* QA-1985	Web Console: Improvements to Create new GREG experiment dialog
* QA-1616	Web Console: Move Transcribe+ from /sa API to /sa/offline API
* BE-2997	Web Console: Redesign of customer portal.
* QA-1998	Web Console: Switched Transcribe+ from /sa API to /sa/offline API
* QA-1981	Web Console: Trim spaces from entries into login form

Changes related to Integrity of Processing (fixes):
* BE-3166	Fix - /sa/call/search when instructed to search NOTES seems to be searching the transcript text
* BE-3168	Fix - aivrTransferDestType field on /sa/call does not seem to be populated
* BE-3192	Fix - Cases where /sa/call is missing /sa/offline session
* BE-3133	Fix - Hints in real-time word-for-word transcription mess up the results
* BE-3222	Fix - redis memory leak caused by EventBus in Services that were not consuming events (only sending)
* BE-3209	Fix - Unrecognized field "sessionDuration" during warm-transfer
* BE-3170	SA: Fix - Error loop due to expired nonces
* QA-1889	SA: Fix - In some cases call's transcript only recognizes the agent and fails to identify the caller and their dialogues.
* QA-2026	SA: Fix - Missing Tag Edit icon if call does not have any tags already
* BE-3175	SA: Fix - Selectable items in search Filters should be show closer together and they should be sorted
* BE-3183	SA: Fix - spacing between call id and search box
* QA-1930	SA: Fix - The same number should not be allowed for both ANI and DNIS fields during call upload.
* BE-3160	SA: Fix - Warm transfer audio (4 tracks) are incorrectly labeled
* BE-3174	SA: Fix how the IDs are displayed on hover
* QA-1931	TA: Fix - For accounts with OIDC enabled we should not show normal Signup page, instead we should show info about logging in with the OIDC creds.
* QA-1950	Web Console: Fix - CLEAR FILTER button not clearing text from input fields in GREG Experiment Browser
* BE-3180	Web Console: Fix - Context search is doing search also on date - it should search only Name
* QA-1965	Web Console: Fix - Date range handling on the Logs page
* QA-1949	Web Console: Fix - Experiment Browser Filter is not working
* QA-1971	Web Console: Fix - If the imported GREG Experiment file does not match the required format, the import button should be disabled.
* QA-1964	Web Console: Fix - Missing tooltips for the elements in the header
* BE-3172	Web Console: Fix - Referrer Policy for https://console.ascalon.ai
* QA-1972	Web Console: Fix - Search Reset behavior on User Management page
* QA-2002	Web Console: Fix - Unable to upload Grammar file for creating Grammar under MRCP ASR.
* BE-3157	Web Console: Fix AIVR App table width

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.111.0 is scheduled for 11/11/2024 between 11pm and 12am US Central Time

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

### Minor release 1.110.0 is scheduled for 10/29/2024 between 11pm and 12am US Central Time

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

### Maintenance release 1.109.1 is scheduled for 9/29/2024 between 11pm and 12am US Central Time

New or changed functionality in platform components:
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

### Minor release 1.109.0 is scheduled for 9/17/2024 between 12am and 2am US Central Time

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

### Maintenance Window is scheduled for 9/15/2024 between 10pm and 12am US Central Time

Next Sunday, September 15th between 10pm and midnight Central Time a maintenance window is scheduled during which Voicegain **APIs may be unavailable**.
This is to reconfigure Voicegain Google Cloud setup to improve High Availability.

### Minor release 1.108.0 is scheduled for 9/2/2024 between 10pm and 12am CDT

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



All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.107.0 is scheduled for 8/5/2024 between 8pm and 11pm CDT

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

### Minor release 1.106.0 is scheduled for 7/13/2024 between 7pm and 10pm CDT

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


### Minor release 1.105.0 is scheduled for 6/18/2024 between 7:30pm and 9:00pm CDT

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


### Minor release 1.104.0 is scheduled for 5/29/2024 between 7:30am and 9:00am CDT

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

### Maintenance release 1.103.1 is scheduled for 5/16/2024 between 4pm and 5pm CDT

New or changed functionality in the Transcribe App:
* BE-2143: (TA) Show Recompute option also if status Error under certain conditions

Changes related to Integrity of Processing (fixes):
* BE-2163: Fix - Incorrect nginx routing for auth-svc from admin app

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.103.0 is scheduled for 5/7/2024 between 9:30pm and 11:30pm CDT

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

