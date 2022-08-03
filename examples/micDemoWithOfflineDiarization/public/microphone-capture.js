let websocketSendUrl,
  websocketReceiveUrl,
  websocketReceiveName,
  stompClient,
  jwtToken,
  semiRtSessionid,
  rtSessionid,
  pollInterval,
  numberSpeakers,
  prevSpeaker=0,
  speakerChange=false,
  currentSpeaker=0,
  uuidData,
  websocket;



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

      const fetchWebsocketUrl = async () => {

        // Takes only first character of input.
        numberSpeakers = parseInt(document.getElementById("speakersInput").value[0]);

        // Check for upper limit 0 and beyond, else it is a single digit number or 1
        if(parseInt(document.getElementById("speakersInput").value)>=10){
          numberSpeakers=10;
        } else if(!(numberSpeakers>1 && numberSpeakers<10)){ // Cases where user enters invalid entries - set to 1
          numberSpeakers=1;
        } // End of else statement

        const bearer = "Bearer " + jwtToken;

        const body = JSON.stringify({
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
              // If numberSpeakers within range of 2 to 10 use diarization, else we leave the below line out
              ...(numberSpeakers!=1) && {diarization : { minSpeakers : "2", maxSpeakers : numberSpeakers }},
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
          let fetchWebsocketResponse = await fetch(
            websocketApiUrl.toString(),
            options
          );

          if (fetchWebsocketResponse.ok) {
            let fetchWebsocketData = await fetchWebsocketResponse.json();
            websocketSendUrl = fetchWebsocketData.audio.stream.websocketUrl;
            websocketReceiveUrl = fetchWebsocketData.sessions[0].websocket.url;

            // Required for offline request, make sure capture is set to true in request body
            uuidData = fetchWebsocketData.audio.capturedAudio;

            // Function to start real-time microphone capture
            startMicrophoneCapture(websocketSendUrl, websocketReceiveUrl);
          }
        } catch (err) {
          window.alert("Unable to start capture.");
          console.log(err.message);
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

        const interpretTranscriptionMessage = (message) => {
          const isTranscriptionResult = message.hasOwnProperty("utt");
          const isWordCorrection = message.hasOwnProperty("del");
          const hasEdit = message.hasOwnProperty("edit");

          // Conditional statement to group text based on a speaker change
          // Works similar to a for loop comparing current speaker against the previous words speaker
          if(numberSpeakers!=1 && message.spk!=undefined){
            
            currentSpeaker=message.spk;
            // console.log("CurrentSpeaker : "+currentSpeaker+" PrevSpeaker : "+prevSpeaker);
            if(currentSpeaker==prevSpeaker){
              speakerChange=false;
            }else{ // Speaker changed case
              speakerChange=true;
              
              // If the speaker is '0', the assign just 'Speaker' before the word
              if(currentSpeaker==0){
                words.push('<span id="insertedText"> Speaker </span>');
              } else{
                words.push(`<span id="insertedText"> Speaker${currentSpeaker.toString()} </span>`)
              }

            }
            prevSpeaker=currentSpeaker;

          }

          // Check for deletions or edits when adding words to result
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
  // Function to call the offline POST request here for offline session
  offlineTranscript();

};



// Request for offline transcription!
const offlineTranscript = async () => {
  let startButton = document.getElementById("start-capture-button");
  let stopButton = document.getElementById("stop-capture-button");
  let result = document.getElementById("transcription-result");
  result.style.display = "none";
  showFinalizingStatus(true);
  const bearer = "Bearer " + jwtToken;

  try {
    startButton.disabled = true;
    stopButton.disabled = true;

    const voicegainOfflineUrl = new URL(
      `https://api.voicegain.ai/v1/asr/transcribe/async`
    );


    const offlineBody = JSON.stringify({
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
              // If numberSpeakers within range of 2 to 10 use diarization, else we leave the below line out
              ...(numberSpeakers!=1) && {diarization : { minSpeakers : "2", maxSpeakers : numberSpeakers }},              // "hints" : ["rupees:10", "Hyderabad:10", "lakh:10", "lakhs:10", "lakh_rupees"]
              // "langModel": "af1433a5-4e81-4df8-bf86-a48e0f409157"
          }
          // "formatters" : [{"type" : "digits"}]
      }
    });

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

        // Call for polling repeatedly until 'result.final' is true
        pollTranscript();
        pollInterval = setInterval(() => pollTranscript(), 5000);
      }
    } catch (err) {
      window.alert("Unable to parse offline capture.");
      console.log(err.message);
    }

  } catch (err) {
    window.alert("Unable to obtain offline capture.");
    console.log(err.message);
  }
};





// Make api call to Voicegain polling for transcript to get finalized
const pollTranscript = async () => {
  let startButton = document.getElementById("start-capture-button");
  let stopButton = document.getElementById("stop-capture-button");
  let result = document.getElementById("transcription-result");
  result.style.display = "none";
  showFinalizingStatus(true);
  const bearer = "Bearer " + jwtToken;
  try {

    // Use the rtSessionid obtained from the offline request in offlineTranscript() to fetch the transcript
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

        // Re-initialize the variables used in real-time session
        prevSpeaker=0;
        speakerChange=false;
        currentSpeaker=0;

        //Initialize utterance,duration, and start array
        for( i=0; i<pollTranscriptData.result.words.length; i++){

          // The current speaker for the word
          currentSpeaker=pollTranscriptData.result.words[i].spk;

          // Duration and start time for computing when to indent text
          pollWordDuration[i] = pollTranscriptData.result.words[i].duration;
          pollWordTimeFromStart[i] = pollTranscriptData.result.words[i].start;

          if(numberSpeakers==1){

            pollWordArray[i] = pollTranscriptData.result.words[i].utterance;


          } else if(numberSpeakers!=1 && currentSpeaker!=undefined){

            // console.log("CurrentSpeaker : "+currentSpeaker+" PrevSpeaker : "+prevSpeaker);
            if(currentSpeaker==prevSpeaker){
              speakerChange=false;
            }else{
              speakerChange=true;
            }
            prevSpeaker=currentSpeaker;
          
            // Within diarization loop, below are 2 cases for when spk=0 and spk!=0
            if(currentSpeaker==0 && speakerChange==true){
              pollWordArray[i] = '<span id="insertedText"> Speaker </span>'+pollTranscriptData.result.words[i].utterance;
            } else if(numberSpeakers!=1 && speakerChange==true){
              pollWordArray[i] = `<span id="insertedText"> Speaker${currentSpeaker.toString()} </span>`+pollTranscriptData.result.words[i].utterance;
            } else{
              pollWordArray[i] = pollTranscriptData.result.words[i].utterance;
            }

          }
        } // End of for loop

        
        // Assign gap times for indentation
        pollWordGapTimes[0] = pollWordTimeFromStart[0];
        for( i=1; i<pollWordArray.length; i++){
          pollWordGapTimes[i] = pollWordTimeFromStart[i]-pollWordTimeFromStart[i-1]-pollWordDuration[i-1];
        }
        //console.log("Gaps are : "+pollWordGapTimes);
        //console.log("Duration values in array are : "+pollWordDuration);
        //console.log("Start values in array are : "+pollWordTimeFromStart);


        for( i=1; i<pollWordArray.length; i++){
          if(pollWordGapTimes[i]>1500){
            pollWordArray[i] = "<br>"+pollWordArray[i];
          }
          else{
            pollWordArray[i] = pollWordArray[i];
          }
        }
        var finalStringResult = pollWordArray.join(" ");

        result.innerHTML="";
        result.style.display = "none";
        result.style.display = "block";
        document.getElementById("transcription-result").style.color = "white";
        //result.innerHTML = pollTranscriptData.result.transcript;
        result.innerHTML = finalStringResult;


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
