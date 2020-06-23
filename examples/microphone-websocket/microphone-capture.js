let websocketSendUrl, websocketReceiveUrl, websocketReceiveName, stompClient;

//Obtain Voicegain websocket URL for async transcription. Requires JWT token for authorization.
const connectVoicegainWebsocket = async () => {
  const transcriptionApiUrl = "https://api.ascalon.ai/v1/asr/transcribe/async";
  const bearer = "Bearer " + voicegainJwt;

  const data = {
    sessions: [
      {
        asyncMode: "REAL-TIME",
        websocket: { adHoc: true, minimumDelay: 2000 },
      },
      {
        asyncMode: "SEMI-REAL-TIME",
        portal: { label: "sample-transcription", persist: 604800000 },
      },
    ],
    audio: {
      source: { stream: { protocol: "WEBSOCKET" } },
      capture: true,
      rate: 16000,
    },
    settings: {
      preemptible: false,
      asr: {
        noInputTimeout: 59999,
        incompleteTimeout: 3599999,
      },
    },
  };

  const options = {
    method: "POST",
    headers: {
      Authorization: bearer,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  };

  try {
    showLoader(true);
    let transcriptionResponse = await fetch(transcriptionApiUrl, options);
    if (transcriptionResponse.ok) {
      let transcriptionData = await transcriptionResponse.json();
      websocketSendUrl = transcriptionData.audio.stream.websocketUrl;
      websocketReceiveUrl = transcriptionData.sessions[0].websocket.url;
      websocketReceiveName = transcriptionData.sessions[0].websocket.name;

      startMicrophoneCapture(
        websocketSendUrl,
        websocketReceiveUrl,
        websocketReceiveName
      );
    } else throw new Error("Unable to retrieve websocket URL.");
  } catch (err) {
    console.log(err.message);
  } finally {
    showLoader(false);
  }
};

//Start audio capturing services using microphone input
const startMicrophoneCapture = (
  websocketSendUrl,
  websocketReceiveUrl,
  websocketReceiveName
) => {
  showCaptureStatus(true);
  AudioCaptureStreamingService.start(websocketSendUrl);

  // Connect to Websocket to receive data
  if (stompClient === undefined) {
    const client = new StompJs.Client({
      brokerURL: websocketReceiveUrl,
    });
    client.onConnect = (frame) => {
      client.subscribe(`/topic/${websocketReceiveName}`, (message) => {
        const json = JSON.parse(message.body);
        const string = JSON.stringify(json);
        const div = document.createElement("div");
        const text = document.createTextNode(string);
        div.appendChild(text);
        const result = document.getElementById("transcription-result");
        result.appendChild(div);
      });
    };
    client.onDisconnect = () => {
      AudioCaptureStreamingService.stop();
    };
    client.onWebSocketError = () => {
      console.log("onWebsocketError");
    };
    client.activate();
  }
};

//Stop audio capturing services
const stopMicrophoneCapture = () => {
  showCaptureStatus(false);
  AudioCaptureStreamingService.stop();
  if (stompClient !== undefined) {
    stompClient.deactivate();
    setStompClient(undefined);
  }
};

//Show loading spinner while fetching websocket data from API
const showLoader = (isLoading) => {
  let loader = document.getElementById("loader-container");
  if (isLoading === true) loader.style.display = "block";
  else loader.style.display = "none";
};

//Show "Capturing..." in HTML when microphone capture is started
const showCaptureStatus = (isCapturing) => {
  let captureStatus = document.getElementById("capture-status");
  if (isCapturing === true) captureStatus.style.display = "block";
  else captureStatus.style.display = "none";
};
