### Minor release 1.141.0 is scheduled for 9/26/2026 between 10:00pm and 1:00am US Central Time

New or changed functionality:
* BE-6346	Copilot: Added support for automatically applying version updates and an "Ask again later" option for the update prompt
* BE-6350	Copilot: Added support for automatically opening links in new tabs the first time they appear on a call
* BE-6341	Copilot: Added support for range-based public announcements for highest priority updates
* BE-6281	Copilot: Added support for Voicebot notes in the Details tab
* BE-6331	Copilot: Retracted announcements now show the reason and note instead of being silently removed
* BE-6319	Copilot: Transferred calls now show the transfer reason and destination agent on hang-up
* BE-6326	SA: Added a Billing card to the Call Overview page for specific roles
* BE-6306	SA: Added an Audit Status column filter to the Call History page
* BE-6332	SA: Added support for announcement retraction reasons and expiry
* BE-6307	SA: Added support for custom tags in agent and segment views
* BE-6318	SA: Added support for section-level conditionals in QA forms
* BE-6327	SA: Added support for Voicebot call segment views
* BE-6339	SA: Added support for Voicebot segments in Call History
* BE-6284	SA: Implemented logout on password change for other browser sessions
* BE-6328	SA: Improved and corrected time breakdowns for agent segments
* BE-6324	SA: Improved phone number formatting to E.164 format across the app
* BE-6305	SA: Improved the call header design for a better user experience
* BE-6285	SA: Improved the new project creation flow for a better user experience
* MST-1593	Shorten safety screening questions in the call note output
* MST-1770	Support per-day-of-week time ranges for campaigns (e.g. different Saturday range)
* BE-6292	TA: Added support for logging out other browser sessions after a password change
* MST-586	Upgrade pytorch and whisper to the latest version
* BE-6290	Web Console: Added support for logging out other browser sessions after a password change

Changes related to Integrity of Processing (fixes):
* BE-6349	SA: Fix - Call History filter row no longer wraps to multiple lines in Firefox
* BE-6304	SA: Fix - Calls list no longer briefly shows "No calls available" while call data is loading
* BE-6303	SA: Fix - Incorrect "Call in progress" banner when loading Call Details
* BE-6317	SA: Fix - Reordering columns now enables the Save Filter button on the Call History page
* BE-6329	SA: Fix - Sentiment X-axis range exceeds the duration of an agent segment on the Call Overview page

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.140.0 is scheduled for 9/4/2026 between 10:30pm and 1:00am US Central Time

New or changed functionality:
* MST-1646	Add portal referral to prior-auth intake and prior-auth status-check flows
* BE-6254	Copilot: Added account and SA session mismatch detection for SSO login
* BE-6255	Copilot: Improved SSO login with a focused popup window for a better user experience
* BE-6200	Copilot: Improved the release date and release notes mechanism for better accuracy
* MST-1638	Enable YTD claim and claim-detail fax-back for all clients
* MST-1649	Implement an advanced member filter (also on the campaign view)
* MST-1650	Improve the engagement web app dashboard
* MST-1534	Include inbound calls in the member timeline via member's phone-number query
* MST-1469	Inspect and Resolve Redaction Issues Reported by customer before July 2026
* MST-1606	Integrate with the Reassigned Number Database (RND) and add a per-campaign scrub flag applied during the nightly scan
* MST-1633	Reduce first-message latency in the outreach campaign bot
* BE-6269	SA: Added QA form versioning support in settings and the call review form
* BE-6260	SA: Added the reference number to the call history page with filter support
* BE-6273	SA: Added tooltips to each card on the voicebot dashboard for a better user experience
* BE-6270	SA: Improved red flag question UX by hiding fractional values in the call review form
* BE-6279	SA: Improved the display of multi-value questions in the call review form
* BE-6261	SA: Made the channel name copyable in the Call Debug tab
* BE-6256	SA: Redesigned the call details overview page for a better user experience
* BE-6225	SA: Redesigned the team creation and editing flow for a better user experience
* MST-1644	Update production dashboard bot list and group by client
* BE-6262	Web Console: Added a percolator sound toggle in the telephony bot app
* BE-6265	Web Console: Added support for bot, queue, and agent saConfig in settings and the telephony bot app
* BE-6272	Web Console: Added support for RingCentral RingEX CCaaS integration in the phone app
* QA-3649	Web Console: Unsupported pages now redirect to Home on mode switch

Changes related to Integrity of Processing (fixes):
* BE-6293	Copilot: Fix - Update notifications and the "Update now" button now reliably appear when a new version is available
* QA-3690	Voicebot Demo: Fix - Blank screen with a content-blocked message displayed when clicking the Contact Sales button
* QA-3668	Web Console: Fix - 2FA QR code was cut off at the corner at 100% browser zoom on smaller screens
* QA-3662	Web Console: Fix - Both success and failure notifications appear when an incorrect OTP is entered
* BE-6156	Web Console: Fix - Intermittent unexpected logout issue

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.139.0 is scheduled for 8/19/2026 between 11:00pm and 1:00am US Central Time

New or changed functionality:
* BE-6170	New: RingCentral RingEX integration — new CCaaS integration
* QA-3641	SA: Added a 10,000-call limit for exports on the Call History page
* BE-6189	SA: Added manual call audits for QA forms and QA audit report export
* BE-6134	SA: Enhanced the Voicebot display card in Call Details for consistency with Copilot
* QA-3630	SA: Improved onboarding screen colors for a better user experience
* BE-6096	Web Console: Added Voicebot display preview for live YAML
* BE-6169	Web Console: Removed call recording and transcription settings from the AIVR App dialog as both are now always enabled
* BE-6224	Web Console: Removed the Gateway tab from the Telephony Bot App configuration dialog
* BE-6228	Web Console: Replaced the AIVR app selector with a context selector for the Five9 connect flow
* MST-1594	Add a generic counter in bot logic returning total characters spoken by each bot session
* MST-1628	Add caller_id_number and caller_id_name columns to Campaign table and include them in the dial request when set
* MST-1586	Design and implement bot A/B test framework — % traffic split between bot versions with logging
* MST-1549	Implement Casey 2.0 intake stage composing the intent detection and collect-account skills + verify stage
* MST-1573	Improve voicemail detection in the outbound bot and test against voicemail + iOS call screening
* MST-1581	In multi-agent flow, reuse caller-provided query data instead of re-prompting for it
* MST-1534	Include inbound calls in the member timeline via member's phone-number query
* MST-1469	Inspect and Resolve Redaction Issues Reported by customer before July 2026
* MST-1605	Integrate with the National DNC database and add a per-campaign scrub flag applied during the nightly scan
* MST-1606	Integrate with the Reassigned Number Database (RND) and add a per-campaign scrub flag applied during the nightly scan
* MST-1633	Reduce first-message latency in the outreach campaign bot

Changes related to Integrity of Processing (fixes):
* BE-6205	Copilot: Fix - Improved Live Transcript reliability when the IVR app changes during call connection
* QA-3643	SA: Fix - Agent names missing from Call History after the agent was deleted from Users
* BE-6155	SA: Fix - Deleted QA Form sections remained visible until refresh
* QA-3650	SA: Fix - Error when manually editing the scheduled time of an announcement
* QA-3642	SA: Fix - Incorrect call count briefly displayed when switching between calls and segments in Call History
* BE-6122	SA: Internal/queue transfers now split into bot + agent segments — fixes live agent labeled "Voicebot" and inflated voicebotDuration in analytics
* BE-6248	Web Console: Fix - AIVR App changes are no longer silently overwritten when two people edit the same app at the same time; you'll now see a clear warning if someone else saved changes first.
* QA-2870	Web Console: Fix - Dropdown arrows not clickable for some fields on the Speech Recognition Settings page
* MST-1621	Fix - multi-agent info collection bug - the clarify branch returns the follow-up question without ever running extraction
* MST-1622	Fix - NPI question gets "No problem" and abandonment

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.137.0 is scheduled for 7/7/2026 between 11:00pm and 1:00am US Central Time

New or changed functionality:
* BE-5889	/user API: added lastActive field to record last user activity on the platform
* MST-1521	Add safety-screen trigger to realtime agent assist with suggested screening questions
* MST-1540	Added digit formatter rule to convert spoken "dot" delimiters to literal dots (ddd dot ddd dot ddd -> ddd.ddd.ddd)
* BE-5786	Added queue name to the transcript with annotation for call note generation
* BE-5787	Added safety screening to Copilot call note
* MST-1532	Built an interactive SMS chatbot using Telnyx
* BE-5899	Built-in UK currency grammar
* BE-5965	Call Metric dashboard now shows actual number of total calls instead of rounding off
* MST-1523	Capture date of service in eligibility automation flow to select correct eligibility, accumulator, and benefits data
* BE-5973	Changes to prevent OOM in data-api
* BE-5968	Copilot: KB suggestion link needs to be opened in current tab & replace window.open with chrome.tabs.update
* BE-6011	Copilot: Suggest tab now shows an unread count and scrolls to the first unread suggestion when opened, highlighting new ones as you reach them
* MST-1502	Developed redaction algorithm to redact security-question answers from transcripts
* BE-5941	Do proper validation of Call Review form and also the Call Insights config when doing import
* MST-1506	Fallback to Claim ID query when DOS and billed amount search fails
* BE-5927	Finalized new streaming TTS plugin for unimrcp
* BE-5853	GET /sa/agent-stats: deprecated avgReviewScoreManual & avgReviewScoreAutomatic
* MST-1526	Harden DOB parsing & improve extraction accuracy and reject partial dates
* BE-5896	Implemented answer_redact formatter (security-question answer redaction) 
* MST-1527	Interpret DTMF-entered claim amounts as both whole-dollar and decimal values
* BE-5767	mrcp-rex: Add proper handling for errors writing to rex sockets mid session
* BE-5937	Populate queue wait time in sa call also for not abandoned calls if we have queue wait time info available
* BE-5950	POST /sa/call/search: added support for additional sort_by fields
* BE-5960	POST /sa/call/segment/search: support for additional sort_by fields(sentiment, incidents, segmentSeq) added
* MST-1546	Redact app data value if the key contains "password" or "token"
* MST-1518	Redesigned eligibility data class to support multiple plan types, coverage ranges, and plan IDs
* MST-1462	Research and migrate to a more responsive model for semantic endpointing in llm-svc
* BE-5931	Returned per-agent acknowledgement details (name, team, status, timestamp) for active & archived announcements
* BE-5900	SA call/segment search: implemented callId default sort + tie-breaker
* BE-5930	SA: Added announcement acknowledgement tracking modal
* BE-5867	SA: Added announcement preview for creating and editing announcements
* BE-5915	SA: Added CCaaS Call ID to the Call History/Recent Calls page
* BE-5989	SA: Added justification to NPS and CSAT scores on the call overview page
* QA-3552	SA: Added relative time support for announcement filters for a better UX
* BE-5650	SA: Added select/deselect all support to the call history column selector
* BE-5849	SA: Added Submit a Support Ticket functionality via Freshdesk
* BE-5929	SA: Added support for cloning existing announcements
* BE-5676	SA: Improved pagination on the call history page and removed sorting from nonessential columns
* BE-5898	SA: Updated the calendar icon for better UX
* MST-1499	Support accumulator data in eligibility and benefits automation workflows
* BE-5916	Synced deleted call records to analytics database
* BE-5951	Vonage webhook: added support for accepting connectedCallData.transferredFrom / transferredTo fields
* QA-3574	Web Console Edge: Removed billing page icon and access
* QA-3565	Web Console: Showed success message after adding transcription keyboard shortcut

Changes related to Integrity of Processing (fixes):
* QA-3586	Copilot: Fix -  Unable to copy co-pilot notes from co-pilot extension.
* BE-5962	Copilot: Fix - SSO login failed on the first try via the SA app due to an expired session
* MST-1515	Diagnose and fix VAD early barge-in issue in MRCP ASR
* MST-1529	Fix - discovered exception in llm-svc and guarantee exception fallback to agent transfer
* BE-5864	Fix - asr-api - LEAK: ByteBuf.release() was not called before it's garbage-collected.
* BE-5877	Fix - audio-server - LEAK: ByteBuf.release() was not called before it's garbage-collected.
* MST-1528	Fix - DTMF digits captured into member NAME field during combined name+DOB verification prompt
* BE-6014	Fix - Fields API is too slow
* BE-5879	Fix - RejectedExecutionException is encountered soon after PUT /aivr/uuid with loop=stop is received
* BE-5888	Fix - rex - LEAK: ByteBuf.release() was not called before it's garbage-collected.
* QA-3582	Fixed 500 internal server error on Call History and Recent call pages
* QA-3580	Fixed analytics dashboard showing white page error
* QA-3575	Fixed Announcements acknowledgement bar showing higher total count that the actual number of agents in the account
* QA-3572	Fixed empty-state cropped message text in Call Metrics Widgets
* QA-3558	SA: Fix - Agent last name was not displayed on the upload call audio popup
* BE-5759	SA: Fix - Full-size audio player overlaid call detail page content
* BE-6013	SA: Fix - Help menu now shows a Knowledge Base Articles option
* BE-5967	SA: Fix - Review form showed the wrong question count and updated the red flag icon
* QA-3576	SA: Fix - Send To dropdown showed non-agent users when set to Agent
* QA-3548	TA: Fix - Size in Storage column filtering and sorting did not work properly on the transcript list page
* BE-5876	Web Console Edge: Fix - Copy did not work for API token on the API settings page for some users
* BE-5788	Web Console: Fix - Audio playback now stops automatically when navigating away from the transcript Audio Player page.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.136.0 is scheduled for 6/15/2026 between 11:00pm and 1:00am US Central Time

New or changed functionality:
* BE-5766	Added Announcements feature to SA App and Copilot
* BE-5758	Added Name and Description to a Phone Number
* BE-5609	Added on-device encryption to Desktop Recorder and smart phone Voicegain Recorder
* BE-5550	API to check if asr-api is listening for a specific websocket endpoint
* BE-5765	Bridge Vonage CCaaS transcripts into realtime SA pipeline for Copilot
* BE-5852	Control kb recommendation generation and sending to Copilot using customValues setting on a Context
* BE-5789	Copilot: Agents now see admin announcements as priority-ordered cards in the side panel before calls, with expiry date indicators, expandable content, and one-click acknowledgement to clear each message.
* BE-5791	Copilot: Introduce new UI for AI Suggestions
* BE-5774	Copilot: Real-time transcripts and speech analytics are now shown live during Vonage VCCA calls in the Copilot panel.
* BE-5842	Deprecated detailed flag in GET /sa/offline API
* BE-5752	Detecting abandon/disconnect calls for Vonage 
* BE-5332	Enhanced Copilot Call Notes with Structured Multi-Field Call Note
* MST-1353	Implemented Salesforce integration for Real-Time Agent Assist in ml-svc
* MST-1438	Implemented service integration with the standard Casey client API
* BE-5823	Optimized GET /sa/offline API
* BE-5801	Realtime Knowledge Base recommendation for SA: config tenantName + websocket kbRecommendation list
* BE-5761	Removed long-deprecated /sa & /asr request fields; mark /sa as real-time-only (deprecate OFF-LINE asyncMode and acousticModelNonRealTime)
* QA-3532	SA: Added Tenure Start Date Field to Bulk User CSV Upload
* QA-3335	SA: Use download permission to decide what user role will see the Download button
* BE-5817	Salesforce Knowledge Base Recommendation Feature
* MST-1464	Tuned Whisper parameters to prevent large transcript chunk drops
* BE-5799	Validate grammars before consuming them

Changes related to Integrity of Processing (fixes):
* BE-5833	Fix - AivrRexClient looped-whisper wait is non-interruptible; 5h default leaks taskExecutor threads
* BE-5805	Fix - AivrRexClient.parseCorrections throws UnsupportedOperationException on correction result that leads with addMark
* BE-5746	Fix - NPE in BillingService.getCurrentBalance when Account.billingAccountId is null
* BE-5804	Fix - Rex-bundle GrammarManager fails to resolve session: URI after DEFINE-GRAMMAR â€” Completion-Cause: 004 gram-load-failure
* BE-5233	Fixed DTMF keypad inputs being displayed as bot/agent responses in the call transcript for AIVR calls.
* QA-3541	SA: Fix - API Secret Creation Shows Success Message When Duplicate Key Name Validation Fails
* QA-3512	SA: Fix - Date Range Filter Dropdown Does Not Open in â€œMore Filtersâ€ Panel on 1536Ã—730 Screen Resolution
* QA-3526	SA: Fix - Duplicate Transfer Columns Displayed in Recent Calls Grid
* QA-3513	SA: Fix - Error Popup Should Auto-Dismiss After Certain Time
* QA-3542	SA: Fix - Getting error on Announcements page for Manager and Agent role.
* QA-3514	SA: Fix - LOB Filter Dropdown Data is Not Clearly Visible
* QA-3518	SA: Fix - QA Form questions with conditional logic set to "Review Question" type can now be saved without a validation error.
* BE-5839	SA: Fix - Sidebar profile shows deprecated role field (Agent shown as "User")
* QA-3515	SA: Fix - Topic Dropdown Values Are Truncated and Not Fully Visible
* QA-3507	TA: Fix - Clearing a numeric metadata field set to "Use for Name of Recording" now fully removes the value from the recording Name field.
* QA-3505	TA: Fix - Mandatory field indicator (*) in the recording metadata acknowledgement popup now displays in red, matching the required-field styling used throughout the product.
* QA-3504	TA: Fix - Start and Cancel buttons in the Live Microphone Recording popup are now properly centered with balanced spacing.
* QA-3509	TA: Fix - UI Alignment Issue â€“ â€œText to acknowledgeâ€ Label Overlaps Input Field When â€œAcknowledgeâ€ Type is Selected
* BE-5788	Web Console: Fix - Audio playback now stops automatically when navigating away from the transcript Audio Player page.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.135.0 is scheduled for 5/24/2026 between 11:00pm and 1:00am US Central Time

New or changed functionality:
* MST-1435	Added claim and eligibility automation rate line charts to Voicebot Superset dashboard
* BE-5739	Added new realTimeTranscript copilotSetting in AIVR App
* BE-5613	Added to /webhook API support for asr_realtime resource
* BE-5698	Agent Announcement & Messaging Module â€” Backend API Implementation
* BE-5141	Copilot: Added support for consuming caller and agent transcripts from a single /sa websocket
* BE-5143	Generate call notes from transcription results in the RT SA session
* BE-5734	GET /sa/dashboard: Added accountId field to SaDashboard for account-scoped filtering
* MST-1334	Implemented real-time checklist validation for Agent Assist in ml-svc
* BE-5673	Improved website description for each of our app links
* BE-5725	Include speaker info in the message of RealTimeTranscript event
* BE-5595	Populate saCallBackReference on Call Review Answers responses (back reference from crAnswers to Call / Call Segment)
* MST-1433	Refactored Telnyx API integration to be stateless using presigned URLs and data object references
* BE-5662	SA: Added Back to login and Resend email options on forgot password pages
* QA-3434	SA: Calls count added on the Agents page
* BE-5753	SA: User ID now displays in the edit user modal
* BE-5627	SA: Users can no longer access hidden page routes directly via URL
* MST-1437	Simplified voicebot WebSocket design to support wordstream-only communication
* BE-5581	Standardize 400 / 404 responses on all /sa/call/{callId} and /sa/offline/call/{callId} endpoints
* BE-5606	Support encrypted uploads on POST /data/file and POST /data/audio via keyPairId (CMS EnvelopedData / RSA-OAEP-SHA256 / AES-256-CBC)
* BE-5142	Support SA session ID in the AIVR POST callback
* BE-5745	Web Console: Added support for realTimeTranscript copilot setting in AIVR App
* https://gitlab.com/voicegain/devops/environment-tracking/-/commit/e5ab1aa5bf4b170b4adbba657947267e27733a7c changed waveform_uri for onPrem

Changes related to Integrity of Processing (fixes):
* BE-5750	Fix - ml-svc ProcessText: ValueError on dollar-amount formatting (int('.07'))
* BE-5795	Fix - POST /rex/RecognizeAudio is applied to requests derived from offline /asr/recognize/async requests by mistake
* BE-5751	Fix - POST /sa/call creates users with an identical email if the email is in mixed case
* QA-3483	SA: Fix - AIVR Integration disables Save when no valid app is configured and shows deleted apps as unavailable
* QA-3519	SA: Fix - Call IDs on Call Metrics and Insights dashboard page redirects to PROD env upon click.
* QA-3391	SA: Fix - Call Summary is labeled as Call Notes in downloaded PDF and DOCX.
* BE-5651	SA: Fix - Date selector is now functioning correctly on the Voicebot Dashboard
* BE-5723	SA: Fix - Last active date incorrectly showed the current date for some users in the users table
* BE-5658	SA: Fix - Navigation issues with call count on the call details page
* QA-3479	SA: Fix - PDF content is cropped when downloading QA Score Agent report
* QA-3502	SA: Fix - The selected section on Call metrics dashboard is not visible in Dark mode.
* BE-5712	Web Console: Fix - Lingering UI effect on a button

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


### Minor release 1.134.0 is scheduled for 5/4/2026 between 11:00pm and 1:00am US Central Time

New or changed functionality:
* BE-5582	Add and populate name column in sa_project table 
* BE-5684	Add customUniqueId to AI Output (POST /internal/aiOutput, GET /aiOutput, GET /aiOutput/{aiOutputId}) with uniqueness per (contextId, customUniqueId)
* BE-5685	Add maxWhisperTransferPlayTimeMs to AIVR App: cap whisper transfer prompt playback and DTMF Agent Code listening
* BE-5623	Add optional userId on POST /sa/offline speakers[] (Voicegain User reference), echo back in GET /sa/offline/{saSessionId}/data and allow modify via PUT /sa/offline/{saSessionId}/spk
* MST-1354	Add sentence-level streaming support in ml-svc alongside word stream
* BE-5555	Added Call Resolved Filter on Call Metric Dashboard
* BE-5617	Added CALL_INSIGHT_BOOL search field to Call and Call-Segment search
* BE-5568	Added GET /security/find/jwt/stale endpoint to list stale JWT tokens in the caller's account
* BE-5573	Added timeBreakdown response field and query parameter to GET /sa/offline/{saSessionId}/data
* BE-5493	Added to aivr.lua ability to do direct bridge to failover destination if the AIVR API returns error.
* BE-5587	Admin Tool: Hid logs page from the menu options
* BE-5585	Annotated the APIs used by SA App with vgAuditLogger
* BE-5558	Change the default value of the `discoverable` field in POST /user
* BE-5664	Control sending data to salesforce using customValues setting on a Context
* BE-5556	Created chart for visualizing QA score per agent over period of time
* BE-5709	Customer cant see "moods" in the output. (deprecated properly)
* BE-5544	Enabled download data as csv/xls for charts in superset dashboards
* BE-5580	Ignore deprecated call-resolution fields in Call Review and SA Config (replaced by Call Insight `RESOLVED`)
* BE-5642	Implemented AI Output Feedback API (POST/GET /aiOutput, POST /aiOutput/{aiOutputId}/feedback) with Postgres backing store
* BE-5584	Implemented Key Pair APIs on Context (/confgroup/{uuid}/keyPair)
* BE-5542	Implemented POST /security/find/jwt - look up account/context by JWT token
* BE-5333	Implemented POST /user/bulk - bulk user creation from CSV
* BE-3916	Implemented redundant outbound dialing (using multiple voice connectors)
* BE-5557	Integrate SalesforceDao with AIVR
* BE-5429	Obtain and use Vonage Audio
* BE-5566	Populate read-only `createdBy` field on User when created via POST /user and POST /user/bulk
* BE-5595	Populate saCallBackReference on Call Review Answers responses (back reference from crAnswers to Call / Call Segment)
* BE-5603	Primary/replica datasource routing hardening in Postgres DAOs
* MST-1347	Productize benefits automation using complete benefits summary data
* BE-5498	QA Score AGENT DASHBOARD - Superset refinement
* BE-5375	Redesign Call Metrics Page in Superset
* BE-5622	Retrieve  Voicegain Response objects from SalesForce
* BE-5547	SA: Added Created By and Last Used columns to the API Tokens page
* BE-5589	SA: Added project switching based on the current call on the call detail page
* BE-5592	SA: Added project timezone to the sidebar tooltip for the current project
* BE-5537	SA: Added role display to the profile menu
* BE-5641	SA: Added support for call insights search filters in call and segment history
* BE-5598	SA: Added support for showing or hiding the call download button based on user permissions
* BE-5727	SA: Clear filters when switching between tabs on recent calls page
* QA-3451	SA: Highlighted expiry calls on the Call History page for better UX
* QA-3438	SA: Improved validation for call review QA sections and questions
* QA-3439	SA: Improved validation for creating call insight questions
* BE-5618	SA: Migrate the project to Node version 24
* BE-5435	SA: Redesigned Call History saved filters for better UX
* BE-5438	SA: Redesigned the Agent Segment Detail page for better UX
* BE-5437	SA: Redesigned the Full Call Detail page for better UX
* BE-5588	SA: Removed unsupported isCallResolution option from QA and review forms
* BE-5455	SA: Updated columns and filters for Call History and Segment History pages for better UX
* BE-5683	SA: Use smoothSentiment instead of emotion.list for sentiment chart in CallSentimentCard
* BE-5671	Split CallTimeBreakdown voicebot/caller fields on GET /sa/offline/{saSessionId}/data (add voicebotSegSec, callerInAgentSegSec; redefine voicebotSec, callerSec)
* BE-5625	Store feedback for Voicegain Recommendation retrieved from Salesforce
* BE-5457	Superset Call Metric Dashboard with multiple tabs
* BE-5444	Superset Call Stats Dashboard
* MST-1363	Switch demo bot upfront prompt to improved Google voice and remove SSML usage
* BE-5548	TA: Added Created By and Last Used columns to the API Tokens page
* BE-5520	Upgraded to Java 21
* BE-5559	Utility that changes value of the discoverable field on users in account types other than SPEECH-WORKS
* BE-5546	Web Console: Added Created By and Last Used columns to the API Tokens page

Changes related to Integrity of Processing (fixes):
* BE-5593	Fixed -   Missing talk field from speakers on segmentAnalyticsResults
* BE-4613	Fixed - added missing failover gateways to FreeSWITCH
* BE-5619	Fixed - call.download permissions are not included in responses of User APIs (also call.rerun)
* BE-5553	Fixed - Invalid value for `overtalk_single_duration_maximum_threshold`, must be a value greater than or equal to `1`
* BE-5680	Fixed - NPE in ascalon-cleanup on prod
* BE-5607	Fixed - on SA Call segmentSeq not populated but saSessionSegmentSeq is there
* BE-5615	Fixed - prompt caching on FreeSWITCH
* BE-5545	Fixed - Sentiment KPI score chart not changing when changing Queue in Sentiment Dashboard
* BE-5722	Fixed - SpeakerTimelineSentimentInfo.isAgent is not set under segmentAnalyticsResults for bulk upload
* BE-5549	Fixed - Team filter is not populated in all dashboards
* BE-5726	Fixed - VCCA post-processing fails when only one speaker captured (diarization validation error)
* BE-5597	Fixed - Whenever normalizedScore changes on crAnswers need to update score on sa call (segment)
* BE-5508	Fixed fssk recording delete permission: fssk container (UID 1001) cannot delete files owned by root in freeswitch container
* QA-3441	SA: Fix - Bulk inviting of all users fails if any one of them has the Owner role.
* BE-5569	SA: Fix - Call History page was stuck loading after context changes
* QA-3489	SA: Fix - Call Recompute Button Missing in Call History Screen
* BE-5586	SA: Fix - Call Review Form still processing isCallResolution despite of setting it to false in the QA Form question
* QA-3491	SA: Fix - Caller percentage is missing in Call Time Breakdown in calls.
* QA-3461	SA: Fix - Clear button for custom date filter did not work on the Call History page
* QA-3487	SA: Fix - Error fetching agent stats (400 Bad Request) on opening Integration page
* QA-3442	SA: Fix - Export functionality is not working in Coach Role. Data is available in the table but is missing in the exported CSV file.
* BE-5575	SA: Fix - For some calls the sa/offline/{saSessionId}/data response returns 404, and the Call Details page gets stuck in an infinite loop
* QA-3440	SA: Fix - Incorrect/Unclear error msg when trying to invite user with Owner role using Bulk user upload.
* QA-3448	SA: Fix - In-progress calls were shown as dead air calls
* BE-5645	SA: Fix - Issues in saving data to the LLM Summary Prompt Field on SA Config Settings
* BE-5647	SA: Fix - LLM Prompt Summary does not switch to the correct value when changing tabs on the SA Config page
* QA-3455	SA: Fix - Role filter showed fewer options for users with limited permissions
* BE-5679	SA: Fix - Sentiment is not shown for a segment - in a call where the full call had no sentiment calculated
* BE-5591	SA: Fix - Sorting by Last Active did not work properly in the Users table
* BE-5646	SA: Fix - The backend does not persist saved value of LLM Prompt Summary field correctly
* QA-3378	SA: Fix - Unable to load QA Score Dashboard for Agents, shows the error: â€œFailed to obtain Superset guest token.â€
* QA-3432	SA: Fix - Unable to switch responder types when LLM was selected in the QA form
* QA-3495	SA: Fix - Unexpected error on Repeat Call page scroll in Speech Analytics application
* QA-3473	SA: Fix - Voicemail download option was not working on the voicemail detail tab
* BE-5590	Web Console: Fix - Copy to Clipboard failed in the AIVR App Data table

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.133.0 is scheduled for 4/12/2026 between 10:00pm and 12:00am US Central Time

New or changed functionality:
* BE-5447	Added 2 new voicemail-related user permissions
* BE-5471	Added audio field to POST /public/webhook/vonage to submit call recording via presigned S3 URLs
* BE-5423	Added enabledByDefault field to SA Dashboard response
* BE-5468	Added epochLastUsed and createdBy fields to confgroup newSecret responses
* BE-5405	Added GET/PUT/DELETE /account/{accountId}/maintenance API endpoints
* BE-5408	Added obfuscate parameter to SA offline API methods
* BE-5418	Added obfuscate settings with queueNames to AIVR App
* BE-5399	Added PUT /confgroup/{uuid}/newSecret/{secretId}/regenerate endpoint
* BE-5406	Added text answerType and answerText field to Call Insights
* BE-5451	Added text/csv response support to GET /user endpoint
* BE-5466	Added waitForAudio field to PUT /aivr/{ivrSid}/vcca and new PUT /aivr/{ivrSid}/vcca/audio endpoint
* BE-5495	Added wordsStartAtMs query parameter to GET /sa/offline/{saSessionId}/data
* QA-3331	Admin Portal: Fixed - No Data Displayed on Terms and Service Page
* BE-5417	Apply obfuscation to select groups of Vonage calls
* MST-1234	Detect looped conversations in multi-agent flow and offer or trigger agent transfer
* BE-5332	Enhanced Copilot Call Notes with Structured Multi-Field Call Note
* BE-5422	Ensure that GET /sa/agent-stats returns only the Agents to which the User making the request has access to
* BE-5478	Forward Vonage content.callRecording webhook to ascalon-asr-api /vcca/audio endpoint
* BE-5460	Generate segments for non-transferred speech-based AIVR calls
* BE-5496	GET /sa/call with voicemail flag - apply voicemail permissions
* BE-5531	Implemented GET /sa/call/{callId}/segment/{segmentSeq}/aivr/trace
* BE-5333	Implemented POST /user/bulk -- bulk user creation from CSV
* BE-5562	Implemented PUT /sa/offline/call/{callId}/rerun -- rerun transcription and SA for a call
* MST-1337	Improve Whisper throughput to >50 audio-hours per hour for large-turbo-v3
* BE-5517	New rules for populating sa_call fields in presence of agent and voicebot segments
* BE-5498	QA Score AGENT DASHBOARD - Superset refinement
* BE-5375	Redesign Call Metrics Page in Superset
* MST-1171	Redesign DTMF handling to support voice + DTMF per question when a DTMF grammar is provided
* BE-5467	Returns audioInput in GET /sa/offline/{saSessionId}/data when audio=true
* BE-5472	Returns toBeRecorded field in POST /public/webhook/vonage response
* BE-5421	SA: Added maintenance window configuration on the Time Settings page
* BE-5563	SA: Added re-run option to in Call History items
* BE-5452	SA: Added support for bulk user export on the Users page
* BE-5409	SA: Added support for bulk user import on the Users page
* BE-5407	SA: Added support for the new text answer type when creating call insight questions
* BE-5519	SA: Added support to show copilot debug info for agent segments
* BE-5448	SA: Changed voicemail page visibility based on user permissions
* BE-5432	SA: Hid the Segment History tab on the Call History page when agent config is not configured
* BE-5518	SA: Hiding unrelated toggles/columns if voicebot features is disabled
* BE-5449	SA: Made Call ID the first default column and renamed Segment History to Calls History for agents
* BE-5433	SA: Redesigned the call review form on the Call and Segment Details pages
* BE-5522	SA: Reordered sidebar options for agents after login and changed the landing page to calls
* BE-5538	SA: Show Copilot Notes on the call detail page with Transcript
* BE-5477	SA: Showed the last agent segment review form on the Call Details page
* BE-5487	SA: Standardized date filters, URL state, and the agent refresh icon on the Agents page
* BE-5434	SA: Updated side popup design and navigation for the Users and Account pages
* BE-5491	Sanitize URLs in Cloud API requests (Cloud Only / Not Edge)
* BE-5457	Superset Call Metric Dashboard with multiple tabs
* MST-1333	Support mid-session config updates in ml-svc gRPC streaming
* MST-1388	Support optional audio upload for transcript-generated SA sessions for playback in SA app
* BE-5366	Support POST /rex/RecognizeAudio for ASR sessions derived from an offline ASR session
* BE-5140	Support segment mode in real-time SA websocket payload
* MST-1335	Support string insight extraction in ml-svc call review processor
* BE-5464	toBeRecorded flag is returned from POST /aivr/vcca if the recording is enabled on the AIVR App
* MST-1246	Upgrade llm-svc to GPT-5.2 / GPT-5-mini in all applicable places and ensure test pass
* BE-5331	Voicebot Demo: Redesigned the desktop demo casey for improved UX
* BE-5510	Web Console: Added the ability to configure queue names in the AIVR app for data obfuscation
* QA-3433	Web Console: Hid the log page (unavailable until back-end is upgraded)

Changes related to Integrity of Processing (fixes):
* BE-5462	Fixed - [Voicebot] label incorrectly applied to agent in annotated transcript for some uploaded calls
* BE-5571	Fixed - AivrService.processLoop throws SessionNotFoundException when IvrSession was evicted by onRemoval
* BE-5506	Fixed - ArrayIndexOutOfBoundsException in MrcpStartLine when parsing MRCP start line
* BE-5523	Fixed - Audio server is not batching bytes and adding wav header for download in case of streaming audio
* BE-5535	Fixed - Azure Streaming TTS ignores voice parameter â€” all voices rendered as default
* QA-3408	Fixed - Call Insights Answers are not getting generated for Vonage integration full calls.
* BE-5552	Fixed - Call notes not pushed to copilot when waitForAudio=true (VCCA)
* QA-3407	Fixed - Call summary is not getting generated for Vonage integration full calls.
* QA-3404	Fixed - Call Time Breakdown chart is broken for Vonage integration projects full calls.
* BE-5489	Fixed - Error Disclosure reveals java classes
* BE-5503	Fixed - For Call Segment, speaker key is having value "caller" for both the entries of the sentiment.
* BE-5576	Fixed - for some SA calls the saSessionId does not resolve to an existing sa offline session
* BE-5579	Fixed - Looks like the RTP quality data is not being retrieved from CDR and put int sa call
* BE-5539	Fixed - SegmentResultsProcessor sets callSegment.team to name instead of userGroupId
* BE-5540	Fixed - sentiment field in CSV response from POST /sa/call/search is wrong
* QA-3405	Fixed - Sentiments are not generating for full calls in Vonage integration project.
* BE-5533	Fixed - SsmlDocument: SAXParseException on unescaped '&' in TTS input (e.g., "A&H")
* BE-5446	Fixed conflicting getters for name isNotApplicable on class ReviewConfig.Question
* QA-3411	SA: Fixed -  'Select All' option for Teams/Agents filter on Recent Calls page incorrectly displays and functions as 'De-Select All' when no items are selected.
* QA-3413	SA: Fixed -  The "Checkbox Selection" option is currently visible in the menu, which should not be displayed.
* QA-3436	SA: Fixed - Do not show Voicebot card for Vonage integration
* BE-5486	SA: Fixed - File upload did not show all available agents in some cases
* BE-5575	SA: Fixed - For some calls the sa/offline/{saSessionId}/data response returns 404, and the Call Details page gets stuck in an infinite loop
* QA-3415	SA: Fixed - Incorrect sentiment value shown in Call History table if the call only has Agent speaking
* QA-3462	SA: Fixed - Indicator text overlapping over selectable bar slider option.
* BE-5419	SA: Fixed - Issue with generating a new secret API key
* QA-3395	SA: Fixed - Normal silence indicator was not visible on the call overview chart for some projects
* QA-3343	SA: Fixed - On Agents page only one agent is getting shown when multiple agents have the same name but different email.
* QA-3416	SA: Fixed - Opening a segment call in a new tab via right-click loaded the full call instead of the segment call
* QA-3375	SA: Fixed - Project Search field did not clear after switching to searched projects
* QA-3428	SA: Fixed - Time Selector filters on Call History page are not working properly.
* QA-3464	SA: Fixed - Weekly date labels are not in chronological order in Call resolution on Call metrics dashboard.
* BE-5420	Web Console: Fix - Issue with generating a new secret API key
* BE-5521	Web Console: Fix - TTS audio was being cached in Configure Telephony Bot Voices

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.132.0 is scheduled for 3/19/2026 between 10:00pm and 12:00am US Central Time

New or changed functionality:
* BE-5315	Added "text" response format and "limit" field to Call Insights questions
* BE-5299	Added dashboards field to Context for storing selected SA dashboards per project
* BE-5297	Added defaultSaConfig query parameter to POST /confgroup to auto-create SA configs
* BE-5066	Added new query parameter to GET /sa/call, GET /sa/call/{callId}, GET /sa/call/search called inclSegments
* BE-5341	Added progress field to segment analytics results in SA offline responses
* BE-5353	Added progressPhase field to call segment responses
* BE-5361	Added segmentType query param to GET /sa/call/agent
* BE-5360	Added segmentType query param to GET /sa/call/queue and use sa_queue table
* BE-4904	Added support for multi-segment /sa/call (sa_call)
* BE-5116	Added to /sa/call/segment a new field called agentFeedback
* BE-5344	Allowed access to agent user for APIs /sa/call-stats and /sa/call/queue
* BE-5349	Copilot: Added support for structured call notes where version 2 is enabled
* BE-5363	Create a user for each Vonage agent
* BE-5490	Demo: Casey Voicebot - correct the Claim amount shown
* BE-5354	Deprecated VoiceCall sentiment field, compute from sentiments column
* MST-1271	Enhance logging in llm-svc for critical issues (especially external request failures)
* BE-5332	Enhanced Copilot Call Notes with Structured Multi-Field Call Note
* BE-5355	Generate call/segment notes from llmSummaryPrompt in SA Config instead of llmCopilotNotesPrompt from AIVR App
* BE-5258	Implemented API to query Pusher Events
* BE-5359	Implemented externalUserId field on User entity 
* BE-5314	Implemented GET /sa/call/insights/names endpoint for reserved question names
* BE-5085	Implemented GET /sa/call/segment
* BE-5064	Implemented GET /sa/call/segment/{segmentCallId}
* BE-5092	Implemented GET /sa/call/segment/search/fields
* BE-5298	Implemented GET /sa/dashboard endpoint in SpeechAnalyticsController
* BE-5296	Implemented GET /sa/dashboard: New read-only API to return available SA dashboards
* BE-5295	Implemented POST /confgroup: Add defaultSaConfig query parameter to create default SA configs on Context creation
* BE-5093	Implemented POST /sa/call/segment/search
* MST-1247	Integrate LLM-based diarization post-processing into the offline transcription pipeline
* BE-5357	Made llmSummaryPrompt writable on SA Config endpoints
* BE-5065	Modified GET /sa/call/{callId}, GET /sa/call, and GET /sa/call/search responses and add a new field numSegments
* BE-5117	Populate sa_call_segment field agent_feedback from the AIVR Session agentFeedback
* BE-4444	Populate topics field in /sa/offline and in /sa/call using LLM
* MST-1343	Provide Built-in Prompt for Structured Copilot Call Notes (CRM Notes)
* BE-5319	SA: Added agent codes to the users list page where available
* BE-5300	SA: Added Superset analytics dashboard visibility configuration in project settings
* BE-5316	SA: Added support for a third 'text' answer type for Call Insights questions
* BE-5269	SA: Added support for agent segment detail view pages
* QA-3324	SA: Added support for configuring dashboard visibility when creating a new project
* BE-5317	SA: Added support for exporting and importing Call Insights questions
* BE-5318	SA: Added support for exporting and importing the call review QA form
* QA-3313	SA: Added support for exporting calls on the voicemail calls page
* BE-5111	SA: Added support for multiple Call Review QA forms for agent and voicebot segments and removed full call review configuration
* BE-5288	SA: Added support for the agent segment list view on the call history page
* BE-5369	SA: Added support for up to 4 agents on the call transcript and call time breakdown detail pages
* BE-5110	SA: Added support to create multiple Call Insights questions for agent and voicebot segments
* BE-5290	SA: Added support to create multiple SA configs for each segment in configuration settings
* BE-5279	SA: Added support to hide or show voicebot and voicemail features via project feature settings
* BE-5356	SA: Added the LLM Summary Prompt setting to the configuration page
* BE-5267	SA: Adjusted implementation of Toast messages and placements
* BE-5412	SA: Change how the call segment page populates header call count
* QA-3365	SA: Hid the agent performance dashboard for the agent role
* BE-5327	SA: Increased the maximum number of calls retrieved on the call history page from 2,000 to 5,000
* BE-5358	SA: Made minor UI changes to the debug info Copilot details tab for a better user experience
* QA-3341	SA: Removed call insights config name change for a better user experience
* BE-5348	SA: Replaced CRM Notes with Summary on the call transcript detail and call list pages
* BE-5226	SA: Updated deletion confirmation popup to require project name before deletion
* BE-5385	SA: Updated global filters for the new segment list history view
* BE-5367	Separate Call Segment search fields from Call search fields in GET /sa/call/segment/search/fields
* BE-5383	Skip offline queue limit check for text-based AIVRs
* BE-5305	Support a new set of permissions for segments
* BE-5370	Support new Chirp3-HD Google TTS voices
* MST-1266	Support non-socket communication for derived offline processing in REX
* BE-5347	Use lmSummaryPrompt and llmCopilotNotesPrompt according to rules from BE-5332
* BE-5368	Use segment-specific field enums and sort options in POST /sa/call/segment/search
* BE-5309	Web Console: Added HOTFIX and HACK icons for edge config based on description
* BE-5252	Web Console: Improved app data tab entry fields for better user experience in the AIVR app popup

Changes related to Integrity of Processing (fixes):
* BE-5481	Copilot: Fix - Mixed-case email stored after SSO login causes Pusher channel subscription mismatch
* BE-5465	Fixed: ascalon-asr-api fails to start with global.chd=true due to missing CallSegmentDao bean
* BE-5337	Fixed: Call Review Config Export does not export the redFlag values
* BE-5292	Fixed: copilotSent and copilotAck are not set in sa_call for Vonage calls
* BE-5329	Fixed: Dashboard filters should show only those values for which records exist
* BE-5443	Fixed: Fail to generate sentiments in call segments from InsightsAnswer
* BE-5308	Fixed: Fail to send vonage HungUp event to copilot
* BE-5345	Fixed: Invalid value for `answer_value`, must be a value greater than or equal to `0`
* BE-5389	Fixed: No agent segment is generated for some Vonage calls
* MST-1238	Investigate and fix Whisper hallucination issue and dropping words issue
* BE-5425	SA: Fixed - Agents table is not rendering correctly when zooming out/scroll
* QA-3319	SA: Fixed - Applied filters on new dashboards reset when the page is refreshed or when the user navigates to another page.
* BE-5428	SA: Fixed - Call segment review form is re-rendering page on answer change
* QA-3307	SA: Fixed - Calls in call list section are not rendering in PDF download for new dashboards.
* QA-3387	SA: Fixed - Getting a 400 (Bad Request) error when modifying AIVR apps if any Superset dashboard is enabled.
* QA-3388	SA: Fixed - Getting a 400 (Bad Request) error when modifying PII Redaction if any Superset dashboard is enabled.
* QA-3311	SA: Fixed - Invalid call URL stuck in a loading state instead of showing an error
* QA-3360	SA: Fixed - New Dashboards pages options are not available in Project settings page.
* QA-3374	SA: Fixed - Pie Charts on Call Overview page are broken
* QA-3386	SA: Fixed - Segment history export calls button not working, its exporting call history call list instead.
* QA-3333	SA: Fixed - Sentiment, CSAT Score and Call Resolution - not calculating for Voicebot Projects
* QA-3337	SA: Fixed - The name of the agent created through call upload is not appearing in the Agent column in the call list.
* QA-3410	SA: Fixed - User details are not visible properly on hover on Teams page in Light Theme
* QA-3146	SA: Fixed - Voicebot assistant is getting recognized as an Agent in CRM notes.
* QA-3359	SA: Fixed- Call IDs on QA Dashboard page redirects to Dev (ascalon) env upon click.
* QA-3320	TA Edge: Fixed - Admin was able to add users with invalid domain email addresses
* BE-5250	TA: Fixed - Cursor jumps to the end when the email is edited from the middle on the signup page
* QA-3296	TA: Fixed - HTML tags are appearing in the generated PDF documents instead of being properly rendered, which impacts the document formatting and user experience.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


### Minor release 1.131.0 is scheduled for 2/23/2026 between 11:00pm and 12:00am US Central Time

New or changed functionality:
* BE-5225	Add sa_user and sa_group tables in Postgresql
* BE-5102	Added a new table sa_project to postgresql DB to support reporting aggregation
* BE-5217	Added aivrAppId to the Answered message sent via Pusher to Copilot
* BE-5228	Added API to export Call Insights Config
* BE-5204	Added Call Review Section columns to sa_project table and keep them updated
* BE-5113	Added new aivrPlatform (aivr_platform) field to /sa/call (sa_call) and populate it when /sa/call is created when AIVR session starts
* BE-5135	Added new topics field to the /sa/config
* BE-5070	Added POST /confgroup/{uuid}/defaultInsightsConfig and POST /confgroup/{uuid}/defaultCallReviewConfig
* BE-4955	Added POST /public-asr/{ccaas}/user/feedback API method for Copilot to use
* BE-5072	Added POST /sa/call/review/config/{crConfigId}/section and PUT/DELETE /sa/call/review/config/{crConfigId}/section/{crSectionId}
* BE-5073	Added POST /v1/sa/call/review/config/{crConfigId}/section/{crSectionId}/question and PUT/DELETE /sa/call/review/config/{crConfigId}/section/{crSectionId}/question/{crQuestionId}
* BE-5071	Added to Call Insights API methods for creating (POST) , modifying (PUT), and deleting (DELETE) of Call Insights Questions
* BE-5151	Added two new fields to the topic scores in the response from GET /sa/offline/{sSessionId}/data
* QA-3169	Admin Tool: Removed edit notes actions for deleted accounts
* BE-5172	All API methods for /sa/call/insights now support contextId query parameter
* BE-5171	All API methods for /sa/call/review now support contextId query parameter
* BE-5242	Better reporting of any errors related to URL access when accessing and processing GRXML grammars
* BE-5082	Copilot: Added option to display real-time transcripts via Pusher when enabled
* BE-5091	Copilot: Added option to display real-time transcripts via WebSockets when enabled
* BE-5223	Copilot: Added support for automatic switching between Multi-AIVR apps per agent
* BE-5212	Copilot: Added support to disable the Details tab based on Copilot settings
* BE-4119	Copilot: Customize behavior using settings tied to AIVR App plus other Copilot improvements
* BE-5181	Copilot: Made multiple UI improvements to the header, footer, and placeholder screens for improved UX
* BE-5009	Copilot: show live transcript
* BE-5169	Copilot: Support new Pusher message type with event=HungUp
* BE-5010	Copilot: support SSO login via SA App
* BE-5098	Demo App: Casey healthcare page new design/copy changes - v.2.8
* BE-5291	Ensure that hold and retrieve events are handled properly for Vonage calls
* BE-5229	Implemented export for Call Review Config
* BE-5063	Implemented methods on ConfGroup to delete defaultInsightsConfig and defaultCallReviewConfig
* BE-5207	Implemented POST and DELETE /confGroup/{uuid}/defaultSaConfig
* BE-5206	Implemented POST and DELETE /confgroup/{uuid}/segment/{segmentType}/defaultCallReviewConfig
* BE-5205	Implemented POST and DELETE /confgroup/{uuid}/segment/{segmentType}/defaultInsightsConfig
* BE-5208	Implemented POST and DELETE /confgroup/{uuid}/segment/{segmentType}/defaultSaConfig
* BE-5156	Implemented proper invite for the Speech Analytics Users with OIDC enabled
* BE-5173	New APIs for reordering Call Review Sections and Questions
* BE-4666	Reduce shutdown time for audio-server
* BE-5103	Remove timeZone and weekStartsOn from PUT /confgroup (now can only be set in POSt)
* BE-5175	SA: 4 new SuperSet Dashboards
* BE-4919	SA: Added a page to enable and configure OIDC SSO settings
* BE-5166	SA: Added an option to unlock locked user accounts on the Users page
* BE-5174	SA: Added Dashboards and Pages visibility configuration in Project General Settings
* BE-5062	SA: Added four new My Team Performance dashboards
* BE-5112	SA: Added option to add or edit comments for answers in the QA Review form when enabled
* BE-4947	SA: Added support to hide audio playback options for calls with no audio on the Call Details page
* BE-5219	SA: Added topics configuration on the Context Configuration page
* BE-5215	SA: Hidden date and time fields on the Recent Calls page
* QA-3168	SA: Hidden the Billing icon for users without permission to view billing
* BE-5159	SA: Implemented changes for Call Review Section
* BE-5105	SA: Made Time Zone and Week Start fields read-only on the Project General Settings page
* BE-4924	SA: Removed email as the default in initialNotification in user creation
* BE-5196	SA: Updated Add/Edit User popup cancel behavior for improved UX
* BE-4894	SA: Updated some filters to display selectable lists for improved UX
* BE-5210	SA: Updated the side navigation to include the new configurable Dashboards and Calls pages
* BE-5130	Set socket connection timeout to 10 seconds for connections between asr-api and rex
* BE-5007	Speedup copilot call notes generation
* BE-5221	SSO: Updated email validation on the Sign In page to allow '+' in email addresses
* BE-4859	Support multi-segment calls
* BE-4911	Support Vonage Real-Time Transcript input (VCCA Event)
* MST-1255	Update topic extraction in ml-svc to use LLM-based processing
* BE-4769	Use ClickHouse for call data aggregation for reporting
* BE-4829	Use SuperSet for reporting dashboards
* MST-1200	Voicebot: Improve re-prompt messaging for failed “A or B” info query questions
* QA-2293	Web Console Edge: Hidden Retrieve Past Invoice option as it is not supported
* BE-5209	Web Console: Added Copilot settings to the AIVR Telephony Bot popup
* BE-5216	Web Console: Move Copilot related settings to a new tab on AIVR App
* QA-3072	Web Console: Updated layout of the Speech Recognition Settings page for improved UX

Changes related to Integrity of Processing (fixes):
* BE-4628	Fix Agent lookup by switching from using agent.user_id instead of aget.agent_id
* BE-5099	Fix:  Zoom meeting bot is in a loop
* BE-5243	Fix: call-stats API seems to use the old scale for Sentiments
* BE-5276	Fix: fail to match an agent's email due to case-sensitivity
* BE-5182	Fix: issue with customValues defined in a context
* BE-5284	Fix: OIDC SSO login fails if user types email in mixed case
* BE-5090	Fix: Support phrases in this trigger function update_tsvector_columns()
* QA-3269	SA: Fix - Agent sentiment graph was getting cropped on the Call Overview page
* BE-5101	SA: Fix - In-progress calls were showing "offline sa missing" instead of "call in progress"
* BE-5283	SA: Fix - In Recent Calls page, agent filter doesn't show all agents that received calls
* QA-3272	SA: Fix - Unable to create or edit a question with Responder set to Auto-Populated in the QA form
* BE-5031	SA: Fix - Voicebot Dashboard time should reflect backend response
* QA-3077	TA Edge: Fix - Admin was able to reset the password for a user with an error status
* BE-5026	Web Console: Fix - Copy changes and preview modal not showing emails correctly in the phone app configuration dialog

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.130.0 is scheduled for 1/31/2026 between 11:00pm and 12:00am US Central Time


New or changed functionality:
* BE-4853	Added Call Insights computed from call transcript using LLM
* BE-4939	Added Context default config for Insights and Segment Analytics 
* MST-1185	Added Gemini API support to ml-svc
* BE-4945	Added name field to the CR Question
* BE-4918	Added OIDC SSO to SA App
* BE-4955	Added POST /public-asr/{ccaas}/user/feedback API method for Copilot to use
* BE-4948	Added POST /sa/offline/call/{callId}/fromTranscript which will do all the SA Offline processing on the input text words
* QA-3256	Admin Tool: Updated column name from Provisioning Status to Status
* BE-4956	Copilot: Added user feedback for call intent
* BE-4984	Copilot: Displayed Call ID when included in a message
* BE-4912	Copilot: Made call notes editable
* BE-4883	Deprecated csatQuestion, npsQuestion, csatAnswer, and npsAnswer
* BE-4977	If AIVR session is associated with SA Integration then create sa_call at start of session
* BE-5002	If available use Call Insights Answers to populate some sentiment values in /sa/offline - also scale sentiment  from -10 to +10
* BE-4874	Implemented conditional Call Review Questions
* BE-4927	Implemented mechanism for obtaining a token for the embedded Superset dashboard that ensures Row Level Security 
* BE-4934	In /auth-svc/openid-relay/login deprecated domain and introduced email instead
* BE-4852	In every place where our APIs accept LLM prompts, now supporting centralized LLM prompt generation
* BE-4983	Include saCallId from AIVR session into Pusher messages sent to copilot
* BE-4873	Modified /sa/call/review API methods to use /sa/call/insights (llm field is being deprecated)
* BE-4967	Periodically invoke the Agent Code generation service
* BE-5001	Reduce socket connection timeout to 10 seconds in RexClient2
* MST-1108	Resolved Redaction Issues Reported in Nov 2025
* BE-4937	Retry redacted audio upload if first upload fails
* BE-4941	SA: Added a fourth responder type (Call Insight) to the QA form configuration
* BE-4946	SA: Added a Name field to the call review QA question form
* BE-4958	SA: Added a new Call Insights Answers page
* BE-4919	SA: Added a page to enable and configure OIDC SSO settings
* BE-4942	SA: Added conditionals to the call review QA form configuration
* BE-5013	SA: Added justification support for Resolution, CSAT, and NPS from call insights on the call overview page
* BE-5023	SA: Added missing details on the Call AIVR Session page
* BE-5019	SA: Added missing validations and UI updates in the QA Question form
* BE-4929	SA: Added more filters to the call history table
* BE-4935	SA: Added new permission settings.sso.edit
* QA-3163	SA: Added predefined values for role filtering on the users page
* BE-4940	SA: Added support for Call Insights configuration and questions
* BE-4921	SA: Added support for OIDC login and updated the login flow accordingly
* BE-4922	SA: Implemented purely local (fallback) login page on /login/local URL
* BE-5029	SA: Improved Call Stats dashboard chart colors in dark mode
* BE-4952	SA: Updated call header on call detail pages, including next and previous button positions
* BE-5014	SA: Updated sentiment range from -1.0:+1.0 to -10:+10 across all pages
* BE-5017	SA: Updated the sentiment graph on the call stats dashboard
* BE-5024	Set call.callResolved to true based on a question whose name=RESOLVED
* MST-1160	Support new summary algorithm in ml-svc
* BE-4911	Support Vonage Real-Time Transcript input (VCCA Event)
* BE-5004	TA: Added support for .webm audio format for audio uploads
* BE-4998	TA: Allowed + in email address validation when inviting users
* QA-3228	Web Console: Added validation to require a language model when a language is selected on the speech recognition settings page
* BE-4908	Web Console: Now loading the previously selected context on login


Changes related to Integrity of Processing (fixes):
* BE-5042	Copilot: Fix - Agent code not refreshing in the side panel after long inactivity
* BE-5022	Fix - Fail to push voicebot_vars to Copilot in Agent-Code transfer 
* QA-3264	SA: Fix - Call audio playback is not working for calls.
* BE-5025	SA: Fix - CRM notes not populating for some calls on the call transcript page
* QA-3190	SA: Fix - Discrepancy in call counts between the voicebot dashboard and the call history page.
* QA-3265	SA: Fix - Selecting an existing question shows the question ID instead of the question text
* QA-3270	SA: Fix - The CSAT, NPS, and AIVR Transfer filters in Call History page are not working
* BE-4900	TA: Fix - Unable to join Zoom meetings via the meeting bot
* QA-3209	Web Console: Fix - API documentation page redirecting to the wrong URL
* QA-3259	Web Console: Fix - Some users were unable to accept the terms and conditions


All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.129.0 is scheduled for 1/10/2026 between 11:00pm and 12:00am US Central Time

New or changed functionality:
* BE-4805	Add call quality data to /sa/call
* BE-4868	Add sentimentFinal and sentimentTrend to the response from GET /sa/offline/{saSessionId}/data 
* BE-4869	Add sentiments field to /sa/call
* QA-3218	Admin Tool: Removed the ability to delete assigned phone numbers
* BE-4856	Demo App Casey healthcare page new design/copy changes - v.2.7
* BE-4775	Implement webhooks for justcall.io events
* BE-4879	Improved exceptions in case of license expiration or license retrieval issues
* BE-4878	Log more details about RateLimitExceededException
* BE-4820	Make the name of the Firestore configurable via env variable
* BE-3368	Migrated to new Google reCaptcha on Google Cloud
* BE-4807	SA: Add voicebot view on the Call Details Page
* BE-4902	SA: Added ability to open call in new tab from calls table
* BE-4867	SA: Draw both Agent and Caller Sentiment and make sure that the sentiment data points are correctly represented in chart
* BE-4886	SA: Remove weekend dates from line graphs on Agent Dashboard
* BE-4841	Support full set of date/time formats in the APIs (as per RFC 3339, section 5.6)
* BE-4650	Tie Agent session to AIVR session by means of an AgentCode
* BE-4649	Track Copilot events - sending and reception
* MST-1136	Voicebot: Use LLM to generate natural, conversational repeat responses
* QA-2964	Web Console: Added a success message when resending the password reset email to an invited user
* QA-3171	Web Console: Added missing button labels on the call review page
* BE-4855	Web Console: Implement Terms of Service Page in Console upon first login

Changes related to Integrity of Processing (fixes):
* BE-4870	Fix cases where the fullyAutomated[].varValue in voicebot stats response has a comma-separated list of values 
* MST-1165	Fix: Should not concatenate two sequences of digits in consecutive answers
* BE-4910	SA: Fix - Corrected the order of AIVR events on the call details AIVR events page
* QA-3222	SA: Fix - Dark theme handling on the terms of service page
* BE-4889	SA: Fix - DTMF keys not showing up on SA app
* BE-4899	SA: Fix - Issues with Call History date filter
* QA-3232	SA: Fix - The "Last 24 Hours" filter option in the Time Selector is not working on the Call History page.
* BE-4875	SA: Fix - Voicebot Dashboard - Fully Automated Calls should compute claims percentage correctly
* QA-3189	Voicebot Demo: Fix - Playback slider goes out of sync when adjusted manually
* MST-1137	Voicebot: Ensure bot responses are plain text only (no rich formatting)
* MST-1123	Voicebot: Fix misclassification of “fax number” questions as “new claim” intent
* QA-3156	Web Console: Fix - “Error loading: grafana-clock-panel” is displayed when trying to navigate to Grafana.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.128.0 is scheduled for 12/15/2025 between 11:00pm and 12:00am US Central Time

New or changed functionality:
* BE-4782	Add `ccaasAgentEmailDomains` and 'ccaasAgentEmailDomainsOutbound' field to Aivr App
* BE-4765	Add agentCode to the response from POST /public/{ccaas}/user-login
* BE-4806	Add copliotSettings to AIVR App and CCaas Login APIs
* BE-4792	Add enum value and new field to AIVR App to support JustCall.io integration
* BE-4781	Add 'generic' enum value to {ccaas} path parameter in several utility API methods called from the Copilot
* BE-4780	Add 'generic" enum value to ccaasIntegration on AIVR App
* BE-4722	Add maintenenceWindow parameter to the Account
* MST-1128	Benefits Automation demo
* MST-1043	Bot: LLM-Driven Member Info Collection with Dynamic Prompts
* MST-1096	Bot: Optimize Benefits RAG to use vector database only when necessary
* MST-1059	Bot: Standardize Intent Naming: Use () Only for Internal Descriptions, Never in Returned Intents
* MST-857	Bot: Store phone number from member query to skip redundant HIPAA verification
* MST-1058	Bot: Track and Return Count of Fully Automated Members in Bot Logic
* MST-1112	Build outbound voice bot to collect HRA (Health Risk Assessment)
* BE-4755	Copilot: Buffer and replay undelivered Copilot messages
* BE-4766	Copilot: If POST /public/{ccaas}/user-login returns agentCode, show it in the Copilot
* BE-4723	Daily, during maintenance windows, generate agentCode for Agent Users
* BE-4764	Implement API features for AgentCode call handshake as well as the actual handshake code.
* BE-4756	Implement redis map that tracks which AIVR session belongs to which Agent
* BE-4775	Implement webhooks for justcall.io events
* BE-4783	In POST /public/{ccaas}/user-login deprecate aivrAppId in the request, and instead lookup it using email and return in response
* BE-4757	New API method POST /public-asr/{ccaas}/user/copilot
* MST-1072	RAG Ingestion Pipeline: Upload & Process Plan PDFs in llm-svc
* BE-4665	Replace aircallId with ccaasCallId in IvrSession
* QA-3147	SA: Added support for searching team members by email in the edit team details popup
* QA-3145	SA: Displaying “N/A” in the calls table when sentiment is missing or has a value of 0.0
* BE-4797	SA: Displaying per-intent automation values in the Voicebot dashboard cards
* QA-3152	SA: Editing the Teams option is now disabled for all roles except Agent in the edit user popup
* QA-3150	SA: Removed the select/deselect all option when performing a search in multi-select component
* BE-4762	Simple license server
* BE-4740	Support playing a prompt into Leg-B immediately after transfer bridge success
* BE-3833	Support Spanish in text redaction API
* QA-3142	TA: Made voice signature text scrollable instead of scrolling the entire page during live transcript
* BE-4721	Transfer to Agent using leg-b prompt and Agent code
* BE-4789	Web Console: Added support for Generic in AIVR app CCaaS integration settings
* BE-4793	Web Console: Added support for JustCall.io in AIVR app CCaaS integration settings
* QA-2965	Web Console: Once the account is locked, the user will be logged out from all active sessions after the page is refreshed.
* BE-4760	Web Console: Replaced select with autocomplete to allow clearing file-type selection for app data upload

Changes related to Integrity of Processing (fixes):
* BE-4812	Fix double RIFF headers in audio from some TTS voices
* QA-3203	SA: Fix - Calls are not loading when a custom date range is selected in voicemail calls
* BE-4839	SA: Fix - Duplicate X-Axis Month Labels in Yearly Call Trends Chart
* QA-3160	SA: Fix - Filter for team lead search not working on the teams page
* QA-3198	SA: Fix - Graphs do not load when expanded on the agent dashboard
* BE-4796	SA: Fix - Max y-axis values exceed possible limits for charts on the agent dashboard
* QA-3172	TA: Fix - PDF file downloads and opens, but it shows the message “Failed to load PDF” for Chinese and Cantonese transcripts


All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


### Minor release 1.127.0 is scheduled for 11/19/2025 between 10:45pm and 12:00am US Central Time

New or changed functionality:
* BE-4607	Add namespace attribute to GRXML grammar if it's missing
* QA-3119	Added code that fixes missing user groups for projects on Edge Transcribe
* BE-4713	Added to /sa/call 2 read-only fields: copilotSent and copilotUnAck
* QA-2977	Admin Tool: Added 'Assigned' filter to provisional status column on Phone page
* BE-3872	Implemented proper fallback for streaming TTS (use correct frame-rate in returned audio)
* BE-3916	Implemented redundant outbound dialing (using multiple voice connectors)
* BE-4731	Implemented webhook receiver for Pusher webhook events
* MST-1070	Inspect and Resolve Redaction Issues Reported Oct 2025
* BE-4727	Keep track of user tokens in a 2nd redis map for 24 hours to improve reporting of expired tokens
* BE-4545	Limited set of possible sample-rate values in audio server to 8, 16, 24, 48 kHz
* BE-4559	Migrated from API keys to service accounts in Grafana
* BE-4714	SA: Added "Copilot Sent" and "Copilot UnAck" columns to the Calls table on the Call History page
* BE-4706	SA: Added AIVR Session and Call IDs to the Calls table on the Call History page
* BE-4712	SA: Added the Copilot Details tab to the Call Debug page to help troubleshoot Copilot-related issues
* QA-3094	SA: Added view-only mode section on Settings page for roles without edit permissions
* BE-4653	SA: Improved average and trend line charts on the Agent Dashboard
* BE-4642	SA: Improved colors for 0-value words in differential word cloud chart on Agent Dashboard
* BE-4656	SA: Improved design and typography for better UX on Call Stats dashboard
* QA-3080	SA: Improved Edit Team popup by combining edit and add members popups for better UX
* QA-3069	SA: Improved placeholder screen for no matching calls on Call History page
* BE-4654	SA: Improved Sentiment Chart and other charts on the Agent Dashboard
* QA-3095	SA: Improved Teams table size to fit page for better UX
* QA-2974	SA: Improved typography styling on Terms of Service page for better UX
* QA-3117	SA: Improved UX by preventing hiding of all columns on the Teams page
* QA-3125	Set the from field on the login from ACP, SA, TA
* QA-3115	TA: Improved new user wizard walkthrough flow for better UX
* BE-4521	Updated EZInit and related scripts to survive bitnami archival
* MST-1033	Voicebot: Allow immediate agent transfer on user request after external query failure
* MST-1050	Voicebot: Enable DTMF Input for Confirmation Block
* MST-1032	Voicebot: Re-prompt user with recognized info when data lookup fails
* MST-1035	Voicebot: Support multiple-member VARs in provider-call bot logic with backward compatibility to single-member vars
* MST-1041	Voicebot: Transfer Caller to Agent When Same Provider Is Provided After “No” Response on Confirmation
* BE-4486	Web Console: Added error toast notification for secret generation failures
* QA-3049	Web Console: Highlighted current login session on the users login sessions page


Changes related to Integrity of Processing (fixes):
* BE-4702	Fixed - aivrTransferDestType not getting populated in some cases
* BE-4700	Fixed - Call that was for more than 1 hour with Agent failed to process
* BE-4523	Fixed - Failed to get data from context-cache
* BE-4594	Fixed - Generating TTS at some sample rate and voice combinations does not have requested sample rate
* BE-4735	Fixed - In an obscure scenario rate-limit tracker may be created with no TTL and value over threshold
* BE-4728	Fixed - Incorrect values of trace.rcvAck 
* BE-4739	Fixed - Race condition while updating AIVR trace in Firestore
* BE-4143	Fixed - SA Call processing failed due to Google Storage glitch
* QA-3050	SA: Fix - After updating a user’s role (e.g., from Agent to Admin), the visibility permissions do not update correctly, and lower roles like Manager and HOD can still view the user.
* QA-3114	SA: Fix - Agent can view data of other users, which is not allowed as per role-based access
* QA-3097	SA: Fix - Corrected active users count on Billing Page
* QA-3131	SA: Fix - Error while creating a new project - unable to set project membership to self
* QA-3070	SA: Fix - Getting 500 (Internal Server Error) error, when trying to access account with QA role.
* BE-4711	SA: Fix - Inconsistent next and previous call numbering in Call Repeat navigation
* QA-3111	SA: Fix - Resolved back navigation issues from sub-paths
* QA-3129	SA: Fix - Resolved Teams page loading issue for some manager-role accounts
* QA-3037	SA: Fix - Team Lead and Agent role are unable to view their Team lead and other users of their own Team.
* QA-3132	SA: Fix - User is unable to create Teams getting 403 (Forbidden).
* QA-3133	SA: Fix - User is unable to edit Teams getting 403 (Forbidden).
* QA-2994	TA: Fix - Unable to open Chinese PDF file generated from the Chinese transcript.
* QA-3124	TA: Fix - Users page is missing from account menus
* QA-3105	Web console [Edge]; fix - Screen Blinking Issue on Login After Signup


All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.126.0 is scheduled for 10/25/2025 between 10:00pm and 12:00am US Central Time

New or changed functionality:
* BE-4563	Added 2 new fields to /public-asr/{ccaas}/user/message-ack: email and app
* BE-4565	Added arbitrary date time range to GET /sa/voicebot-stats query
* BE-4481	Added CSAT and NPS search fields to POST /sa/call/search and GET /sa/call/search/fields
* BE-4569	Added customValues to account
* BE-4566	Added hasNullValue field to the response from GET /sa/call/search/fields
* BE-4597	Added npsScore to GET /sa/call-stats
* BE-4440	Added NullTerm to POST /asr/meeting/search
* BE-4608	Added read-only fields to support HA for AIVR App
* BE-4572	Added team field to /sa/call - also set it properly when agent field is set
* BE-4580	Added team field to /sa/call - also set it properly when agent field is set
* BE-4540	Added transferTime field to /sa/call
* BE-4617	API method that returns Business Config now returns opening hours sorted by day of week
* MST-1029	Attach ANI & DNIS metadata to llm-svc JSON logs and ensure metadata presence
* BE-4483	Copilot: Add a test routine whenever we lose connection to Pusher
* BE-3590	Copilot: Various improvements to the Pusher Client
* MST-1034	Design and implement algorithm to solve Whisper hallucination issue in transcriptions
* MST-1031	Ensure LLM extracts member IDs as digits (not spelled-out words) across all bots
* BE-4609	Implemented redundant dial string in aivr.lua if two voice connectors are specified
* BE-3916	Implemented redundant outbound dialing (using multiple voice connectors)
* BE-4533	In /confgroup API methods return only content that the given user has access to
* BE-4532	In /sa/call API methods return only content that the given user has access to
* BE-4535	In /user API methods return only content that the given user has access to
* BE-4534	In /user-group API methods return only content that the given user has access to
* BE-4562	In POST /sa/call/search deprecate CONTEXT_ID term and add contextId query parameter
* BE-4428	Modified /data API - added user and user group fields, support for fileBase64 parameter
* BE-4596	Modified how null source values are handled in GET /sa/call-stats
* BE-4452	New Roles and Permissions Scheme
* BE-4610	Passing the secondary gateway to aivr.lua if applicable
* BE-4542	Removed old MS TTS Server fetcher from audio server
* BE-4644	Replace MarshallingCodec with JsonJacksonCodec
* BE-4289	SA: Added a Repeat Calls tab on the call details page
* QA-3016	SA: Added custom date filter to the Voicebot Dashboard page
* BE-4498	SA: Added filter on caller, intent, and verified column
* BE-4568	SA: Added support for selecting a custom date range on the Voicebot dashboard
* QA-2961	SA: Added support to search for team lead and members by email in the Create Team wizard
* QA-2982	SA: Added tooltips to Call Resolution, Average Agent Score, and CSAT Score cards on the Agent Dashboard
* BE-4541	SA: Added view and edit options for Voicebot business configuration on the integration page
* QA-3027	SA: Added view-only mode banner on pages for roles without edit permissions
* BE-4620	SA: Added view-only mode for the profile page based on user roles
* QA-2985	SA: Allowed users to create two custom filters with the same name on the call history page
* BE-4643	SA: Changed the messages for Differential Word Cloud
* BE-4619	SA: Hid edit and add-member buttons on the Teams page for roles without edit permissions
* BE-4561	SA: Improved design of range filters on the call history page for cases when minimum and maximum values are the same
* BE-4574	SA: Improved placeholder messages for differential cloud and no call cards on the agent dashboard for better UX
* QA-2919	SA: Improved team name validation in the team creation wizard
* BE-4488	SA: Improved transcript labels to correctly show Voicebot or System Speaker names instead of agent
* BE-4441	SA: Improved x-axis with weekly day bands for call counts and duration charts on the call stats dashboard
* QA-3038	SA: Increased 'Date' label font size on the CSAT score graph in the agent dashboard
* QA-2899	SA: Language dropdown on file upload popup enabled only when multiple languages selected
* QA-2990	SA: Made saved filter search on the call history page case-insensitive
* BE-4538	SA: Migrated Settings and other screens from role-based to permission-based control
* BE-4614	SA: Reduced search bar size on the agent detail page for better UX
* BE-4625	SA: Removed 'Add Team' button for users without permission and updated empty screen message
* BE-3210	SA: Showing currently selected AIVR apps on the voicebot integration page
* BE-4468	SA: Support multiple roles for users in Create/Edit modals and display them in the Users table
* BE-4218	SSO: Made login box wider to support longer email addresses
* QA-2921	TA: Added hover messages for delete and share actions on the call transcript page
* QA-2979	Update score field in /sa/call when the Call Review Answers associated with the /sa/offline session belonging to sa/call are updated
* BE-4537	Use user.create. permissions in user creation API
* BE-4600	Voicebot Demo: Added a Contact Sales form on the 'Contact Sales' button click
* MST-1027	Voicebot: Improve no_information Detection in info_collection_block
* BE-4612	Web Console: Added a Gateway tab to the Configure Telephony Bot App popup
* QA-2897	Web Console: Added duplication alerts for callback URL and app data combinations in telephony bot app popup
* QA-2954	Web Console: Improved validation messages for Name field in Edit API Secret popup on API Token Page
* BE-4573	Web Console: Limited users with telco permission to a maximum of 10 phone numbers
* BE-4611	When making outbound call for AIVR App that has 2nd Voice Connector defined, using it as the second gateway in the dial string

Changes related to Integrity of Processing (fixes):
* BE-4646	Address discrepancies in how user tokens are stored and fetched
* QA-2925	Admin Tool: Fix - Selection of Users column in account details was showing a blank page for some accounts
* QA-2959	Admin Tool: Made users table header full width to match the table body
* MST-630	Better exception in offline-main task
* BE-4634	Copilot: Fix - Call expiration timer settings does not work
* BE-4587	Copilot: Fix bugs related to multiple event binding issue with pusher and other issues
* BE-4546	Fixed - /sa/offline enforces the old persist limit on 365 days
* BE-4648	Fixed - digit formatting for Spanish in segment mode not working
* BE-4578	Fixed - Keyword annotations are not being populated for words in /sa/offline
* BE-4632	Fixed - NullPointerException: Cannot invoke "java.lang.Comparable.compareTo(Object)" because the return value of "java.util.function.Function.apply(Object)" is null
* BE-4500	Fixed - POST /public-asr/{ccaas}/user/message-ack with a body of incorrect JSON
* BE-4605	Improve cleanup in the close of mod_vg_tap_ws
* BE-4437	Properly report rate-limit utilization for /sa/offline sessions submitted in AIVR post-processing
* QA-3043	SA: Fix - Agent, Team Lead and Coach should not be allowed to view all calls list.
* QA-1763	SA: Fix - Agents are able to access calls by URL manipulation
* BE-4555	SA: Fix - Agents page was not scrollable, hiding the agents list
* QA-2948	SA: Fix - Call overview score did not update after QA form responses were changed
* BE-2414	SA: Fix - Data for the Differential Word Cloud is not being generated.
* QA-2958	SA: Fix - Editing saved filters on Call History page sometimes failed
* QA-3003	SA: Fix - Getting Authorization error when trying to log into Digital QA user role account.
* QA-3000	SA: Fix - Head of Operations user role cannot invite new users with any role other than Agent.
* BE-4581	SA: Fix - Incorrect Average Handle Time chart for the current week on the Agent Dashboard
* BE-4579	SA: Fix - Incorrect charts displayed for partial periods on the Agent Dashboard page
* QA-3012	SA: Fix - Manager should not be allowed to edit project settings.
* QA-3010	SA: Fix - Manager unable to Add and Edit team
* QA-3007	SA: Fix - Manager unable to view invited user with agent role
* QA-3004	SA: Fix - Manager user role cannot invite new users with any role other than Agent.
* QA-2901	SA: Fix - Moved QA form name error message outside input box border
* QA-2998	SA: Fix - Non-admin and non-owner roles were unable to access calls and other features
* QA-3013	SA: Fix - Profile icon not displaying in the sidebar menu
* BE-4548	SA: Fix - Project Setup Wizard wrongly shown to all new users even after setup
* QA-2991	SA: Fix - Search button in the call history page search bar was not working
* QA-3037	SA: Fix - Team Lead and Agent role are unable to view their Team lead and other users of their own Team.
* QA-3064	SA: Fix - Team lead should not be allowed to have a Delete option to delete users.
* QA-3052	SA: Fix - The "Last 24 Hours" filter in the Time Selector is not working on the Voicebot Dashboard page, when Month, Week or Today filter is selected initially.
* QA-3009	SA: Fix - The Manager should be able to see all the users that they can invite/create.
* QA-2997	SA: Fix - The Owner or Admin user role cannot invite new users with any role other than Admin.
* QA-2993	TA: Fix - A user invited with an invalid email address should not be shown as active on the user page, even after receiving the alert message for the invalid email address.
* QA-2992	TA: Fix - Projects are not showing in the 'Invite User' popup, even though the admin has existing projects.
* QA-3005	TA: Fix - The admin is unable to invite users and receives an 'Access Denied' alert popup.
* QA-2984	TA: Fix - Timer in Browser Share Page Does Not Reset After Stopping Previous Recording
* QA-2916	Voicebot Demo: Fix - Text overlap issue on mobile call transcript page resolved
* QA-3068	Voicebot Demo: Fix - Timer on Browser Share Page does not reset after stopping previous recording: Fix - When the user clicks on the “Contact Sales” page, the content does not display.
* QA-2999	Web Console: Fix - Admin user is unable to add the new user(invite user).
* QA-2966	Web Console: Fix - If the account status is locked from the admin side, the user should not be allowed to access the application.
* QA-2988	Web Console: Fix - Profile icon was not displaying in the header for some accounts
* QA-2896	Web Console: Fix - Unable to delete callback URL when creating phone app
* QA-2955	Web Console: Fix - When the user does not make any changes on the API Security page, the submit button should be disabled.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release

### Minor release 1.125.0 is scheduled for 9/27/2025 between 11:00pm and 1:00am US Central Time

New or changed functionality:
* MST-964	Added “Press 0” Check Before Transfer to Prevent Dead-End Calls
* BE-4381	Added 4 new columns to the CDR API 
* BE-4388	Added agentCallsOnly parameter to GET /sa/call-stats
* BE-4245	Added aivrTransferDestType parameter to the /sa/call search API
* BE-4336	Added chartData to agentScore in GET /sa/call-stats API method
* BE-4387	Added csatStats to GET /sa/call-stats
* BE-4458	Added mergedAudioId field to /sa/call
* BE-4442	Added NPS computation for calls shown in Speech Analytics App
* BE-4439	Added NullTerm to POST /sa/call/search
* BE-4425	Added time period filter to GET /sa/call/search/fields
* MST-954	Added Utility Code in llm-svc to Send Fax and SMS
* BE-4453	Changes to User API to support new Roles and Permissions scheme
* BE-4502	Copilot: Show real name instead of caller-provided name in member calls only
* MST-955	Implemented “Fax Back” and “Text Back” Request Handling in Eligibility Automation
* MST-975	Implemented NPS Support via QA Form Flow (Modeled After CSAT in Offline-Task Project)
* MST-980	Improved "A or B" Info Query Handling: Ask for B If User Says They Don’t Have A
* MST-873	Improved Alphanumeric Prompting for Voicebot in llm-svc
* MST-918	Improved Date NER Model for Formatted Date Recognition
* BE-4428	Modified /data API - added user and user group fields, support for fileBase64 parameter
* BE-4436	Modified DELETE /asr/transcribe/{sid} to remove session from the Queue
* BE-4509	Modified GET /cluster-version to return up to 120 entries instead on only 40
* BE-4394	Order CDR rows returned from the CDR API by date
* MST-973	Report Accurate Audio Duration in Offline-Main When Using Whisper Model
* BE-4503	Report caller_faxId variable as a tag fax_sent
* BE-4479	SA: Added corresponding labels in the Calls table for errored calls with missing SA offline sessions or merged audio
* BE-4339	SA: Added filter saving and applying functionality on the Call History page
* BE-4422	SA: Added global filters to the Recent Calls page with new filter design
* BE-4385	SA: Added justification to the Call Resolution card on the Call Overview dashboard
* BE-4424	SA: Added meaningful tooltips for actions on the Teams page and removed sentiment breakdown from the Sentiment card
* QA-2852	SA: Added name validation for QA form section name
* BE-4420	SA: Added sorting by duration to the Voicemail Audio column on the Voicemail Calls page
* BE-4337	SA: Added timeline to the Average Agent Score card on the Agent Dashboard
* QA-2850	SA: Added Verified column in the calls table
* QA-2874	SA: Added warning to newly created QA form sections to include at least one question for better UX
* QA-2862	SA: Columns in the calls table are now matched between the Recent Calls and Call History pages
* BE-4431	SA: Improved Call History filters with new design and support for All Calls/Transferred Calls tabs
* BE-4484	SA: Improved CSAT before/after preview for LLM prompts in the Preview Changes modal
* BE-4423	SA: Improved Edit User modal with multi-select support for teams
* BE-4426	SA: Made features like QA Form, Add Project, Teams page, etc. available for all, regardless of project settings
* QA-2918	SA: Prevented users from creating duplicate team names
* BE-4472	SA: Replaced Customer Dissatisfaction card with CSAT Scorecard on the Agent Dashboard
* QA-2949	SA: Show Incident and Scorecard labels based on the displayed value on the Call Overview dashboard
* BE-4309	SA: Showing call duration in mm:ss format on the Call Stats dashboard.
* BE-4468	SA: Support multiple roles for users in Create/Edit modals and display them in the Users table
* QA-2866	SA: Updated Billing Info page for improved dark mode support and design changes
* MST-606	Use GPU UUID to enforce license on REX (GPU dockerized deployment)

Changes related to Integrity of Processing (fixes):
* BE-4485	Fix - Memory Leak issue with real-time transcript results submitted to a websocket server
* BE-4506	Fix - set the mergedAudioId in /sa/call
* BE-4417	Fixed - Before-last event missing from AIVR session
* BE-4419	Fixed - Issue with prompt playback event arriving delayed.
* MST-963	Resolved Remaining Issues in Audio & Text Redaction Test Cases
* QA-2909	SA: Fix - Agent should not be allowed to add/edit/delete the JWT in API security.
* QA-2945	SA: Fix - ANI/Dialed Number filter was not working when the country code was not provided explicitly
* BE-4035	SA: Fix - do not pass answerValue if we are doing human override of AI and the question type is choice
* BE-4508	SA: Fix - Filters now update correctly when refreshing calls on the Call History page
* QA-2857	SA: Fix - Issues with adding and deleting conditions in Criteria Configuration on the Context Config page
* QA-2854	SA: Fix - 'Select All' checkbox not working in the language dropdown on the Upload Call Audio modal
* QA-2910	SA: Hide Settings tab for Agent role
* QA-2853	TA: Fix - Error transcript from meeting bot shows a 'Something went wrong' page when the user tries to perform a full re-run.
* MST-877	Updated Omega Model to correct "thank you" issue
* QA-2922	Voicebot Demo: Disable "View My Transcript" button until a demo code is added
* QA-2867	Voicebot Demo: Fix - Submenu overlap between tabs on the main demo page
* QA-2923	Web Console: Fix - 500 Internal Server Error when clicking the time selector twice for ASR Web API requests on the Home page
* QA-2863	Web Console: Fix - Form fields remain populated with previous values after creating a context in the Add Context modal

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release

### Minor release 1.124.0 is scheduled for 9/6/2025 between 11:00pm and 1:00am US Central Time

New or changed functionality:
* BE-4363	Added 7 new fields to GET/sa/call/search API method
* BE-4362	Added 7 new fields to GET/sa/call/search/fields API method
* BE-4094	Added Metadata to the transcript used for QA Call Review by LLM
* BE-4279	Added support for longer expiry time for SA Calls
* BE-4392	Added uuid= parameter to calls to shout://
* BE-4329	APIs that report for a given Context how many AIVR sessions or Calls will expire when
* MST-867	Bot: Streamline Provider Lookup (NPI, TaxID)
* BE-4352	Doubled the amount of data objects processed by cleanup task at each execution.
* MST-870	Enable Edge Deployment for llm-svc with Optional Env-Based Bot Activation
* BE-4333	Expose transcriptionExpireAt in GET /sa/offline and GET /sa/offline/{sid}/data
* MST-863	Implement Eligibility Disclaimer Prompt with Variant Logic
* BE-4328	In AIVR-App API allow for expiry to be older than 365 days.
* BE-4338	Increase allowed combined size of clientSideProperties in in User object to 64KB
* BE-4411	SA: Added a note about QA score normalization
* BE-4280	SA: Added AIVR prompt from AIVR app for Voicebot app on Configuration page
* BE-3607	SA: Added call expiry date column to Call History table
* BE-4384	SA: Added CSAT score to Call Resolution card on Call Overview page
* QA-2844	SA: Added Show/Hide All option for columns on Recent Calls page to prevent deselecting all
* QA-2888	SA: Added Time column to Recent Calls page
* BE-4219	SA: Added user name and email to profile menu
* QA-2840	SA: Changed all Calls table background to white for better UX
* BE-4326	SA: Delayed call audio loading for calls older than 90 days on Call Details page
* BE-4290	SA: Hid analytics option from Call Details view
* BE-4297	SA: Improved applying filters and search UX on Call History page
* QA-2898	SA: Improved auto-fill color in login input fields for better visibility
* BE-4335	SA: Improved Call Resolution card timeline to match AHT timeline on Agent Dashboard page
* BE-4380	SA: Improved card responsiveness on Call Overview page
* QA-2875	SA: Improved dark mode handling for QA form name and selected queues
* QA-2871	SA: Improved dark mode handling for voicemail audio popup on Voicemail page
* BE-4298	SA: Improved empty state for Voicebot Data Card on Call Overview page
* BE-4316	SA: Improved masking of PII redaction fields for partial examples
* QA-2869	SA: Updated display of oldest and newest call times in account format on Call Stats dashboard
* BE-4332	SA: Updated multi-select dropdown to display +x filters for better UX
* QA-2893	SA: User column preferences now persist on Recent Calls page after refresh
* BE-4218	SSO: Made login box wider to support longer email addresses
* BE-4397	TA: Added 'Copy Debug Info' button on Meeting Bot page in debug mode
* BE-4087	Voicebot Demo: Displaying AIVR session events on transcript wait page
* BE-4370	Voicebot Demo: Updated design and copy on Demo Healthcare page
* BE-4317	Web Console: Added Duration column to Call Sessions table
* QA-2812	Web Console: Added edit button to modify logic when creating AIVR app in Telephony Bot modal
* BE-4327	Web Console: Allowed entry of Telephone App call expiry greater than 365 days
* BE-4272	Web Console: Displaying actionStart and event time for all AIVR events
* QA-2795	Web Console: Do not show Mode Selector if only one mode is available

Changes related to Integrity of Processing (fixes):
* MST-892	Bot: Fixed - bot reads NPI number like a normal number.
* MST-924	Bot: Test and Fix Spanish Member Flow
* MST-903	Fix - Bot Intent Reply: Distinguish Member vs Provider
* BE-4281	Fix issue with channel_id in Words for Text Redaction API Requests to ml-svc
* BE-4386	Fix issues with memory leak when webhook retries are processed
* MST-902	Fixed - Bot stuck talking about account validation
* QA-2769	Fixed - Voicebot calls are failing to process and going in Error state due to empty formatter definition
* BE-4372	Fixed issue invalid audio duration would break processing of SA calls
* BE-4307	Fixed issue with audio-server returning 504 for invalid JWT tokens
* BE-4404	Fixed issue with some of the voicebot prompts getting stuck on terminate.
* BE-4369	SA: Fix - Call loading issue for Manager role on some accounts
* BE-4373	SA: Fix - Calls incorrectly showing failed status while still in progress
* QA-2894	SA: Fix - File upload failure on Integration page when selecting languages
* QA-2851	SA: Fix - Internal Server Error when modifying AIVR app Integration
* BE-4319	SA: Fix - Missing IDs for error calls in Calls table resolved
* BE-4406	SA: Fix - Navigation issue after sorting/filtering on Recent Call
* QA-2876	SA: Fix - Save button disabled when option points exceeded max points in QA Review form
* BE-4351	SA: Fix - Section name in QA Review form allowed saving empty strings
* BE-4275	SA: Fix - UI crashing after multiple date changes on Voicebot dashboard page
* QA-2848	SA: Fix - Voicebot Data Card information not fully visible on Call Overview page
* BE-4228	SA: Fixed issue where front-end code would overwrite the integration JWT
* QA-2834	TA: Fix - Microphone Recording – Transcription is failing intermittently for microphone recordings.
* QA-2846	TA: Fix - Save button remaining enabled while entering tag and added helper text
* QA-2809	Web Console: Fix - Unable to edit AIVR app when 'Connection Logic' is an Adapter

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release

### Minor release 1.123.0 is scheduled for 8/17/2025 between 11:00pm and 1:00am US Central Time

New or changed functionality:
* BE-4231	Add 3 new query params to GET /sa/call - userGroup, internalEndpoint, direction
* BE-4256	Add 4 new vars to POST /sa/call: voicebotVars, aivrVars, whuHungUp, businessOpenState
* BE-4222	Add appliesToQueues field to QA Review questions and answers
* BE-4181	Add tenureStartDate to User API
* BE-4001	Add to audio-server support for streamed Azure TTS Audio
* BE-4125	Apply misspelling correction to offline ASR sessions if a whisper model is used
* MST-822	Collect Tax ID from Caller When Not Available in System After NPI Lookup
* BE-3988	Copilot: Update help docs to support customer-specific copilot extensions
* BE-4096	Extract voicemail transcript from /sa/offline transcript and store in /sa/call
* BE-4258	For AIVR Session events - set timeMsec to when the event ends and add new actionStartMsec to event
* BE-4265	GET /sa/call/review/answers/{crAnswersId} - added normalizedScore and minTotalValue read-only fields
* MST-834	Identify Some Blocks in llm-svc to Use GPT-4.1 Mini for Performance and Cost Efficiency
* MST-742	Improve Confirmation Handling for Irrelevant or Ambiguous Yes/No Answers
* MST-569	Improve Handling of "Yes/Okay/no" Responses When Asking for Information
* BE-4257	In /sa/call compute voicebotDuration and voicemailDuration from markers
* MST-703	Integrate Provider Search Callback Logic into Demo Bot from OpenAI Realtime Bot
* BE-4276	Limit number of histogram bins to max 100
* BE-4180	Make all AIVR vars available in sa/call API
* BE-4151	Modify /synthesis method in audio-server to use ResponseEntity<StreamingResponseBody> return type
* BE-4154	Move llmCopilotNotesPrompt from /sa/config to /aivr-app
* BE-4254	Provide Bot Info to Non-AIVR Calls in POST /sa/call API
* BE-4185	Remove sa-call-api from Edge deployments by default
* BE-4148	SA: Add CSAT
* BE-4244	SA: Added ability to enter and edit agent tenure on Add/Edit User modals
* BE-4182	SA: Added agent email, role, creation date, tenure, and team details on Agent Details page
* BE-4225	SA: Added annotatedTranscript fields to Calls Debug page
* BE-4269	SA: Added avatars to the Team Lead selection dropdown
* BE-4236	SA: Added CSAT configuration option on Context Configuration page
* BE-4240	SA: Added CSAT field to Calls table and Call Detail page
* BE-4264	SA: Added delete functionality for teams
* BE-4201	SA: Added edit and remove avatar functionality in Edit User modal
* BE-4124	SA: Added error screens for request timeouts and internal server errors
* BE-4108	SA: Added markers indicating voicemail start and end in the call audio player
* BE-4270	SA: Added minimum points possible to the QA form creation page
* BE-4200	SA: Added upload avatar functionality in Add User modal
* BE-4203	SA: Added user avatars for agents in Calls table on Recent Calls and Calls History pages
* BE-4202	SA: Added user avatars in Users table on Users page
* BE-4204	SA: Added user avatars to Agents table on Agents page
* QA-2849	SA: Added voicemail column for voicemail calls on Call History page
* BE-4101	SA: Added voicemail text preview on the voicemail calls page and full transcript display in the playback popup
* BE-4223	SA: Changed default Incident threshold values for new projects on Context Configuration page
* QA-2804	SA: Enhanced visibility of My Notes and CRM Notes icons in Calls table Dark mode
* BE-4214	SA: Handled No Teams state in Add/Edit User modals for improved UX
* QA-2814	SA: Improved alert toast messages for QA form actions to provide better context
* BE-4213	SA: Improved empty state on Teams Creation page when no teams are present
* QA-2803	SA: Improved error message copy on QA form creation page for better UX
* BE-4111	SA: Improved PII redaction design for better UX
* QA-2813	SA: Improved QA form to disable only the current question during edit and not the full form
* BE-4229	SA: Improved QA Review form section and question flow; added queue support for sections
* BE-4211	SA: Improved Team creation flow and design consistency for better UX
* BE-4215	SA: Improved Teams column to display team names in Users table on Users page
* BE-4266	SA: Improved Teams Settings table design and dark mode support
* BE-4241	SA: Improved Yearly Call Trends chart to show data from oldest call if under one year on Call Stats dashboard
* BE-4221	SA: Move C_, R_, V_ tags to fields in voicebotVars
* BE-4159	SA: Renamed Calls page to Recent Calls, Advanced page to Call History, and improved table design for better UX
* BE-4084	SA: Support different set of call QA review questions per Queue
* BE-4260	SA: Updated Calls to Recent Calls page; added Today and Last 24 calls filters; improved No Calls state
* BE-4271	SA: Updated QA Review Form by replacing Section Count with Normalized Score
* BE-4212	SA: Updated Team Performance page with improved table and headers for better UX
* BE-4209	SA: Updated Teams icon and improved design consistency
* BE-4259	SA: Use /sa/call aivrVars to display Voicebot Card if aivrVars are available
* MST-800	Support "One of" Input Prompts in Info Query Block (e.g., "Can I have A or B?")
* MST-614	Support Metadata in QA Form by Decoupling Transcript Submission in Offline Transcribe
* MST-833	Switch Default GPT Model to GPT-4.1 on Demo Bot
* BE-4282	Use annotated transcript as realTimeTranscriptText for CRM Call Notes
* MST-821	Use GPT to Generate Natural Response for Intent Detection without Revealing Internal Categories
* QA-2579	Voicebot Demo: Improved subject line for the "Contact Sales" email call-to-action
* BE-4234	Web Console: Adapter Settings language choices updated to match Default Voices for languages
* BE-4128	Web Console: Added Call Detail Record page
* QA-2768	Web Console: Added 'click to copy' tooltip for app ID copy icon in Telephony Bot App modal
* BE-4169	Web Console: Added Copilot Notes LLM Prompt field to AIVR app advanced settings
* QA-2802	Web Console: Improved error message to clearly indicate when a JWT token name is already in use

Changes related to Integrity of Processing (fixes):
* BE-3906	Fix - In the outbound bot, the "input" event before "hangup" event is missing
* BE-4253	Fix - SA config is not included in the offline-sa task when creating the offline session from a call using JWT
* BE-3704	Fix - Telephony bot API didn't make the next PUT request after DTMF NO-MATCH callback
* BE-4115	Fix - The recording captured by FS is shorter than the actual call duration
* BE-3660	Fix - Transcript submitted for after-call Call Note/Summary is wrong - FS removes silences from audio
* BE-4233	Fix - Unable to delete user avatar from PUT method on /user/{uuid}
* BE-4267	Fix - UserGroup deletion API method does not seen to work
* BE-4198	Fix - Voicemail transcript is incorrectly extracted.
* BE-4189	Fix issues with AIVR websocket
* BE-4262	SA: Fix - API Security page loading issue
* BE-4013	SA: Fix - Call playback timestamp can go beyond call duration
* QA-2837	SA: Fix - Calls are going into error after Re-compute.
* BE-4032	SA: Fix - Duplicate sections in QA Form Config
* BE-4227	SA: Fix - Edit Teams modal pre-fill, lead selection, validation, and display issues
* QA-2786	SA: Fix - email domains not shown correctly in toast messages
* BE-4179	SA: Fix - Resolved loading issue on Call Detail Analytics page when incidents are not defined
* BE-4268	SA: Fix - Review Form not updating when switching context from QA Form page
* BE-4210	SA: Fix - Team lead addition fixed in Team Creation wizard
* QA-2778	SA: Fix - Uploaded calls are going into error if Omega model is being used
* QA-2693	SA: Fixed metrics call detail loading issue for some voicebot calls
* QA-2825	SA: Fixed time selector resetting to D‑Today after visiting Recent Calls on the Voicebot Dashboard
* QA-2815	TA Edge: Fix - Real-time transcription shows an error when the user tries to save the recording.
* QA-2788	Web Console: Fix - Fixed 404 error when switching modes when the previous left-menu option isn’t valid in new mode
* QA-2771	Web Console: Fix - Issue where unauthenticated users were redirected to a 404 page for valid URLs; now they are redirected to the login page
* BE-4170	Web Console: Fix - Request to include contextId when fetching AIVR Apps, ensuring correct app filtering
* BE-4261	Web Console: Fix - Transcript page loading issue in Speech Analytics App

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release

### Minor release 1.122.0 is scheduled for 7/24/2025 between 11:00pm and 1:00am US Central Time

New or changed functionality in the Transcribe App:
* QA-2722	TA: Added URL validation for meeting links on the Meeting Bot page
* QA-2761	TA: Changed banner text colors for better visibility in dark mode on the import page

New or changed functionality:
* BE-4053	Add a new Reason tag value - R_Unknown
* BE-4021	Add vg_aivr_cb_count variable to CDR
* BE-4095	Added API for reading Freeswitch CDR records
* BE-4109	Added configurable format for webhook
* BE-4129	Added modifiableNote to /sa/call
* BE-4107	Added voicemail markers to /sa/call
* BE-4093	Adjust the reported start of the AIVR session to be equal to the start of the recording.
* BE-4045	API to generate temp JWT to access SA account from ACP
* BE-4023	DAO for reading CDR data form Postgres table
* MST-761	Don't redact short sequence of digits when using approximate redaction
* BE-4152	Extract information from the CDR table and set the whoHungUp field in /aivr and /sa/call
* BE-4027	Implement deletion of data Objects attached to AIVR appData items
* BE-4060	Implement influxDB measurements for /sa/offline sessions
* BE-4135	Improved speed of GET /sa/call-stats API method
* BE-3694	In error messages returned from the APIs do not include full java types
* BE-3890	License server retains ticket information through shutdown and restart
* BE-4056	Miscellaneous improvements to MS Teams Meeting Bot
* MST-478	Moved Spanish basic formatter to text-ml-utils
* MST-772	New NER for bank numbers
* BE-4136	Pass vgContext to aivr.lua to be stored in CDR
* BE-3186	Populate fields in the markers field after a SA call is completed
* MST-538	Provider search full automation demo using VACA
* BE-4161	Return 504 code rather then 401 if a request is made with a nonce that is being currently used by a request in progress
* BE-4147	SA: Added "CRM Notes" column with filtering in the call sessions table
* BE-4149	SA: Added "My Notes" column in the call sessions table
* QA-2753	SA: Added a maximum limit of 100 points for both Individual and Total scores in QA form questions
* BE-4137	SA: Added ability to add "My Note" for each call on the call transcript page
* QA-2738	SA: Added assistive tooltips to audio player action icons
* BE-4066	SA: Added display of selected time range on the agents dashboard
* BE-4108	SA: Added markers indicating voicemail start and end in the call audio player
* BE-4065	SA: Added strike-through on LLM justification when a human override occurs in the QA review form
* BE-4155	SA: Added support to mark a QA review question as "N/A" if the question allows it
* BE-4101	SA: Added voicemail text preview on the voicemail calls page and full transcript display in the playback popup
* BE-4099	SA: Added voicemail transcript on the voicemail detail page
* BE-4100	SA: Displaying voicemail icon and page only when voicemail is present
* BE-4017	SA: Hide Provider callback field on the VoiceBot data card in the call overview page if the caller type is not provided
* BE-4025	SA: Improved voicemail audio player styling for better appearance in both light and dark modes
* BE-4052	SA: Refreshing the call resolution value after changes to the call resolution question in the QA/CR form
* QA-2418	SA: Removed Speaker field from advanced search filters as Agent field is already present
* BE-4132	SA: The survey details page is now hidden when no survey data is present
* BE-4019	Store RTCP stats in CDR
* BE-4114	Support two more entities (BAN and BRN) for all redact formatter
* MST-803	Upgrade python packages and services that have high / medium vulnerabilities
* BE-4009	Use default whisper as acoustic model instead of whisper:medium for offline SA sessions derived from AIVR sessions
* QA-2579	Voicebot Demo: Improved subject line for the "Contact Sales" email call-to-action
* QA-2644	Web Console: Added a custom 404 page for handling unavailable URLs
* BE-4022	Web Console: Added a new "App Data" tab in the Telephony Bot drawer for configuring app data
* BE-4051	Web Console: Added an Initial Prompt field to adapter settings in the Telephony Bot drawer
* BE-4120	Web Console: Added caching for calls on the call sessions page for better UX
* BE-4069	Web Console: Added error screens on the call review transcript detail page to improve handling and visibility of API errors
* QA-2555	Web Console: Added support to delete Speech Analytic Configuration on the SA Configuration page
* BE-4127	Web Console: Added the ability to create user-bound JWT tokens (only for Admins) on the profile page
* BE-4123	Web Console: Added toast messages and redirect to login page in case of session expiry
* QA-2704	Web Console: Enforced mandatory password reset without the possibility to bypass the "Password reset required"
* BE-4138	Web Console: Improved cancel confirmation modal copy for the Telephony Bot drawer for better UX
* QA-1980	Web Console: Prevented users from de-selecting all columns in the calls table to ensure at least one column is always visible
* BE-4085	Web Console: Removed transcribe mode

Changes related to Integrity of Processing (fixes):
* BE-4116	Fix - AIVR fails to store output events in db for record.prompt and record.playtone
* BE-4117	Fix - Audio-Server /get and /sclip API method does not use Transfer-Encoding chunked in case of streaming TTS
* BE-4102	Fix - externalSaSession set incorrectly to true
* BE-4122	Fixed Hints with misspellings for whisper model.
* BE-4140	SA: Fix - Added the missing no-sorting state in the call sessions table
* QA-2743	SA: Fix – Enabled Save button when "LLM" is selected as responder and "Use Questions as LLM Prompt" is toggled in the QA form
* QA-2752	SA: Fix – Improved facility name visibility in dark mode on the VoiceBot data card in call overview and voicemail views
* BE-4031	SA: Fix – Resolved "Review config not found" error when saving the first question in the QA form without a name
* BE-3997	SA: Fix – Resolved display issue with the VoiceBot card for certain calls
* QA-2744	SA: Fix – Resolved issue preventing adding questions in QA form sections using the top "New Question" button
* QA-2757	SA: Fix – Resolved issue where the sentiment graph gets compressed when the score field is present on the call overview page
* QA-2758	SA: Fix - Resolved issue with the call resolution filter not working in the call sessions table
* QA-2789	SA: Fix – The Voicebot data card now shows "Not Acquired" instead of "Provided" when no Member ID is present
* QA-2772	TA: Fix - MS Teams meeting validation failing for valid meeting links on the Meeting Bot page
* QA-2721	TA: Fix – Resolved cursor jumping to the end issue when editing password on the login page
* QA-2562	TA: Fix – Resolved issue where language flag icons for projects were not showing on the advanced search page
* QA-2725	TA: Fix – Resolved issue with a few words not visible in dark mode on the call transcript page
* BE-4070	TA: Fix – Resolved issue with multicolor transcription on the audio timeline
* QA-2724	TA: Fix – Resolved save button enable behavior in the voice signature modal when a tag is removed or a speaker is edited
* QA-2741	TA: Fix – Stopped previously played voice signature from continuing when a new voice signature is edited
* QA-2737	TA: Fix - The Zoom meeting bot does not automatically leave the meeting when the time limit for a free meeting is reached.
* QA-2774	TA: Fix - Unable to join meetings on the Meeting Bot page due to incorrect validation of valid Webex meeting links
* QA-1970	Web Console: Fix - Filters and search gets reset after deleting a context
* BE-4089	Web Console: Fix – Removed extra blue Modified label in the Telephony Bot preview modal when no modification changes are made
* BE-4040	Web Console: Fix – Resolved loading issue on the call review page for calls integrated with the SA app
* QA-2776	Web Console: Fix - The Listen icon is disabled if a call has no audio on the call sessions page
* QA-2770	Web Console: Fix - Unable to remove or change phone numbers from a phone (AIVR) app.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release

### Minor release 1.121.0 is scheduled for 6/25/2025 between 11:00pm and 1:00am US Central Time

New or changed functionality:
* BE-3926	Add none value to ccaasIntegration field in AIVR App API
* BE-4011	Added appData to AIVR App API
* BE-4010	Added initialPrompt for adapterLogic field in AIVR App API
* BE-3937	Added optional prompt to the AIVR record command in callback response
* BE-3882	Added support for sa_offline resource in /webhook API
* BE-3973	Added usage tracking for the license server
* BE-3944	Added voicemail fields to /sa/call API
* BE-3281	Admin Tool: Added ability to Add and Remove Grafana from Account
* QA-2691	Admin Tool: Fix - Account count remains constant despite account changes
* BE-3962	Copilot: handle combination of the new standardized vars and customer-specific vars
* BE-3958	Copilot: Implement a new login flow
* BE-3994	Copilot: Improved update check with "Check for updates" button in settings
* BE-3961	Copilot: Update all the old apis to new api paths specific to CCaaS platform used
* BE-3929	Generalize Utility APIs that used to be aircall only and replace fixed aircall path with a ccaas path parameter
* BE-3936	Implemented POST /public/{ccaas}/user-login API
* BE-3957	Implemented POST and GET /license methods in license-svc
* BE-3866	Implemented Webhook listener for Five9 webhooks
* BE-3935	Improve input validation in POST /sa/offline API method
* BE-3945	In GET /sa/call API method added a voicemail query parameter
* BE-4006	Increased max llmJustification length to 1024 chars
* BE-3843	Modified the call transfer handshake scheme that we use for Aircall so that it can support either Aircall or Five9
* BE-3972	Modified the POST and GET /license to support the network parameters (interface, mac, ip)
* BE-3992	Modify POST /confgroup/uuid/integrationSecret to return JWT tokens that work with both /aivr and /data apis
* BE-3982	Optimize Five9 webhooks by immediately ignoring all webhook requests not matching the domain of the X-F9-APIKEY
* BE-4030	SA: Added a new page on the Call Details for Survey
* BE-3999	SA: Added direct callback number for provider on Voicebot card in Call Overview page
* BE-4012	SA: Added HC provider Tax ID to Voicebot card on Call Overview page, if available
* BE-3946	SA: Added new Voicemail Calls page to the main menu
* BE-3947	SA: Added new Voicemail page to detailed Call View
* QA-2563	SA: Added proper validations for First Name and Last Name fields on Users page
* BE-3920	SA: Customer-specific download pages for Copilot Extension
* BE-3931	SA: Improved Agents Dashboard layout and styling for consistency with other dashboards
* BE-3985	SA: Improved Call Review form highlighting colors and added total score alongside questions
* QA-2564	SA: Improved project name and description field validations on both Project Settings and Creation pages
* QA-2678	SA: Improved Review form styling and spacing on Call Detail page for consistency with the app
* QA-2521	SA: Replaced spinner with 'In Progress' label with tooltip while call is in progress
* MST-667	SA: Review Voicebot dashboard and provide better vars to get more accurate data on the dashboard
* BE-3989	SA: Tweaks and corrections to Voicebot Dashboard
* QA-2504	TA: Improved speaker color scheme with support for up to 60 distinct speaker colors in both light and dark mode
* QA-2719	TA: Removed "Others" project tab for accounts on Individual plan
* QA-2684	Voicebot Demo: Improved audio playback interface layout for clearer design on main demo page
* BE-3930	Voicebot Demo: Updated copy and design on Casey Healthcare page for improved UX
* MST-744	Voicebot Logic: Let caller leave voicemail if the call is outside business hour
* MST-710	Voicebot: Allow user to transfer to agent at any time on claim info collection block
* MST-699	Voicebot: Answer eligibility follow-up questions in the bot
* MST-638	Voicebot: Automate eligibility calls
* MST-708	Voicebot: Fix - The follow-up question in info collection block sometimes asks for wrong info
* MST-711	Voicebot: Improved the agent transfer condition detection in claim faq block
* MST-641	Voicebot: Option to leave voicemail if we can't automate the call
* MST-668	Voicebot: Provide more information in the claim upfront prompt
* MST-639	Voicebot: Provide reference number and portal url after automation
* MST-640	Voicebot: Survey at the end of the call flow
* BE-3983	Web Console: Added "Connection Logic" column to Telephony Bot App table
* BE-3871	Web Console: Added Advanced tab to Telephony App Settings with CCaaS Integration settings
* BE-3942	Web Console: Added new "record" event in AIVR Call Session detail view
* BE-3943	Web Console: Added new Voicemail (VM) column to Call Sessions page to highlight calls with voicemail
* BE-4003	Web Console: Changed "Save" to "Save..." in Phone App drawer to indicate upcoming preview step
* BE-3933	Web Console: Changed API method used to get TTS prompts - from /synthesize to /get with dl=true option
* QA-2514	Web Console: Improved AIVR Sessions page layout by displaying 'VUI Alternative' in a table correctly and reducing empty space
* QA-2620	Web Console: Improved Edit button positioning on Account Settings page
* BE-3980	Web Console: Updated ASR settings to support only English and Spanish recognition
* BE-3939	Web Console: Updated language options in AIVR app add logic to match available voices

Changes related to Integrity of Processing (fixes):
* BE-3981	Fix - AudioSocketManagerTest.testOpenSocket_OneAvailablePort() fails in some cases
* BE-3925	Fix - crQuestionId needs to be returned from GET /sa/call/review/config/{ID} request
* BE-3991	Fix - DTMF barge-in is not working on dev cloud in Telephony Bot API
* BE-3905	Fix - In rex-grpc-proxy IOException: Could not create directory /var/rex/log 
* BE-3984	SA: Fix – Call Review Config form now correctly shows Responders as LLM instead of Manual
* BE-3740	SA: Fix – Corrected inaccurate Call Time Breakdown chart on Call Overview page
* BE-3735	SA: Fix – Corrected inaccurate Overtalk data in Call Time Breakdown chart on Call Overview page
* BE-3995	SA: Fix – Corrected titles of Call Duration Histograms chart on Call Stats dashboard
* BE-4035	SA: Fix - do not pass answerValue if we are doing human override of AI and the question type is choice
* BE-4032	SA: Fix - Duplicate sections in QA Form Config
* BE-4026	SA: Fix – Error message no longer shown prematurely on Voicebot data card in Call Overview page
* BE-4034	SA: Fix - Individual providers are not begin shown on Voicebot Card
* QA-2731	SA: Fix – Member ID verification status now updates correctly on Voicebot card in Call Overview page
* BE-4028	SA: Fix – Replaced provider name with member name in Voicebot data card on Call Overview page
* QA-2723	SA: Fix – Resolved cursor jumping to end when editing ANI and DNIS fields in the middle in Upload File modal
* QA-2714	SA: Fix – Timezone for calls is now consistent between Calls page and Call Overview page
* BE-4016	SA: Fix - Trimmed leading and trailing whitespace in context name and description fields
* QA-2736	SA: Fix - Unable to edit or add questions to the QA form, receiving a '400 Bad Request' error.
* BE-3932	SA: Fix - Voicebot Dashboard card now returns appropriate error for any 400 response from the backend
* BE-4018	SA: Fix - Voicebot data card verification status shows incorrect values
* QA-2651	TA Edge: Fix – Resolved issue causing shared transcript to refresh periodically
* QA-2675	TA: Fix – Add button for Regex no longer hidden when left menu is expanded on Text Redaction page
* QA-2679	TA: Fix - After Webex Meeting end, App not automatically submitting for Transcription
* QA-2674	TA: Fix – Edit icon for name field no longer visible on shared Transcribed page
* QA-2729	TA: Fix - LLM playground chat box prompt on Transcribe page is not working properly.
* QA-2668	TA: Fix – LLM Playground now works correctly on shared transcripts
* QA-2706	TA: Fix – Long project names no longer overlap with buttons on Upload page
* QA-2659	TA: Fix – Previously played Voice Signature no longer continues after clicking 'Add' on Users Speakers page
* QA-2682	TA: Fix - Right Side Border is Missing on Action Items Table in Zoom Meeting Assistance PDF
* QA-2655	TA: Fix – Tags added in 'Browser Share' now correctly appear on transcripts
* QA-2685	TA: Fix - The Action Items table appears blank in the downloaded .docx file.
* QA-2601	TA: Fix – Users with only user-level permissions can no longer access the 'Invite Other Users to Project' pop-up
* QA-2727	TA: Fix - Webex meeting bot failed to connect
* QA-2686	TA: Fix - Zoom Meeting Bot – The bot initially fails to join the Zoom meeting, displaying a "Failed to join the meeting" message. After some time, it requests permission to be admitted, but the transcript is not generated even after joining.
* BE-3968	Web Console: Fix – English (IN) was incorrectly auto-selected when clicking the Voice selection box in Telephony Bot App modal
* QA-2676	Web Console: Fix – Prevented duplicate apps when Save button is clicked multiple times while creating AIVR App
* BE-4002	Web Console: Fix – Resolved unexpected scroll behavior on Phone Management page
* BE-3856	Web Console: Fix – Speaker info now correctly displayed in Transcribe text view for affected calls
* BE-3967	Web Console: Fix – Suggestion box no longer appears outside modal when selecting voice language in Telephony Bot App modal

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release

