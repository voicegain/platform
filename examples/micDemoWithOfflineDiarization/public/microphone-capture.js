let websocketSendUrl,
  websocketReceiveUrl,
  websocketReceiveName,
  stompClient,
  jwtToken,
  semiRtSessionid,
  rtSessionid,
  pollInterval,
  numberSpeakers,
  prevSpeaker,
  speakerChange=false,
  currentSpeaker=0,
  uuidData,
  websocket;

// Sorry for not the nicest code (it was written by an itern - that is how easy it is).
// We will try to clean it up soon to make is easier to understand

//Fetch temporary JWT Token and make call to Voicegain API to get websocket URL's
const connectWebsocket = async () => {
  const audioContext = new AudioContext();
  const sampleRate = audioContext.sampleRate;
  const jwtApiUrl = new URL(`${appProps.serverUrl}/api/jwt`);
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
      let body = undefined; // initially

      const fetchWebsocketUrl = async () => {
        // Takes only first character of input
        numberSpeakers = parseInt(document.getElementById("speakersInput").value[0]);
        if(parseInt(document.getElementById("speakersInput").value)==10){
          numberSpeakers=10;
        }

        if( numberSpeakers>10 ){
          numberSpeakers=10;

          body = JSON.stringify({
            sessions: [
              {
                asyncMode: "REAL-TIME",
                websocket: { adHoc: true, minimumDelay: 175, useSTOMP: false },
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
                noInputTimeout: 59000,
                incompleteTimeout: 69000,
                diarization : { minSpeakers : "2", maxSpeakers : numberSpeakers }
              },
            },
          });

        } else if(numberSpeakers>1 && numberSpeakers<10){

          body = JSON.stringify({
            sessions: [
              {
                asyncMode: "REAL-TIME",
                websocket: { adHoc: true, minimumDelay: 175, useSTOMP: false },
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
                noInputTimeout: 59000,
                incompleteTimeout: 69000,
                diarization : { minSpeakers : "2", maxSpeakers : numberSpeakers }
              },
            },
          });

        } else{

          numberSpeakers=1;
          // Send request without diarization
          body = JSON.stringify({
            sessions: [
              {
                asyncMode: "REAL-TIME",
                websocket: { adHoc: true, minimumDelay: 175, useSTOMP: false },
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
                noInputTimeout: 59000,
                incompleteTimeout: 69000,
              },
            },
          });

        } // End of else statement

        const bearer = "Bearer " + jwtToken;

        const options = {
          body,
          method: "POST",
          headers: {
            Authorization: bearer,
            "Content-Type": "application/json",
          },
        };

        try {
          let fetchWebsocketResponse = await fetch(
            websocketApiUrl.toString(),
            options
          );

          if (fetchWebsocketResponse.ok) {
            let fetchWebsocketData = await fetchWebsocketResponse.json();
            websocketSendUrl = fetchWebsocketData.audio.stream.websocketUrl;
            websocketReceiveUrl = fetchWebsocketData.sessions[0].websocket.url;
            // semiRtSessionid = fetchWebsocketData.sessions[1].sessionId;

            uuidData = fetchWebsocketData.audio.capturedAudio; //Required for offline request

            startMicrophoneCapture(websocketSendUrl, websocketReceiveUrl);
          }
        } catch (err) {
          window.alert("Unable to start capture.");
          console.log(err.message);
        } finally {
          // console.log("Done");
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
  let words = [];
  // Connect to Websocket to receive data
  if (websocket === undefined) {
    const socket = new WebSocket(websocketReceiveUrl);
    socket.onopen = () => {
      socket.addEventListener("message", (event) => {
        const jsonData = JSON.parse(event.data);
        // console.log(jsonData);

        const interpretTranscriptionMessage = (message) => {
          const isTranscriptionResult = message.hasOwnProperty("utt");
          const isWordCorrection = message.hasOwnProperty("del");
          const hasEdit = message.hasOwnProperty("edit");

          // Assign currentSpeaker and prevSpeaker comparison here
          if(numberSpeakers!=1 && message.spk!=undefined){
            
            currentSpeaker=message.spk;
            // console.log("CurrentSpeaker : "+currentSpeaker+" PrevSpeaker : "+prevSpeaker);
            if(currentSpeaker==prevSpeaker){
              speakerChange=false;
            }else{ // Speaker changed case
              speakerChange=true;
              
              if(currentSpeaker==0){
                words.push('<span id="insertedText"> Speaker </span>');
              } else{
                words.push(`<span id="insertedText"> Speaker${currentSpeaker.toString()} </span>`)
              }

            }
            prevSpeaker=currentSpeaker;

          }

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

        // If statement to check message.spk is different from previous speaker
        if(speakerChange==true){
          
          const string = words.join(" ");
          const result = document.getElementById("transcription-result");
          result.innerHTML = string;

        } else {
          const string = words.join(" ");
          const result = document.getElementById("transcription-result");
          result.innerHTML = string;
        }

        
        // const string = words.join(" ");
        // const result = document.getElementById("transcription-result");
        // result.innerHTML = string;
      });

      socket.addEventListener("close", () => {
        console.log("Websocket closed.");
        AudioCaptureStreamingService.stop();
      });

      socket.addEventListener("error", (event) =>
        console.log("Websocket error:", event)
      );
    };
  }
};

//Stop audio capturing services
const stopMicrophoneCapture = () => {
  showCaptureStatus(false);
  AudioCaptureStreamingService.stop();
  // pollTranscript();
  // pollInterval = setInterval(() => pollTranscript(), 5000);
  if (websocket !== undefined) {
    websocket.close();
    websocket = undefined;
  }
  offlineTranscript(); // Call the offline POST request here for offline session

};



// Request for offline transcription!
const offlineTranscript = async () => {
  let startButton = document.getElementById("start-capture-button");
  let stopButton = document.getElementById("stop-capture-button");
  let result = document.getElementById("transcription-result");
  result.style.display = "none";
  showFinalizingStatus(true);
  const bearer = "Bearer " + jwtToken;
  let offlineBody = undefined; // initially

  try {
    startButton.disabled = true;
    stopButton.disabled = true;

    const voicegainOfflineUrl = new URL(
      `https://api.voicegain.ai/v1/asr/transcribe/async`
    );

    if( numberSpeakers!=1 ){

      offlineBody = JSON.stringify({
        sessions: [
          {
              asyncMode: "OFF-LINE",
              poll: {
                  afterlife: 60000,
                  persist: 120000
              },
              content: {
                  incremental: ["progress"],
                  full : ["words"]
              }
          }
        ],
        audio:{
            source: {
                dataStore: {
                    uuid: uuidData
                }
            }
        },
        settings: {
            asr: {
                speechContext : "normal",
                noInputTimeout: -1,
                completeTimeout: -1,
                sensitivity : 0.5,
                speedVsAccuracy : 0.5,
                languages : ["en"] ,
                diarization : { minSpeakers : "2", maxSpeakers : numberSpeakers }
                // "hints" : ["rupees:10", "Hyderabad:10", "lakh:10", "lakhs:10", "lakh_rupees"]
                // "langModel": "af1433a5-4e81-4df8-bf86-a48e0f409157"
            }
            // "formatters" : [{"type" : "digits"}]
        }
      });

    } else{

      offlineBody = JSON.stringify({
        sessions: [
          {
              asyncMode: "OFF-LINE",
              poll: {
                  afterlife: 60000,
                  persist: 120000
              },
              content: {
                  incremental: ["progress"],
                  full : ["words"]
              }
          }
        ],
        audio:{
            source: {
                dataStore: {
                    uuid: uuidData
                }
            }
        },
        settings: {
            asr: {
                speechContext : "normal",
                noInputTimeout: -1,
                completeTimeout: -1,
                sensitivity : 0.5,
                speedVsAccuracy : 0.5,
                languages : ["en"]
                // "hints" : ["rupees:10", "Hyderabad:10", "lakh:10", "lakhs:10", "lakh_rupees"]
                // "langModel": "af1433a5-4e81-4df8-bf86-a48e0f409157"
            }
            // "formatters" : [{"type" : "digits"}]
        }
      });

    }

    const options2 = {
      body: offlineBody,
      method: "POST",
      headers: {
        'Content-Type': 'application/json',
        Authorization: bearer,
      },
    };



    try {
      let fetchofflineWebsocketResponse = await fetch(
        voicegainOfflineUrl.toString(),
        options2
      );

      if (fetchofflineWebsocketResponse.ok) {
        let fetchOfflineWebsocketData = await fetchofflineWebsocketResponse.json();
        rtSessionid = fetchOfflineWebsocketData.sessions[0].sessionId;

        // Call for polling until result.final is true
        pollTranscript();
        pollInterval = setInterval(() => pollTranscript(), 5000);
      }
    } catch (err) {
      window.alert("Unable to parse offline capture.");
      console.log(err.message);
    } finally {
      // console.log("Done");
    }

  } catch (err) {
    window.alert("Unable to obtain offline capture.");
    console.log(err.message);
  } finally {
    // audioContext.close();
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
    startButton.disabled = true;
    stopButton.disabled = true;

    const voicegainPollUrl = new URL(
      `https://api.voicegain.ai/v1/asr/transcribe/${rtSessionid}`
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
        showFinalizingStatus(false);
        startButton.disabled = false;
        stopButton.disabled = true;

        //  Code for computing gap with polled words
        var pollWordGapTimes = [];

        var pollWordArray = [];
        var pollWordDuration = [];
        var pollWordTimeFromStart = [];
        prevSpeaker=0;
        speakerChange=false;
        currentSpeaker=0;
        let tempSpk=undefined;

        //Initialize utterance,duration, and start array
        for( i=0; i<pollTranscriptData.result.words.length; i++){

          tempSpk=pollTranscriptData.result.words[i].spk;
          // console.log("tempSpk : "+tempSpk);


          if(numberSpeakers==1){
            pollWordArray[i] = pollTranscriptData.result.words[i].utterance;
            pollWordDuration[i] = pollTranscriptData.result.words[i].duration;
            pollWordTimeFromStart[i] = pollTranscriptData.result.words[i].start;
          }

          // Add in this loop!!!!
         // Assign currentSpeaker and prevSpeaker here -- check if message.spk exists by using numberSpeakers or just check message.spk!=undefined
          if(numberSpeakers!=1 && tempSpk!=undefined){

            currentSpeaker=tempSpk;
            // console.log("CurrentSpeaker : "+currentSpeaker+" PrevSpeaker : "+prevSpeaker);
            if(currentSpeaker==prevSpeaker){
              speakerChange=false;
            }else{
              speakerChange=true;
            }
            prevSpeaker=currentSpeaker;
          
          

            if(currentSpeaker==0 && speakerChange==true){
              pollWordArray[i] = '<span id="insertedText"> Speaker </span>'+pollTranscriptData.result.words[i].utterance;

            } else if(numberSpeakers!=1 && speakerChange==true){
              pollWordArray[i] = `<span id="insertedText"> Speaker${currentSpeaker.toString()} </span>`+pollTranscriptData.result.words[i].utterance;

            } else{
              pollWordArray[i] = pollTranscriptData.result.words[i].utterance;
            }

            pollWordDuration[i] = pollTranscriptData.result.words[i].duration;
            pollWordTimeFromStart[i] = pollTranscriptData.result.words[i].start;
          }
        }

        

        pollWordGapTimes[0] = pollWordTimeFromStart[0];
        for( i=1; i<pollWordArray.length; i++){
          pollWordGapTimes[i] = pollWordTimeFromStart[i]-pollWordTimeFromStart[i-1]-pollWordDuration[i-1];
        }
        //console.log("Gaps are : "+pollWordGapTimes);
        //console.log(" duration values in array are : "+pollWordDuration);
        //console.log(" start values in array are : "+pollWordTimeFromStart);


        for( i=1; i<pollWordArray.length; i++){
          if(pollWordGapTimes[i]>1500){
            pollWordArray[i] = "<br>"+pollWordArray[i]; //replace with <br> later
          }
          else{
            pollWordArray[i] = pollWordArray[i];
          }
        }
        //console.log(" Final words in array are : "+pollWordArray);
        var finalStringResult = pollWordArray.join(" ");
        //console.log(" Final Result is : "+finalStringResult);

        result.innerHTML=""; //added
        result.style.display = "none";
        result.style.display = "block";
        document.getElementById("transcription-result").style.color = "white";
        //result.innerHTML = pollTranscriptData.result.transcript;
        result.innerHTML = finalStringResult; //added: new poll word string with computed gap time



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
    console.log(err.message+err);
    showFinalizingStatus(false);
    startButton.disabled = false;
    stopButton.disabled = false;
  }
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
