### Maintenance release 1.36.2 is scheduled for 7/6/2021 between 7:30pm and 10pm CST

This release fixes one issue and adds one enhancement
* #rcj-303: 'missing websocket name' error in audiocodes API 
* #rcj-304: flush RT SA data faster if hypotheses allow it

### Maintenance release 1.36.1 is scheduled for 6/30/2021 between 6:30pm and 11pm CST

This release switches the new account email to AWS SES and it fixes 1 issue:
* #rcj-293: differential word cloud empty on Voicegain

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








 




































 





