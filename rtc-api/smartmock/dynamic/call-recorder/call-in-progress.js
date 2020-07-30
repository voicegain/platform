// PUT http(s)://<??>.app.smartmock.io/speech/dynamic-test/{csid}?seq
/* SAMPLE OUTPUT
{
  "csid": "{{req.pathParams.[csid]}}",
  "sid": "{{jsonPath req.body path='$.sid'}}",
  "sequence": {{req.query.[seq]}},
  "question": {
    "name" : "phone",
    "text": "Say or Enter the number you want to call",
    "audioProperties": {
      "voice": "catherine"
    },
    "audioResponse" : {
        "bargeIn" :  true,
        "grammar" : [{
            "type" : "BUILT-IN",
            "name" : "phone"
        },
        {
            "type" : "BUILT-IN",
            "name" : "dtmf/phone"
        }]
    }
  }
}
callState.csid = csid;
callState.seq = seq;
callState.sid = sid;
callState.voice = voice;
*/
faker.locale = 'en_US';
json = req.jsonBody;
sid = json.sid;
seq = req.query.seq[0];
csid = req.pathParams.csid;

callState = state.get(sid);

if(seq == 2) {
    body = {};
    body.csid = csid;
    body.sid = sid;
    body.sequence = seq;
    body.prompt = {};
    body.prompt.text = "Welcome to Call Recorder";
    body.prompt.audioProperties = {};
    body.prompt.audioProperties.voice = callState.voice;    
}




state.set(sid, callState,3600);

res.status=200;
res.body=body;
res.addHeader('Content-Type', 'application/json');


