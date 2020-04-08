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

