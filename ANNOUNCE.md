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

### Minor release 1.120.0 is scheduled for 6/2/2025 between 11:00pm and 1:00am US Central Time

New or changed functionality in the Transcribe App:
* BE-3795	TA Edge: Disable Test LLM button if any settings in standard LLM are changed but not yet saved
* BE-3777	TA: Added support for a keyword to belong to multiple groups and improved keyword designs on the configuration page
* BE-3892	TA: Improved action cards with new icons and layouts on home page
* QA-2462	TA: Improved design of Project Users page and moved current user to the top of the list
* BE-3891	TA: Updated Meeting Bot and Zoom icons, and adjusted ordering in the left-hand menu
* BE-3837	TA: Updated the YAML file that is driving the "What do you want to do?"

New or changed functionality in other platform components:
* BE-3813	Add new fields to /sa/call: businessOpenState, voicebotDuration, and voicebotVars
* BE-2449	Added account API methods to add/remove Grafana support to account
* BE-3875	Added ccaasIntegration and five9 fields to the AIVR App API
* BE-3850	Added new logicConnectMethod method - adapter - to AIVR App API
* BE-3874	Added optimizeFor setting to transcribe and sa offline APIs
* BE-3883	Added Redis Cache also to the Audio Server API that is used by the Telephony Bot
* BE-3807	Added to /sa/config API checks for uniqueness and disjointness of keyword and phrase tags
* BE-3562	Connected AIVR to Open AI Realtime API (Inbound calling)
* BE-3788	Copilot: Show claim-related information if provided by Pusher
* BE-3867	Demo Voicebot: Made design and copy changes to Casey Healthcare page in both English and Spanish versions
* BE-3812	If AIVR App has BusinessConfig attached then we report in AIVR session if the call was within or outside of business hours
* BE-3814	Implemented /sa/voicebot-stats API method
* BE-3866	Implemented Webhook listener for Five9 webhooks
* MST-634	Improve phone number entity (NER) context detection
* BE-3763	Improved validation of keywords and keywordGroups in each SA Config
* BE-3884	Made /sa/offline use the hints specified in the context and in the request
* BE-3909	Made loading of our AIVR Apps more robust 
* MST-535	Reduce Spanish NER model memory usage on offline-main
* BE-3898	Return Bad Request Error if POST /sa/offline is invoked with both speakers and diarization for single audio
* BE-3606	SA Call Resolution now uses LLM
* BE-3605	SA QA Form now supports LLM
* QA-2548	SA: Added API Security option and improved design of Project options page
* BE-3859	SA: Added Call Hold and Hold Removed states to both call transcript and audio timelines on Call Details page
* BE-3789	SA: Added claim-related information to Voicebot Data card on the Call Details page
* BE-3815	SA: Added new Voicebot Dashboard in beta for Voicebot projects
* BE-3517	SA: Added support for a keyword to belong to multiple groups and improved keyword designs on the configuration page
* BE-3776	SA: Added support for a keyword to belong to multiple groups and improved keyword designs on the configuration page
* BE-3857	SA: Added support for a phrase to belong to multiple groups and improved phrase designs on the configuration page
* BE-3849	SA: Added time spent in HOLD to call sections card on call details dashboard
* BE-3313	SA: Added Voicebot Dash
* BE-3430	SA: Improved design of Criterion Configuration dialog on Project Configuration page
* BE-3775	SA: Improved design of Criterion Configuration dialog on Project Configuration page
* BE-3796	SA: Improved layout of Voicebot Data card on Call Details dashboard
* QA-2564	SA: Improved project name and description field validations on both Project Settings and Creation pages
* BE-3811	SA: Improved topic distribution pie chart sizing and labels on the Agent Stats dashboard
* QA-2615	SA: Improvements for the QA Form configuration
* BE-3797	SA: Optimized Call Duration Statistics histogram on Call Stats dashboard to support large data sets
* BE-3647	SA: Redesigned left-hand menu navigation with menu collapse support and updated project selector
* BE-3774	SA: Redesigned left-hand menu navigation with menu collapse support and updated project selector
* BE-3888	SA: Updated call duration and call count colors on call stats dashboard for consistency across all charts
* BE-3893	SA: Updated demo and generic project type icons in project creation flow and project switcher
* BE-3682	Store AIVR markers for Aircall HOLD (start and stop)
* BE-3721	Support flavor (genesys or other) for each builtin grammar
* MST-589	Support N/A in QA form
* MST-565	Support signature in licensing service
* BE-3854	Support streaming for Google TTS for the streaming-capable voices
* MST-593	Train and test Omega model using SA and Australian accents dataset
* BE-3603	TTS stats are collected into influxDB
* MST-597	Update demo bot to support claim automation features 
* BE-3802	Web Console: Added a download button for voice sample in Phone App configuration dialog
* BE-3870	Web Console: Added AIVR app name to the delete confirmation dialog
* BE-3801	Web Console: Added common email field validations to both signup and login forms
* BE-3869	Web Console: Added new 'Adapter' connect mode in Telephony Bot app configuration
* BE-3880	Web Console: Implemented support for assigning different voices to multiple languages in Phone app configuration
* QA-2556	Web Console: Save button disabled if any input error on Speech Analytics configuration page

Changes related to Integrity of Processing (fixes):
* BE-3885	Cleanup all TTS voices available in Audio Server
* QA-2592	Demo Voicebot: Fix - Improved routing for /voicebot/ page to correctly redirect to Voicebot options page
* QA-2632	Demo Voicebot: Fix - Made all fonts consistent in Copilot sections on Call Details page
* QA-2657	Demo Voicebot: Fixed - Unable to access the voicebot call transcript.
* BE-3899	Fixed - /text/redact API does not check the debug.level value and always returns the redactions.originalValue
* MST-656	Fixed - DTMF grammar is not enabled by default when asking for date
* BE-3868	Fixed - TextUtils in pdfGen is not thread-safe
* BE-3673	Fixed behavior of incremental transcribe polling
* BE-3832	SA: Fix - "other" topic was incorrectly grouped into the "Other" slice of the pie chart on Call Stats dashboard
* QA-1588	SA: Fix - Downloaded PDF issues for call transcript.
* QA-2664	SA: Fixed - Sorting on QA Form page is not working.
* QA-2602	TA: Fix - Added translations for error messages in invite user during project creation
* QA-2660	TA: Fix - Delete confirmation popup showed total selection count instead of filtered count
* QA-2634	TA: Fix - HTML <br> tag present between the paragraph content in PDF.
* QA-2616	TA: Fix - LLM Playground input field was getting disabled on Transcribe Details page when disabling the video in the profile section
* QA-2604	TA: Fix - Text was attributed to a single speaker even when multiple speakers were present in browser share audio
* QA-2596	TA: Fix - User is able to set Public Share to never expire by manually modifying the expiration year to 0000
* QA-2609	TA: Fix - Zoom Meeting Bot – If the bot fails to join the meeting at the same time it requests admission, multiple instances of the bot may appear as participants. Eventually, the bot shows a "failed to join the meeting" status.
* BE-3897	Web Console: Fix - Fixed issue with retrieving AIVR session details by ID
* QA-2554	Web Console: Fix - Straight line cutting through row on Phone app page
* QA-2002	Web Console: Fix - Unable to upload Grammar file for creating Grammar under MRCP ASR.
* QA-2608	Web Console: Fix - Unable to view all sessions on user profile page due to table scroll not working
* QA-2643	Web Console: Fix - Users are no longer allowed to delete the default context on context dashboard
* QA-2672	Web Console: Fix - Voice field was showing blank in edit flow in the phone app drawer for some projects


All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release

### Minor release 1.119.0 is scheduled for 5/10/2025 between 11:00pm and 12:00am US Central Time

New or changed functionality in the Transcribe App:
* BE-3538	TA Edge: added a Test Chat on the LLM Settings page
* BE-3741	TA: Added a setting on the Profile Settings page to hide video on the Transcript Details page
* BE-3757	TA: Added an info message on the LLM Settings page to indicate that changes may take a few minutes to take effect
* BE-3702	TA: Added context size text box to each LLM service settings
* BE-3767	TA: Added support to disable copying and remove all clipboard icons in the Transcript Detail view based on app's disableCopy settings
* BE-3737	TA: Added X-VG-Audit header for asr meeting APIs
* QA-2493	TA: Removed the 'Others' tab from the project selection menu in the basic plan, as there are no shared projects
* BE-3707	TA: Removed the unnecessary Key column from the API Token page
* QA-2089	SA/TA: Added deletion animation for regex settings and repositioned the Save button on the Redaction Settings page
* QA-2520	SA/TA: Added validation error message for phrase name field in the add keyword modal

New or changed functionality in other platform components:
* BE-3643	Added expiryDate to /sa/call
* BE-3408	Added POST /sa/call/context/{contextId}/recompute
* BE-3644	Compute call duration histogram data in GET /sa/call-stats-overall API
* MST-338	Concatenate stereo audio to improve whisper, and fix the boundary words issue
* BE-3784	Demo Voicebot: Enhanced error handling screen for transcript errors and added a "Try Again" button on the transcript details page
* QA-2479	Demo: Made the entire upload box clickable for uploading a file on the main demo page
* BE-3618	Implemented PUT /aivr/{ivrSid}/command API method
* MST-563	Improve English NER model on lower case and digits
* MST-585	Improved diarization model
* BE-3565	In dialplan that launches aivr lua pass new argument called: mod_vg_tap with possible values: rex or vaca
* MST-551	Integrate OpenAI realtime audio API in llm-svc
* BE-3570	Modify aivr.lua to invoke mod_vg_tap without the ivrSid parameter if connecting to VACA socket instead of Rex socket
* BE-3351	On-Prem License Server
* BE-3730	SA: Added LLM-generated QA form answers
* BE-3521	SA: Added new 'Voicebot Data' card on the Calls dashboard, replacing the "Date and Time" card for valid calls
* BE-3736	SA: Added optimizeForWebUi:level2 parameter to POST offline requests
* QA-2552	SA: Added validation to prevent creating duplicate keywords on the configuration page
* QA-2546	SA: Added validation to prevent creating phrase names with only empty spaces in the Keywords modal
* BE-3771	SA: Improved the call counts weekly comparison graph on the Call Stats dashboard to highlight current week data more clearly
* QA-2467	SA: Increased the visibility of the search box on the Agents page
* QA-2540	SA: Prevented hiding all columns in the Agents table via the column filter
* QA-2458	SA: Removed duplicate table filter from the Users table on the Users page
* BE-3646	SA: Removed the review button if the review answer form is not available
* BE-3782	SA: Removed the SA config name field and made the LLM prompt field multi-line on the configuration page
* BE-3706	SA: Removed the unnecessary Key column from the API security page
* BE-3663	SA: Replaced the boxplot with a histogram plot in the call duration statistics chart on the Call Stats dashboard page
* QA-2523	SA: Updated the placeholder text in the Phrase Groups modal from "No rows" to "No phrases added"
* MST-531	Support QA form automatically in ml-svc
* MST-543	Use context to improve the accuracy of NER
* BE-3724	Voicebot Demo: Implemented the new design which includes full automation for the Healthcare page in both English and Spanish versions
* QA-2476	Web Console: Added cancel icons to the language selection dropdown's closed state on the Web ASR Settings page for better UX
* BE-3460	Web Console: Added confirmation dialog for changes and enabled in-place editing in the Configure AIVR App modal for better UX
* BE-3622	Web Console: Added OpenAI Realtime API support to configure new AIVR App
* QA-2432	Web Console: Added profile avatar in the header's profile menu
* QA-2542	Web Console: Added validation for the app name in the Configure AIVR App modal
* BE-3786	Web Console: Improved email validation in the signup form to support addresses like jackson@replay.sale
* QA-2561	Web Console: Improved UX on the ASR Settings page by hiding Real-Time Acoustic Model fields for unsupported languages and adding info messages
* BE-3658	Web Console: Redesigned the logic creation/edit flow in the Configure AIVR App modal and added support for default logic with enhanced validation

Changes related to Integrity of Processing (fixes):
* BE-2083	Fix for negative duration of words
* BE-3645	Fixed - Mod Review Config has no way of deleting sections
* QA-2551	SA: Fix - Added validations to prevent creating keywords with only empty spaces
* QA-2481	SA: Fix - Call Time Breakdown chart on the Call Details page not showing data correctly
* BE-3685	SA: Fix - Data selectors not working correctly in the Yearly Call Trends chart on the Call Stats dashboard
* QA-2518	SA: Fix - Removed duplicate success toasts when copying the configuration ID on the Configuration page
* QA-2470	TA: Fix - Amount '0' missing for the first time user on the billing page
* QA-2532	TA: Fix - API Security page was inaccessible from Project Settings for some projects.
* QA-2062	TA: Fix - In downloaded PDF - some speaker name is "null"
* BE-3780	TA: Fix - Meeting URL box became unresponsive on the Meeting Bot page for long URLs.
* QA-1987	TA: Fix - PDF download showing Something Went Wrong
* QA-2587	Web Console: Fix - Updated the user profile menu from a hyperlink to a dropdown menu item
* BE-3727	Web Console: Removed the extra Cancel button from the phone number purchase success modal

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release

### Minor release 1.118.0 is scheduled for 4/15/2025 between 11:00pm and 12:00am US Central Time

New or changed functionality in the Transcribe App:
* BE-3634	TA: Added call duration in header on transcript details page
* QA-2236	TA: Disable LLM Playground box while the transcript is playing
* QA-2461	TA: Improved role filter in Project Settings to display all options when any filter is selected for easier selection

New or changed functionality in other platform components:
* BE-3482	Add epochReportedMsec to k8sStatus field on the onPremCluster API
* BE-3626	Added llm field to question in the Call Review Config
* BE-3577	Allow use of normal JWT token in GET /sa/call/search/fields and POST /sa/call/search
* BE-3031	Copilot: Added ability to pull up notes after internal transfer.
* BE-3628	Demo Voicebot: Display payment related fields in demo copilot
* BE-3564	In AIVR App added openAiRealtimeApi as value of logicConnectMethod
* BE-3526	In AIVR Session, log Error events for bad Callback responses
* BE-3566	In POST /aivr add handling of VACA init if openAiRealtimeApi is value of logicConnectMethod
* BE-3571	Modify mod_vg_tap to work without the rex_sid parameter (so that it can open socket to VACA)
* BE-3621	Most read-only sql queries can now use the replica DB instead of the master.
* QA-2464	Prevent the default JWT token for a Context from deletion via the Web UI
* BE-3641	Return only 6 digits after the decimal point for confidence values
* QA-2465	SA: Added option to delete Criteria in project configuration under project setting.
* BE-3584	SA: Added trendlines to Yearly call trends chart on call stats dash
* QA-2391	SA: Changed delete option from text to button on users settings page
* BE-3586	Sa: Changed the zoom of the Yearly call trends chart to be along the x-axis only on the call stats dash
* BE-3637	SA: Changed times in Call Sections card from timestamps to time durations on Call Details page
* QA-2388	SA: Improved column spacing on user settings page to better fit longer fields like email
* BE-3558	SA: Improved dark mode styling for Call Stats Dashboard
* BE-3458	SA: Improved Design for 'Confirm Configuration Changes' Dialog on project configuration page
* BE-3585	SA: Improved look of the charts on the Call Stats Dain in dark mode
* BE-3617	SA: Improved performance of advanced search page
* BE-3582	SA: Larger fonts used in Call Duration Statistics card on stats dash
* BE-3593	SA: Make QA Call Review form visible
* BE-3654	SA: Removed call selection checkboxes from all calls table to improve UX
* BE-3583	SA: Removed extra gap on x-axis and increased line thickness in Call Duration Statistics card on Stats Dash
* BE-3594	SA: Removed unnecessary scroll on advanced search page
* QA-2469	SA: 'Select All' in advanced search filters now selects only the filtered results
* BE-3624	Switch to using mod_shout for playback in AIVR
* BE-3640	Web Console: Added 404 Error Page for api path which does not exist.
* QA-2446	Web Console: Added first and last name validations on user profile page
* QA-2447	Web Console: Changed filtering 'No rows' placeholder text to "No Logs Data Found" in case of no match on Logs Page
* QA-2410	Web Console: Copy button not working for SIP URI field in Phone apps drawer on Phone apps page
* QA-2313	Web Console: Improved design of account management page to show all columns of login sessions section in a single view
* QA-2168	Web Console: Improved language selection widget on the Settings Speech Recognition
* QA-2431	Web Console: Improved placeholder messaging from "No rows" to "No Phone apps found" on phone apps page
* QA-2414	Web Console: Increased font size of helper text for 'Session ID' and 'Messages' field on Logs Page for better visibility
* BE-3559	Web Console: Replaced heavy background.svg to lighter png file
* QA-2433	Web Console: Save button now remains disabled until the data cleanup interval is changed on settings page

Changes related to Integrity of Processing (fixes):
* BE-3648	Fix a potential vulnerability where the session id for a new ASR session could be provided in the request
* BE-3650	Fixed - Call Review Section name is not being saved
* BE-3671	Fixed - GET /confgroup?type=SpeechAnalytics returns a plain JWT token instead of displayJwt
* BE-3578	Fixed - GET /sa/call-stats does not seem to use the keywordGroup parameter
* BE-3560	Fixed - StackOverflowException from a realtime SA session when no web socket connection is established for results
* BE-3579	SA: Fix - Date and Time on stats dashboard should be in the format defined in the Project settings
* BE-3580	SA: Fix - In stats dash, the duration display should support values larger than 59:59
* QA-2466	SA: Fix - Negation toggle not working in Criterion Dialog in project configuration settings
* QA-2389	SA: Fix - On API Security page, success message no longer shown without JWT creation. 'Create' button now requires valid name with note field validation
* QA-2486	SA: Fix - Selected role not displayed in 'Add User' form on User Settings page after selection
* QA-2224	SA: Fix - The end date of the demo project is earlier than the start date.
* QA-2443	SA: Fix - The text inside call time breakdown card getting cut off on call details dash
* BE-3581	SA: Fix - Total Call card values vertically aligned on call stats dash
* BE-3627	SA: Fix issues in Call Review Form Configuration in settings
* QA-1800	TA Edge: Fix - Meeting Minutes missing
* QA-2468	TA: Fix - 'Last Active' column sorting not working in Project Settings
* QA-2426	TA: Fix - Resolved overlapping 'beta' label issue in 'Download as PDF' pop-up on Transcribe Details page
* QA-2427	TA: Fix - The Chinese flag displayed in the project settings is different from the project flag shown on the homepage
* QA-2463	TA: Fix - The dropdown icon overlap with the exclamation (!) icon for the expected speakers field.
* QA-2460	TA: Fix - The selected timezone is not visible in the timezone field after selection.
* QA-2488	TA: Fix - Webex bot joins the meeting but doesn't show as admitted on UI until the meeting ends where it then shows as admitted and failed to join.
* QA-2365	TA: Fixed - The bot has already left the meeting but is still appearing in the meeting. This issue occurs for all three bots: Zoom, Teams, and Webex.
* QA-2362	TA: Fixed - The meeting bot encounters a 500 Internal Server Error when attempting to leave a meeting.
* QA-2072	TA: Fixed - The meeting bot is showing as admitted even though the meeting organizer has not admitted the bot.
* QA-2364	TA: Fixed - The recording bot appears as admitted in the meeting, even though the organizer did not admit it.
* BE-3638	Web Console: Fix - 'Clear Filters' button on Logs page did not clear Session ID and Messages fields
* QA-2436	Web Console: Fix - Large extra space observed at the beginning of message when copied to clipboard and pasted on logs page
* QA-2374	Web Console: Fix - Removed unnecessary scrollbar from the signup dialog
* QA-2473	Web Console: Fix - Validation for numeric fields like 'Max alternatives', 'Incomplete Timeout' etc. on Speech Recognition Settings Page to not accept 0 as manual input
* QA-2448	Web Console: Fixed - On the logs page, searching by message displays random errors and an internal service error in the console.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


### Minor release 1.117.0 is scheduled for 3/23/2025 between 11:00pm and 12:00am US Central Time

**Key changes related to the core APIs**
* All builtin grammars are now available in Spanish version
* Second dashboard for the Speech Analytics App
* Errors in AIVR callback are now reported as events associated with a session
* Beta version of Webex bot for the TRanscribe App

New or changed functionality in the Transcribe App:
* BE-3452	TA Edge: Pages for Webex OAuth handshake
* BE-3530	TA: Add LLM Model to LLM settings
* BE-3488	TA: Add support for Chinese language for transcription (beta)
* BE-3496	TA: Added extra info to the Project delete dialog

New or changed functionality in other platform components:
* BE-3471	Add a billingCode parameter to /asr/transcribe/async API
* BE-3497	Add to onPremCluster API fields to define external Postgre
* BE-3408	Added POST /sa/call/context/{contextId}/recompute
* BE-3450	API methods needed for Webex OAuth hanshake
* BE-3381	APIs to generate data for the generic dashboard on SA App
* BE-3453	Bot that joins Webex meeting using SDK to collect speaker activity, audio, and video.
* BE-3491	Implemented DELETE /sa/call
* BE-3526	In AIVR Session, log Error events for bad Callback responses
* BE-3527	In AIVR Session, log Error events for failed Callback requests
* BE-3469	On Edge in influxDB measurements that have context - store context as a tag instead of a field
* BE-3498	On Edge, all code using Postgres will use external Postgres if it is specified in onPremCluster Settings
* BE-3464	Reopen transcribe-results websocket connection if connection is lost
* QA-2338	SA/TA: Improve UI for Phrase detection config
* QA-2342	SA/TA: Pre-set default value for the Location Channel under Phrases settings.
* BE-3255	SA: Add a card that shows time distribution of various parts of the call
* BE-3519	SA: Condense Agent Sentiment card to show 5+5 agents (5 best and 5 worst) in one view
* BE-3332	SA: Generic Call Stats Dashboard
* QA-2166	SA: Improved Keyword selection filter on Search Page
* BE-3525	SA: Improvements in phrase settings
* BE-3258	SA: In the Call Detail view on Debug page show the date when the call will expire
* BE-3518	SA: In the Dashboard requests for call-stats change keywordGroup to "dissatisfied"
* BE-3529	SA: Make smaller the icons in the top-right corner of the cards on the call detail page
* QA-2275	SA: Make the toaster message for Add/Edit and Delete JWT disappear after 5-10 seconds.
* BE-3512	SA: Swap Agents and Keyword cards on Dash
* BE-3451	Store in the onPremCluster the UserId of the User who did Webex OAuth to obtain auth_token
* BE-3349	Submit CRM notes at the end of Voicebot call (Claims Automation use case)
* BE-3360	Universal HTTP webhook proxy via Cloud to Edge
* BE-3499	Web Console: Add settings for specifying Internal/External Postgres
* BE-3487	Web Console: Added Avatars
* BE-3485	Web Console: On Edge view show Cluster Id
* QA-2368	Web Console: Show Avatar of the Context creator on the page that lists all the Contexts

Changes related to Integrity of Processing (fixes):
* BE-3457	Demo Voicebot: Fix - Start Over leaves the old polling still running if I make another call immediately
* BE-3480	Fix builtin grammar for currency
* BE-2835	Fix - API GET /share/{shareId} for a "within account" share, executed on a different account return 401 Forbidden, instead of 200 and empty response.
* BE-3516	Fix - OOM from production asr-api 
* BE-3515	SA/TA: Fix - Rules for phrases too restrictive
* QA-2363	SA/TA: Fix - The user is unable to update the Relation Parameter for the phrase group.
* BE-3500	SA/TA: Fix bug with pop-confirm while deleting a phrase or phrase group
* BE-3548	SA: Fix - Agent Dashboard - Top card's text and line graph should be aligned to baseline
* QA-2086	SA: Fix - Call Center ID filter has incorrect validation
* QA-2398	SA: Fix - Overlapping issues on call overview page.
* BE-3099	SA: Fix - PII redaction broken in /sa/offline
* BE-3467	SA: Fix - Sentiment card keeps shrinking if there is not data in a chosen period
* QA-2224	SA: Fix - The end date of the demo project is earlier than the start date.
* BE-3513	SA: Fix - Top Dashboard cards look bad on a wide screen
* QA-2399	SA: Fix - Unable to apply "Agent and Queue" filters in Advance search filter.
* BE-3534	SA: Fix - Upload - Selected Queue name does not show on input field upon creation of new option
* QA-1857	SA: Fix - User should not be allowed to create two projects with same name.
* BE-3510	SA: Fix issues with Sentiment Card on the Dash
* BE-3511	SA: Fix issues with the Topic Distribution card
* BE-3505	SA: Fix the Call Time Breakdown
* QA-1786	TA Edge: Fix - LLM Query is not working giving 500 Internal Server Error.
* QA-2395	TA: Fix - getting something went wrong page for the first time login after signup to the application.
* QA-2180	TA: Fix - LLM playground always returns summary in response to first question even if the question is not about a summary
* QA-2339	TA: Fix - Phrase settings- the Min Word field should not accept negative or zero values.
* QA-2397	TA: Fix - The toaster message 'API token created successfully' is incorrect, as the token is not actually created
* QA-2343	TA: Fix - When a tag is separated by a comma, it should be added properly and should not remain visible in the input field after being added.
* QA-2387	TA: Fix - When a user tries to create an API token without entering a name, the displayed message is incorrect. It should indicate that "Name is a required field."
* QA-2344	TA: Fix - When a user uploads a file with an invalid tag value, field validation should be applied to prevent submission.
* QA-2369	TA: Fix - When User Click on Voice signature page than showing on page "speaker not found".
* QA-2359	Web Console: Fix - When the user clicks on 'Transcription' and uploads a file, the placeholder text for 'Hint' does not disappear after entering input.
* QA-2360	Web Console: Fix - When the user clicks on 'Transcription,' uploads a file, and enters input in the 'Hint' field, the input text goes outside the box.


All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


### Minor release 1.116.0 is scheduled for 3/3/2025 between 11:00pm and 12:00am US Central Time

**Key changes related to the core APIs**
* Nuance SWI_ slots supported in MRCP NLSML return
* Added DTMF tone redaction
* Added ADDRESS to redaction options
* Added recompute support to /sa/offline API

New or changed functionality in the Transcribe App:
* BE-3382	TA: Implementation of a new design for Phrase Settings
* QA-2203	TA: Improved error handling in the steps of Project creation
* BE-3417	TA: Refactoring of Project Creation Flow and Project Settings for better separation of concerns
* BE-3386	TA: Show the owner of the account in the user profile

New or changed functionality in other platform components:
* BE-3399	Add option to our MRCP ASR to return NLSML in complete Nuance format
* BE-3395	Add saAppHiddenFeatures to POST and PUT on the account.
* BE-3362	Add to /asr/transcribe/async OFFLINE API ability to redact DTMF tones out of audio.
* BE-3372	Added a method to apply redaction to existing /sa/offline transcription and audio
* BE-3427	Added ADDRESS entity type to the redacting formatter (both transcribe and sa/offline)
* BE-3408	Added POST /sa/call/context/{contextId}/recompute
* BE-3407	Added POST /sa/offline/{saSessionId}/recompute
* BE-3434	Added recomputePhase query parameter to GET /sa/call
* BE-3426	Added two new read-only fields to sa/call -- recomputePhase and lastRecomputeTime
* BE-2920	Admin Tool: Add ability to control settings for Speech Analytics accounts
* BE-2989	API for setting hidden features for SA Account
* BE-3412	App Selector / Web Console: Inform about $5 credit for personal email 
* QA-2185	Demo Voicebot: Removed collecting user feedback
* BE-3437	For Genesys platform support builtin grammars with languages other than English
* BE-3279	In Webex Meeting Bot obtain email from the participants and store it
* BE-3436	Made the language parameter for the builtin grammars case-insensitive and make it check only the language part of locale
* BE-3322	Migrate Java services to spring-boot-3.2.11 (spring 6.1.16)
* BE-3400	Remove asr-api as a dependency from sa-call-api
* QA-2228	SA: Added a hover msg over Call Time Breakdown pie chart.
* BE-3410	SA: Added CVV and ADDRESS PII Redaction type
* BE-3432	SA: Added Recompute option to calls in the Call table
* BE-3387	SA: Improve the time period selectors plus other Dashboard issues
* QA-2270	SA: When searching for something not found in the transcript, now it displays 0/0.
* QA-2020	SSO: Hide Forgot Password option on Edge
* BE-3363	The artificial delay at Login API applies now only in case of non-200 response
* QA-758	Updated messaging for App Selector
* BE-3413	Web Console: Account signup - apply lower Credit to gmail and outlook.
* QA-2268	Web Console: Add a back button on transcript page.
* QA-2283	Web Console: Edit Phone App - A Close icon is provided to close the edit page.
* QA-2306	Web Console: Meetings section displays 'No Data Available' instead of 'No rows' when there is no data for better user experience.
* QA-2305	Web Console: Transcription section displays 'No Data Available' instead of 'No rows' when there is no data for better user experience.

Changes related to Integrity of Processing (fixes):
* BE-3402	App Selector: Fix - Signup url takes me to login select page
* BE-3447	Demo Voicebot: Fix - Bad Content Security Policy
* QA-2333	Demo Voicebot: Fix - During the call, the voice assistant reports an error from the AIVR logic.
* BE-3448	Demo Voicebot: Fix - Not loading the transcript (transcriptError)
* QA-2246	Demo: Fix - file upload layout needs to be modified as the filename text is not properly aligned and appears cluttered.
* BE-3438	Fix - /sa/call-stats is slow for the 30D period
* BE-3371	Fix - If there are only 2 speakers, make sure that mergedAudio has 100% channel spearation
* BE-3431	Fix - The vars returned in the Telephony bot DELETE callback are not stored
* BE-3388	Fix recent vulnerabilities in 3rd-party Java Libraries
* BE-3425	Fix: If using whisper model, Audio selector is ignored when creating stereo audio in offline-sa
* BE-3391	SA: Fix -  Do not show "+1 More" for tags, use that only with "+2 More" or higher
* QA-2282	SA: Fix - Getting error while processing the uploaded file
* BE-3445	SA: Fix - Sentiment weird for on certain screen sizes
* QA-2266	SA: Fix - Settings -> Configurations : 'Overtalk Percentage' of 'Incidents Threshold' % value shouldn't be more that 100%
* QA-2265	SA: Fix - Settings -> Configurations : 'Silence Percentage' of 'Incidents Threshold' % value shouldn't be more that 100%
* QA-1811	SA: Fix -The user is logged out when deleting larger number of users at the same time from Users page.
* QA-2237	TA: Fix - Input fields behave as if the user has entered special characters after adding a tag, as the tag requirements are being displayed.
* QA-2259	TA: Fix - Latest News page, text formatting, background color and bullet point is missing.
* QA-2336	TA: Fix - Meeting bot - not working for MS-Teams and Webex
* QA-2116	TA: Fix - Project name should have a limit of 200 characters.
* QA-2223	TA: Fix - Some participants' details are hidden on mouse over when a large number of filters are selected
* QA-2218	TA: Fix - The content on the zoom background light SVG image may appear confusing to users on the Zoom-App page
* QA-2288	TA: Fix - Unable to Re-diarize transcripts for zoom upload directories.
* QA-2331	TA: Fix - When the Regex Example tab is selected, the 'Add Neural Network Example' button should not be displayed, as it creates confusion about whether it is clickable.
* QA-2102	TA: Fix - Zoom Meeting Bot is not recognizing that meeting has ended (for long meetings)
* QA-2330	Web Console: Fix - "###" Extra text present in reslease notes section .
* QA-2337	Web Console: Fix - Listen button clickable even though there is no saSessionId
* QA-2284	Web Console: Fix - Telephony Bot API -> Business Configuration || 'Special Dates' name shouldn't accept the blank space
* QA-2277	Web Console: Fix - Transcribe -> SA Configuration : 'Overtalk %' of 'Incidents Threshold' % value shouldn't be more that 100%
* QA-2276	Web Console: Fix - Transcribe -> SA Configuration : 'Silence %' of 'Incidents Threshold' % value shouldn't be more that 100%
* QA-2285	Web Console: Fix -Telephony Bot API -> Business Configuration || 'Named Prompts' name shouldn't accept the blank space


All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.115.0 is scheduled for 2/10/2025 between 11:00pm and 12:00am US Central Time

**Key changes related to the core APIs**
* Ability to switch language during async real-time transcribe session
* Support for user-bound JWT tokens
* Spanish sentiment and sentence similarity models
* Text redaction supports chat and email formats directly
* Outbound calling supports initial prompt
* Voicebot Business Config supports multiple opening hours per day

New or changed functionality in the Transcribe App:
* BE-3377	TA: Add In User Profile for Admin users ability to generate and manage user-bound JWT tokens
* QA-2077	TA: Add success message when deleting a voice signature from account settings
* BE-1468	TA: Add to Transcribe App Cloud an option to delete account
* QA-2196	TA: Added input data validation for Webhook URL, Name, Token fields
* QA-2143	TA: Change design for Keywords settings
* QA-2225	TA: Voice signature - Play button now is disabled till the status turns into ready.

New or changed functionality in other platform components:
* BE-3337	Add a field on aivr app to indicate a different fssk to launch outbound calls
* BE-3350	Add ability to switch language during async real-time transcribe session
* BE-3359	Add member information to the Call notes generated for the Provider calls
* BE-3369	Add outboundPrompt to POST /aivr/dial/{destination}
* BE-3373	Add outboundPrompt to POST /public-asr/aircall/user/dial-outbound
* BE-3339	Add to POST /text/redact API ability to handle chat xml format
* BE-3340	Add to POST /text/redact API ability to handle email html format
* QA-2155	Admin Tool: Fix - Table Search- after clicking on the reset button table should reset to the previous value
* BE-3376	APIs to create and manage JWT tokens that are bound to users
* QA-1790	App Selector: Nicer formatting for Privacy Policy and Terms and Conditions pages
* BE-3370	Copilot: Add outboundPrompt to the AIVR API dial command
* MST-426	Deploy Spanish sentence similarity model
* MST-406	Hang up the call when the user is calling a wrong line of business
* BE-3329	Improve visibility into /sa/offline processing stats
* BE-3358	In normalOpeningOurs deprecate open/close fields and replace with openPeriods
* BE-3364	Limit Context name to 200 chars
* BE-3325	Move /sa/call API to a separate microservice sa-call-api
* MST-389	Multi-language design and framework in ml-svc
* QA-2232	SA: Add success/alert notification after Add/Delete or Edit JWT
* BE-3303	SA: Better Sentiment card on the Dashboard
* BE-3320	SA: Better Topic distribution card
* BE-3352	SA: Implementation of new Design for Phrase Settings
* BE-3301	SA: Improved view for AHT card
* BE-3302	SA: New design for time period selectors
* BE-3374	Send email to support@voicegain.ai if an account status switches to "suspended"
* QA-2020	SSO: Hide Forgot Password option on Edge
* BE-2728	Support auto-reconnect if fssk loses connection to Freeswitch.
* MST-431	Support MRCP confidence score scaling in rex
* MST-430	Support multiple open/close prompt in business config
* MST-370	Train and deploy the Spanish sentiment model
* MST-407	Use LOB to filter account from the given phone number
* QA-2186	Voicebot Demo: Remove Survey option.
* BE-3375	Web  Console: Provide info how to request Account cancellation and data deletion
* QA-2114	Web Console: Add "Copy to Clipboard" tooltip on logs page
* BE-3366	Web Console: Multiple open-close hours in the Normal Opening hours in the Business Config
* BE-3218	Web Console: Redesign Home page (not logged in) 
* QA-2226	Web Console: The toggle button on SA Config is overlapping with the text.

Changes related to Integrity of Processing (fixes):
* BE-3312	Fix - Customer reports that for each meeting they get 4 DONE webhook requests
* QA-1992	SA: Fix - Inconsistent date format on call's page.
* QA-2119	SA: Fix - Project names should not be allowed to start with spaces or dots
* BE-3379	TA: Fix -  Project name entry cursor with strange behavior
* QA-2092	TA: Fix - Add tag field is missing on the zoom directory upload page.
* QA-2217	TA: Fix - Language dropdown is not centrally aligned during project creation
* QA-2094	TA: Fix - Recomputing overlaping with size in storage.
* QA-2253	TA: Fix - Settings- 'Keyword' name shouldn't accept the blank space
* QA-2252	TA: Fix - Settings- 'Phrase' name shouldn't accept the blank space
* QA-2073	TA: Fix - The tag field is not available when the user tries to save a browser share recording
* QA-2220	TA: Fix - walkthrough wizard does not properly highlight features as expected
* QA-2159	TA: Fix - When the owner downloads a transcript as a docs file, the transcript's background color is not included in the file.
* QA-2139	Web Console: Fix - Added Regex is not clearly visible in settings.
* QA-2250	Web Console: Fix - API Security - 'New Secret Token' name shouldn't accept the blank space
* QA-2247	Web Console: Fix - 'Download' icon shouldn't be active until transcribe status is ready like 'View Transcript' icon as if user click on
* QA-2230	Web Console: Fix - For a brief moment, "Logout returned: Authentication token missing" is displayed.
* QA-2249	Web Console: Fix - SA Configuration name shouldn't accept the blank space
* QA-2241	Web Console: Fix - Settings-> Speech Recognition: 'Sensitivity' should only accept value between 0-1
* QA-2175	Web Console: Fix - Shortcut keys should be unique, and users should not be able to assign all shortcuts to a single key
* QA-2147	Web Console: Fix - Unable to edit the description of any api security as it always shows the error
* BE-3257	Web Console: Fix - various issues on the Logs page

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.114.0 is scheduled for 1/20/2025 between 11:00pm and 12:00am US Central Time

This release updates Edge deployments from Mongo version 6 to 7.

New or changed functionality in the Transcribe App:
* QA-2183	TA: Advanced Search - Improve filter for selecting languages
* QA-2190	TA: Advanced Search - Improve filter for selecting participants
* QA-2189	TA: Advanced Search - Improve filter for selecting speakers
* QA-2181	TA: Advanced Search - Improve filter for selecting tags
* QA-2130	TA: The speakers table under account settings now has sorting functionality by Email.
* BE-2874	TA: Introduced fallback error page for Loading Chunk Issue
* QA-2137	TA: Show 'Copy to clipboard' message when hovering the mouse over the copy icon for the project ID
* QA-2083	TA: Until a profile picture is updated by the user, display the avatar image in the profile settings
* QA-2142	TA: When no group is available for the keyword to merge, display the option to create a new group

New or changed functionality in other platform components:
* BE-3274	Add clientParams to openId Login API
* BE-3273	Add languageDetection parameter to /sa/offline API
* BE-3317	Add support for new CVV NER in our APIs
* BE-2449	Added account API methods to add/remove Grafana support to account
* BE-3311	Enable MRCP by default on all new Developer accounts
* BE-3277	In Add Meeting Audio API method add email field to speaker or participant
* BE-3280	In response from Login API return account Grafana setting if account has Grafana enabled
* BE-3279	In Webex Meeting Bot obtain email from the participants and store it
* BE-3090	Redesign the sso.voicegain.ai 
* QA-2198	Return from login API correct set of permissions for the user even if passwordChangeRequired is true
* BE-3255	SA: Add a card that shows time distribution of various parts of the call
* BE-3287	SA: Add a filter on Direction to the Calls table
* BE-3266	SA: Add a set of fast filters for date selection to advanced search
* QA-2053	SA: Add Save button for add/edit tags
* BE-3306	SA: Better check for correct Keyword settings before saving them
* QA-2184	SA: Better indication for case when sentiment has not been computed.
* BE-3299	SA: Better read-only view of the AIVR integrations
* BE-3298	SA: Increase size of Sentiment Icons
* QA-2201	SA: Use the same rules on the call details page for considering an error as we use in the calls table
* BE-3032	Support async writes to influxdb
* BE-3292	Support CVV redaction in formatter in ASR API (transcribe, meeting and offline SA api)
* QA-2099	Web Console: Copy to clipboard info shows when user mouse hover on copy icon
* QA-2018	Web Console: Improved Edge logout behavior
* QA-2006	Web Console: Improved transcript highlight efficiency so that pagination could be removed
* QA-2082	Web Console: In user profile make clear that email field is read-only
* BE-2448	Web Console: Only select accounts show Grafana option
* QA-1867	Web Console: Show audio graph also for whisper models
* MST-332 Train Kappa model using customer data
* MST-357 Review and release the latest gpt-4o integration in llm-svc
* MST-364 Improve billing intents routing
* MST-380 Integrate new CVV feature in offline-main and ml-svc
* MST-382 Support whisper-large-v3-turbo in APIs, and decide the default model for each use case
* MST-409 Disable previous NER context when entering new context

Changes related to Integrity of Processing (fixes):
* QA-2194	Fix for section formatting in Meeting API for certain cases
* QA-2127	SA: Fix - Call Time Breakdown chart flickers when call is played.
* QA-2234	SA: Fix - Date filter in Advanced search is not working when "Include current partial period" is un-selected.
* QA-2165	SA: Fix - Keywords hidden on mouse over in advanced filter selection when a large number of keywords are selected
* BE-3291	SA: Fix - Usage in Keywords must be optional
* QA-2182	SA: Fix - Word cloud gets broken when user play call on overview page and then move to transcript page
* QA-2138	SA: Fix - Word cloud toggle is missing in Confirm Configuration pop-up.
* QA-1498	TA Edge: Fix  - Unable to detect the Browser OS Device IP for all login sessions.
* QA-2113	TA: Fix - Advanced Search: Project filter having extra white space that is covering whole page
* QA-2129	TA: Fix - behavior of the tag entry box
* QA-2110	TA: Fix - Duplicate tags shouldn't be allowed
* QA-2209	TA: Fix - Meeting Bot - Displaying 'Forgot Meeting' instead of 'Leave Meeting' for a Webex call."
* QA-2204	TA: Fix - Occasional unable to join Zoom meeting bot - Error: “Failed to join meeting"
* QA-2120	TA: Fix - Project names should not be allowed to start with spaces
* QA-2163	TA: Fix - Properly handle Projects with missing saConfig
* QA-2160	TA: Fix - Unable to move multiple files across all projects, as the pop-up page displays differently and does not allow selecting the destination.
* QA-2115	Web Console: Fix -  New User Wizard: The header menu location is incorrect; it should be highlighted in the top right corner of the page.
* QA-2013	Web Console: Fix - Alignment issue in the 'Word Cloud'
* QA-2122	Web Console: Fix - Column names e.g. Languages, Non-Real Time Models appear duplicated due to each 'ASR Transcription' and 'ASR Recognition' widget having an associated column
* QA-2124	Web Console: Fix - Context filter should either have unique column names or provide a way to distinguish between the 'ASR Transcription' and 'ASR Recognition' widgets
* QA-2216	Web Console: Fix - Edge Portal Logout is not working properly for Cloud Login.
* QA-2105	Web Console: Fix - Fields names are different in table and column on call session page.
* BE-3288	Web Console: Fix - In Phone number table, filtering by number does not work and/or is super slow
* QA-1967	Web Console: Fix - 'Level' filter is not working as expected
* QA-1953	Web Console: Fix - Log Filter is not working
* QA-1404	Web Console: Fix - Logs filter is not working
* QA-2170	Web Console: Fix - 'Max Alternatives' textbox of 'Real-Time Acoustic Model' section shouldn't accept 0 as it's value should be between 1-100
* QA-1966	Web Console: Fix - 'Services' filter is not working as expected
* QA-2097	Web Console: Fix - Sorting for Duration is not working properly on calls page.
* QA-2098	Web Console: Fix - Sorting for Events is not working properly on call sessions page.
* QA-2104	Web Console: Fix - Sorting is not working for ANI and FS UUID on call sessions page.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.113.0 is scheduled for 1/4/2025 between 11:00pm and 12:00am US Central Time

This release prepares Edge deployments for Mongo upgrade from version 6 to 7.

New or changed functionality in the Transcribe App:
* BE-3226	TA: Add a title and heading to LLM Page.
* BE-3229	TA: Disable invoices button if there are no invoices available
* QA-2045	TA: When no speaker is present, the dropdown now displays the text 'No speaker present' under project creation

New or changed functionality in other platform components:
* BE-3220	Add comfort noise to AIVR lua app
* BE-3137	Added consecutive mode to GET /sa/call
* BE-3240	ASR API now return urls with local host names and ports for internal requests
* BE-3186	Populate fields in the markers field after a call is completed
* BE-3188	Remove inactive login sessions faster
* BE-3206	SA/TA: Better design for PII Redaction settings
* BE-3255	SA: Add a card that shows time distribution of various parts of the call
* QA-2052	SA: Add a search box for selecting the time zone under account settings.
* BE-3215	SA: Add search on Time Zone selector
* BE-3269	SA: Add sorting to the lists of values in Filters for Advanced Search
* BE-3230	SA: Implement the call-section marking - audio line
* BE-3258	SA: In the Call Detail view on Debug page show the date when the call will expire
* BE-3253	SA: Mark sections of the call also on the timeline of the expanded audio view
* BE-3233	SA: New icons for Inbound Call and Outbound Call
* BE-3234	SA: On Call Detail Debug page show a link to the AIVR Session in Web Console
* QA-1989	SA: On Calls page - improved data range selector
* BE-3201	SA: Replace Topic Cloud with a pie/bar chart showing topics
* BE-3283	SA: Support for phrase text queries in Advanced Search
* BE-3237	Speed up the agent stats API
* BE-3286	Web Console: Added clarification about formatter applicability to different transcription modes
* QA-2004	Web Console: Added success message when creating a GREG Grammar
* BE-3235	Web Console: Changes on AIVR session page: 1) obtain name from session, 2) add link to SA call details
* BE-3243	Web Console: Improved ASR settings
* BE-3146	Web Console: Improve look of the User profile page
* BE-3254	Web Console: On the Context page make the languages the 1st column under ASR Transcription/Recognition grouping
* QA-1982	Web Console: Remember selected column fields so that they survive page refresh
* QA-2028	Web Console: Validate IP Address entered for IVR Proxy download

Changes related to Integrity of Processing (fixes):
* BE-3250	Copilot: Fix - Refresh of the Pusher button does not work - but logout and login back works
* BE-3252	Fix - Call-stats method sometimes fails with 500 error
* QA-1999	SA: Fix - Call Center ID filter is not working in advanced search filters.
* QA-1919	SA: Fix - Demo Calls are not generating in Demo calls in PROD.
* BE-3214	SA: Fix - Gender and Word Cloud toggles do not work
* BE-3212	SA: Fix - Mood selection does not work
* BE-3259	SA: Fix - Sorting Calls by VB Transfer does not work
* BE-3213	SA: Fix - Tooltip on NER behavior weird
* QA-2011	TA: Fix - Downloading audio file with text file issue
* QA-2046	TA: Fix - Microphone capture: The transcript scrollbar is overlapping with the start time.
* QA-2064	TA: Fix - Zoom Meeting Bot is not working properly as it is failing even after joining a Zoom meeting.
* BE-3261	TA: Fix speaker activity detection in Webex Meeting Bot if screen is being shared
* QA-1952	Web Console: Fix - "Clear Filters" button is missing in Console log Filter section
* BE-3185	Web Console: Fix - Collapsed LH menu icons are identical for many items
* QA-2058	Web Console: Fix - Password Change button should disable after first click it should not invoke two calls
* QA-1958	Web Console: Fix - Sorting of 'Business Configuration' is not working as expected
* QA-2017	Web Console: Fix - Unable to change the speed of the transcript.
* QA-2065	Web Console: Fix - Unable to download transcript under Transcribe+(beta) getting 403 (Forbidden) error.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.112.0 is scheduled for 12/06/2024 between 12:00am and 1:00am US Central Time

This release upgrades Mongo on Edge from version 5 to 6.

**Key changes related to the core APIs**
* Improver Web Console UI.
* /sa/call API supports call event marking which is utilized in the SA App to highlight various parts of the call
  * NOTE: there is a known issue with the offset for the markers being somewhat off - this will be fixed in a patch
* API for outbound calling that is used by Copilot
* Copilot User may request Call Notes generation after internal transfer

New or changed functionality in the Transcribe App:
* QA-1628	TA: Search functionality provided for Admin users when they delete any other user and transfer their projects to another user.
* BE-2934	TA: Improved design of the Webhook Settings.

New or changed functionality in other platform components:
* BE-3173	Add markers field to /sa/call
* BE-3199	Added ignore_early_media parameter to POST /aivr/dial/{destination}
* BE-2320	AIVR sessions will expire (using expiry period from AIVR App).
* BE-3149	API that will be used to launch outbound call from the Copilot
* BE-3197	Avoid storing null values under trace in each ivr_session document
* BE-3204	Flag as error sa calls that will never recover from pending status
* BE-3189	Implement the call-section marking
* BE-3117	Improve performance of /sa/call-stats
* BE-3202	In redaction, modify partial masking algorithm to always do a full mask if we have 4 or fewer digits total
* BE-3161	Mark Meetings stuck in Processing as Error within 6 hours
* BE-3109	Migrated Mongo 5 to Mongo 6 on Edge.
* BE-3156	Modify account creation code to not create grafana org if type=SPEECH-WORKS
* BE-3123	New API that can be invoked from Copilot that Agent can use to indicate transferred calls, so that Call Notes are generated and pushed.
* BE-3021	Outbound Calling from Copilot with call submitted to SA App Project
* BE-3186	Populate fields in the markers field after a call is completed
* BE-3159	SA: Add "VB Transfer" column
* BE-3203	SA: Add indicator for Fields data still loading
* BE-3163	SA: Added a filter on Call Center Call Id
* BE-3164	SA: Added more quick time period selectors for the calls
* BE-3165	SA: Do not set sorting on the search query if query includes TxtSearchTerm
* BE-3205	SA: Improved Tag editing
* QA-1874	SA: More compact columns in the Calls table
* BE-3154	SA: New design for the Keyword settings
* BE-3125	SA: New SA project type - Generic Project
* BE-3162	SA: On Call Details page show the time of the call including seconds
* BE-3158	SA: Reduce the width of columns by shrinking displayed content and headers
* BE-3201	SA: Replace Topic Cloud with a pie/bar chart showing topics
* BE-3176	SA: Show playback position and total time in audio player
* BE-3178	SA: Show Word Cloud
* BE-3193	Store only top 100 words for WordCloud on the /sa/call
* BE-2899	User records that have never been activated are actually deleted by DELETE api
* BE-3184	Web Console: Added "Last Deployment Date" column to table of Edge deployments
* BE-3198	Web Console: Added shortcut from app name in call session to the app definition
* BE-3181	Web Console: Added UUID column to the table with Contexts
* QA-1942	Web Console: Allowed User to enter time manually rather bound to select 'Open' and 'Close' time from clock selection in Business Configuration
* QA-1988	Web Console: Better error messages in case of uploading bad grammar to GREG
* BE-3216	Web Console: Improved Mode Switcher
* QA-1984	Web Console: Improvements to Create GREG Question dialog
* QA-1985	Web Console: Improvements to Create new GREG experiment dialog
* QA-1616	Web Console: Move Transcribe+ from /sa API to /sa/offline API
* BE-2997	Web Console: Redesign of customer portal.
* QA-1998	Web Console: Switched Transcribe+ from /sa API to /sa/offline API
* QA-1981	Web Console: Trim spaces from entries into login form

Changes related to Integrity of Processing (fixes):
* BE-3166	Fix - /sa/call/search when instructed to search NOTES seems to be searching the transcript text
* BE-3168	Fix - aivrTransferDestType field on /sa/call does not seem to be populated
* BE-3192	Fix - Cases where /sa/call is missing /sa/offline session
* BE-3133	Fix - Hints in real-time word-for-word transcription mess up the results
* BE-3222	Fix - redis memory leak caused by EventBus in Services that were not consuming events (only sending)
* BE-3209	Fix - Unrecognized field "sessionDuration" during warm-transfer
* BE-3170	SA: Fix - Error loop due to expired nonces
* QA-1889	SA: Fix - In some cases call's transcript only recognizes the agent and fails to identify the caller and their dialogues.
* QA-2026	SA: Fix - Missing Tag Edit icon if call does not have any tags already
* BE-3175	SA: Fix - Selectable items in search Filters should be show closer together and they should be sorted
* BE-3183	SA: Fix - spacing between call id and search box
* QA-1930	SA: Fix - The same number should not be allowed for both ANI and DNIS fields during call upload.
* BE-3160	SA: Fix - Warm transfer audio (4 tracks) are incorrectly labeled
* BE-3174	SA: Fix how the IDs are displayed on hover
* QA-1931	TA: Fix - For accounts with OIDC enabled we should not show normal Signup page, instead we should show info about logging in with the OIDC creds.
* QA-1950	Web Console: Fix - CLEAR FILTER button not clearing text from input fields in GREG Experiment Browser
* BE-3180	Web Console: Fix - Context search is doing search also on date - it should search only Name
* QA-1965	Web Console: Fix - Date range handling on the Logs page
* QA-1949	Web Console: Fix - Experiment Browser Filter is not working
* QA-1971	Web Console: Fix - If the imported GREG Experiment file does not match the required format, the import button should be disabled.
* QA-1964	Web Console: Fix - Missing tooltips for the elements in the header
* BE-3172	Web Console: Fix - Referrer Policy for https://console.ascalon.ai
* QA-1972	Web Console: Fix - Search Reset behavior on User Management page
* QA-2002	Web Console: Fix - Unable to upload Grammar file for creating Grammar under MRCP ASR.
* BE-3157	Web Console: Fix AIVR App table width

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.111.0 is scheduled for 11/11/2024 between 11pm and 12am US Central Time

This release prepares for upgrade to Mongo 6 in 1.112.0

New or changed functionality in other platform components:
* BE-3136	Copilot: Acknowledge all messages received via Pusher back to Voicegain.
* BE-3130	Copilot: Added "Mark Call Transferred" button.
* BE-3082	Implement mechanism to delete recordings from FreeSWITCH after they have been uploaded for processing
* BE-3135	Implement POST /public/aircall/user/message-ack
* BE-3086	Implemented trace field on the AIVR session.
* BE-3123	New API that can be invoked from Copilot that Agent can use to indicate transferred calls, so that Call Notes are generated and pushed.
* BE-3126	SA: Added the JWT token generation/management features as we have in Developer Web Console.
* QA-1847	SA: Agents should not be allowed to edit PII Redaction in settings.
* BE-2950	SA: Enhance the visibility of un-selectable rows for the user in both dark and light modes.
* BE-3068	SA: Improve tag entry/edit - show existing tags already used within project.
* BE-3125	SA: New SA project type - Generic Project
* BE-3078	SA: Showing DTMF words in a distinct way in the Call audio timeline view.
* BE-2863	Separate fav-icons for each product.
* QA-1914	Web Console: Made Business Configuration UI user-friendly, so that users can manually enter the start and closing times.

Changes related to Integrity of Processing (fixes):
* BE-3145	Fix - Hints with apostrophes should be allowed to be set on a context
* BE-3114	SA: Fix - App may get into a loop
* QA-1908	SA: Fix - Checkboxes are overlapping on advanced search filter pop-up.
* BE-3035	SA: Fix - Credit card numbers are not being masked out in spite of NER redaction being turned on
* QA-1787	SA: Fix - Demo calls are not generating for Demo projects.
* QA-1909	SA: Fix - DNIS search is not working on calls page.
* QA-1910	SA: Fix - Getting "Sorry, there was an error." when using DNIS search.
* QA-1822	SA: Fix - Password reset button were not responding.
* BE-3113	SA: Fix - Sentry Integration for SA app as source-maps are not working for recent events.
* QA-1809	SA: Fix - The agent created during the upload is not appearing on the Agents page.
* QA-1813	SA: Fix - The owner is unable to edit their first and last name on the user page.
* QA-1935	SA: Fix - The save button should stay disabled until changes are made on configuration page.
* QA-1778	SA: Fix - Unable to access Demo calls getting "Sorry, there was an error! We were unable to download the call audio.
* QA-1934	SA: Fix - Unable to edit project configuration name in settings.
* QA-1927	SA: Fix - User is able to access integration page for Generic projects through left menu.
* QA-1921	SA: Fix - When the keywords field is empty, it overlaps with 'Average Handle Time'.
* BE-2973	TA: Enhance the visibility of un-selectable rows (User table).
* QA-1917	TA: Fix - 'Continue' button shouldn't be enabled if project name is empty at first time login after signup. 
* QA-1901	TA: Fix - Delete Device text is not translated in German, Spanish and Hindi languages.
* QA-1912	TA: Fix - Getting error while meeting Bot joining Webex meetings, "failed to join the meeting" even when the bots are present in the meeting.
* QA-1906	TA: Fix - If a user tries to forget the meeting, the message 'The Bot is not in the meeting' should also be translated into languages other than English.
* QA-1886	TA: Fix - Showing something went wrong page for the account setting.
* QA-1913	Web Console: Fix - New User Wizard were not working properly.
* BE-3131	Web Console: Fix - Removed hardcoded sensitivity setting from mic capture.
* QA-1915	Web Console: Fix - When the user tries to explore the left menu for the telephone bot API, the business configuration text is overlapping and hidden.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.110.0 is scheduled for 10/29/2024 between 11pm and 12am US Central Time

**Key changes related to the core APIs**
* Multiple improvements and fixes to the Speech Analytics App

**Key changes related to Transcribe APP**
* Improvements to the Webhook functionality
* UI improvements

New or changed functionality in the Transcribe App:
* BE-3075	TA: Added time-to-live (TTL) setting for the webhook JWT.
* BE-2983	TA: Check the Error Boundary implementation and catch all errors
* QA-1760	TA: Improved Profile page layout.
* QA-1721	TA: Provide way to identify Zoom, MS Teams or Webex meeting. 
* QA-1821	TA: Removed Edit Tag functionality for the shared transcript for both public and account share pages.
* QA-1851	TA: The password menu is available under the profile settings, so removed it from the "My Profile" menu.
* BE-2940	TA: Updated Transcribe App styles.


New or changed functionality in other platform components:
* BE-3074	Added jwtTTL parameter to Webhook API.
* BE-2966	Allow Managers to get results of advanced search POST /sa/call/search and GET /sa/call/search/fields
* BE-3101	Implement API to get all tags attached to /sa/calls in a given Context.
* BE-3086	Implemented trace field on the AIVR session.
* BE-2964	In the confGroup API throw Bad Request if someone tries to create a new confGroup without a name or with empty name.
* BE-2986	Made SpeechAnalyticsCallDao optional so that asr-api can start without it in CHD environment.
* BE-2978	Play audio while AIVR is making an outbound call triggered by warm-transfer.
* BE-3052	SA: Added "Resend Invite" in menu under account Users.
* BE-3039	SA: Added a cancel button in profile page.
* BE-3088	SA: Added dailyRepeatCalls to API - /sa/calls
* BE-3102	SA: Added filter for DNIS and a search for ANI.
* BE-3073	SA: Added hours:minutes to the date filter in Advanced Search.
* QA-1881	SA: In the login page, "Email Address" text is overlap on error message or pending approval message.
* QA-1854	SA: Introduced option to delete "Examples", "Keywords" and "Entity".
* BE-2938	SA: On Users table added filtering by Role.
* QA-1766	SA: The status filter should function like the role filter, using predefined values instead of working like email filter on the Users page.
* BE-3077	SA: Time-query to the back-end from the Advanced Search should use UTC.
* BE-2863	Separate fav-icons for each product.
* QA-1852	Web Console: Added maximum length limit validation for Business Configuration name.
* QA-1827	Web Console: Added pop-up/ alert message appears when edit a user in User Management.
* BE-2976	Web Console: In Phone number table, added a filter on Status column. 
* BE-2981	Web Console: In the AIVR App list, if the App has many phone numbers, then wrap them over multiple lines.
* BE-3049	Web Console: In the Call Sessions page, DNIS column is now sorted in ascending order.
* QA-1839	Web Console: Prevent Duplicate Shortcut Keys to Avoid Interference with Audio Playback.

Changes related to Integrity of Processing (fixes):
* QA-1768	Admin Portal: Fix - Special characters and numbers are accepted in the "First Name" field.
* BE-3096	Fix - Newly created Contexts from Web Console get type Transcription.
* BE-3093	Fix - Syntax error in tsquery
* BE-2944	Fix/Modify how we match names of meeting participants to the names obtained from Zoom API.
* QA-1765	SA: Fix - Agents and Manager are able to access Users and Time setting page via URL manipulation.
* QA-1802	SA: Fix - All demo calls are failing in processing and returning an error.
* QA-1739	SA: Fix - ANI and DNIS fields in upload file should not accept characters as inputs.
* QA-1840	SA: Fix - Call ID icon is overlapping with filter selector on Advanced search page.
* QA-1888	SA: Fix - Call Time Breakdown in Call Overview is not showing for uploaded call with single channel.
* QA-1855	SA: Fix - Calls tables column header and cell data are not aligned properly [1920 X 1080]
* QA-1873	SA: Fix - Color inconsistency in delete project modal.
* QA-1789	SA: Fix - Debug page is not clearly visible in Dark theme in call details.
* QA-1850	SA: Fix - Direction filter shows is not working properly.
* BE-3083	SA: Fix - Filter dates are reported in wrong format.
* QA-1804	SA: Fix - PII Redaction feature not working.
* BE-3100	SA: Fix - PII redaction in /sa/offline does not redact audio.
* QA-1849	SA: Fix - Resolution field column is missing from calls table.
* QA-1825	SA: Fix - The agent created during the upload is not appearing in the Agent filter on Advanced search page.
* QA-1880	SA: Fix - The country flag icons are not showing up in the ANI and DNIS fields during call uploads.
* BE-3095	SA: Fix - The date range component doesn't work in Chrome.
* QA-1857	SA: Fix - User should not be allowed to create two projects with same name.
* BE-3006	SA: Fix - Weird chars on the Calls list pagination.
* QA-1836	SA: Fix - Wrong pop-up msg on copying Voicebot ID.
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
* QA-1869	Web Console [Edge]: Fix - Showing Transcribe App projects as context on the customer portal and user can also delete the projects.
* QA-1700	Web Console: Fix - A vague error occurs when trying to upload files with long names.
* QA-1870	Web Console: Fix - Creating a new context and switching to the other context shows a type error page on the customer portal.
* QA-1859	Web Console: Fix - Creating a new context on the customer portal displays a type error and shows a blank page.
* QA-1853	Web Console: Fix - 'Open' and 'Close' time can't be same time of 'Normal Opening Hours' in Business Configuration.
* BE-2980	Web Console: Fix - Sorting of the Phone Numbers by App name does not work.
* QA-1897	Web Console: Fix - The Change Password page UI has layout and alignment issues.
* QA-1882	Web Console: Fix - User is unable to select a time for "Open time" if "Close time" is not set
* QA-1904	Web Console: Fix - When a user hover at billing label in header section, no cursor:pointer


All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Maintenance release 1.109.1 is scheduled for 9/29/2024 between 11pm and 12am US Central Time

New or changed functionality in platform components:
* BE-3088	Add dailyRepeatCalls to /sa/calls
* BE-3011	Add dtmfEvents field to /sa/call
* BE-2968	Add fallback in case of Azure TTS issues
* BE-2877	Added new variable in /sa/call that stores the type of transfer - Internal, Agency, None.
* BE-3087	Additional fields added to the Pusher messages to be sent to Copilot
* BE-2966	Allow Managers to get results of advanced search POST /sa/call/search and GET /sa/call/search/fields
* BE-3065	API for text redaction POST /text/redact
* BE-2961	API introduced to get Zoom Server API access_token.
* BE-1820	Ascalon-cleanup to support removing expired sa_offline sessions.
* BE-2957	At the end of the AIVR session, set language field of the /sa/call based on the language of the AIVR session.
* BE-2959	Copilot: If not logged in show message about need to login.
* BE-2974	Copilot: Implementation for updating co-pilot extension for Edge/Chrome browser. 
* BE-2985	Copilot: Improvements in settings page.
* BE-3016	If a call came from a provider then prepend to the GPT Call Notes the info about provider from Voicebot
* BE-3012	In /sa/offline obtained from /sa/call add DTMF values into the words returned
* BE-2958	In POST /sa/offline/call/{callId} use the language specified in /sa/call unless overridden by settings.asr
* BE-2944	Modify how we match names of meeting participants to the names obtained from Zoom API.
* BE-3015	New API method to modify sa call tags
* BE-2902	Poll URL returned from POST /asr/transcribe/async is a sticky url.
* BE-3010	Record DTMF detected in AIVR session
* BE-3023	SA: Add a direction column to call tables
* BE-3040	SA: Add Regex formatter to the PII Redaction settings
* BE-3064	SA: Add search functionality in Filters
* BE-2945	SA: Added ANI and DNIS to the Call table and Advanced Search table
* BE-2941	SA: Added callCenterCallId to /sa/call and set it from aivr session aircallId.
* BE-2956	SA: Added language field to /sa/call.
* QA-1730	SA: Added spinner when deleting admin user to show admin user is being deleted.
* BE-2936	SA: Added status of the Users in the Users Table.
* QA-1732	SA: Added user's role in the profile section.
* BE-3000	SA: Browser-specific text on the extension download page
* BE-3057	SA: Change the number of calls retrieved on the Calls page to max 1000
* BE-3022	SA: Consistent ANI/Dialed Number and CLI/DNIS naming
* BE-2939	SA: If no sentiment value is returned from the API we are showing "N/A" along with icon/emoji.
* QA-1751	SA: Improved design for Agents & Agents Detail page.
* BE-2954	SA: In Call Details added a Debug page that is visible to the Admins.
* BE-3070	SA: Increase the limit for number of calls in the Export query from 1000 to 2000
* QA-1752	SA: Made company details in profile read-only for Manager 
* BE-2962	SA: New design introduced for Agent pages.
* BE-3044	SA: Remember number of items per page setting till user modify.
* BE-2999	SA: Show callCenterCallId in the Call in Calls list
* BE-3013	SA: Show DTMF words in a distinct way in the Call transcript view
* BE-3014	SA: Show tags and allow adding new or editing existing ones
* BE-3027	SA: Show the next/prev buttons also on a call details page that is in processing right now
* BE-2652	Sync AIVR session with Aircall callId at transfer
* QA-1693	TA: If the number of speakers exceeds the expected amount, providing a scroll bar. This will not affect the transcript view.
* BE-3017	Web Console: Add a refresh button on the AIVR Call Session Details page
* BE-3004	Web Console: In AIVR session list, remove Version column, and add IVR Sid and FS UUID columns - both searchable
* BE-3048	Web Console: In the Call Sessions page, On the ANI column, instead of a Selection Filter we will have Search option.

Changes related to Integrity of Processing (fixes):
* QA-1734	Demo: Fix - For Long transcripts- text were overlapping with buttons.
* QA-1735	Demo: Fix - Typography issue on the demo healthcare call details page.
* BE-3043	Fix - Bad Event Bus configuration causing some events being dropped
* BE-3041	Fix - Did not report Queue and Agent in /sa/call
* BE-2991	Fix - Enforce non-empty name on Contexts in a correct way
* BE-3045	Fix - GET /aivr-app/uuid/jwt fails to return JWT tokens using authToken in some cases
* BE-2996	Fix - GET /asr/transcribe/uuid/transcript returns 500
* BE-2987	Fix - Glitch in business operating hours/days
* BE-3024	Fix - Issue with ascalon-asr-api starting on Edge deployment (specifically smopqa)
* BE-2780	Fix - netty.io Buffer leak in Java FreeSWITCH ESL library
* BE-3061	Fix - NPE when reading IvrSession.Recordings from Firestore
* BE-2943	Fix - NullPointerException in Aircall webhook
* BE-3058	Fix - Phone number formatter StringIndexOutOfBoundsException
* BE-3003	Fix - PII redaction does not work for /sa/offline transcript
* BE-3009	Fix - Real-time transcript possibly available too late for Call Notes
* BE-1366	Fix - RedisConnectionException: Issues with Redis Marshalling Codec
* BE-3020	Fix - Some Voicebot calls that get transferred end up in Disconnect instead of Hangup
* BE-3060	Fix - START-INPUT-TIMERS is sent to Rex right after RECOGNITION-COMPLETE is received
* BE-3050	Fix - The Users that we create when saving /sa/calls that have Agent data, do not have accountId
* BE-3066	Fix - Voicebot to Aircall call transfer handshake error.
* BE-2953	Fix - Voicegain call incorrectly matched to data from Aircall.
* QA-1784	SA: Fix - Admin account user is able to change Owner account user's role.
* BE-3047	SA: Fix - Advance search is not working for ANI/Dialed Number
* QA-1740	SA: Fix - After successfully deleting a user through the checkbox, another user gets selected. 
* QA-1761	SA: Fix - Agents and Manager should not delete project created by Admin.
* BE-3018	SA: Fix - Download from Advanced Search does not use the same max calls setting as the search
* BE-3037	SA: Fix - If we are using a 12 hour format we should show AM/PM in the time displayed
* BE-3046	SA: Fix - Need to access next/previous call transcript, if there is no call audio available.
* QA-1753	SA: Fix - No calls are showing on Advanced search page getting 500 (Internal Server Error).
* QA-1769	SA: Fix - Placeholder text does not disappear when the user enters data.
* QA-1831	SA: Fix - Sorting is not working for ANI and DNIS fields on Calls and Advanced search page.
* QA-1698	SA: Fix - The Call's Overview page is not responsive when zoomed in, causing text to overlap.
* QA-1706	SA: Fix - The Queue option in the file upload under Integration displays duplicate entries.
* BE-3076	SA: Fix - The search query in the Advanced Search Page should by default include sort by date so that most recent calls are retrieved first
* QA-1738	SA: Fix - Unable to delete multiple users when there are admin users among them.
* QA-1528	SA: Fix - When a user uploads a corrupted audio file, an error message repeatedly appears.
* QA-1157	TA Edge: Fix - For some audio URL showing something went wrong issue.
* QA-1800	TA Edge: Fix - Meeting Minutes missing
* BE-2951	TA Edge: Fix - Projects returned from the back-end are ignored. 
* QA-1723	TA: Fix - "Meeting Minutes" string  should not appear two times.
* QA-1708	TA: Fix - [Dark Theme] When the owner attempts to rename the transcript, the cancel icon is not visible.
* QA-1717	TA: Fix - After file uploading, the 'File uploaded' text weren't translated. 
* QA-1757	TA: Fix - Edit transcript icon overlapping with the transcripts name.
* QA-1701	TA: Fix - Hindi translation in "Delete Transcribe" pop-up.
* QA-1707	TA: Fix - Made Phrases visible for the dark theme.
* QA-1716	TA: Fix - Meeting Bot Placeholder text translation according to selected language.
* QA-1709	TA: Fix - No space between "Timezone" text and the dropdown box border.
* QA-1702	TA: Fix - Time zone pop-up was hiding the left menu.
* QA-1724	TA: Fix - When owner unable to join meeting bot receive "Failed to join meeting" string was not translated as per selected language.
* QA-1663	TA: Fix - When the Hindi language is selected, the 'Apply' button overlaps with the participants dropdown on the advanced search page.
* BE-2984	Web Console: Fix - Timezone prompt not taking spaces as input
* QA-1685	Web Console: Fix - When admin try to create "Add broadcast websocket" receive 400 bad request error.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Minor release 1.109.0 is scheduled for 9/17/2024 between 12am and 2am US Central Time

**Key changes related to the core APIs**
* Added Webhook API (phase 1)
* UI redesign for the Speech Analytics App
* Speech Analytics app now supports Warm Transfer scenario
* Copilot Browser Extension for Agent Assist

**Key changes related to Transcribe APP**
* Support Webhook API (phase 1)
* Added third set of LLM service settings and add model name field to all 3 LLM services.
* Including transcript metadata together with transcript when using LLM to generate meeting minutes items.
* Improved reliability of the Meeting Bot on longer meetings

New or changed functionality in the Transcribe App:
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

New or changed functionality in other platform components:
* BE-2856	Add Korean (ko) as one other possible value of switchLanguage in AIVR callback response.
* BE-1043	Add secure SIP and RTP to freeswitch.
* BE-2450	Added ability to obtain temporary JWT token from AIVR session using authToken
* BE-2891	Added metadata value to the speakers field in API /sa/offline
* BE-2714	Added new Group of items sent to Aircall as Caller Insight.
* BE-2843	Added originatingCallId and spawnedCalls to API - /sa/call
* BE-2819	Added processing status to API -  /sa/call
* BE-2226	Added Webhook Notification APIs.
* BE-2896	Adding in API - /sa/call an Agency tag, If AIVR inbound call is an Agency call (warm transfer bridged).
* QA-1633	Admin Tool: Updated Terms and Conditions page.
* BE-2832	API - /public/aircall/user-check used to check if user info matches data in Aircall.
* BE-2904	Copilot: Create a web interface to host the .crx download links
* BE-2884	Copilot: Implemented override of the Intent by Agent.
* BE-2861	Copilot: Implemented the Login.
* BE-2888	Copilot: Remove the dev/qa/prod selector and /dev/qa indicators.
* BE-2847	Copilot: Show Intent card with Agency Transfer data.
* BE-2876	Edge: If Action Items LLM prompt is not defined, then do not generate Action Items at all.
* BE-2897	For real-time transcription sending metadata over results websocket, also every time metadata is added/modified.
* BE-2886	Generate full call notes for the agency call that was bridged to the caller (not transferred to Aircall)
* BE-2826	Handling 2x2 audio channels from warm transfer call in API - /sa/offline.
* BE-2824	Improved design of Copilot.
* BE-2825	In AIVR session allowing for caller id to be any of the secondary phone numbers attached to the AIVR App.
* BE-2889	Included aivr_authToken and aivr_sessionId variables when pushing the AIVR Voicebot variables to the Copilot.
* BE-2787	INVALID_ARGUMENT: Sample rate must be empty or 24khz for this voice.
* BE-2929	Log the response payload from the Zoom API method that gets info about Zoom Meeting participants
* BE-2320	Make AIVR Sessions expire (use expiry period from AIVR App)
* BE-2928	Make sure that all calls in SA Demo project have progressPhase=DONE
* BE-2775	make sure that user deletion does not fail if context deletion takes too much time
* BE-2854	Modifications to llmSettings field (introduced premiumLlmService) on the onPrem cluster API.
* BE-2710	New version of the Sidepanel (Copilot Browser Extension) that integrates with Aircall.
* BE-2892	Populate speaker metadata in API - /sa/offline/call/{callId}
* BE-2844	POST /sa/offline/call/{callId} need to be able handle calls with spawnedCalls (from warm transfer).
* BE-1366	RedisConnectionException: Unable to init enough connections amount! Only 0 of 24 were initialized. 
* BE-2829	Return 400 Bad Request if someone tries to create a new AIVR App or assign a phone to existing App if the phone is not available.
* QA-1695	SA : Highlighting any calls that had error in processing
* BE-2885	SA: Added a Export button for the Advanced Search Results.
* QA-1623	SA: Added limit of 1024 characters against description under General settings. 
* BE-1796	SA: App should be customisable per account.
* BE-2808	SA: Enabled currency formatting for /sa/offline in AIVR sessions.
* QA-1587	SA: Enhancement - Downloaded call transcript should have Call ID as name instead of timestamp.
* BE-2933	SA: For call overview, render in processing page rather error page if call is in progress.
* BE-2704	SA: For the call sessions that are being processed, adding a subtle overlay that says processing
* QA-1695	SA: Highlighting any calls that had error in processing
* QA-1533	SA: Optimized call page & made fields small enough to fit all data without scrolling.
* QA-1690	SA: Provide correct information for Aircall Integration
* BE-2818	SA: Redesign of Speech Analytics App UI
* BE-2916	SA: Show first and last name in the user table
* BE-2862	SA: Showing more than 2 channels in the SA Call Detail view if present.
* BE-2907	SA: UI changes to implement the new design
* BE-2879	Setting ANI correctly on calls coming from AIVR Voicebot to Aircall.
* BE-2881	Submitting tags to Aircall when doing the call handshake between AIVR and Aircall.
* BE-2728	support auto-reconnect if fssk loses connection to Freeswitch
* BE-2836	Supporting Korean Prompt in telephony bot and in audio server.
* BE-2883	Taking the Voicebot intent and insert it into /sa/offline and /sa/call.
* BE-2880	Updated Advanced Search API - /sa/call/search  to return results in CSV format.
* BE-2859	Use premium LLM Service with the new LLM Query logic and use standard with the old LLM Query logic.
* QA-1536	Web Console: Added popup after adding or deleting a user under User management.
* QA-1540	Web Console: Added popup for deleting a WebSocket under Live Broadcasting.
* BE-2001	Web Console: Notify about inability to to microphone capture on HTTP urls.
* BE-2830	Web Console: Remember last items per page setting on the Call Sessions page.
* BE-2831	Web Console: Remember the last value of items-per-page setting on the Phone Apps page.

Changes related to Integrity of Processing (fixes):
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
* BE-2809	Fix - Bad currency formatting for thousands plus
* BE-2722	Fix - Bot logic doesn't get input callback if the caller hangup immediately after saying something.
* BE-2436	Fix - In meeting Join if the pod/puppeteer leaves the meeting because it is not progressing there is no info about that event
* BE-2814	Fix - MS-Teams puppet bot were not terminating if the meeting gets ended.
* BE-1354	Fix - NatsEndpoint fails to reconnect to NATS when its connection is lost
* BE-2869	Fix - Not working error prompt in telephony-bot LUA
* BE-2927	Fix - Pusher sending DNIS instead of the ANI
* BE-2663	Fix - Several calls where the merged meeting audio is missing a speaker.
* BE-2923	Fix Demo Prod
* BE-2913	SA: Fix - Agent and Caller labels are incorrect
* BE-2918	SA: Fix - Call Transcript page failing in case of single speakers
* QA-1699	SA: Fix - Exports in advanced search is not working with filters.
* QA-1686	SA: Fix - Getting error on Call's Transcript page.
* QA-1733	SA: Fix - Issues when Agent/Manager user try to edit/delete Admin user.
* BE-2915	SA: Fix - New User Dialog starts with values of the previously created user
* BE-2917	SA: Fix - Save button not activated for all values on Profile page
* QA-1729	SA: Fix - Selected duration is not shown in applied filters in advanced search page.
* BE-2898	SA: Fix - Spinning forever if the /sa/call has no saSesisonId.
* BE-2898	SA: Fix - Spinning forever if the /sa/call has no saSesisonId.
* QA-1719	SA: Fix - The added user role changes to "User" even if a different role was assigned while inviting.
* QA-1725	SA: Fix - The calls continue to load and display an error icon when hovered over, but the call itself is still accessible.
* QA-1622	SA: Fix - Timestamp interval dropdown have values that are more than transcript runtime.
* BE-2914	SA: Fix - Unable to add Admin Users
* QA-1710	SA: Fix - Unable to edit role of user under Profile users.
* BE-2926	SA: Fix - User Edit dialog has just First Name and it does not even populate it
* QA-1596	SA: Fix - User is unable to modify AIVR app getting "400 Bad Request".
* QA-1687	SA: Fix - User is unable to upload file under Integration section.
* QA-1528	SA: Fix - When a user uploads a corrupted audio file, an error message repeatedly appears.
* QA-1535	Web Console: Fix - Audio URL field box is too small.
* QA-1625	Web Console: Fix - For Phone Management, clickable area is too small. 
* QA-1571	Web Console: Fix - Logs - When a user tries to filter logs, filter not working.
* BE-2908	Web Console: Fix - Phone number deletion from AIVR App does not work
* BE-2813	Web Console: Fix - Playback timeline cut off after the last word.
* QA-1509	Web Console: Fix - 'Speed and Audio' control panels should be in proper size.
* QA-1392	Web Console: Fix - When we click the back button more than once, the time interval goes to minus and after that the video pauses.

All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.

### Maintenance Window is scheduled for 9/15/2024 between 10pm and 12am US Central Time

Next Sunday, September 15th between 10pm and midnight Central Time a maintenance window is scheduled during which Voicegain **APIs may be unavailable**.
This is to reconfigure Voicegain Google Cloud setup to improve High Availability.

### Minor release 1.108.0 is scheduled for 9/2/2024 between 10pm and 12am CDT

**Key changes related to the core APIs**
* More accurate offline transcription model
  * Removed artifacts from training data
  * Added additional Call Center data to training set
* Finalized warm transfer support in Telephony Bot API
* Support for pushing Voicebot data and Call Notes to Copilot

**Key changes related to Transcribe APP**
* Cloud only: Major improvement to capabilities of LLM Query
* Major makeover of the look of the UI
* Added UI dark mode
* Added Configurable Meeting Minutes (via LLM prompt)
* Added tracking of LLM tokens (in the Cloud)
* On Edge: Added ability to retrieve speaker data (incl. email) using Zoom API


New or changed functionality in the Transcribe App:
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

New or changed functionality in other platform components:
* BE-2758	Add codec restrictions to the dial string for outbound
* BE-2045	Add to AIVR API subReturn action.
* BE-1782	Added Copilot Call Notes support.
* BE-2777	Added info about LLM tokens to GET account new-billing method.
* BE-2698	Added information regarding Member being Verified to the Call Notes
* BE-2695	Added realTimeTranscriptText to AIVR Session and store the transcript from real-time transcription in it.
* BE-1757	Added required features for Inbound Bot.
* BE-2821	Added secondary voice connector id to AIVR App api.
* BE-2768	Added speaker email value in the meeting data (ASR Meeting API)
* BE-2404	Added support for language switching in telephony bot.
* BE-1761	Added to AIVR API warmTransfer action.
* BE-2767	Added to Edge Configuration parameters for connecting to Zoom Service.
* QA-1319	Admin Tool: Added email validation on add account page.
* BE-2657	Admin Tool: Convert API Use chart to chart-js
* BE-2114	Check if we are within phone number quota on AWS before creating a new one
* BE-2749	Check Voice Connector number against quota before creating a new one.
* BE-2765	Demo: Collect events to Matomo from the voicebot part of the demo
* BE-2761	For confGroups of type other than Transcription do not delete them if the creator is deleted
* BE-2726	Get available information about participants of the specified Zoom meeting.
* BE-2776	Grouping segments by meeting and attaching meeting metadata for /asr/meeting/llm/query
* BE-2712	If the rex sessions are stuck (in error) do not count them towards the live session count during shutdown
* BE-2759	If user deletion fails for any reason, we should still audit log it.
* BE-2737	In AIVR, send vg::sub-return Event to Lua script (Freeswitch)
* BE-2799	Introduced wew llmSettings.prompts for Meeting minutes.
* BE-2733	Push data from Aircall Integration to the Copilot.
* BE-2754	SA: Add extra confirmation before deleting a user who has the Admin role.
* BE-2678	SA: Added API - GET /sa/offline/{id}/transcript 
* BE-2713	SA: Added context to the return values from GET /sa/call/agent
* BE-2703	SA: Added contextId to the request for /sa/call
* BE-2677	SA: Added download ability to the transcript view.
* QA-1427	SA: Added search feature to transcript page.
* BE-2689	SA: Addedd contextId to the GET /sa/call/{callId}
* QA-1534	SA: New project gets default time settings from the Account.
* BE-2774	SA: Supporting accounts with INVOICE billing on first login.
* BE-2697	SA: When submitting /sa/offline request to as part of SA AIVR Integration set correct formatting parameters.
* BE-2572	Send Caller Insight to Aircall as part of handling call.created webhook
* BE-2790	Set the non-Speaker email value in the meeting data.
* BE-2670	Transcribe App Client can get notified over websocket of any meeting join events instantaneously.
* BE-2732	Using Pusher to push information to the Copilot Browser Extension.
* BE-2736	Web Console: Added editable description to Edge Cluster
* BE-2622	Web Console: AIVR Sessions table show which sessions have SA integration.
* BE-2755	Web Console: Do not allow spaces in the names of AIVR Apps.
* BE-2696	Web Console: Show real-time transcript text in the AIVR session detail view
* BE-2747	Web Console: Showing AIVR App Id on the AIVR App detail drawer.
* QA-1472	Web Console: Unable to add second URL in logic when its name is same as first.

Changes related to Integrity of Processing (fixes):
* BE-2822	Fix - Can't play audio from URL in bot logic callback
* BE-2741	Fix - Duplicate data in meeting_vector database on Edge
* BE-2727	Fix - Error when leaving a meeting (meeting join API).
* BE-2721	Fix - Large vocabulary BUILT-IN grammar is not working in telephony bot
* BE-2760	Fix - Origination data is not properly set for a new Voice Connector.
* BE-2753	Fix - Outbound calling does not work anymore.
* BE-2204	Fix - Percolator stop request ignored if sent immediately after start
* BE-2806	Fix - The hidden checkbox stops working on ascalon TranscribeApp in some cases
* BE-2817	Fix - Voice Connector quota check is not working OK
* BE-2752	Fix - voiceConnectorId is not set on AIVR App if a phone gets added to AIVR App that did not have any phone
* BE-2700	Fix - Weird Agent Composite values for the Demo Project /sa/calls
* BE-2766	Fix prompt for Action Items.
* BE-2729	Fix the shutdown of ascalon-asr-api
* BE-2773	SA: Fix - Clicking on Terms of Service during SA Signup messes up signup
* BE-2550	SA: Fix - Incorrect default time in file upload.
* BE-2595	SA: Fix - JWT is not automatically inserted into the selected AIVR App.
* QA-1475	SA: Fix - Pagination on Users page looks weird.
* QA-1531	SA: Fix - Queue filter in Advanced search is not working for Uploaded file.
* QA-1474	SA: Fix - Score filter is still available in advanced search even when score has been removed.
* QA-1373	SA: Fix - The Continue button should remain disabled until all mandatory fields have been filled out.
* QA-1541	SA: Fix - The login button should remain disabled until all required fields are filled.
* QA-1437	SA: Fix - The role "Coach" is displayed as "QA" after being saved in Users.
* QA-1480	SA: Fix - Unable to clear the description in General settings.
* BE-2701	SA: Fix - undefined:undefined on the Topic chart
* QA-1476	SA: Fix - User deletion is not working properly.
* QA-1467	SA: Fix - User is able to set Persistence time more than 365 days in AIVR app.
* QA-1446	SA: Fix - When a user goes back, they are redirected to the calls page instead of the Advanced Search.
* BE-2699	SA: Fix - When I add a new keyword the dialog opens prepopulated with the name of the previous keyword I created
* QA-1525	TA: Fix - Accepting only digits in the domain name for the "Allow signup with emails from the following domains:" field.
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
* BE-2828	Web Console: Fix - AIVR App creation allows you to pick phone numbers that are not yet ready for use.
* QA-1425	Web Console: Fix - Double error showing when phone number purchase.
* BE-2716	Web Console: Fix - Error page when trying to open AIVR session details.
* QA-1513	Web Console: Fix - Transcript play time exceeds than actual time when playback speed increases.
* QA-1575	Web Console: Fix - User is unable to Logout properly.
* QA-1483	Web Console: Fix - User Management Search - When user searches with leading or trailing whitespace with email then no results come.
* QA-1526	Web Console: Fix - When user switch context on Profile page then 2FA pop-up keeps showing each time context is changed.



All changes affecting Security, Availability, Integrity of Processing, Confidentiality, Privacy are reported as such above. If nothing is reported in the specific category then it means there were no such relevant changes in this release.


