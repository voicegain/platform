### How to contact Voicegain

If you encounter any problems, just give us a shout at support@voicegain.ai

### January 5, 2023

This release enables Browser Capture in the Transcribe App on Edge.

This release also addresses the following spacific issues:
* Pause was behaving like mute
* "No Microphone" option added in Browser Capture
* Cancel out of the Mic Save dialog was not working
* (Meeting Minutes) Made Modifications to the KeyItems settings in Project
  * Support negative examples and regex
  * Add Enabled toggle for each Key Item

### December 15, 2022

This release offers improved Key Items feature within the Meeting Minutes in the Transcribe App.

The release addresses these specific issues:
* (Edge users only) make some Profile fields read-only on Edge
* Add a button for applying defaults to Key Items
* Add a check for validity of regex to the Key Items Example dialog
* Switch from regex to advancedRegex for key items
* Show projects alphabetically sorted

### December 8, 2022

This release adds configurability of the Key Items of the Meeting Minutes.

The release addresses these specific issues:
* Prepopulate the Name with the file name
* Show project name on transcript detail view
* Show avatar if Speaker is a User
* In Overview view, clicking on the times in the Summary should scroll to relevant Section
* Remove the front-end bolding of keywords in key sentences (done in back-end now more accurately)

### November 21, 2022

The release addresses these specific Transcribe App issues:
* Highlight the topics/keywords in the key sentences in Meeting Minutes
* Add audio playback and transcript text links to the sentences in Overview and Key Items
* In Profile: Separate Account from User settings
* In New Project Wizard set the toggle for Meeting Minutes to enabled by default
* (Edge users only) disable Download if transcribeAppSettings has disableDownload:true

### November 16, 2022

This release adds two major new features in the Transcribe App:
* Meeting Minutes - an AI generated overview of the meeting including key sections with topics/keywords and key sentences in 4 categories: Actions, issues, Risks, Requirements. Meeting Minutes can be enabled from Project Settings.
* Text search of transcripts - from the Home page find transcripts containing the specified words.

Other Transcribe App issues addressed in this release:
* Fixed confusing text in the confirmation dialog for user deletion
* Fixed a scroll issue where the last line of transript was only partially visible.
* Do not allow Phrase example sensitivity values outside the 0-1 range
* Fixed a glitch in multi-column formatting
* Made user email not editable - the User dialog incorrectly was allowing it to be modified
* Added scroll shortcuts to the right pane in the Transcript Detail view
* (Edge usrs only) Added `Sync from Cloud` button which can be used to sync all the user info from Cloud to the Edge.
* (Edge users only) Added `Send Test Email` button. This is in preparation of the rollout of the SMTP email support on Edge.


### October 28, 2022

The key features in this release are:
* Improved diarization in the text areas where one speaker switches to another. 
* More accurate speaker Voice Signature matching.

This release fixes numerous small Web UI issues, mainly usability, in the Transcribe App related to the Voice Signature functionality made first available in the 2 previous releases.

The installer for the Zoom Meeting Assistant is now signed with an Extended Validation Certificate so you will no longer see warnings when trying to install that software.

### October 25, 2022

The release addresses these specific Transcribe App issues:

* Admin users now have access to a page for managing all Speakers
* Added ability to assign transcript speaker to a known Speaker (with or without voice signature) - also create new Speaker if needed
* Older projects were not generating topics
* Saving a project used to switch it to a different one

### October 21, 2022

This release includes improved punctuation for the English Offline transcription.

### October 17, 2022

This release provides an improved model for Offline English transcription - you will notice about 1% higher accuracy

The release provides these overall improvements to the Transcribe App:
* Voice Signature support. Users can now create voice signatures and be automatically recognized in transcripts. Next release will add support for creating Voice Signatures for other speakers based on audio.
* Phrase detection in transcript is now suported.
* Topic detection has been improved. Still a beta feature.

The release addresses these specific Transcribe App issues:
* (For Edge users) encrypt password passed in login request
* Tweaked space around arrows pointing to other speakers text
* Do not show the expiry info if the expiry time is "Never"
* Fix for browser capture -  is used to show same preview text in both channels
* Fix for issue where sometimes getting a blank page when opening transcript, which required a reload to get the page

The current version of the Zoom Meeting Assistant going with this release is 0.2.17

### September 27, 2022

This release brings the following improvements:
* Added option to move transcript to a different project
* Run additional tests when saving microphone recording to ensure audio is available for transcription
* Better tooltips regarding Project
* Improved behavior when user selects project while on Home page
* An all of the Project Settings pages show the Project name the same way we do it on e.g. Transcripts page
* Allow apostrophe in the Project name
* Change the "data not found" text to "No transcripts"
* Improved information on the Apps Download page

### September 15, 2022

This release brings a lot of small improvements and fixes, including:
* Added options for profanity masking and digits formatting
* "My Transcripts" Project now has correct Creator value set
* Added owner information on Project Settings page
* On the Cloud, for Basic Account, do not show User setting for a Project
* Creator avatars no longer vanish when I do search
* Several changes to make it easier to identify current Project and create a distinction between a Home page and a Project Transcript List page
* Show non-speaking participants on the Transcript Details page - Requires Zoom Meeting Assistant ver 0.2.11 or higher
* First project for a new user is now not called "My Transcripts" but "{firstname}'s Transcripts"

Zoom Meeting Assistant installer is now digitally signed.


Note: This release requires Zoom Meeting Assistant version **0.2.3** or higher.








































 













































