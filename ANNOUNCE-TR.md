### How to contact Voicegain

If you encounter any problems, just give us a shout at [support@voicegain.ai](mailto:support@voicegain.ai)

### January 17, 2024

New functionality:
* BE-1186	TA: Meeting search fields API returns intermediate values
* BE-1377	TA: In Advanced Search filters use the intermediate values returned from the fields API
* QA-421	TA: Improved inactivity timeout functionality
* QA-660	TA: Transcript caption popup window now is resizable in full-screen video player

Fixes:
* BE-1252	TA: Fix - After Submit on Zoom Upload still staying on the same page
* BE-1383	TA: Fix - The User avatar is currently saved to the currently selected context - we need to save it to another bucket
* BE-1385	TA: Fix - Password reset link incorrect on some Edge deployments
* QA-509	TA: Fix - Incorrect behavior if User tries to use Share "within account" while not being logged in
* QA-594	TA: Fix - On uploading the zoom folder getting the status as error
* QA-703	TA: Fix - Shares is not showing under My Shares (on accounts with many transcripts)
* QA-709	TA: Fix - Filter by Phase/Status not working in advanced search.
* QA-756	TA: Fix - Zoom App Page is not loading for some new users
* QA-799	TA: Fix - For new users "Something went wrong" error page shown instead of a First Project Wizard
* QA-802	TA: Fix - Save button is not getting enabled after updating the settings.
* QA-809	TA: Fix - Advanced Search Filter is not working on Status Filter
* QA-811	TA: Fix - Advanced search: Searching for the error transcripts filter not working.
* QA-820	TA: In Advanced Search now able to enter duration manually (in addition to slider)
* QA-829	TA: Fix - For new User Search Page is coming blank
* QA-833	TA: Fix - After changing the profile picture "Hide Project Language Reminder" checkbox automatically gets unchecked.

### January 2, 2024

New functionality:
* BE-1158	TA: In Advanced Search show Headlines in the list of search results
* BE-1172	TA: Identify currently paired Zoom Meeting Assistant
* BE-1193	TA: In Advanced Search - Add filter on transcript language
* BE-1258	TA: Add a filter on creator in Advanced Search
* QA-350	TA: Upload button is now disabled when max allowed minutes are exceeded for the basic plan. 
* QA-671	TA: Revised search location of the Home page
* QA-726	TA: Voice signature status is shown in specific colors like green for "Ready" and blue for processing.
* QA-729	TA: Added special page for 500 errors
* QA-773	TA: Tags have their own specific alert message on Editing (Adding and Deleting).
* QA-778	TA: Improved login behavior if accessing a meeting shared within Account

Fixes:
* BE-1333	TA: Fix - Mute/Unmute gets confused if we press the mute/unmute button too fast in a seqeunce several times
* BE-1336	TA: Fix - Refresh icon gets squished when we open search box
* QA-669	TA: Fix - Various issues on Advanced search feature
* QA-672	TA: Fix - Unable to choose the folder directory in Zoom upload
* QA-710	TA: Fix - Page behavior is unusual after URL upload.
* QA-718	TA: Fix -Search for transcript on the home page is not working if searching by transcript name
* QA-752	TA: Fix - Owner account should not show while creating a project and adding users to the project.
* QA-768	TA: Fix - Advanced search page is going blank.
* QA-770	TA: Fix - Filters are getting reset, when user open any transcript through advanced search.
* QA-772	TA: Fix - Load more button the Advance search not working properly it respond after 3 to 4 clicks
* QA-774	TA: Fix - Save button shouldn't get enable if inactivity timeout field is empty.
* QA-780	TA: Fix - Tags, Speakers, Participants filters associated with zoom upload are not searchable in Advanced search.
* QA-781	TA: Fix - Sometimes Word Cloud gets broken for some random transcripts.
* QA-782	TA: Fix - All 5 languages should be mentioned under language filter.
* QA-792	TA: Fix - "May Download" checkbox getting automatically enable after adding the project in user setting
* QA-794	TA: Fix - No error or alert msg on login page, when login with incorrect password.


### December 7, 2023

New functionality:
* BE-1255	TA: After new content is loaded by clicking "Load More" the page should scroll to the same place as before
* BE-1256	TA: Do not truncate meeting names if not needed
* BE-1274	TA: Check sizes of all Zoom folder files before starting upload and not during
* BE-1276	TA: Add our own controls over the small video window of Shaka Player
* QA-719	TA: Now, after search the page scrolls past "Get Started" and "Actions" to results
* QA-720	TA: Share link now does proper redirect back to the share link if login is required

Fixes:
* BE-1221	TA: Fix - Uncaught TypeError: Cannot read properties of null
* BE-1257	TA: Fix - For Duration the sorting toggle is placed weird
* BE-1259	TA: Fix - Keywords and tags displayed are missing spaces between them
* BE-1261	TA: Fix -Show correct color for each project in Project filter
* BE-1277	TA: Fix - Sometimes the Zoom Meeting Assistant page show stale value of the installed version
* BE-1299	TA: Fix - When searching for text in meetings on home page, the API request should not contain any sort parameters
* BE-1304	TA: Fix - POST /auth-svc/auth/login/openid fails if the User account exists but is only in the CREATED state
* BE-1313	TA: Fix - weird behavior of Project search
* BE-1314	TA: Fix - Weird logic for showing Move button on multiple selects
* BE-1317	TA: Fix - On Edge the option to add users to project is not visible to the Project Owner
* QA-651	TA: Fix - Date formats should not get translated in other languages.
* QA-657	TA: Fix - File submit fails if we change project after upload and before submit.
* QA-677	TA: Fix - Show current month in the right pane of the calendar
* QA-698	TA: Fix - Project search by name is not working properly.
* QA-699	TA: Fix - At the time save Transcript if we change the project then getting error
* QA-700	TA: Fix - User is able to update the email in update payment but updated mail is not showing after saved
* QA-701	TA: Fix - Add user- There should be words limit for entering the name
* QA-705	TA: Fix - Tag for the voice signature showing like a single word not showing any gap between them.
* QA-706	TA: Fix - Overlapping text in Download option when Spanish or German language is selected
* QA-716	TA: Fix - If the chat is long then White blank screen showing after the Video
* QA-717	TA: Fix - On large Chat video view -closed captioning, Video minimize buttons is not working
* QA-721	TA: Fix -  My Shares page stuck on loading after we Edit a share.
* QA-725	TA: Fix - User should only able to delete the voice signature by clicking on the delete icon.
* QA-727	TA: Fix - mouse hover on the Regenerate button showing in English when Hindi language is selected.
* QA-732	TA: Fix - There should be a limit for max allowed char for the project name.
* QA-733	TA: Fix - My shares table - tags should be separated.
* QA-735	TA: Fix - Restart when adding a new voice signature is not working properly.
* QA-736	TA: Fix - On the archival text reduction page, unable to save the updated time as the save button not enabled when changing days.
* QA-741	TA: Fix - On Advance search Project check box is not showing similar for all project
* QA-743	TA: Fix - On Changing the setting of "Start of the calendar week" from Sunday to Monday and vice versa getting the error of enter valid data
* QA-744	TA: Fix - Invited user is able to move the transcript of Admin project But the Admin is not able to move the transcribe to User project and also the error message is not showing on the Frontend
* QA-749	TA: Fix - Project creation page-users page is missing
* QA-753	TA: Fix - Re-Upload option is showing for Recording and Browser.
* QA-757	TA: Fix - On navigating back from the browser arrow from the large video mode then left menu disappear from the screen


### November 26, 2023

New functionality:
* BE-1054	TA: Avatar image can now be edited (cropped)
* BE-1104	TA: Better reporting of file size errors on upload (413 error)
* BE-1167	TA: Show Project settings only to Project owners and Admins
* BE-1168	TA: Add user Profile Setting: "Show advanced Project settings"
* BE-1170	TA: Any text redaction Settings (Account, Project) visible only to Account Owner and Admins
* BE-1171	TA: Menu actions in the Advanced Search results list work now the same as on the Home Page
* BE-1174	TA: Added "Re-upload" that opens Zoom Upload form
* BE-1190	TA: Show countdown on the modal that shows the QR code.
* BE-1196	TA: Prompt user to reload if there is a new version (also invalidate any open session)
* BE-1234	TA: Do not show Analytics settings on a Project unless user has enabled advanced settings
* BE-1236	TA: Upgrade to Node version 18
* BE-1254	TA: For Admins the "Show advanced Project settings" is now enabled by default
* BE-1264	TA: Added more logs around the login process
* QA-602	TA: Cleaned up the Inactivity Timeout setting
* QA-619	TA: Remove settings in Shaka Player
* QA-642	TA: Similar Date formats are now together in Settings under Account in Profile menu.

Fixes:
* BE-875	TA: Fix -Warning about a too large file is not being shown
* BE-1105	TA: Fix - Submit button gets enabled too early while uploading zoom recording folders
* BE-1128	TA: Fix - "walkThroughWizardSeen" gets set to True even if user has not done the Wizard
* BE-1156	TA: Fix - In Advanced Search Filters should be remembered
* BE-1157	TA: Fix - In Advanced Search show Project icon as the first column
* BE-1169	TA: Fix - Show error message when hovering over the Error in Transcript list (was broken)
* BE-1180	TA: Fix - When SSO user gets logged out from TA they see normal login page for a few seconds
* BE-1182	TA: Fix - Weird behavior after clicking back button on detail page opened from Advanced search
* BE-1217	TA: Fix - Advanced Search API should return al the values if body is not passed.
* BE-1220	TA: Fix - Missing translations
* BE-1265	TA: Fix - First Project wizard not running is new user was invited to some projects
* BE-1269	TA: Fix - On a new account the My Shares page hangs forever with a spinner
* BE-1270	TA: Fix - GET /asr/meeting sharedBy returns meetings for a brand new user that has not shared anything
* BE-1272	TA: Fix - Getting incorrect error "cannot transcribe audio from video file" while uploading zoom folder
* BE-1273	TA: Fix - Checking for file size in Zoom Upload is broken (looks at files that will not be uploaded)
* QA-537	TA: Fix - Current Project is not picking correctly while move
* QA-613	TA: Fix - On uploading zoom folder- chat not uploaded correctly
* QA-643	TA: Fix - Search is not working on Homepage
* QA-644	TA: Fix - Do not show tag edit option in Shared transcripts
* QA-655	TA: Fix - Submit button shouldn't get enable until all selected files are uploaded.
* QA-670	TA: Fix - Right outline of the box is missing the speaker popup
* QA-674	TA: Fix - After deleting the project still showing name on homepage and setting icon, and clicking on setting no result showing.
* QA-686	TA: Fix - Project Invited user is able to access the project setting by URL
* QA-688	TA: Fix - Search user is not working on the Add User(s) to Project setting popup and its redirecting to the General Project Settings
* QA-695	TA: Fix - Advanced search button stays there on the page even after search collapsed.


### November 3, 2023

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

















































 













































