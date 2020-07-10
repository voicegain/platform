let jwtToken, pollInterval;

// eslint-disable-next-line no-unused-vars
const fetchTempJwt = async () => {
  showUploadLoader(true);
  const apiUrl = "http://localhost:8080/api/jwt";
  const selectedFile = document.getElementById("custom-file").files[0];
  if (selectedFile) {
    try {
      let fetchTempJwtResponse = await fetch(apiUrl, { method: "GET" });
      if (fetchTempJwtResponse.ok) {
        let fetchTempJwtData = await fetchTempJwtResponse.json();
        jwtToken = fetchTempJwtData.jwtToken;
        uploadFile(jwtToken, selectedFile);
      } else throw new Error("Unable to fetch temporary JWT token.");
    } catch (err) {
      console.log(err.message);
    }
  }
};

const uploadFile = async (jwtToken, file) => {
  let transcriptResult = document.getElementById("transcript-result");
  let statusTag = document.getElementById("status-tag");
  transcriptResult.innerHTML = "";
  statusTag.style.display = "none";
  try {
    const bearer = "Bearer " + jwtToken;
    const voicegainUploadUrl = new URL("https://api.voicegain.ai/v1/data/file");
    voicegainUploadUrl.searchParams.append("reuse", false);
    const formData = new FormData();
    formData.append("file", file, file.name);
    const body = formData;
    const options = {
      body,
      method: "POST",
      headers: {
        Authorization: bearer,
      },
    };

    let uploadFileResponse = await fetch(
      voicegainUploadUrl.toString(),
      options
    );

    if (uploadFileResponse.ok) {
      let uploadFileData = await uploadFileResponse.json();
      startAsyncTranscribe(
        bearer,
        uploadFileData.name,
        uploadFileData.objectId
      );
    }
  } catch (err) {
    alert(err.message);
    console.log(err.message);
  }
};

const startAsyncTranscribe = async (bearer, label, objectId) => {
  try {
    const voicegainTranscribeUrl = new URL(
      "https://api.voicegain.ai/v1/asr/transcribe/async"
    );
    const body = JSON.stringify({
      sessions: [
        {
          asyncMode: "OFF-LINE",
          content: { full: ["transcript", "words"] },
          poll: { persist: 5000, afterlife: 5000 },
          portal: { label, persist: 604800000 },
        },
      ],
      audio: { source: { dataStore: { uuid: objectId } } },
    });
    const options = {
      body,
      method: "POST",
      headers: {
        Authorization: bearer,
        "Content-Type": "application/json",
      },
    };

    let asyncTranscribeResponse = await fetch(
      voicegainTranscribeUrl.toString(),
      options
    );

    if (asyncTranscribeResponse.ok) {
      let asyncTranscribeData = await asyncTranscribeResponse.json();
      pollInterval = setInterval(
        () => pollTranscript(bearer, asyncTranscribeData.sessions[0].sessionId),
        5000
      );
    } else throw new Error("Unable to start async transcription.");
  } catch (err) {
    alert(err.message);
    console.log(err.message);
  }
};

const pollTranscript = async (bearer, sessionId) => {
  let uploadButton = document.getElementById("non-loading-button");
  try {
    showPollSpinner(true);
    uploadButton.disabled = true;

    const voicegainPollUrl = new URL(
      `https://api.voicegain.ai/v1/asr/transcribe/${sessionId}`
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
      setTranscriptionStatus(pollTranscriptData.progress.phase);

      if (pollTranscriptData.result.final === true) {
        clearInterval(pollInterval);
        showPollSpinner(false);
        uploadButton.disabled = false;

        let transcriptResult = document.getElementById("transcript-result");
        transcriptResult.innerHTML = pollTranscriptData.result.transcript;
      }
    } else throw new Error("Unable to poll transcript.");
  } catch (err) {
    alert(err.message);
    console.log(err.message);
    uploadButton.disabled = false;
  } finally {
    showUploadLoader(false);
  }
};

const showUploadLoader = (isLoading) => {
  let loadingButton = document.getElementById("loading-button");
  let nonLoadingButton = document.getElementById("non-loading-button");
  if (isLoading) {
    nonLoadingButton.style.display = "none";
    loadingButton.style.display = "block";
  } else {
    loadingButton.style.display = "none";
    nonLoadingButton.style.display = "block";
  }
};

const showPollSpinner = (isLoading) => {
  let spinner = document.getElementById("poll-spinner");
  if (isLoading) spinner.style.display = "inline-block";
  else spinner.style.display = "none";
};

const setTranscriptionStatus = (phase) => {
  let statusTag = document.getElementById("status-tag");
  statusTag.style.display = "inline-block";
  switch (phase) {
    case "ACCEPTED":
      statusTag.className = "badge badge-primary";
      statusTag.innerHTML = "ACCEPTED";
      break;
    case "QUEUED":
      statusTag.className = "badge badge-warning";
      statusTag.innerHTML = "QUEUED";
      break;
    case "FETCHING":
      statusTag.className = "badge badge-primary";
      statusTag.innerHTML = "FETCHING";
      break;
    case "FETCHED":
      statusTag.className = "badge badge-primary";
      statusTag.innerHTML = "FETCHED";
      break;
    case "PROCESSING":
      statusTag.className = "badge badge-warning";
      statusTag.innerHTML = "PROCESSING";
      break;
    case "DONE":
      statusTag.className = "badge badge-success";
      statusTag.innerHTML = "DONE";
      break;
    case "STOPPED":
      statusTag.className = "badge badge-danger";
      statusTag.innerHTML = "STOPPED";
      break;
    case "ERROR":
      statusTag.className = "badge badge-danger";
      statusTag.innerHTML = "ERROR";
      break;
    default:
      break;
  }
};
