let websocketSendUrl,
  websocketReceiveUrl,
  websocketReceiveName,
  stompClient,
  jwtToken,
  semiRtSessionid,
  pollInterval;

//Fetch temporary JWT Token and make call to Voicegain API to get websocket URL's
const connectWebsocket = async () => {
  const audioContext = new AudioContext();
  const sampleRate = audioContext.sampleRate;
  const jwtApiUrl = new URL("http://localhost:4040/api/jwt");
  const websocketApiUrl = new URL(
    "https://api.voicegain.ai/v1/asr/transcribe/async"
  );
  const result = document.getElementById("transcription-result");
  result.innerHTML = "";

  try {
    let fetchTempJwtResponse = await fetch(jwtApiUrl, { method: "GET" });
    if (fetchTempJwtResponse.ok) {
      let fetchTempJwtData = await fetchTempJwtResponse.json();
      jwtToken = fetchTempJwtData.jwtToken;

      const fetchWebsocketUrl = async () => {
        const bearer = "Bearer " + jwtToken;
        const body = JSON.stringify({
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
            format: "F32",
            capture: true,
            rate: 16000,
          },
          settings: {
            asr: {
              noInputTimeout: 59999,
              incompleteTimeout: 3599999,
            },
          },
        });
        const options = {
          body,
          method: "POST",
          headers: {
            Authorization: bearer,
            "Content-Type": "application/json",
          },
        };

        try {
          showLoader(true);
          let fetchWebsocketResponse = await fetch(
            websocketApiUrl.toString(),
            options
          );
          if (fetchWebsocketResponse.ok) {
            let fetchWebsocketData = await fetchWebsocketResponse.json();
            websocketSendUrl = fetchWebsocketData.audio.stream.websocketUrl;
            websocketReceiveUrl = fetchWebsocketData.sessions[0].websocket.url;
            websocketReceiveName =
              fetchWebsocketData.sessions[0].websocket.name;
            semiRtSessionid = fetchWebsocketData.sessions[1].sessionId;

            startMicrophoneCapture(
              websocketSendUrl,
              websocketReceiveUrl,
              websocketReceiveName
            );
          }
        } catch (err) {
          window.alert("Unable to start capture.");
          console.log(err.message);
        } finally {
          showLoader(false);
        }
      };

      fetchWebsocketUrl();
    } else throw new Error("Unable to fetch temporary JWT token.");
  } catch (err) {
    window.alert("Unable to fetch temporary JWT token.");
    console.log(err.message);
  } finally {
    audioContext.close();
  }
};

//Start audio capturing services using microphone input
const startMicrophoneCapture = (
  websocketSendUrl,
  websocketReceiveUrl,
  websocketReceiveName
) => {
  let stopButton = document.getElementById("stop-capture-button");
  stopButton.disabled = false;
  showCaptureStatus(true);
  AudioCaptureStreamingService.start(websocketSendUrl);
  let words = [];
  // Connect to Websocket to receive data
  if (stompClient === undefined) {
    stompClient = new StompJs.Client({
      brokerURL: websocketReceiveUrl,
    });
    stompClient.onConnect = () => {
      stompClient.subscribe(`/topic/${websocketReceiveName}`, (message) => {
        const jsonData = JSON.parse(message.body);

        //Handle corrections/deletions of words
        const interpretTranscriptionMessage = (message) => {
          const isTranscriptionResult = message.hasOwnProperty("utt");
          const isWordCorrection = message.hasOwnProperty("del");
          const hasEdit = message.hasOwnProperty("edit");
          if (isTranscriptionResult) {
            words.push(message.utt);
          } else if (isWordCorrection && hasEdit) {
            const nDeletions = message.del;
            const newWords = words.slice(0, words.length - nDeletions);
            const edits = message.edit.map((it) => it.utt); //throwing issue
            newWords.push(...edits);
            words = newWords;
          } else {
            return words;
          }
        };

        interpretTranscriptionMessage(jsonData);

        const string = words.join(" ");
        const result = document.getElementById("transcription-result");
        result.innerHTML = string;
      });
    };
    stompClient.onDisconnect = () => {
      console.log("...stomp disconnected");
      AudioCaptureStreamingService.stop();
    };
    stompClient.onWebSocketError = () => {
      console.log("onWebsocketError");
    };
    stompClient.activate();
  }
};

//Stop audio capturing services
const stopMicrophoneCapture = () => {
  showCaptureStatus(false);
  AudioCaptureStreamingService.stop();
  pollTranscript();
  pollInterval = setInterval(() => pollTranscript(), 5000);
  if (stompClient !== undefined) {
    stompClient.deactivate();
    stompClient = undefined;
  }
};

//Make api call to Voicegain polling for transcript to get finalized semi-real time results
const pollTranscript = async () => {
  let startButton = document.getElementById("start-capture-button");
  let stopButton = document.getElementById("stop-capture-button");
  let result = document.getElementById("transcription-result");
  result.style.display = "none";
  showFinalizingStatus(true);
  const bearer = "Bearer " + jwtToken;
  try {
    showLoader(true);
    startButton.disabled = true;
    stopButton.disabled = true;

    const voicegainPollUrl = new URL(
      `https://api.voicegain.ai/v1/asr/transcribe/${semiRtSessionid}`
    );
    voicegainPollUrl.searchParams.append("full", true);
    const options = {
      method: "GET",
      headers: {
        Authorization: bearer,
      },
    };

    let pollTranscriptResponse = await fetch(
      voicegainPollUrl.toString(),
      options
    );

    if (pollTranscriptResponse.ok) {
      let pollTranscriptData = await pollTranscriptResponse.json();

      if (
        pollTranscriptData.result.final === true &&
        pollTranscriptData.progress.phase !== "ERROR"
      ) {
        clearInterval(pollInterval);
        showLoader(false);
        showFinalizingStatus(false);
        startButton.disabled = false;
        stopButton.disabled = true;

        result.style.display = "block";
        result.innerHTML = pollTranscriptData.result.transcript;
      } else if (pollTranscriptData.progress.phase === "ERROR") {
        result.style.display = "block";
        let div = document.createElement("div");
        let errorText = document.createTextNode(
          "Error getting semi-real-time transcription."
        );
        div.appendChild(errorText);
        div.style.textAlign = "center";
        div.style.padding = "1rem";
      }
    } else throw new Error("Unable to poll transcript.");
  } catch (err) {
    alert(err.message);
    console.log(err.message);
    showLoader(false);
    showFinalizingStatus(false);
    startButton.disabled = false;
    stopButton.disabled = false;
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

//Show "Finalizing..." in HTML when polling for transcript is started
const showFinalizingStatus = (isFinalizing) => {
  let captureStatus = document.getElementById("finalizing-status");
  if (isFinalizing === true) captureStatus.style.display = "block";
  else captureStatus.style.display = "none";
};
