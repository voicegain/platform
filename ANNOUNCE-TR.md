### How to contact Voicegain

If you encounter any problems, just give us a shout at [support@voicegain.ai](mailto:support@voicegain.ai)

### November 3, 2023

### Minor release 1.93.0 is scheduled for 11/2/2023 between 9:00pm and 11:59pm CST

New functionality:
* BE-1100	TA: In large Video view put the Transcript (CC) in a frame that can be moved around the screen.
* BE-1135	TA: Better copy-to-clipboard of the Meeting Minutes components
* BE-1147	TA: Show "This Meeting has no video" in the large-video view if meeting has video
* BE-1152	TA: In tag editor enable Save button only if something has changed

Fixes:
* BE-1099	TA: Fix - Specified date format is not being used
* BE-1110	TA: Modify NSIS Installer use proper setting of REINSTALLMODE
* BE-1126	TA: Fix - Large-video chat popup captures focus and icons become not clickable
* BE-1142	TA: Fix - When Zoom upload contains a video file we should set the "video" tag on this meeting
* BE-1145	TA: Add beta label over the DOCX selector
* BE-1146	TA: Fix - Remove UUID tool tips in the large-video view
* BE-1162	Fix - Failure in sa-recompute on Edge
* QA-545	TA: Now not be allowed to play multiple voice signature at the same time.
* QA-567	TA: Fix - Files under processing status shouldn't get option for (Re-Compute, Move or Delete)
* QA-630	TA: Fix - Transcripts on Homepage are not updating after changing Projects.
* QA-631	TA: Fix - Unable to edit Download permission after changing role from admin to user in one go.

### October 19, 2023

New functionality:
* BE-779	TA: Show chat messages in Right-Hand pane
* BE-856	TA: Fix - Login - not showing the locked until information
* BE-883	TA: Zoom OAuth Handshake page added
* BE-999	TA: Include video in the manual Zoom folder upload
* BE-1003	TA: Implemented large video view
* BE-1004	TA: New design for the Audio Source selector
* BE-1010	TA: Add export in Docx format
* BE-1014	TA: Better error massage in case of Recaptcha related Error
* BE-1015	TA: Fixed the +tag message and added hover text
* BE-1022	TA: Added a tag editor
* BE-1053	TA: Edge: If SSO is enabled make login automatic if user hits /login url
* BE-1055	TA: Show both installed version and available version of Zoom Meeting Assistant if newer version available
* BE-1061	TA: Ability to Control Download permissions
* BE-1063	TA: Ability to set a download permission on a User
* BE-1082	TA: Meeting Chat now being shown
* BE-1086	TA: Add Copy-to-Clipboard feature on the Overview page
* BE-1087	TA: Add new download option for docx files
* BE-1101	TA: Prevent entering regex that can match too much text
* QA-488	TA: Make Meta Description Tags SEO friendly
* QA-538	TA: Show message after user delete successfully 

Fixes:
* BE-966	TA: Fix - Weird pause and play behavior on the Voice Signatures page
* BE-967	TA: Fix - Missing Users step in new Project Wizard on Edge
* BE-1078	TA: Fix - Password reset by admin does not work
* BE-1080	TA: Fix - Unable to play audio/video in certain Edge deployments
* QA-537	TA: Fix - Current Project is not picking correctly while move

### September 30, 2023

New functionality:
* BE-71	Show Meeting VIdeo
* BE-709	New meeting submitted by ZoomMA shows up on the home page automatically
* BE-886	Support new guides for Zoom Meeting Assistant Use
* BE-961	Remove Recompute button from Project settings - we can now select multiple Transcripts and recompute them
* BE-975	Save latest project opened by a user in clientSideProperties
* BE-977	Show Project info on the list of Shares
* BE-986	Re-enable API Security settings
* BE-990	Show Privacy Policy same way we show Terms of Service

Fixes:
* QA-310	Features and Usage are not being translated in selected language instead of English language
* QA-467	Taking any URL as audio URL.
* QA-505	Mouse hovering on the upload/ upload type always showing microphone recording.
* QA-510	Editing any shared link changing its scope to public.
* QA-511	After audio finish play icon should be paused.
* QA-514	Hindi translation is on Recomputing the multiple transcription

Upload of video to the Transcribe App requires Voicegain Zoom Meeting Assistant version 1.2.1 or higher.

### September 20, 2023
New functionality:
* BE-669	Transcribe App: Added audit log
* BE-681	Transcribe App: Implement Person obfuscation in Meetings after a set time threshold
* BE-824	Transcribe App: Add ability to select multiple transcripts from the table an perform selected Action on them
* BE-843	Transcribe App: Add ability to specify Regex Redaction on the Project/Account Settings Text Redaction
* BE-873	Transcribe App: Added multi-selector delete on the Shares list
* BE-888	Transcribe App: Improve message on Zoom Meeting Assistant status
* BE-894	Transcribe App: Change name of the exe file in installer bundle to install.exe
* BE-909	Transcribe App: Make the digit formatting a default enabled option on creating new Project
* BE-910	Transcribe App: Store collapsed status of home page elements in ClientSide Properties on a User
* BE-915	Transcribe App: Add settings for Archival Text Redaction
* BE-919	Transcribe App: Tweak behavior of the 4 selectors on Transcripts on Home Page
* BE-929	Transcribe App: On Devices page - add a button to pair a Phone App

Fixes
* QA-469	Transcribe App: Fix multiple translation issues
* QA-482	Transcribe App: Fix - Inactivity timout set on zero hrs and zero is showing out of the box, when toggle is disabled no value should show.
* QA-497  Transcribe App: Fix for accepting anything in tag, also taking space as tag.
* BE-870	Transcribe App: Fix - jumping to time in MP3 audio playback does not work
* BE-890	Transcribe App: Fix for being logged out when accessing Speakers page with many voice signatures
* BE-899	Transcribe App: Fix - Meeting audio redaction only works on the first 3 speakers in a meeting session
* BE-935	Transcribe App: Fixed - incorrectly imposing share limit on Edge

### September 7, 2023

New functionality:
* BE-168	Transcribe App: Add ability to upload a directory with Zoom meeting recordings
* BE-777  Transcribe App: Remove Project Transcripts page and show project transcripts on home page
* BE-837	Transcribe App: Use GET /asr/meeting/search API on the home page
* BE-845	Transcribe App: Show tags in full if just 1 or 2

Fixes:
* BE-794	Transcribe App: Fixed Word Cloud in Spanish
* BE-799	Transcribe App: Fixed - summary and key items generated by recompute are always in English
* BE-809	Transcribe App: Fixed - Enabling full masking (*****) caused Meeting Minutes to not be generated
* BE-813	Transcribe App: Fixed - Wrong text shown if no Speakers shown on page
* QA-418	Transcribe App: Fixed - While creating new project "Profanity Masking" tabs are showing hidden at 100% screen resolution
* QA-426	Transcribe App: Fixed some missing German translations in the UI
* QA-444	Transcribe App: Fixed - User detail is missing on the delete confirmation pop up, In case user delete the account from edit user popup
* QA-448	Transcribe App: Fix - For multiple file uploads, no speakers show a difference even after selecting a range of speakers.

### August 22, 2023

New functionality:
* BE-416	 Login from Transcribe App to Freshdesk
* BE-640	 Support renaming existing Speaker
* BE-685	 Admin (Account level) controlled PII redaction
* BE-699	 More options for PII Redaction (add full and partial masking)
* BE-704	 Change the URL for Help->Submit a Support Ticket
* BE-721	 Add PII Redaction page inside Account settings
* BE-732	 Add x to cancel a search for transcript within project
* BE-751	 Support upload of multiple files for transcription
* BE-752	 Add two filter toggles on the Speakers list
* BE-755	 On home page show selected Project together with Home
* BE-756	 Allow change of name of an External Speaker
* BE-757	 Show email for User Speaker
* BE-759	 Modify the list of entities to redact (ZIP, DMY)
* BE-764	 Show only current project on the LH menu
* QA-369	 Improved Error message if user tries to sign-up second time with same email
* QA-373	 Improved title of page with Account Users
* QA-400	 Disable Save button if no new users have been selected

Fixes:
* BE-708	 Fix: Cannot delete a device that is shown in the device list
* BE-715	 Fix: At larger zoom levels Left-Hand menu unusable
* BE-761	 Fix: Project Transcript list shows meeting from home page after auto refresh due to STOP message
* BE-791	 Fix: We are not generating Meeting Minutes in German if the Project is German
* BE-795	 Fix: Weird long topics for Spanish Meetings
* QA-365	 Fix: Next Audio button not responding on Single Click (or with delay)
* QA-368	 Fix: Search and Project Name is overlapping over each other
* QA-370	 Fix: Trying to recompute any file, resulting all files showing across all projects.
* QA-372	 Fix: Transcripts table-Table sorting by "Name" and "Created on" is not working.
* QA-374	 Fix: My shares table-Table sorting not working for name, transcription date, and scope.
* QA-377	 Fix: Search text should reset on Project switch
* QA-401	 Fix: Other users table- Sorting by last active is not working.
* QA-403	 Fix: other accounts users table- Sorting by name is not working.
* QA-410	 Fix: Left menu is breaking down when selecting it rapidly.
* QA-417	 Fix: Account Text redaction/project setting- When placeholder is selected fields should be required fields.


### August 7, 2023

New functionality:
* BE-603	Automatically refresh status of the transcripts
* BE-621	Hide invalid transcript move project destinations
* BE-623	Improved Error message in case of transcript move error
* BE-626	Limit Basic Plan user to only 5 shares
* BE-628	Enhanced Project selection
* BE-638	PII Redaction placeholder validators allow non-ASCII characters
* BE-651	Add Table of Contents in the exported PDF
* BE-657	Add Metadata in the exported PDF
* BE-668	Zoom Meeting Assistant Download name now has version included
* BE-671	Add ability to completely disable Download on Edge
* BE-675	Update content of Home Page if there are no transcripts
* BE-680	Add ability to completely disable transcript copy to clipboard on Edge
* BE-693	Update content of Home Page if there are no transcripts
* BE-694	Add Login and SignUp buttons to the Share Expired/Invalid page
* BE-695	Do not show the Move option for transcripts in a project that does not belong to a user and has not been shared with the user

Fixes:
* BE-620	Sorting shares by Expiry time
* BE-637	Prevent invalid PII Redaction placeholders in Project settings during creation 
* BE-672	Prev/Next buttons not working correctly
* QA-261  Make transcript not clickable if status is Queued
* QA-362  Sorting by transcript Status

### July 18, 2023

This release includes an improved real-time English model delivering higher accuracy of speech recognition in microphone transcription preview.

### July 14, 2023

Fixes:
* QA-301    Removed recompute option from transcripts in Error state.
* QA-308    Fixed getting blank screen on My Shares
* QA-323    Fixed project flag indicators not working as expected on Homepage (also BE-611)
* QA-324    Fixed unable to move transcript between projects (also BE-616)
* BE-612    Incorrect area outlines on the Home Page

### July 13, 2023

New functionality:
* BE-550	Usability improvement in share creation.
* BE-458	Add a checkmark to indicate among the matching Speakers the one that is assigned to the Speaker from transcript
* BE-494	Added validation for values entered in the text redaction fields
* BE-555	Added support for multiple languages to the UI of the Transcribe App.
* BE-568	Delete all devices belonging to a User when a User is being deleted
* BE-570	Improvements to the projects view in the Left-Hand menu
* BE-571	Add new Zoom Icon (with status) in left-hand Menu
* BE-576	Add name of the user to be deleted to the User Deletion confirmation dialog
* BE-582	Modified text on the Signup page for EDGE if OIDC SSO is enabled on the account
* BE-596	Add support for Hindi language for transcription.
* BE-605	Improved instructions on ZoomMA download page
* BE-598	Added PDF export option (beta)
* BE-569	Change the Home Page Plan info to a new format
* BE-575	Replace Browser Capture Icon with Google Meet Icon
* BE-580	Move Latest News to a separate page that in accessible from the Help Menu



### June 28, 2023

New functionality in the Transcribe App:
* BE-45	Add Sharing of transcripts from Transcribe App
* BE-422	Add Custom behavior for Help->Submit a Support Ticket option
* BE-423	In Support sharing from the Transcript Detail Page
* BE-424	In Add Page where the user can see all the meetings that they have shared
* BE-426	Added Page that shows a single shared transcript to a not logged-in user
* BE-427	Added Page that shows a single shared transcript to a logged-in user
* BE-449	In add ability to recompute Meeting Minutes for all Meeting withing Project

Fixes:
* QA-183  Fix the link from "Manage Users"
* BE-446	Improve prompt in the URL entry box
* BE-453	Fixed the "missing voice signature speaker" error
* BE-454	Configured brotli for Cloud ACP and Transcribe App
* BE-527	Fix in Download no longer downloads TXT and Audio
* BE-538	Fixed in the request for meetings on the home page should retrieve only 20 meetings

### June 8, 2023

One issue has been fixed:
* BE-448    Project transcript view shows also Home Page transcripts directly after switch from Home to Project view

### June 7, 2023

This release adds a more accurate Spanish model and a Task Advisor

Here is a list of fixes and changes:
* BE-242	Finalized the new style of the Browser Capture pop-up in Transcribe App
* BE-281	Added a page with Terms of Use that is reachable via the Help menu
* BE-288	Fixed: Asks to setup a payment method while payment method already setup on the account
* BE-336	Improved English NER
* BE-370	Fixed in meeting minutes: Summaries truncated mid sentence
* BE-371	Fixed: Save button not enabled on EDGE in user profile
* BE-372	In Transcribe App left-hand menu - prevent overlapping scroll bars
* BE-373	Fixed: Error when deleting last Device
* BE-374	Fixed : asr-api doesn't allow users to move a meeting session to a different context in some case
* BE-382	Fixed: incorrect speaker names found in exported meeting transcription
* BE-391	Trim spaces from entered URL
* BE-392	Disable Password Recovery Key page if user is logged in using SSO
* BE-396	Do not offer local password change to users logged in via SSO
* BE-408	Fixed: Wrong confirmation dialog show when deleting user from Account
* BE-412	When syncing users, avoid copying a user to edge if the user's email is found on edge
* BE-429	Fixed formatting anomaly: ok, let's try number 1
* BE-431	Fixed: Bad URL in Advisor
* BE-442  Fixed in Transcribe App: Voice Signature sample playback always plays from the beginning of audio
* BE-443  Fixed in Transcribe App: Transcription fails because unable to find the speaker

### May 22, 2023

Key things that are new in this release:
* Meeting summaries are generated by GPT-3.5
* Zoom Meeting Assistant now uses Device Pairing to authenticate with the Transcribe App. You will need to download and install Zoom Meeting Assistant ver 1.0.0+
* On EDGE, Transcribe App now supports OIDC SSO.

### March 20, 2023

This release has the following fixes and improvements in the Transcribe App:

* BE-21	Fix expanded left-hand menu obscuring page content if frozen
* BE-24	In user Profile add a setting to hide language flags on Project icons
* BE-26	New Project design for the Transcribe App (mainly left-hand menu)
* BE-27	Add Search within transcript in the detail view in Transcribe App
* BE-52	Flags on Projects are inconsistent
* BE-59	Back button doesn't work
* BE-63	Transcribe from URL not working in Transcribe App
* BE-64	Upgrade on home page of the Transcribe App takes you to Password Reset
* BE-65	Plan Upgrade page working off stale billing data
* BE-66	Walk-Through Wizard cannot be launched
* BE-68	Hide expanded LH menu upon a click
* BE-112	None or not all Projects are visible on Edge
* BE-126	Clicking on the Downgrade button has no effect
* BE-127	Show a Tool Tip for Project Settings
* BE-128	Sending password confirmation in clear-text
* BE-140	Modify behavior of the expandable LH menu - do not expand when I merely move the mouse across it
* BE-141	Show tooltip when hovering over project icon in the transcript list on home page

### March 9, 2023

Changed pricing and time limits on Transcribe App plans.

### February 15, 2023

This release includes the following:
* Keyword and phrase highlighting in the transcript text
* Bug fixed: home/login page loop in all the nonces somehow are removed from the indexedDB

### February 3, 2023

This release adds Zoom Meeting Assistant status display to the Transcribe App.
Due to this change this release will require Zoom Meeting Assistant version 0.3.0 at minimum.

This release also addresses the following specific issues:
* Automatically insert underscores into multi-word hints
* Do not hide microphone and browser capture icons for old projects that have no language setting value

### January 30, 2023

This release has the improved Spanish Real-Time model.

This release also addresses the following specific issues:
* Add ability to delete a keyword in Speech Analytics settings
* The downloaded audio file now has correct mp3 extension instead of wav
* In languages Project settings show if microphone transcription is not available for given language
* Change the lock-out message to show the local time instead of the UTC.
* Fix weird behavior in Settings if old Project has no Meeting Minutes enabled
* Add a hide button for the Zoom Meeting Assistant banner

The current version of the Zoom Meeting Assistant going with this release is 0.2.18

### January 24, 2023

This release has an improved Spanish Offline model.

This release adds ability to Recompute meetings in the Transcribe App. 
This means that all the NLU processing of the transcript can be redone after, e.g., change in the Project analytics settings.

Other changes to the Transcribe App:
* Info about available Zoom Meeting Assistant is shown on the home page.
* List of search results shows also topics for each transcript.
* Removed Update button on the Key Items settings. Key Items will always be updated to the latest configuration.
* Hid Key Items configuration from non-Admin users.

### January 5, 2023

This release enables Browser Capture in the Transcribe App on Edge.

This release also addresses the following specific issues:
* Pause was behaving like mute
* "No Microphone" option added in Browser Capture
* Cancel out of the Mic Save dialog was not working
* (Meeting Minutes) Made Modifications to the KeyItems settings in Project
  * Support negative examples and regex
  * Add Enabled toggle for each Key Item















































 













































