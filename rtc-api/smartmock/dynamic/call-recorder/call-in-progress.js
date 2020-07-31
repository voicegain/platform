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
callState.seq = seq;
body = {};
body.csid = callState.csid;
body.sid = sid;
body.sequence = seq;

if(seq == 2) { // 1st one was welcome greeting, 2nd is the question

    body.question = {};
    body.question.name = "phone";
    body.question.text = "Say or Enter the number you want to call";
    body.question.audioProperties = {};
    body.question.audioProperties.voice = callState.voice;    
    body.question.audioResponse = {};
    body.question.audioResponse.bargeIn = true;
    body.question.audioResponse.grammar = [];
    body.question.audioResponse.grammar[0] = {};
    body.question.audioResponse.grammar[0].type = "BUILT-IN";
    body.question.audioResponse.grammar[0].name = "phone";
    body.question.audioResponse.grammar[1] = {};
    body.question.audioResponse.grammar[1].type = "BUILT-IN";
    body.question.audioResponse.grammar[1].name = "dtmf/phone";
}
else if(seq == 3) { // 3rd is a response to the question about phone
    phone = json.vars["phone.phone"];
    callState.phone  =  phone;
   
    body.prompt = {};
    body.prompt.text = "Got it.";
    body.prompt.audioProperties = {};
    body.prompt.audioProperties.voice = callState.voice;
}
else if (typeof callState.phone !== 'undefined' && callState.phone !== null) { // we have a phone so let's dial it
/*
{
  "csid": "mobid9-lmps973g-zhhdf7-7287dtk",
  "sid": "{{jsonPath req.body path='$.sid'}}",
  "sequence": {{req.query.[seq]}},
  "transfer" : {
    "prompt": {
      "text": "Dialing: ",
      "audioProperties": {
        "voice": "catherine"
      }
    },
    "phone" : {
      "phoneNumber" : "9725180863"
    }
  }
}
*/
    body.transfer = {};
    body.transfer.prompt = {}
    body.transfer.prompt.text = 'Dialing: <say-as interpret-as="telephone">'+callState.phone+'</say-as>';
    body.transfer.prompt.audioProperties = {};
    body.transfer.prompt.audioProperties.voice = callState.voice;
    body.transfer.phone = {};
    body.transfer.phone.phoneNumber = callState.phone;
    callState.phone = null; // mark as used
}

state.set(sid, callState,3600);

res.status=200;
res.body=body;
res.addHeader('Content-Type', 'application/json');

/* sample response with phone number
{"sid":"38d65f19-878f-4f99-a3a8-eebc38c3d7a6","estimatedQueueWaitSeconds":null,
"vars":{"phone.d6":"0","phone.d7":"8","phone.d4":"1","phone.d5":"8","phone.d8":"6","phone.d9":"3","phone.response":"phone","phone.input":"dtmf",
"phone.phone":"9725180863","phone.d2":"2","phone.d3":"5","phone.d0":"9","phone.d1":"7"},
"events":[
    {"type":"output","timeMsec":4451,"logicType":"inbound","sequence":"2.1","text":"Say or Enter the number you want to call","endReason":"completed","method":"vui"},
    {"type":"input","timeMsec":16103,"logicType":"inbound","sequence":"2.2","name":"phone",
    "vuiAlternatives":[{"utterance":"9 7 2 5 1 8 0 8 6 3","confidence":1.0,"grammar":"dtmf/phone",
    "semanticTags":{"d0":"9","d1":"7","d2":"2","d3":"5","d4":"1","d5":"8","input":"dtmf","d6":"0","d7":"8","d8":"6","d9":"3","phone":"9725180863","response":"phone"}}],
    "method":"vui","vuiResult":"MATCH"}]}
*/


