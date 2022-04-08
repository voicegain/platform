### Minor release 1.54.0 is scheduled for 4/11/2022 between 6:00pm and 10:00pm CST

This release includes:
* Edge deployment improvements:
  * Support for external S3-compatible object storage
  * Support for SSL Certificates
  * Configurable Grafana Dashboard for visualizing API use 
* Other improvements:
  * beta version of new /asr/meeting API suitable for transcribing per-speaker audio from e.g. a Zoom Meeting 
  * Faster offline transcribe, including optimized pipeline for audio coming from S3 (or other external URL)
  * Improved English acoustic model (offline mode) - about 1.5% better accuracy on meeting / lecture type of audio
  * Beta version of a German offline acoustic model
  * Language settings in the Web Console improved - only acoustic models compatible with a selected language are shown
  * Added profanity masking option to the Transcribe Dialog

Backwards incompatibility:
* the `reuse` parameter in the /data API will now be ignored - each POST request will create a new Data Object

Fixed issues:
* #rcj-484: better error handling for Fusebill
* #rcj-496: audio redaction no longer works for mono audio

### Maintenance release 1.53.3 is scheduled for 3/21/2022 between 6:00pm and 10:00pm CST

This release adds:
* improved food-kappa model 

This release fixes the following issue:
* #rcj-488: spanish offline transcription ignores languages defined in the associated context

### Maintenance release 1.53.2 is scheduled for 3/17/2022 between 6:00pm and 10:00pm CST

This release adds:
* Choice of 4 high quality TTS voices in Indian English (en-IN)

This release fixes the following issue:
* #rcj-486: support using context.asrSettingsRecognition.acousticModelRealTime for Rex resource reservation for AIVR sessions if present

### Maintenance release 1.53.1 is scheduled for 3/16/2022 between 5:00pm and 10:00pm CST

This release addresses the following issue:
* #TranscribeApp-338: Fix countries images icon at Transcribe App - Acoustic model selection

### Acoustic Model VoiceGain-rt-en-us no longer available

With Release 1.53.0 the Acoustic model named `VoiceGain-rt-en-us` is no longer available. If you still use it in your API requests you will get "Resource available error". Please replace references to it with `VoiceGain-kappa`.

### Minor release 1.53.0 is scheduled for 3/15/2022 between 6:00pm and 10:00pm CST

This release includes:
* Telephony Bot API uses a more efficient method to stream audio to the recognizer. The response latency has been reduced a bit.
* Model selection mechanism has been changed. A single Acoustic Model can now support multiple languages; therefore, we added a extra language parameter that can be provided together with a model name.
* MRCP ASR now supports a dual language mode - it is possible to do recognition not knowing what language is spoken. Currently, only en/es combination is available.
* Profanity masking has been added to the Transcribe API
* In Web Console - the audio display now shows milliseconds in tooltip and when zoomed in.
    

### Minor release 1.52.0 is scheduled for 3/4/2022 between 3:00pm and 6:00pm CST

This release includes:
* Browser Capture feature available in the transcribe app. This allows you to capture full audio of e.g. Zoom or MS Teams meetings.

This release addresses the following issues:
* #rcj-477: AIVR - attempt to play empty questionPrompt results in error (was re-opened)
* #rcj-475: Unable to listen to recordings of Telephone Bot API sessions

### Minor release 1.51.0 is scheduled for 3/3/2022 between 5:00pm and 10pm CST

This release provides the following more accurate models:
* English real-time (streaming)
* Spanish off-line

This release addresses the following issues:
* #rcj-477: AIVR - attempt to play empty questionPrompt results in error
* #rcj-476: AIVR -the last prompt in disconnect is not being played and the hangup is not done
* #rcj-474: REX returns incorrect long result for certain utterances in recent benchmark
* #vgp-833: The startTime field datatype is "String in the spec, but web-api returns integer
* #rcj-472: Get exception when submit silence to SA
* #rcj-470: Cannot GET SA transcript
* #vgp-830: DEL SA session and DEL SA config need to be in the public API spec
* #ocp-773: offline-process occasionally return empty result
* #vgp-831: "name" field should be required when creating SA config
* #rcj-469: attempt to get /sa results returns INTERNAL_SERVER_ERROR
* #ocp-770: diarization is not returned when audio is short

Two enhancements:
* Old and/or orphan data cleanup has been moved to separate task and made faster
* Time filter has been added to the GET /data query method  


### Maintenance release 1.50.1 is scheduled for 2/16/2021 between 11:00am and noon CST

This release fixes the following issue:
* #rcj-463: call duration reported from offline transcription to billing is 1/1000th of what it should be


### Support for ACH Payments

ACH payments are now available.

**Backwards incompatibility:**
* requests to `/asr/transcribe/async` API with `portal` field value but no `portal.label` specified will fail - `portal.label` is now a required value 









































 













































