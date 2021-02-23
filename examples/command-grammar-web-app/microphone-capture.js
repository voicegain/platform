let websocketSendUrl, websocketReceiveUrl, stompClient, jwtToken, websocket;

//Configuring the request body to the API
let request = {
  sessions: [
    {
      asyncMode: "REAL-TIME",
      websocket: { adHoc: true, minimumDelay: 0, useSTOMP: false },
      continuousRecognition: {
        enable: true,
        stopOn: ["ERROR"],
        noResponseFor: ["INPUT-STARTED", "NOINPUT"],
      },
    },
  ],
  audio: {
    source: { stream: { protocol: "WEBSOCKET" } },
    format: "F32",
    rate: 16000,
    channels: "mono",
    capture: true,
  },
  settings: {
    asr: {
      confidenceThreshold: 0.175,
      noInputTimeout: 9000,
      incompleteTimeout: 2500,
      completeTimeout: 100,
      sensitivity: 0.1,
      grammars: [
        {
          type: "JJSGF",
          parameters: { "tag-format": "semantics/1.0-literals" },
          grammar: "command",
          public: {
            root:
              "<first> {first} | <second> {second} | <third> {third} | <fourth> {fourth}",
          },
          rules: {
            first:
              "((first alt phrase of first command) | (second alt phrase of first command))",
            second:
              "((first alt phrase of second command) | (second alt phrase of second command))",
            third:
              "((first alt phrase of third command) | (second alt phrase of third command))",
            fourth:
              "((first alt phrase of fourth command) | (second alt phrase of fourth command))",
          },
        },
      ],
    },
  },
};

//Passes text box input to the request grammar
function updateGrammar() {
  let command = request.settings.asr.grammars[0].rules;
  //FIRST TEXT BOX
  const grammarOne = document.getElementById("firstText").value;
  const firstArr = grammarOne.toString().split(",");
  let semiStringOne = firstArr[0];
  for (i = 1; i < firstArr.length; i++) {
    semiStringOne = "(" + semiStringOne + ")" + "|" + "(" + firstArr[i] + ")";
  }
  if (grammarOne.trim().length > 1) {
    command.first = semiStringOne;
  } else command.first = `<VOID>`;

  //SECOND TEXT BOX
  const grammarTwo = document.getElementById("secondText").value;
  const secondArr = grammarTwo.toString().split(",");
  let semiStringTwo = secondArr[0];
  for (i = 1; i < secondArr.length; i++) {
    semiStringTwo = "(" + semiStringTwo + ")" + "|" + "(" + secondArr[i] + ")";
  }
  if (grammarTwo.trim().length > 1) {
    command.second = semiStringTwo;
  } else command.second = `<VOID>`;

  //THIRD TEXT BOX
  const grammarThree = document.getElementById("thirdText").value;
  const thirdArr = grammarThree.toString().split(",");
  let semiStringThree = thirdArr[0];
  for (i = 1; i < thirdArr.length; i++) {
    semiStringThree =
      "(" + semiStringThree + ")" + "|" + "(" + thirdArr[i] + ")";
  }
  if (grammarThree.trim().length > 1) {
    command.third = semiStringThree;
  } else command.third = `<VOID>`;

  //FOURTH TEXT BOX
  const grammarFour = document.getElementById("fourthText").value;
  const fourthArr = grammarFour.toString().split(",");
  let semiStringFour = fourthArr[0];
  for (i = 1; i < fourthArr.length; i++) {
    semiStringFour =
      "(" + semiStringFour + ")" + "|" + "(" + fourthArr[i] + ")";
  }
  if (grammarFour.trim().length > 1) {
    command.fourth = semiStringFour;
  } else command.fourth = `<VOID>`;

  console.log("Request first tag: " + command.first);
}

//Fetch temporary JWT Token and make call to Voicegain API to get websocket URLs
const connectWebsocket = async () => {
  const audioContext = new AudioContext();
  const sampleRate = audioContext.sampleRate;
  const jwtApiUrl = new URL("http://localhost:4040/api/jwt");
  const websocketApiUrl = new URL(
    "https://api.voicegain.ai/v1/asr/recognize/async"
  );
  const output = document.getElementById("transcription-result");
  output.innerHTML = "";

  try {
    let fetchTempJwtResponse = await fetch(jwtApiUrl, { method: "GET" });
    if (fetchTempJwtResponse.ok) {
      let fetchTempJwtData = await fetchTempJwtResponse.json();
      jwtToken = fetchTempJwtData.jwtToken;

      const fetchWebsocketUrl = async () => {
        const bearer = "Bearer " + jwtToken;

        updateGrammar();
        const body = JSON.stringify(request);
        console.log("Request body: " + body);

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
            websocketSendUrl = fetchWebsocketData.audio.stream.websocketUrl; //streams audio to the recognizer
            websocketReceiveUrl = fetchWebsocketData.sessions[0].websocket.url; //receives results

            startMicrophoneCapture(websocketSendUrl, websocketReceiveUrl);
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
const startMicrophoneCapture = (websocketSendUrl, websocketReceiveUrl) => {
  let stopButton = document.getElementById("stop-capture-button");
  stopButton.disabled = false;
  showCaptureStatus(true);
  AudioCaptureStreamingService.start(websocketSendUrl);

  //Connect to websocket to receive result data
  if (websocket === undefined) {
    const socket = new WebSocket(websocketReceiveUrl);
    socket.onopen = () => {
      console.log("Websocket is connected");
      socket.addEventListener("message", (event) => {
        let currentDate = new Date();
        console.log("At " + currentDate + " Websocket message: " + event.data);
        const jsonData = JSON.parse(event.data);

        //Processing grammar websocket results
        interpretGrammarMessage = (message) => {
          grammarOutput = document.getElementById("matchMessage");
          grammarOutput.style.display = "none";

          try {
            if (message.lastEvent === "RECOGNITION-COMPLETE") {
              console.log("recognition is complete");
              //If a word in the grammar has MATCHED
              if (message.status == "MATCH") {
                grammarOutput.style.display = "block";
                grammarOutput.innerHTML = message.alternatives[0].utterance;

                const grammarOne = document.getElementById("firstText").value;
                const grammarTwo = document.getElementById("secondText").value;
                const grammarThree = document.getElementById("thirdText").value;
                const grammarFour = document.getElementById("fourthText").value;
                //highlights matched text box green
                if (
                  grammarOne.includes(message.alternatives[0].utterance) == true
                ) {
                  document
                    .getElementById("secondText")
                    .classList.remove("green");
                  document
                    .getElementById("thirdText")
                    .classList.remove("green");
                  document
                    .getElementById("fourthText")
                    .classList.remove("green");
                  document.getElementById("firstText").classList.add("green");
                }
                if (
                  grammarTwo.includes(message.alternatives[0].utterance) == true
                ) {
                  document
                    .getElementById("firstText")
                    .classList.remove("green");
                  document
                    .getElementById("thirdText")
                    .classList.remove("green");
                  document
                    .getElementById("fourthText")
                    .classList.remove("green");
                  document.getElementById("secondText").classList.add("green");
                }
                if (
                  grammarThree.includes(message.alternatives[0].utterance) ==
                  true
                ) {
                  document
                    .getElementById("firstText")
                    .classList.remove("green");
                  document
                    .getElementById("secondText")
                    .classList.remove("green");
                  document
                    .getElementById("fourthText")
                    .classList.remove("green");
                  document.getElementById("thirdText").classList.add("green");
                }
                if (
                  grammarFour.includes(message.alternatives[0].utterance) ==
                  true
                ) {
                  document
                    .getElementById("firstText")
                    .classList.remove("green");
                  document
                    .getElementById("secondText")
                    .classList.remove("green");
                  document
                    .getElementById("thirdText")
                    .classList.remove("green");
                  document.getElementById("fourthText").classList.add("green");
                }
              } else if (message.status == "NOMATCH") {
                grammarOutput.style.display = "block";
                grammarOutput.innerHTML = message.status;
              } else grammarOutput.style.display = "none";
            } else if (message.lastEvent !== "RECOGNITION-COMPLETE") {
              grammarOutput.style.display = "block";
              let div = document.createElement("div");
              const errorText = document.createTextNode(
                "Error getting real-time grammar results."
              );
              div.appendChild(errorText);
              div.style.textAlign = "center";
              div.style.padding = "1rem";
            } else throw new Error("Unable to obtain grammar.");
          } catch (err) {
            alert(err.message);
            console.log(err.message);
          }
        };

        interpretGrammarMessage(jsonData);
      });

      //Resets text box highlight on websocket close
      socket.addEventListener("close", () => {
        console.log("Websocket closed.");
        AudioCaptureStreamingService.stop();
        document.getElementById("firstText").classList.remove("green");
        document.getElementById("secondText").classList.remove("green");
        document.getElementById("thirdText").classList.remove("green");
        document.getElementById("fourthText").classList.remove("green");
      });

      socket.addEventListener("error", (event) => {
        console.log("Websocket error:", event);
      });
    };
  }
};

//Stop audio capturing services
const stopMicrophoneCapture = () => {
  showCaptureStatus(false);
  AudioCaptureStreamingService.stop();
  if (websocket !== undefined) {
    websocket.close();
    websocket = undefined;
    startButton.disabled = false;
    stopButton.disabled = true;
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
