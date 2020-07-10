const express = require("express");
const got = require("got");
const cors = require("cors");
const app = express();

const PORT = 8080;

let jwt_token;

app.use(cors());

app.get("/api/jwt", async (req, res) => {
  let voicegainApiUrl = new URL("https://api.voicegain.ai/v1/security/jwt");
  const bearer =
    "Bearer " +
    "<Your JWT Here>"; //Replace with your Voicegain JWT token

  const options = {
    headers: {
      Authorization: bearer,
      "Content-Type": "application/json",
    },
    searchParams: {
      aud: "localhost:8081",
      expInSec: 3600,
    },
  };

  try {
    const jwtResponse = await got(voicegainApiUrl.toString(), options);
    jwt_token = jwtResponse.body;
    res.send({ jwtToken: jwt_token });
  } catch (err) {
    console.log(err);
    res.send(err);
  }
});

app.listen(PORT);
