# Release 1.1.0_beta.2

This release adds functionaliy that did not make it into the initial release. It also fixes several bugs.

## Major Features and Improvements
* Added ASR engine resource status monitoring to Voicegain Portal UI
* Added Password strength checking
* Added Release Notes info to Voicegain Portal UI
* All three billing styles (manual-refill, auto-refill, invoice) now supported for Enterprise Voicegain customers. Speech.Works customers are created with manual-refill style.

## Known issues
* Edge deployment is still in Alpha status - please contact us before attempting Edge Deployments
* Cloud IVR has not passed full test suite yet. Also it lacks documentation. Please contact us if you would like to test Cloud IVR.
* Audio Sender Daemon does not support encryption yet.

## Breaking Changes
none

## Bug Fixes and Other Changes
* buf #142: Provisioning Portal times out after login.
* bug #143: ASR resets occasionally in the middle of transcription. Was due to empty request to NLM.
* bug #144: Passowrd Lockout mas mistakenly set to occur onlu after one mistake. Has been increased to 5.
* bug #145: 401 errors when logging in after a period of inactivity
* bug #147: Service name at the end of the URL in the password (re)set email incorrect.
* bug #148: New Language Models not shown unless user has Manager role
* bug #149: Language Model created as Built-in shows up as User model
* minor bugs #150

# Release 1.1.0_beta.1

This is a first public release of Voicegain Speech-to-Text Platform.

## Major Features and Improvements
This being a first public release, here is a list of key features of the Voicegain platform:
* Cloud based Speech-to-Text API supporting both Transcription (large vocabulary) and Recognition (limited context-free grammars)
* MRCP/VXML/GRXML compatible ASR - tested with Dialogic and Aspect (Voxeo) VXML platforms
* Real-Time transcription - core Real-Time Speech-to-Text engine plus tools like: Audio Sender, Web UI for managing multiple transcription channels, Web based client for displaying live transcriptions
* Voicegain Enterprise Web Portal
* Simplified Transcription only Web Portal (Speech.Works)

## Known issues
* Edge deployment is still in Alpha status - please contact us before attempting Edge Deployments
* Cloud IVR has not passed full test suite yet. Also it lacks documentation. Please contact us if you would like to test Cloud IVR.
* Audio Sender Daemon does not support encryption yet.

## Breaking Changes
* none

## Bug Fixes and Other Changes
* we will begin reporting bug fixes starting from the next release

