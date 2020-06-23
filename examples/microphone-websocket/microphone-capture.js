let websocketSendUrl, websocketReceiveUrl, websocketReceiveName, stompClient;

//Obtain Voicegain websocket URL for async transcription. Requires JWT token for authorization.
const connectVoicegainWebsocket = async () => {
  const transcriptionApiUrl = "https://api.voicegain.ai/v1/asr/transcribe/async";
  const bearer = "Bearer " + voicegainJwt;

// this is the body of the request to /asr/transcribe/async
// 1) the real time session - the recognition output will be directed to adHoc websocket
// 2) the semi-real-time session - this is in order to obtain a more accurate transcript after real-time
//    addtionally result of semi-real-time session is stored in the portal
//
// microphone audio is streamed over websocket to the recognizer
// ASR setting shave very long timeouts so you will have to stop capture by pressing stop button
  const data = {
    sessions: [
      {
        asyncMode: "REAL-TIME",
        websocket: { adHoc: true, minimumDelay: 1000 },
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
      // retrieve relevant results from the reponse to POST /asr/transcribe/async
      // websocket for sending audio
      websocketSendUrl = transcriptionData.audio.stream.websocketUrl;
      // websocket for receiving transcription results
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
  // capture audio and send to websocket
  AudioCaptureStreamingService.start(websocketSendUrl);

  // Connect to Websocket to receive data in STOMP format
  if (stompClient === undefined) {
    const client = new StompJs.Client({
      brokerURL: websocketReceiveUrl,
    });
    client.onConnect = (frame) => {
      // subscribe to STOMP topic with transcribe results
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
