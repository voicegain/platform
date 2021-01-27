const got = require("got");
const express = require("express");
const cors = require("cors");
const app = express();

const PORT = 4040;

let jwt_token;

app.use(cors());

app.get("/api/jwt", async (req, res) => {
  let voicegainApiUrl = new URL("https://api.voicegain.ai/v1/security/jwt");
  const bearer = "Bearer " + "<Your JWT Here>";
  const options = {
    headers: {
      Authorization: bearer,
      "Content-Type": "application/json",
    },
    searchParams: {
      aud: "localhost:8080",
      expInSec: 3600,
    },
  };

  try {
    const jwtResponse = await got(voicegainApiUrl.toString(), options);
    jwt_token = jwtResponse.body;
    res.send({ jwtToken: jwt_token });
  } catch (err) {
    console.log(err)
    res.status(err.response.statusCode).send(err.response.body);
  }
});

app.listen(PORT);
