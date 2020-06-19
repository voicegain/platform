# Voicegain Platform Pricing
Last modified: June 17, 2020 

## Definitions ##

Before we present pricing let's define the terminology that will used in the pricing table.

### API method types ###

Voicegain ASR API provides two methods to invoke speech-to-text:
* **sync** method - intended for short audio up to 30 seconds. The result of recognition will be returned in the HTTP response.
* **async** method - suitable for short and long audio, up to several hours. The initial HTTP request returns the details of the speech-to-text session that was started. This session can later be queried for results. 

### Speech-to-Text mode ####

Voicegain ASR API supports two modes for speech-to-text:
* **recognize** - where the language model is provided by the grammars (e.g. GRXML) included in the request
* **transcribe** - where the ASR engine uses a large vocabulary NLM (natural language model) which is part of Voicegain Platform

### Acoustic Model types ###

Voicegain ASR uses two Acoustic Model types. The model type gets automatically chosen based on the API mehod (sync vs async), speech-to-text mode, and the Session Type (see below). The two models are:
* **high accuracy / high latency** - this model ensures highest accuracy but the trade-off is longer processing latency (time to first response)
* **normal accuracy / low latency** - this model is optimized for real-time use cases, but it needs to trade-off some of the accuracy in order to achieve low latency.

### Standard vs Custom Acoustic Models ###

* **standard acoustic model** - also called base model - this model is available to all users of voicegain platform. It has high accuracy, in particular the *high accuracy / high latency* version of it. The accuracy is better than standard acoustic models from Google, Mircosoft, and Amazon over wide range of speech types. It is not as good as the Google Video model.
* **custom acoustic model** - this is a model that has been trained on customer data. In our tests we have observed about 5% decrease of WER (word error rate) after training/customization.

### GPU Resource ###

API requests are assigned to one of the two types of GPU resource to use:
* **on-demand** - this is the default GPU resource with high availability and SLA of 99.9%
* **preemptible** - this is the GPU resource that may occasionally be subject to a restart. Voicegain platform ensures that despite the preemptibility of the underlying resource the request results will not be affected by that. The benefit of using this resource is lower price.

The assignment depends on the type of Session, see definition below.

### Session types ###

When **async** speech-to-text is launched the following session types can to be chosen:
* **real-time** - delivers fast response, suitable for IVR and live transcription, uses normal accuracy / low latency acoustic model
* **semi-real-time** - delivers results with about 30 seconds delay, suitable for live transcription in streaming scenarios where the larger delay is ok, uses high accuracy / high latency acoustic model 
* **offline** - this session type puts recognition requests into a job queue and they are then processes on the available resources - still generally the processing time is much faster than the duration of the audio. Uses high accuracy / high latency acoustic model. Runs on preemeptible GPU resource for lower price, but the success is guaranteed, unlike preemptible (semi-)-real-time session.
* **offline-rt** - this is a special session type tailored for bulk recognition with the same model as used for real-time. Main use case for this session type is regression testing for IVRs.

Note: it is possible to combine some of the Session Types in a single Web APi request. In such a case each session will be billed separately, e.g. if 10 minutes of audio is processed in HTTP request that starts both real-time and semi-real-time session, the final cost will be (1.25 + 1.25) * 10 = 25.0 cents.

## Pricing for Speech-to-Text ##

Given the above definitions, below is the complete pricing list for all possible combinations. Basically, both offline session types have lower pricing, while the real-time or sync requests are priced 25% higher.

| API</br>method|Speech-to-Text</br>mode| Session </br>Type |Acoustic</br>Model|GPU</br>resource|Price:</br> standard model|Price:</br> custom model|
|--------------|--------------------|----------|---|---|---|----|
|sync|both | n/a|high accuracy </br> high latency|on-demand|1.25 </br>cents/minute|1.75 </br>cents/minute|
|async |both|real-time|normal accuracy </br> low latency|on-demand|1.25 </br>cents/minute|1.75 </br>cents/minute|
|async |both|semi-real-time|high accuracy </br>high latency|on-demand|1.25 </br>cents/minute|1.75 </br>cents/minute|
|async|both |**offline**|high accuracy </br> high latency|guaranteed</br>preemptible|1.00 </br>cents/minute|1.50 </br>cents/minute|
|async |recognize| **offline**-rt|normal accuracy </br> low latency|guaranteed</br>preemptible|1.00 </br>cents/minute|1.50 </br>cents/minute|

## Pricing for IVR or MRCP Sessions ##

MRCP and/or IVR sessions are priced at **0.25 cent per minute**. Any Speech Recognition during such session is priced on top of the MRCP/IVR session price. Speech Recognition time will be counted from the moment when speech has been detected (barge-in time) until either MATCH or NO-MATCH terminates the recognition.


