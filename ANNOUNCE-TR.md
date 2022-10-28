### How to contact Voicegain

If you encounter any problems, just give us a shout at support@voicegain.ai

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








































 













































