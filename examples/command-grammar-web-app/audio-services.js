class AudioCaptureStreamingService {
    //Create new websocket and start microphone
    static start = (webSocketUrl) => {
      console.log("starting...");
      const webSocket = new WebSocket(webSocketUrl);
      webSocket.addEventListener("close", (event) => console.debug(event));
      webSocket.addEventListener("message", (event) => console.debug(event));
      webSocket.addEventListener("open", (event) => {
        AudioCaptureService.start((audioProcessingEvent) => {
          webSocket.send(audioProcessingEvent.inputBuffer.getChannelData(0));
        });
      });
      AudioCaptureStreamingService.webSocket = webSocket;
    };
  
    //Stop microphone capture and close the websockets
    static stop = () => {
      const { webSocket } = AudioCaptureStreamingService;
      AudioCaptureService.stop();
      if (webSocket !== undefined) {
        webSocket.close();
        AudioCaptureStreamingService.webSocket = undefined;
      }
    };
  }
  
  const browser = navigator.userAgent.toLowerCase();
  const BUFFER_SIZE = 1024;
  const AUDIO_CONTEXT_OPTIONS = {
    sampleRate: 16000,
  };
  
  class AudioCaptureService {
    //Start microphone streaming
    static start = (onAudioProcess) => {
      console.debug("Start audio capture");
      if (!AudioCaptureService.isCapturing) {
        window.navigator.mediaDevices
          .getUserMedia({ audio: true, video: false })
          .then(async (mediaStream) => {
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
            AudioCaptureService.audioContext = audioContext;
          })
          .catch((error) => console.error(error));
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
