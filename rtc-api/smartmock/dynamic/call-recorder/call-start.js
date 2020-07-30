// POST http(s)://<??>.app.smartmock.io//speech/dynamic-test

/* SAMPLE OUTPUT
{
    "csid": "7c7bba54-86b7-4aae-86fd-5797e2d81c5e",
    "sid": "hd63d9-hmps973g-shhdf7-1287dt",
    "sequence": 1,
    "prompt": {
        "text": "Welcome to Call Recorder",
        "audioProperties": {
            "voice": "catherine"
        }
    }
}
*/
faker.locale = 'en_US';
json = req.jsonBody;
sid = json.sid;
seq = json.sequence;
csid = faker.random.uuid();
voice = "catherine";

body = {};
body.csid = csid;
body.sid = sid;
body.sequence = seq;
body.prompt = {};
body.prompt.text = "Welcome to Call Recorder";
body.prompt.audioProperties = {};
body.prompt.audioProperties.voice = voice;

callState = {};
callState.csid = csid;
callState.seq = seq;
callState.sid = sid;
callState.voice = voice;
state.set(sid, callState,3600);

res.status=200;
res.body=body;
res.addHeader('Content-Type', 'application/json');
