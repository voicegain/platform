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

### Maintenance release 1.32.3 is scheduled for 6/10/2021 between 8pm and 11pm CST

This release has fixes for:
* bug #rcj-262: Word Cloud has no content on Demo Integration Dash

Our mail provider has an issue that forces us to temporarily switch to a very simple forgot-password email.




 




































 





