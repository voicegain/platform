// DELETE http(s)://<??>.app.smartmock.io/speech/dynamic-test/{csid}?seq
/* SAMPLE OUTPUT

callState.csid = csid;
callState.seq = seq;
callState.sid = sid;
callState.voice = voice;
*/
faker.locale = 'en_US';
json = req.jsonBody;
sid = json.sid;
seq = req.query.seq[0];

callState = state.get(sid);
callState.seq = seq;
body = {};
body.csid = callState.csid;
body.sid = sid;
body.sequence = seq;
body.termination = "normal";


state.set(sid, callState,3600);

res.status=200;
res.body=body;
res.addHeader('Content-Type', 'application/json');



