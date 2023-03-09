### How to contact Voicegain

If you encounter any problems, just give us a shout at support@voicegain.ai

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


The current version of the Zoom Meeting Assistant going with this release is 0.2.17










































 













































