### How to contact Voicegain

If you encounter any problems, just give us a shout at support@voicegain.ai

### September 15, 2022

This release brings a lot of small improvements and fixes, including:
* Added options for profanity masking and digits formatting
* "My Transcripts" Project now has correct Creator value set
* Added owner information on Project Settings page
* On the Cloud, for Basic Account, do not show User setting for a Project
* Creator avatars no longer vanish when I do search
* Several chanages to make it easier to identify current Project and create a distinction between a Home page and a Project Transcript List page
* Show non-speaking participants on the Transcript Details page - Requires Zoom Meeting Assistant ver 0.2.11 or higher
* First project for a new user is now not called "My Transcripts" but "{firstname}'s Transcripts"

### September 6, 2022

This release brings a lot of small improvements and fixes, including:
* Fix for  wrong (previous) audio being played
* Reduced spacing in the Keyword dialog
* Tags are now displayed
* Added a password view icon to Transcribe App login
* App download page now shows on Chrome on Mac
* In Project settings - if switching the project, the settings now do switch to reflect the selected project
* Increases max file size for upload to 256MB
* Improved terminology when removing user from Project
* Fixed lag in switching between audio being played
* Added Role setting to Edit User dialog
* Header change: Latest Activity => Latest activity across all Projects
* Allow someone with role=User to share their own Projects with other users
* Handle a case where words are empty
* Changed wording on the transcript delete form

Note: This release requires Zoom Meeting Assistant version **0.2.3** or higher.

### August 26, 2022

This release brings a lot of small improvements and fixes, including:
* Add ability to delete a Keyword example
* In multi-user plans, ability to assign users to Project directly from Project settings
* Project deletion is insanteneous.
* Fix for the issue where American English is highlighted instead of Spanish which is the actual setting on the Context
* Changing Transcript name now works
* Shows error message as a tooltip over Error
* A column selected for sorting a table can now be unselected
* Sorting by storage size works properly
* Back button takes you back to where you came from rather than always returning Home
* On projects settings - we moved NER to bottom of page
* More characters are now allowed for Transcript names
* Allow max number of speakers for diarization to be 12 instead of 10

Known issue in Transcribe App:
* Uploading files larger than 128MB may fail in the Web Browser.

### August 17, 2022

This release includes a major overhaul of the Transcribe App:
* Transcribe App now supports Zoom Meeting Assistant App which can submit all your local Zoom Meeting recordings for transcription to the Transcribe App.
* New Transcript Detail display that no longer requires paging and supports transcript from overlapping speech.
* All transcripts are now stored indefinitely. The new Storage Gauge on the home page shows you storage usage. If you start running out of space you can either upgrade to a higher plan or delete some transcripts.
* Transcribe App is now available on Edge - this way you can deploy it to all users in an Enterprise and keep all your confidential data local.

This release includes improved offline speech-recognition model with about 1.5% improvement in accuracy.

### May 24, 2022

This release speeds up the transcript loading and provides tool-tips for prev/next buttons.

### June 15, 2022

Issues fixed:
* #tsw-3: Default language selection in new Transcribe App project

### May 31, 2022

Issues fixed:
* #358: (Transcribe App) Login not working if email is not lower case

### May 24, 2022

This release includes:
* Ability to set the transcript expiry to "Never expire"
* Improved pop-up preview for transcript in browser-capture mode.

### May 23, 2022

This release includes:
* Even more accurate offline transcription.

Issues fixed:
* #rcj-536: Stop users from logging into a different application from account.type
* #rcj-534: handling unknown speaker it transcript export


































 













































