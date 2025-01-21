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

