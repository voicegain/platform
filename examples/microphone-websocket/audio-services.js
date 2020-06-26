class AudioCaptureStreamingService {
  static start = (webSocketUrl) => {
    const webSocket = new WebSocket(webSocketUrl);
    webSocket.addEventListener("close", (event) => console.debug(event));
    webSocket.addEventListener("message", (event) => console.debug(event));
    webSocket.addEventListener("open", (event) => {
      console.debug(event);
      AudioCaptureService.start((audioProcessingEvent) => {
        // console.debug(audioProcessingEvent);
        webSocket.send(audioProcessingEvent.inputBuffer.getChannelData(0));
      });
    });
    AudioCaptureStreamingService.webSocket = webSocket;
  };

  static stop = () => {
    const { webSocket } = AudioCaptureStreamingService;
    AudioCaptureService.stop();
    if (webSocket !== undefined) {
      webSocket.close();
      AudioCaptureStreamingService.webSocket = undefined;
    }
  };
}

const BUFFER_SIZE = 1024;
// sample rate is set to 16kHz
const AUDIO_CONTEXT_OPTIONS = {
  sampleRate: 16000,
};

class AudioCaptureService {
  static start = (onAudioProcess) => {
    console.debug("Start audio capture");
    if (!AudioCaptureService.isCapturing) {
      window.navigator.mediaDevices
        .getUserMedia({ audio: true, video: false })
        .then((mediaStream) => {
          const audioContext = new AudioContext(AUDIO_CONTEXT_OPTIONS);
          const source = audioContext.createMediaStreamSource(mediaStream);
          const processor = audioContext.createScriptProcessor(
            BUFFER_SIZE,
            1,
            1
          );
          processor.onaudioprocess = onAudioProcess;
          source.connect(processor);
          processor.connect(audioContext.destination);
          AudioCaptureService.isCapturing = true;
          AudioCaptureService.mediaStream = mediaStream;
          AudioCaptureService.processor = processor;
          AudioCaptureService.source = source;
        })
        .catch((error) => console.error(error.message));
    }
  };

  static stop = () => {
    console.debug("Stop audio capture");
    const { mediaStream, processor, source } = AudioCaptureService;
    if (AudioCaptureService.isCapturing) {
      if (
        mediaStream !== undefined &&
        processor !== undefined &&
        source !== undefined
      ) {
        processor.disconnect();
        source.disconnect();
        mediaStream
          .getTracks()
          .forEach((mediaStreamTrack) => mediaStreamTrack.stop());
        AudioCaptureService.isCapturing = false;
        AudioCaptureService.mediaStream = undefined;
        AudioCaptureService.processor = undefined;
        AudioCaptureService.source = undefined;
      }
    }
  };
}
