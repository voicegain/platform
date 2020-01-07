## Release 1.2.0_beta

This release adds control of features available to various types of accounts.

### Major Features and Improvements
* More convenient Billing status and control from within the Portal.
* Fine grained control of features enabled for each account.  This allows us to control access to features that still are in beta.
* Enhanced Admin/Account Provisioning Portal - password reset, referrer/referral, premium features.

### Known issues
* Edge deployment is still in Alpha status. Disabled by default. Can be enabled upon request.
* Cloud IVR has not passed full test suite yet. Disabled by default. Can be enabled upon request.
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

