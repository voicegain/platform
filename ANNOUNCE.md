### Minor release 1.36.0 is scheduled for 6/27/2021 between 6pm and 11pm CST

This release improves the Speech Analytics App.

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

### Minor release 1.35.0 is scheduled for 6/23/2021 between 6pm and 9pm CST

This release has the following changes:
* POST /sa now supports notifying subscribers to a STOMP topic
* Added lightweight GET /sa/{saSesId}/status polling method
* Added `detailed` query parameter to GET /sa query method

### Minor release 1.34.0 is scheduled for 6/18/2021 between 6pm and 9pm CST

This release has the following changes:
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

### Minor release 1.33.0 is scheduled for 6/11/2021 between 7pm and 11pm CST

This release has the following changes:
* We are switching to AWS SES as our provider for outbound emails. This should makes Password Reset and other emails more reliable.
* The Named Entity Recognition (NER) model has been improved.
* The beta Speech Analytics App adds: Account time and profile settings, users table and add new users to accounts, full time-zones list.

This release also fixes the following issues:
* #rcj-265: validate each email address for POST /user
* #rcj-260: in phrase detection - location.time setting should be in seconds
* #rcj-259: PII Redaction enhancement (defaults)











 













































