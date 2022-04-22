### Maintenance release 1.55.1 is scheduled for 4/22/2022 between 11:00am and 3:00pm CST

This release fixes the following issue:
* #ocp-779: offline process returns NOINPUT for audio shorter than 1.25s

### Minor release 1.55.0 is scheduled for 4/19/2022 between 7:00pm and 10:00pm CST

This release includes:
* Web Console now supports Meeting view - for viewing transcripts from /asr/meeting API
* Alpha version of the Zoom Recorder utility is available upon requests - it captures individual audio of each Zoom Meeting participant and submits it for transcription to /asr/meeting API. It works both with Voicegain Cloud and Edge.
* Improvement to internal ml-svc request routing - previously in certain scenarios the requests to ml-svc service might end up going to just a subset of available pods thus reducing performance. 

Issues addressed:
* #rcj-522: GET /asr/transcribe/{uuid}/transcript fails intermittently
* #rcj-520: support replacing acoustic model(s) with languages
  * this is in place to accommodate older pre-1.53.0 style requests which reference names of acoustic models that no longer exists (have been merged into model bundles)
  * new style requests should use `languages` parameter which is sufficient in most cases

### Maintenance release 1.54.1 is scheduled for 4/18/2022 between 11:15am and 2:00pm CST

This release partially addresses the following issue:
* #rcj-517: old/expired data cleanup inefficiency

### Minor release 1.54.0 is scheduled for 4/11/2022 between 4:00pm and 10:00pm CST

This release includes:
* Edge deployment improvements:
  * Support for external S3-compatible object storage
  * Support for SSL Certificates
  * Support for Kubernetes clusters with no GPU
  * Configurable Grafana Dashboard for visualizing API use 
* Other improvements:
  * Beta version of new /asr/meeting API suitable for transcribing per-speaker audio from e.g. a Zoom Meeting 
  * Beta version of encryption for the /data API
  * Faster offline transcribe, including optimized pipeline for audio coming from S3 (or other external URL)
  * Improved English acoustic model (offline mode) - about 1.5% better accuracy on meeting / lecture type of audio
  * Beta version of a German offline acoustic model
  * Language settings in the Web Console improved - only acoustic models compatible with a selected language are shown
  * Added profanity masking option to the Transcribe Dialog

Backwards incompatibility:
* the `reuse` parameter in the /data API will now be ignored - each POST request will create a new Data Object

Fixed issues:
* #ocp-777: When afterlife is 0, offline process does not submit ERROR status to asr-api (no error callback)
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
    

**Backwards incompatibility:**
* Certain acoustic model names are no longer available. Unless using specific custom models, it is now sufficient to just provide `languages` parameter - no need to specify acoustic model by name.
* requests to `/asr/transcribe/async` API with `portal` field value but no `portal.label` specified will fail - `portal.label` is now a required value 









































 













































