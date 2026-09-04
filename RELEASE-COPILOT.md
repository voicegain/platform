## Release 1.140.0

* Fixed silent SSO login failures from a mismatched Speech Analytics account
* Opened Speech Analytics login in a focused popup instead of a tab
* Refined diagnostics details captured as part of copy diagnostics

## Release 1.139.0
* Improved Live Transcript reliability when the IVR app changes during call connection

## Release 1.138.1

* Fixed Copy feature to include Safety Screening information in call notes

## Release 1.138.0

* Added support for config-driven Details tab display so unsupported fields no longer show Unknown values
* Fixed call details not clearing automatically when the clear timeout elapses
* Disabled the Copy button when there are no call notes to copy
* Added thumbs-up/thumbs-down feedback and view tracking for AI Suggestions
* Added option to save an AI-suggested KB article directly to the call's Salesforce Case instead of opening it in browser
* Improved error handling and overall stability

## Release 1.137.0

* Added an unread count badge on the Suggest tab that decrements as you scroll through new suggestions and persists across the call
* Suggest tab now scrolls to the first unread suggestion when opened, and new suggestions highlight as they scroll into view
* Fixed link button in AI Suggestion Card to open suggestions in exisiting tab instead of creating new tab

## Release 1.136.1

* Fixed empty split layout appearing in side panel when all announcements had expired
* Improved WebSocket error reporting and gracefully handle server-initiated connection closures
* Improved Copilot settings to apply updates automatically when the session is refreshed
* Added WebSocket connection status indicator to Transcript and Suggest tabs
* Fixed live transcript connection to only start after successful message acknowledgement

## Release 1.136.0

* Added Suggest tab with real-time knowledge base suggestion cards surfaced during active calls
* Added icon-based tab navigation with notification badges for unread content across all tabs
* Added Announcement cards in the side panel showing admin-broadcast messages with priority ordering and one-click acknowledgement

## Release 1.135.0

* Enabled real-time transcript display for both caller and agent from a single Speech Analytics WebSocket

## Release 1.132.1

* Fixed SSO login issue where mixed-case email caused real-time events to stop working

## Release 1.132.0

* Added structured call notes display with labeled fields and copy-to-clipboard support

## Release 1.131.1

* Mark Call as Transferred button will now only show if the call is 'Ongoing'

## Release 1.131.0

* Added OIDC-based authentication support for Copilot login
* Enhanced Sidepanel UI and overall user experience
* Enabled configurable real-time transcript streaming via Pusher or WebSocket
* Added support for Multiple AIVR apps based on Copilot settings
* Improved real-time communication reliability and messaging stability
* Refactored core architecture for improved scalability, session handling, and MV3 service worker resilience

## Release 1.128.1

* Modified API endpoint to work with client specific configurations
* Added agent code for client specific configurations

## Release 1.128.0

* Added Buffer and replay functionality for undelivered Copilot messages

## Release 1.126.1

* Fixed issues with call detail retain timeout settings

## Release 1.126.0

* Fixed bugs related to platform stability and error handling
* Added rate throttling and offline caching for log tracing in case of network issues
* Improved logger functions to capture useful data for issue debugging

## Release 1.125.0

* Added caller real name in the member card for easier distinction
* Fixed issue with message acknowledgement at backend upon recieving an event

## Release 1.123.0

* Added configurable after-call data retain time, with a new default value of 30 seconds
* Updated mui core packages to latest version

## Release 1.122.0

* Added AIVR App integration for UnitedAg
* Switched to new variable naming format at the backend

## Release 1.121.0

* Updated Sentry for better error tracking
* New Login Authentication Flow with Email Verification
* Updated variables to support client specific configurations
* Added new updated icons for the extension
* Removed content page interactions

## Release 1.120.0

* Voicegain Copilot - Initial setup with basic integration
