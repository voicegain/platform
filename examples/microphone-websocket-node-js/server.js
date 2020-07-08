const https = require("https");
const express = require("express");
const cors = require("cors");
const token = require("./config.js");
const app = express();

const PORT = 8080;

let websocketSendUrl, websocketReceiveUrl, websocketReceiveName, apiResponse;

app.use(cors());

app.get("/api/capture", (req, res) => {
  const bearer = "Bearer " + token.voicegainJwt;

  const data = JSON.stringify({
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
  });

  const options = {
    hostname: "api.voicegain.ai",
    path: "/v1/asr/transcribe/async",
    method: "POST",
    headers: {
      Authorization: bearer,
      "Content-Type": "application/json",
    },
  };

  const reque = https.request(options, (res) => {
    let body = "";

    res.on("data", (chunk) => {
      body += chunk;
    });

    res.on("end", () => {
      let transcriptionResponse = JSON.parse(body);
      websocketSendUrl = transcriptionResponse.audio.stream.websocketUrl;
      websocketReceiveUrl = transcriptionResponse.sessions[0].websocket.url;
      websocketReceiveName = transcriptionResponse.sessions[0].websocket.name;

      apiResponse = {
        websocketSendUrl,
        websocketReceiveUrl,
        websocketReceiveName,
      };
    });
  });

  reque.on("error", (err) => {
    console.log("Error: " + err.message);
  });

  reque.write(data);
  reque.end();

  res.send(apiResponse);
});

app.listen(PORT);
