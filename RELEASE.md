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

