### Maintenance release 1.43.4 is scheduled for 9/30/2021 between 6:30pm and 10pm CST

This release fixes the following issues:
* Certain fields not saved on a transcription record due to NPE
* Uploaded LM corpus files incorrectly reported as having wrong format/encoding
* Edge Web Console not showing all Application Modes correctly

### Maintenance release 1.43.3 is scheduled for 9/28/2021 between 8:00pm and 10pm CST

This release fixes issues:
* #rcj-349: Acoustic model setting in context is not used in offline transcribe

For Transcribe App released fixes for the following:
* Issue with navigating away from microphone capture which would break the recording
* Not able to upgrade in a single step from monthly to annual and to a higher Plan
* Computation of remaining days till usage reset
* Minor issues in password entry for a new password
* Several small UI issues 

### Maintenance release 1.43.2 is scheduled for 9/27/2021 between 7:00pm and 10pm CST

This release fixes issues:
* #rcj-345: On ACP, Edge configuration selection is not filtered by selected version
* #rcj-347: Invalid value for `persist`, must be a value less than or equal to `604800000`

For Transcribe App:
* Fixed several small UI issues 
* Fixed pricing values shown on Billing Plans page - was reporting price/user/month as price/month
* Fixed double counting usage for microphone transcriptions.
* Fixed error when doing transcription with Expiry set to longer than 1 Week.

### Maintenance release 1.43.1 is scheduled for 9/26/2021 between 8:00pm and 10pm CST

This release:
* Changes signup text for Developer Web Console from "300 free monthly minutes available" to "$50 one-time credit available" 

### Minor release 1.43.0 is scheduled for 9/24/2021 between 7:00pm and 11pm CST

This release:
* Significantly improves Hint and Language Model functionality. You can now achieve much higher accuracy using Hints and/or Language Model
* Available configurations for Edge deployments now are annotated with the compatible release range - the Web UI ensures that you can apply to your Edge cluster only compatible configurations
* New accounts get $50 credit instead of the monthly 300 minutes allowance. Old accounts retain 300 minutes allowance.

Two new Applications are being released:
* Speech Analytics App - analyze call-center calls
* Transcribe App - transcribe audio from meetings and other audio files

See [www.voicegain.ai](https://www.voicegain.ai) for how to signup.

Issues fixed:
* Memory issue affecting Offline transcription which occasionally would cause the transcription to be stuck in Processing

## Maintenance release 1.42.1 is scheduled for 9/15/2021 between 6:00pm and 10pm CST

This release:
* Reduces the amount of memory used by the offline transcription tasks leaving more space that may be used for transcoding audio files. Should reduce chance of failed offline transcription.






















 




































 





