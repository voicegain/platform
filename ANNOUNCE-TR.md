### How to contact Voicegain

If you encounter any problems, just give us a shout at [support@voicegain.ai](mailto:support@voicegain.ai)

## January 20, 2025

New:
* QA-2183	TA: Advanced Search - Improve filter for selecting languages
* QA-2190	TA: Advanced Search - Improve filter for selecting participants
* QA-2189	TA: Advanced Search - Improve filter for selecting speakers
* QA-2181	TA: Advanced Search - Improve filter for selecting tags
* QA-2130	TA: The speakers table under account settings now has sorting functionality by Email.
* BE-2874	TA: Introduced fallback error page for Loading Chunk Issue
* QA-2137	TA: Show 'Copy to clipboard' message when hovering the mouse over the copy icon for the project ID
* QA-2083	TA: Until a profile picture is updated by the user, display the avatar image in the profile settings
* QA-2142	TA: When no group is available for the keyword to merge, display the option to create a new group

Fixes:
* QA-1498	TA Edge: Fix  - Unable to detect the Browser OS Device IP for all login sessions.
* QA-2113	TA: Fix - Advanced Search: Project filter having extra white space that is covering whole page
* QA-2129	TA: Fix - behavior of the tag entry box
* QA-2110	TA: Fix - Duplicate tags shouldn't be allowed
* QA-2209	TA: Fix - Meeting Bot - Displaying 'Forgot Meeting' instead of 'Leave Meeting' for a Webex call."
* QA-2204	TA: Fix - Occasional unable to join Zoom meeting bot - Error: “Failed to join meeting"
* QA-2120	TA: Fix - Project names should not be allowed to start with spaces
* QA-2163	TA: Fix - Properly handle Projects with missing saConfig
* QA-2160	TA: Fix - Unable to move multiple files across all projects, as the pop-up page displays differently and does not allow selecting the destination.

## January 5, 2025

New:
* BE-3226	TA: Add a title and heading to LLM Page.
* BE-3229	TA: Disable invoices button if there are no invoices available
* QA-2045	TA: When no speaker is present, the dropdown now displays the text 'No speaker present' under project creation

Fixes:
* QA-2011	TA: Fix - Downloading audio file with text file issue
* QA-2046	TA: Fix - Microphone capture: The transcript scrollbar is overlapping with the start time.
* QA-2064	TA: Fix - Zoom Meeting Bot is not working properly as it is failing even after joining a Zoom meeting.
* BE-3261	TA: Fix speaker activity detection in Webex Meeting Bot if screen is being shared

## December 4, 2024

New:
* QA-1628	TA: Search functionality provided for Admin users when they delete any other user and transfer their projects to another user.
* BE-2934	TA: Improved design of the Webhook Settings.

Fixes:
* QA-1931	TA: Fix - For accounts with OIDC enabled we should not show normal Signup page, instead we should show info about logging in with the OIDC creds.

## October 30, 2024

**Key changes related to Transcribe APP**
* Improvements to the Webhook functionality
* UI improvements

New:
* BE-3075	TA: Added time-to-live (TTL) setting for the webhook JWT.
* BE-2983	TA: Check the Error Boundary implementation and catch all errors
* QA-1760	TA: Improved Profile page layout.
* QA-1721	TA: Provide way to identify Zoom, MS Teams or Webex meeting. 
* QA-1821	TA: Removed Edit Tag functionality for the shared transcript for both public and account share pages.
* QA-1851	TA: The password menu is available under the profile settings, so removed it from the "My Profile" menu.
* BE-2940	TA: Updated Transcribe App styles.

Fixes:
* BE-3103	TA Edge: Fix -  Webhook page refresh is taking time and render page with no web-hook defined even there is existing web-hook.
* QA-1791	TA: Fix -  Cancel icon visibility is low in dark theme.
* QA-1846	TA: Fix - "Title" field should be editable for Admin account user in profile.
* QA-1780	TA: Fix - A type error page is showing on the advanced search page when the user tries to apply a filter.
* QA-1826	TA: Fix - advanced search - The selected start and end dates are not populated in the UI, but they appear when saved in Date filter.
* QA-1805	TA: Fix - Allowed domain settings are now visible for the Cloud version, whereas they were previously exclusive to Edge.
* QA-1819	TA: Fix - An "unexpected character" error is displayed during signup on Transcribe Cloud
* QA-1773	TA: Fix - An unexpected error page appears when a user tries to delete a device after changing its status to "Rejected."
* QA-1823	TA: Fix - Basic user should not be allowed to create share.
* BE-2994	TA: Fix - Does not allow entry of valid hints.
* QA-1812	TA: Fix - If the user is on the basic plan, the allowed email domain settings should not be displayed, as users on the basic plan cannot invite new users.
* QA-1845	TA: Fix - In Dark theme input field text is not visible.
* QA-1781	TA: Fix - Meeting Bot: If a user fails to join the meeting, they are unable to leave the meeting.
* QA-1783	TA: Fix - Missing "Allow signup with the domain" field
* QA-1833	TA: Fix - Partial translation when join a meeting by meeting bot.
* QA-1797	TA: Fix - PDF Download: The meeting details table should be properly sized to fit the screen.
* QA-1764	TA: Fix - Text was not translated based on selected language.
* QA-1883	TA: Fix - The 'Click here' hyperlink appears on the login page immediately after entering the email.
* QA-1856	TA: Fix - The user is able to add a Webhook without providing any details.
* BE-3104	TA: Fix - Webhook jwtTTL information weren't consistent.

## Spetember 17, 2024

**Key changes related to Transcribe APP**
* Support Webhook API (phase 1) - Edge only.
* Added third set of LLM service settings and add model name field to all 3 LLM services - Edge only.
* Including transcript metadata together with transcript when using LLM to generate meeting minutes items.
* Improved reliability of the Meeting Bot on longer meetings

New:
* BE-2798	TA: Added new LLM Prompts for Meeting Minutes.
* BE-2855	TA: Added third set of LLM service settings and add model name field to all 3 LLM services.
* BE-2805	TA: Added user's status column in users lists
* BE-2860	TA: Added Webhook settings page.
* BE-2857	TA: Addition to the LLM Prompts Settings.
* QA-849	TA: Consistent password complexity requirements.
* BE-2812	TA: Enforced LLM token limit.
* BE-2850	TA: Including transcript metadata together with transcript when using LLM to generate meeting minutes items.
* BE-2874	TA: Introduced fallback error page for Loading Chunk Issue.
* BE-2875	TA: Introduced fallback page for error boundary case.
* QA-1228	TA: Sorting given for users by name, for the Login all session table.

Fixes:
* QA-1635	TA: Fix - "MINE/SHARED/ALL" option should not be visible to Basic account on LLM Query page.
* QA-1225	TA: Fix - Clicking on backward icon of any transcript results in value of time getting negative.
* QA-1665	TA: Fix - Clicking on microphone capture save recording page showing, it should show the start recording pop-up page.
* BE-2842	TA: Fix - Dialog to reset password.
* QA-1485	TA: Fix - Error page when opening rediarized transcript (partial fix)
* BE-2906	TA: Fix - error when searching for a phrase with an apostrophe 
* QA-1604	TA: Fix - Footer of Document should not overlap with transcript in downloaded PDF.
* QA-1689	TA: Fix - For longer meetings, after it ends, the transcript isn't processing properly.
* BE-2900	TA: Fix - If a Zoom meeting is long and is eventually ended by the host the bot does not notice that meeting has ended.
* QA-1605	TA: Fix - In share meeting pop -up , month name is not translating and always show in default language.
* QA-1497	TA: Fix - Invalid date and year showing for the last active under account users.
* QA-1672	TA: Fix - LLM Query not working and returning 500 error (Internal Server Error).
* QA-1718	TA: Fix - Meeting bot icon should also show as disabled when the maximum allowed minutes limit is exceeded.
* QA-1490	TA: Fix - Meeting Bot were unable to join Webex meeting.
* BE-2845	TA: Fix - Meeting platform selection tiles were too indistinct.
* QA-1677	TA: Fix - Some old transcripts still showing the queued status and user can not delete or remove them.
* BE-2195	TA: Fix - Stuck on login.
* QA-1662	TA: Fix - The error message should be displayed in the selected language after the maximum allowed minutes have been exceeded.
* QA-1667	TA: Fix - The walkthrough wizard is not functioning properly for new users.
* QA-1600	TA: Fix - Unable to join the webex meeting by meeting bot.
* BE-2834	TA: Fix - Unexpected Application Error! Loading chunk failed.
* QA-1609	TA: Fix - Voicegain logo is not fully visible in the 100% zoom.
* QA-1668	TA: Fix - When a user selects more than 12 speakers, the submit button becomes disabled however we have limit for 20 speakers.
* QA-1560	TA: Fix - When user try to invite user, it shows an invalid email address error but when user re-click on the save button it showing "User already exists".


### September 2, 2024

**Key changes related to Transcribe APP**
* Cloud only: Major improvement to capabilities of LLM Query
* Major makeover of the look of the UI
* Added UI dark mode
* Added Configurable Meeting Minutes (via LLM prompt)
* Added tracking of LLM tokens (in the Cloud)
* On Edge: Added ability to retrieve speaker data (incl. email) using Zoom API

New:
* BE-2798	TA: Added new LLM Prompts for Meeting Minutes
* BE-2811	TA: Added Purple project color (instead of black).
* QA-1003	TA: Add option to rename transcripts.
* BE-2668	TA: Change Key Items to Meeting Minutes : Add more categories in addition to Action Items
* BE-2762	TA: Change naming from Key Items to Meeting Minutes.
* BE-2786	TA: Changed border radius on avatars.
* BE-2718	TA: Dark mode is enabled for transcribe app.
* BE-2763	TA: On LLM Settings have two tabs - one for Prompts and one for Services
* BE-2797	TA: Post signup to Transcribe App, sending signup email.  
* QA-1515	TA: Show creator avatar on the transcript detail page
* BE-2781	TA: Show usage of LLM Tokens
* BE-2789	TA: Showing email icon next to the speaker/participant if there it an email field for that speaker/participant.
* BE-2810	TA: Switch Black Project color to Purple (for dark mode)
* BE-2329	TA: Track LLM token use in Transcribe App Cloud
* BE-2739	TA: Tracking used time on Transcribe App.
* BE-2791	TA: Update look and feel of transcribe app

Fixes:
* QA-1443	TA: Fix - Error message is wrong for the password reset page.
* QA-1638	TA: Fix - Getting 500 server error when Users use Special characters in search bar on Advanced search page.
* BE-1388	TA: Fix - Getting identical values of confidence when running transcript/{session-id} REAL-TIME
* QA-1493	TA: Fix - HTML element showing in overview section on production.
* QA-1613	TA: Fix - In Advance search Filter, tag is not working.
* BE-2756	TA: Fix - List of transcripts on Home page loads twice
* QA-1511	TA: Fix - LLM prompt box on transcript should not be available for shares.
* QA-910	TA: Fix - Search by numbers is not working properly.
* QA-1454	TA: Fix - Text "Undefined" populate when user left blank while signup
* QA-1593	TA: Fix - The Advanced Search functionality breaking on searching more than one word.
* QA-1461	TA: Fix - There should be a limit for the expiry time limit for shared transcript.
* QA-1481	TA: Fix - There should be warning Dialog when user click on Back Button or Close Browser
* BE-2330	TA: Fix - Transcribe is showing one-line per word.
* QA-1636	TA: Fix - Unable to check the creator on the advanced search filter.
* QA-1462	TA: Fix - Walk through wizard breaks when user switch language between walkthroughs.
* QA-764	TA: Fix - When a whole sentence entered in search box, it is not working and overlapping with close icon.

### August 5, 2024

**Key changes related to Transcribe APP**
* Meeting metadata used in LLM Playground
* LLM Query uses history of previous Q and As
* More detail for the relevant meeting display in LLM Query
* Enhancements to text file download

New:
* BE-2633	TA: Add metadata information to LLM Playground query
* BE-2724	TA: Add option to include header in the downloaded text file
* BE-2651	TA: Add Project information to the relevant-meeting list in LLM Query page
* BE-2687	TA: API Key entry boxes should be set to not remember history
* BE-2634	TA: For text transcript download, add configurable transcript timestamp
* BE-2725	TA: Improve the rules to show the speakers and non-speaking participants
* BE-2577	TA: Indicate the relevance of the relevantMeetings returned from /asr/meeting/llm/query
* BE-2717	TA: Make sure that the transcript submitted to LLM Playground has timestamps (interval parameter)
* BE-2601	TA: Remember sorting on home page when returning to it from open meeting details
* BE-2589	TA: Replace HighCharts WordCloud with another library
* BE-2570	TA: Show the scope of the LLM query in the Answer

Fixes:
* BE-2560	TA: Fix - After latest change the Meeting Bot does not distinguish between progress Processing or Done
* BE-2630	TA: Fix - Meeting search seems to not always return the newest first
* QA-1485	TA: Fix - Error page when opening rediarized transcript (partial fix)

### July 13, 2024

**Key changes related to Transcribe APP**
* Added Meeting Bot that can join a meeting and record/transcribe it (beta)
* Added Rediarize option
* LLM Playground and LLM Query available on Cloud
  * Note there is a limit of 16K tokens - about 1.5h of audio
* LLM Query results now show which transcripts were used in answering the query
* Added LLM Service authorization header settings
* Improved Action Items LLM query
* Show which users have Zoom Meeting Assistant installed

New:
* BE-2468	TA: Add a meeting_bot tag to meetings recorded using Bot
* BE-2470	TA: Add BOT selector on the home page
* BE-2345	TA: Add Meeting Bot
* BE-2412	TA: Add Re-diarize option for a meeting
* QA-766	TA: Added search to time-zone selector
* QA-1281	TA: Better error message when inviting user with invalid domain
* BE-2545	TA: Do not hide LLM Playground on the Cloud
* BE-2546	TA: Do not hide LLM Query on the Cloud
* QA-1377	TA: Fix after-login redirect URL on Edge
* BE-2508	TA: For first time login, after creating first project, we should take user to the page with the Zoom Meeting Assistant
* BE-2529	TA: Handle 429 response from /llm/chat API and /asr/meeting/llm/query
* BE-2467	TA: Identify Meeting Bot recordings as such in Transcribe App
* BE-1998	TA: Improved 404 Error handling
* BE-2394	TA: Improvements to LLM Playground UI
* BE-2495	TA: In LLM settings add Authorization header settings
* BE-1094	TA: Information about the use of Shared links is displayed
* BE-2514	TA: Make the request for Action Items be similar to the request made from the LLM Playground
* BE-2487	TA: Modify the LLM Query page to have the same look and feel as the new LLM Playground
* BE-2392	TA: New widgets to set number of speakers for Saving microphone recording
* BE-2391	TA: New widgets to set number of speakers for Upload
* QA-1416	TA: Remove language selector on Project Settings page on Edge
* BE-2339	TA: Show on Users page if the user has Zoom Meeting Assistant installed
* BE-2486	TA: Show relevant meetings if they are returned by the /llm/query API
* BE-2207	TA: Show share usage
* QA-321	TA: When a new user creates his first project there is now an option for change language for page translation

Fixes:
* QA-1298	TA: Fix - Admin User is unable to update the LLM setting.
* QA-1277	TA: Fix - After submitting a microphone recording, no success or upload message is shown. It should display a success message.
* BE-2331	TA: Fix - Browser Capture Pop-Up seems to load bunch of stuff that it does not need
* QA-1304	TA: Fix - For browser share and microphone capture recording, the Success message is not displaying after saving the recording.
* QA-1357	TA: Fix - LLM Query is not working
* QA-1359	TA: Fix - Redux is not clearing up in case of session logout
* QA-1196	TA: Fix - Sometimes, the login process gets stuck on the login page.
* QA-1384	TA: Fix - Three dot menu are not visible for the account users table.
* QA-965	TA: Fix - Within account share is not working properly.

### June 18, 2024

**Key changes related to Transcribe APP**
* Added basic LLM Query over data stored in vector database
* User-level time settings (previously time settings were only account-wide)
* Korean transcription should now be less likely to shift to translation
* Summary LLM prompts are customizable on Edge

New:
* QA-1230	TA: Active login sessions now displayed and highlighted at the top by default.
* BE-2276	TA: Add 3 more LLM prompts to LLM settings
* BE-2224	TA: Add 'copy to clipboard' for action items
* BE-2278	TA: Add time settings also on User Profile
* QA-1237	TA: Added an option for Logout from all devices on My Login sessions.
* BE-2217	TA: Added basic Vector LLM Query
* BE-2284	TA: Apply MD formatting to the section summaries
* BE-2314	TA: If a user clicks the LLM Query button on the home page - take them to the LLM settings if needed
* BE-2240	TA: Implement page for Vector based querying - Edge Only
* BE-2196	TA: Make sure that whenever we discard the login session in the browser we do call logout API
* BE-2218	TA: Provide immediate feedback of the Start mic capture button being clicked
* BE-2282	TA: Use the customer overrides (if specified) for the summary prompts

Fixes:
* QA-1185	TA Edge: Fix - Unable to recognize transcript's project on homepage. 
* QA-1252	TA Edge: Fix - Port Number is missing in invitation link
* BE-2269	TA: Fix - Action Items are no longer included in the PDF and Docx
* QA-1198	TA: Fix - Advanced Search View does not update after clicking ReRun.
* QA-1263	TA: Fix - After deleting any share, it still shows in the table until the user performs a hard refresh of the page
* QA-1240	TA: Fix - Downloaded pdf for Korean transcript does not open in Acrobat Reader
* QA-1248	TA: Fix - Duplicate transcripts are showing in advance search.
* BE-2275	TA: Fix - Korean sometimes being translated in addition to transcribed
* BE-2274	TA: Fix - LLM Playground needs to be able to get transcript even if user is User role and has no Download permission
* QA-1279	TA: Fix - Microphone recording and browser share menu should not be shown under actions for languages that do not have permissions for browser capture and microphone recording.
* QA-1126	TA: Fix - Null projects displayed for some meetings.
* QA-1199	TA: Fix - Some transcripts are missing a options under the 3-dot menu.
* QA-1232	Ta: Fix - Sorting is not working on MY Login sessions page.
* QA-1219	TA: Fix - The 'Incorrect Password' message should appear when a user tries to download the password recovery key with the wrong password.
* BE-838	TA: Fix - Tracking of time used does not seem to work anymore
* QA-1242	TA: Fix - User gets stuck on Upload page after submitting a file.
* QA-912	TA: Fix - User is able to upload the audio file even when the allotted storage is fully used.
* BE-2313	TA: Fix - User unable to move recording from one project to another
* QA-1205	TA: Fix - Warning not showing for upload of large file.

### May 29, 2024

**Key changes related to Transcribe APP**
* Add pages with list of login sessions (for user and for all account)
* Added "Automatic" setting for number of speakers in diarization
* In Advanced Search added Relative Time filter
* On Edge only:
  * Add Korean Language option
  * Enhanced LLM Playground to support temperature setting and markdown rendering

New:
* BE-2133	TA: Add "Go to Home" button on "Something Went Wrong" page
* BE-2202	TA: Add a 3 second timeout on the request to ipfy
* BE-2134	TA: Add Korean Language option for Edge
* BE-2078	TA: Add page with list of all logged-in sessions on the account
* BE-2182	TA: Add support for m4a files in file upload
* BE-2155	TA: Add temperature to LLM Settings
* QA-680	TA: Better reporting of Recompute in progress on Advanced Search page
* BE-2125	TA: LLM playground able to render markdown format in LLM responses
* BE-2190	TA: Modify message template used LLM Playground to work with Mixtral
* BE-2141	TA: Modify the number of speakers selector for diarization on Upload
* BE-2184	TA: Remove diarization from Live Microphone recording preview
* BE-2118	TA: Remove previous error message from the login screen as soon as the user clicks the login button
* QA-848	TA: Show all login sessions of the current user
* BE-2136	TA: Show PC Name when hovering over Installed-Connected
* BE-2164	TA: Support Relative Time search filter on Start Time in Advanced Search
* BE-1885	TA: Use Mixtral for Summarization on Edge

Fixes:
* QA-1200	TA Edge: Fix - Invitation email is not coming to the provided email address.
* QA-1236	TA: Fix - After editing any expired shared transcript to Never Expire, the save button is not working.
* QA-1223	TA: Fix - Back button is not working on Walkthrough Wizard
* QA-1153	TA: Fix - Blank page is showing for the login for one account.
* QA-1211	TA: Fix - Hover msg over Never share Expiry status is wrong.
* BE-1989	TA: Fix - Inconsistent Project membership as shown in the UI
* QA-1076	TA: Fix - Personal projects are not showing in the destination projects while moving any transcript.
* QA-1122	TA: Fix - Resend invites to bad email address throwing the something went wrong issue.
* BE-2146	TA: Fix - Right-click not working on Edge
* QA-1227	TA: Fix - Showing the American flag for all project language projects.
* QA-1197	TA: Fix - Specific No. of Speakers field is accepting blank inputs.
* BE-1987	TA: Fix - Stuck on Import/Upload page after Submit
* QA-1231	TA: Fix - There is no limit given for the Time range in advanced search.
* QA-1209	TA: Fix - Walkthrough wizards not working properly on 90% page zoom.
* QA-586	TA: Fix - When a user clicks on “edit” of a Share it automatically increases its “Expires in” time by a day.

### May 7, 2024

**Key changes related to Transcribe APP**
* LLM Playground for Edge Deployments - ask a LLM any questions about the transcript.
* Fix for negative duration of words which was impacting recomputing data from transcripts.

New:
* BE-2068	TA: Add LLM Playground page to Transcribe App (on Edge only)
* QA-1054	TA: Add validator for keyword group names
* BE-2060	TA: Option to set share within account to not expire

Fixes:
* QA-1111	TA: Fix - "ID to Clipboard" option is missing in Advanced Search.
* QA-1125	TA: Fix - After deleting any transcript, success message not showing.
* BE-2022	TA: Fix - bad http request URLs in Edge deployments 
* QA-1140	TA: Fix - Project numbers going blank after filtering role in Users under Account.
* QA-1081	TA: Fix - Proper translation should be there for mouse hovering on error.
* BE-2021	TA: Fix - running out of nonces in some scenarios
* BE-2027	TA: Fix - Sentry errors when sending to Glitchtip
* QA-1184	TA: Fix - Shared transcript page getting refresh continuously(Public share)
* QA-1141	TA: Fix - Sorting in Users under Account section is not working properly.
* QA-1143	TA: Fix - The duration filter is not working as intended, having issues setting it up manually, and also not showing the transcripts.
* QA-1167	TA: Fix - The owner is unable to log in to below mentioned IP addresses and the "Failed to fetch" error is being received.
* QA-786	TA: Fix - Transcripts with no duration are not available in advanced search.
* QA-1117	TA: Fix - Unable to edit "Users" when creating a new project.
* QA-685	TA: Fix - Updated User name is not showing on the admin Speaker screen
* QA-1116	TA: Fix - Walkthrough wizard not working properly, back button not working when user tries to go back from the transcripts.
* BE-2013	TA: Fix - When inviting the user to the account, if we provide an invalid email it throws a 500 error and goes to the "Something went wrong" page
* QA-1114	TA: Fix back button from transcript opened from Advanced Search results

### April 16, 2024

**Key changes**
* Cloud version uses whisper:small for English (it already used whisper:medium for foreign languages)
* Generating just one Action Items table per entire transcript instead of one per Section.
* Fixed errors in PDF and DOCX generation for some meetings

New:
* BE-1595	TA: Improve the User Edit Dialog - project selection
* BE-1699	TA: Better message if there are no other users on the Project
* BE-1870	TA: Improve the User Delete dialog
* BE-1871	TA: Make the Avatar icons larger
* BE-1881	TA: Display Release Version in the app.
* BE-1893	TA: Upload Zoom files using POST/data/s3 API
* BE-1913	TA: Add option to copy session id to Clipboard
* BE-1936	TA: Add browser client info to login request
* BE-1975	TA Cloud: Enable whisper:small on English language
* QA-1036	TA: Show allowed characters when entering a tag
* QA-1041	TA: Added 365 days time limit for expiry of shared transcript.
* QA-1089	TA: Added sorting by email to Users table

Fixes:
* BE-1585	TA: Inspect all cases of using "dangerouslySetInnerHTML"
* BE-1724	TA: Fix - SyntaxError: The string did not match the expected pattern, during fetchVersion in AppReloadModal
* BE-1725	TA: Fix - TypeError: Failed to fetch version.json
* BE-1727	TA: Fix - TypeError: c is not a function at handleDelete in components/ProjectsList/DeleteMultiSelectDialog
* BE-1835	TA: Fix - Try Again button has no effect after a failed upload
* BE-1841	TA: Fix - Unable to select audio files for upload on iPad
* BE-1857	TA: Fix - Generated Avatar not working ok for single user account where use has no avatar picture uploaded
* BE-1932	TA: Fix - Bad content security policy for GlitchTip
* BE-1937	TA: Fix - After logging in, the home page initially loads but then suddenly goes blank
* BE-1941	TA: Fix - TypeError: Cannot read properties of undefined (reading 'includes')
* BE-1945	TA: Fix - TypeError: Cannot read properties of undefined (reading 'value') on Settings page
* QA-1027	TA: Fix - Close Icon is missing on "Pair Voicegain Phone App" pop up
* QA-1031	TA: Fix - User is able to set value above 365 days on Archival Text Redaction.
* QA-1039	TA: Fix - User is able to set blank or invalid names as external speakers names.
* QA-1044	TA: Fix - bad link in the guide
* QA-1069   TA: Fix - Errors in PDF and DOCX generation for some meetings
* QA-1083	TA: Fix - Inconsistent Upload success message on upload page
* QA-1088	TA: Fix - Sorting indicators are broken for the Owned Projects and Shared Projects
* QA-1092	TA: Fix - Projects with same names getting automatically selected in Advanced Search project filter.
* QA-1093	TA: Fix - Player disappear when user clicks on anywhere near to the play button.
* QA-1100	TA: Fix - Assigning a role for invited user should be a must required filed.
* QA-1113	TA: Fix - Do not allow a tag with only underscores 
* QA-1114	TA: Fix back button from transcript opened from Advanced Search results
* QA-641	TA: Fix - Account Owner should be irremovable for any the project under Account Users.
* QA-800	TA: Improve behavior of resize on browser-share pop-up window

### March 25, 2024

**Key changes**
* Improved User deletion logic functionality.
* Added LLM Settings to Account profile
* Action Items tables now correctly rendered in PDF and DOCX
* Upload audio data directly to storage without sending data through data API service
* Improved tables with lists of Shared transcripts (User and Admin view)

New: 
* BE-1189	TA: Add option for Admins to see what others have shared
* BE-1271	TA: Support a workflow for the Admin to delete a user account and take over the user's project
* BE-1536	TA: Improved Splash page after login which shows the different stages
* BE-1646	TA: If there are no devices we show 2 options: download and phone app setup
* BE-1708	TA: On All Shares table, added sorting and filter on the Creator column, and filters on the Scope and Expires columns
* BE-1709	TA: In account users show Own Projects and Shared Projects columns in place of the current single Projects column
* BE-1713	TA: Modify the PDF output to render markdown tables
* BE-1714	TA: Modify the DOCX output to render markdown tables
* BE-1721	TA: Improved error message on the Zoom directory upload
* BE-1733	TA: Generate avatar based on user name if they have not uploaded a picture for avatar
* BE-1741	TA: Add extra parameter to /asr/transcribe/async request used in Microphone transcription
* BE-1744	TA: Upload files using the POST /data/s3 API
* BE-1807	TA: Add LLM Settings to Account profile
* BE-1810	TA: More functional user delete
* BE-1818	TA: Show info of users that have been deleted
* BE-1823	TA: Add Polish language transcription
* BE-1834	TA: Remove "Sync From Cloud" button
* QA-1009	TA: Increase max number of transcripts shown on home page from 100 to 250
* QA-1010	TA: Show the Upgrade button only to the Owner role
* QA-1017	TA: Better error message in case of an error resetting password
* QA-1021	TA: When user is deleted all user sessions will be invalidated.

Fixes:
* BE-1629	TA: Fix - It is impossible to share a project with an Owner of the account
* BE-1734	TA: Fix - Sorting of devices by date broken if any device is deleted
* BE-1802	TA: Fix - Search for creator by name in Advanced Search filter
* QA-1012	TA: Fix -  Project setting- Save button enabled when there is no change
* QA-1022	TA: Fix - In some rare cases Voice Signature page is showing white page.
* QA-887	TA: Fix - Walk through wizard should get automatically initiated when new user logs in for the first time.
* QA-929	TA: Fix -  Project (number) information is confusing
* QA-967	TA: Fix - User is able to add invalid keywords under project setting.


### March 4, 2024

New functionality:
* BE-1559	TA: Automatically update the currently installed Zoom App version
* BE-1582	TA: Add "Mine | Shared | All" selector to the home page
* BE-1625	TA: Add a logout confirmation dialog.
* BE-1642	TA: Show avatars on Account Users table
* BE-1659	TA: Support action items using GPT for cloud Transcribe App
* BE-1665	TA: Support action items using custom LLM for Edge 
* BE-1669	TA: Advance Search  - Type filters populated dynamically from audio_src in fields api.
* BE-1671	TA: Hide the project settings for the Key Items

Fixes:
* BE-1596	TA: Fix - Zoom Device Approvals pop up on wrong accounts
* BE-1629	TA: Fix - It is impossible to share a project with an Owner of the account
* BE-1649	TA: Fix - When the delete button is clicked in advanced search, it triggers an incorrect API, leading to inaccurate transcript result, Furthermore, post-deletion, filtered and searched data fail to display accurately.
* BE-1652	TA: Fix - Reload button does not work on Firefox
* BE-1664	TA: Fix - deleting a project should also remove its meetings from databases
* BE-1702	TA: Fix - Advanced Search page goes blank with TypeError: Cannot read properties of undefined (reading 'split')
* QA-822	TA Edge: Fix - User (Role) is able to access Account settings.
* QA-853	TA: Fix - No options to select under "creator" filter in advanced search.
* QA-856	TA: Fix - Alert msg of "maximum allowed minutes exceeded" is not translating in other languages.
* QA-888	TA: Fix - In Advanced search deleted transcript are not getting removed from list, unless we refresh the page.
* QA-892	TA: Fix - partial Translation is there while uploading a file
* QA-903	TA: Fix - There should be proper translation on the share pop-up page.
* QA-913	TA: Fix - Walk through wizard gets hidden after few steps, when left menu is locked.
* QA-920	TA: Fix - For a single project, the move should be disabled 
* QA-931	TA: Fix - User is able to de-select all filters on home page for shared.
* QA-938	TA: Fix - Different loading screens when deleting a single share in compared to deleting multiple shares.
* QA-940	TA: Fix - User is unable to "generate " the JWT token.
* QA-944	TA: Fix - Owner should not be allowed to delete all of its project if any user have shared any project with him.
* QA-946	TA: Fix - Unable to Invite user after we edit a user in account section.
* QA-947	TA: Fix - Voicegain splash screen showing when project user adds other users to a project.
* QA-949	TA: Fix - Unable to close the dialog pop-up for added phrase.
* QA-950	TA: Fix - Project setting- save button overlaps with text when Spanish language is selected.
* QA-953	TA: Fix - Account with only user access can invite other account.
* QA-961	TA: Fix - While creating the first project(new project wizards) Word cloud toggle not showing properly.
* QA-962	TA: Fix - User with Admin role is not able to update address in profile section
* QA-963	TA: Fix - Language reminder- Close icon not showing properly cutting with boundary of the pop-up.
* QA-964	TA: Fix - During Signup user given company name and title, after login title missing under profile section
* QA-970	TA: Fix - Date filter is not working on advanced search page.
* QA-972	TA: Fix - Invited User is able to change "May Download" setting in account.
* QA-973	TA: Fix - Language filter under advanced search should show full language name
* QA-985	TA: Fix - Save button not working properly under profile setting.


### February 13, 2024

New functionality:
* BE-1258	TA: Add a filter on creator in Advanced Search
* BE-1472	TA: Better order of columns in the transcript table on home page
* BE-1532	TA: Record in clientSideProperties when a user downloads Zoom Meeting Assistant
* BE-1582	TA: Add "Mine | Shared | All" selector to the home page

Fixes:
* BE-1621	TA: Fix - User Profile Setting Save button stays permanently disabled after saving once
* BE-1629	TA: Fix - It is impossible to share a project with an Owner of the account
* QA-641	TA: Fix - Project Owner should be irremovable for any the project under Account Users.
* QA-760	TA: Fix - The re-upload menu again shows for the normal uploaded file, it should only show for the zoom uploaded file. 
* QA-822	TA Edge: Fix - User (Role) is able to access and edit Account settings.
* QA-843	TA: Fix - When the user tries to share the transcript as a public share and delete the transcript from the owner account, something went wrong error is showing when login in from the sign-in link on the share.
* QA-860	TA: Fix - Mouse hovering on error, message information should show
* QA-863	TA: Fix - "May Download" checkbox getting automatically disable after adding/removing a project for user (role).
* QA-875	TA: Fix - After processing URL upload blank space showing on home page.
* QA-881	TA: Fix - Clicking on the filter button on advanced search page, showing blank page.
* QA-885	TA: Fix - Voicegain splash screen showing even when deleting a transcript.
* QA-890	TA: Fix - Due to new languages added, profanity maskimg menu not showing properly on 100% zoom screen.
* QA-891	TA: Fix - In Profile deleted Shares are not getting removed, unless we refresh the page.
* QA-899	TA: Fix - Expired shared transcripts showing expiry date in negative.
* QA-906	TA: Fix - Various problems with saving edited user data from Account Settings
* QA-917	TA: Fix - Text-redaction and Archival Text-redaction crashes the app
* QA-922	TA: Fix - Blank page showing when user clicks in Profile on the "Archival text reduction".
* QA-923	TA: Fix - If no Download permission selected on user invite, getting wrong permission error
* QA-925	TA: Fix - Getting blank screen on Users page under account section.
* QA-932	TA: Fix - Voicegain splash screen showing when user save the mic capture recording.


### February 1, 2024

New functionality:
* BE-1395	TA: Improvements on the Share dialog											
* BE-1494	TA: Add Splash page on login											
* BE-1507	TA: Support French, Dutch, Portuguese, Italian languages using the whisper:medium model (Cloud only)											
* BE-1508	TA: Hide the Key-Items configuration in settings of Projects with language other than English											

Fixes:
* BE-1440	TA: Fix - Different Users not able to create Projects with the same name.											
* BE-1549	TA: Fix - For Zoom dir upload the size check should be performed only on files that actually are going to be uploaded											
* QA-723	TA: Fix - First time Login- All the links should be hyperlinked.											
* QA-760	TA: Fix - The re-upload menu again shows for the normal uploaded file, it should only show for the zoom uploaded file. 											
* QA-828	TA: Fix - New User First Login - Zoom App page is coming blank											
* QA-834	TA: Fix - Hint message is missing below Tag input field											
* QA-864	TA: Fix - Error after new login if the Project user used last has been deleted											
* QA-865	TA: Fixes in the speaker number range selection UI											
* QA-887	TA: Fix - Walk through wizard should get automatically initiated when new user logs in for the first time.											


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

















































 













































