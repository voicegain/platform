## Release 1.115.0

**Key changes related to the core APIs**
* Ability to switch language during async real-time transcribe session
* Support for user-bound JWT tokens
* Spanish sentiment and sentence similarity models
* Text redaction supports chat and email formats directly
* Outbound calling supports initial prompt
* Voicebot Business Config supports multiple opening hours per day

New or changed functionality in the Transcribe App:
* BE-3377	TA: Add In User Profile for Admin users ability to generate and manage user-bound JWT tokens
* QA-2077	TA: Add success message when deleting a voice signature from account settings
* BE-1468	TA: Add to Transcribe App Cloud an option to delete account
* QA-2196	TA: Added input data validation for Webhook URL, Name, Token fields
* QA-2143	TA: Change design for Keywords settings
* QA-2225	TA: Voice signature - Play button now is disabled till the status turns into ready.

New or changed functionality in other platform components:
* BE-3337	Add a field on aivr app to indicate a different fssk to launch outbound calls
* BE-3350	Add ability to switch language during async real-time transcribe session
* BE-3359	Add member information to the Call notes generated for the Provider calls
* BE-3369	Add outboundPrompt to POST /aivr/dial/{destination}
* BE-3373	Add outboundPrompt to POST /public-asr/aircall/user/dial-outbound
* BE-3339	Add to POST /text/redact API ability to handle chat xml format
* BE-3340	Add to POST /text/redact API ability to handle email html format
* QA-2155	Admin Tool: Fix - Table Search- after clicking on the reset button table should reset to the previous value
* BE-3376	APIs to create and manage JWT tokens that are bound to users
* QA-1790	App Selector: Nicer formatting for Privacy Policy and Terms and Conditions pages
* BE-3370	Copilot: Add outboundPrompt to the AIVR API dial command
* MST-426	Deploy Spanish sentence similarity model
* MST-406	Hang up the call when the user is calling a wrong line of business
* BE-3329	Improve visibility into /sa/offline processing stats
* BE-3358	In normalOpeningOurs deprecate open/close fields and replace with openPeriods
* BE-3364	Limit Context name to 200 chars
* BE-3325	Move /sa/call API to a separate microservice sa-call-api
* MST-389	Multi-language design and framework in ml-svc
* QA-2232	SA: Add success/alert notification after Add/Delete or Edit JWT
* BE-3303	SA: Better Sentiment card on the Dashboard
* BE-3320	SA: Better Topic distribution card
* BE-3352	SA: Implementation of new Design for Phrase Settings
* BE-3301	SA: Improved view for AHT card
* BE-3302	SA: New design for time period selectors
* BE-3374	Send email to support@voicegain.ai if an account status switches to "suspended"
* QA-2020	SSO: Hide Forgot Password option on Edge
* BE-2728	Support auto-reconnect if fssk loses connection to Freeswitch.
* MST-431	Support MRCP confidence score scaling in rex
* MST-430	Support multiple open/close prompt in business config
* MST-370	Train and deploy the Spanish sentiment model
* MST-407	Use LOB to filter account from the given phone number
* QA-2186	Voicebot Demo: Remove Survey option.
* BE-3375	Web  Console: Provide info how to request Account cancellation and data deletion
* QA-2114	Web Console: Add "Copy to Clipboard" tooltip on logs page
* BE-3366	Web Console: Multiple open-close hours in the Normal Opening hours in the Business Config
* BE-3218	Web Console: Redesign Home page (not logged in) 
* QA-2226	Web Console: The toggle button on SA Config is overlapping with the text.

Changes related to Integrity of Processing (fixes):
* BE-3312	Fix - Customer reports that for each meeting they get 4 DONE webhook requests
* QA-1992	SA: Fix - Inconsistent date format on call's page.
* QA-2119	SA: Fix - Project names should not be allowed to start with spaces or dots
* BE-3379	TA: Fix -  Project name entry cursor with strange behavior
* QA-2092	TA: Fix - Add tag field is missing on the zoom directory upload page.
* QA-2217	TA: Fix - Language dropdown is not centrally aligned during project creation
* QA-2094	TA: Fix - Recomputing overlaping with size in storage.
* QA-2253	TA: Fix - Settings- 'Keyword' name shouldn't accept the blank space
* QA-2252	TA: Fix - Settings- 'Phrase' name shouldn't accept the blank space
* QA-2073	TA: Fix - The tag field is not available when the user tries to save a browser share recording
* QA-2220	TA: Fix - walkthrough wizard does not properly highlight features as expected
* QA-2159	TA: Fix - When the owner downloads a transcript as a docs file, the transcript's background color is not included in the file.
* QA-2139	Web Console: Fix - Added Regex is not clearly visible in settings.
* QA-2250	Web Console: Fix - API Security - 'New Secret Token' name shouldn't accept the blank space
* QA-2247	Web Console: Fix - 'Download' icon shouldn't be active until transcribe status is ready like 'View Transcript' icon as if user click on
* QA-2230	Web Console: Fix - For a brief moment, "Logout returned: Authentication token missing" is displayed.
* QA-2249	Web Console: Fix - SA Configuration name shouldn't accept the blank space
* QA-2241	Web Console: Fix - Settings-> Speech Recognition: 'Sensitivity' should only accept value between 0-1
* QA-2175	Web Console: Fix - Shortcut keys should be unique, and users should not be able to assign all shortcuts to a single key
* QA-2147	Web Console: Fix - Unable to edit the description of any api security as it always shows the error
* BE-3257	Web Console: Fix - various issues on the Logs page

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


## Release 1.114.0

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

## Release 1.2.0_beta

This relese adds fine-grained control of features available to various types of accounts.

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

