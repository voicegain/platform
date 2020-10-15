const AWS = require('aws-sdk');
const https = require('https');
const http = require('http');
const { match } = require('assert');
const s3 = new AWS.S3();

const httpInvoker = http;

const optionsMock = {
    hostname: 'rasa-nlu.app.smartmock.io',
    port: 443,
    path: '/flight/start',
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    }
};

const optionsRasa = {
    hostname: 'ec2-18-224-135-98.us-east-2.compute.amazonaws.com',
    port: 5005,
    path: '/webhooks/rest/webhook',
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    }
};    

const optionsVoicegain =  {
    hostname: 'api.ascalon.ai',
    port: 443,
    path: '/v1/asr/transcribe/async',
    method: 'POST',
    headers: {
        'Authorization' : 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiIqLmFzY2FsbG9uLmFpIiwic3ViIjoiM2MxMjNkNTktODYyMS00YTgzLTkxNWQtNGIzZWU4MDk1ODUzIn0.BccH0gOR6uwFMCo2p9hNkbCUe-eEsgCb8zqBDElOu-U',
        'Content-Type': 'application/json'
     }
};   

const options = optionsRasa;

// initial message to RASA - it will trigger the "how can i help you question"
const sayHiToRasa = "Hi";
// final message to RASA
const sayByeToRasa = "Goodbye"; 

let sequence = 0;
let csid = "no-csid";

exports.handler = async (event, context) => {
// https://rasa-nlu.app.smartmock.io/flight/start
// http://ec2-18-224-135-98.us-east-2.compute.amazonaws.com:5005/webhooks/rest/webhook



    // message to RASA in the middle of the dialogue
    // will be overwritten by actual response captured by voicegain
    

    console.info("START "+JSON.stringify(event));

    // get parameters from incoming AWS Lambda request
    const method = event.requestContext.http.method; // POST, PUT, or DELETE expected
    const queryParams = event.queryStringParameters;
    const bodyStr = event.body;
    console.info("method="+method);

    if(method == "GET") {
        return handleTwilioRequest(context, queryParams);
    }
    else if (method == "POST") {
        return handleVoicegainRequest(bodyStr, queryParams);
    }
    else {
        return handleUnexpectedRequest(method);
    }
}

function handleTwilioRequest(context, queryParams) {
    console.info("handle Twilio request: "+queryParams.seq);

    if(typeof queryParams.seq != 'undefined') {
        sequence = parseInt(queryParams.seq);
    }
    console.info("Sequence: "+sequence);    
    // local (customer) session id defaults to AWS request id
    csid = context.awsRequestId;
    if(typeof queryParams.csid != 'undefined') {
        csid = queryParams.csid;
    }
    console.info("    CSID: "+csid);  
    let vuiResult = "ERROR";

    

    let messageForRasa = "none";
    

    const promise = new Promise(function(resolve, reject) {
        if(sequence == 0) { // start of session
            console.info("START of session");

            messageForRasa = sayHiToRasa;
            handleRasaThenVG(messageForRasa, vuiResult, resolve, reject);
        }
        else  { // mid session
            try {
                const params = {
                    Bucket: "jacek-lambda-1",
                    Key: "LVR-"+csid+"-"+sequence,
                };
                s3.waitFor('objectExists', params, function (err, metadata) {  
                    if (err) {  
                        console.log(err, err.stack)
                        reject(err.message);  
                    } else {  
                        console.info("S3 obj exists: "+JSON.stringify(metadata));
                        s3.getObject(params, function(err, data) {
                            if (err) {
                                console.warn("not in s3 yet");
                                console.log(err, err.stack); // an error occurred
                                reject(err.message);
                            }
                            else {
                                console.log("S3 ok: "+data.Body.toString());           // successful response
                                const dataBody = JSON.parse(data.Body.toString());
                                const result = dataBody.result;
                                const vuiResult = result.status;
                                console.info("Result Status: "+vuiResult);
        
                                if(vuiResult == 'MATCH') {
                                    messageForRasa = result.transcript;
                                }
                                
                                handleRasaThenVG(messageForRasa, vuiResult, resolve, reject);
                            }
                        });                        
                    }
                });


        
            } catch (error) {
                console.log(error);
                reject(error.message);
            } 
        } 

        
    });
    return promise;  
}


function handleRasaThenVG(messageForRasa, vuiResult, resolve, reject) {
    if(messageForRasa == 'none') {
        // init response to be sent back to Voicegain 
        const respBody = {};
        respBody.sequence = sequence;
        respBody.sid = csid;
        if(vuiResult=='NOINPUT') {
            respBody.question = questionData(respBody.sequence, "I did not hear you", "Please speak");
        }
        else if(vuiResult=='NOMATCH') {
            respBody.question = questionData(respBody.sequence, "I did not get it", "Can you say it again");
        }
        resolve(jsonResponseFromLambda(respBody));
    }
    else {
        // Promise that we will return back to AWS Lambda 

        // init request to be sent to RASA
        let rasaReqBody = {};
        rasaReqBody.sender = "voicegain-"+csid; // sender name unique to this session
        rasaReqBody.message = messageForRasa; // the message for RASA
        console.info("Message for RASA: "+messageForRasa);

        // function that will send request to RASA and process the response
        const rasaReq = httpInvoker.request(options, (res) => {
            if (res.statusCode < 200 || res.statusCode >= 300) {
                console.warn(`RASA error response: `);
                resolve(xmlResponseFromLambda( bodyForTwilioErrorResponse("Bad response from Rasa: code "+res.statusCode) ));
            }
            var body = [];
            // assemble data received from RASA
            res.on('data', function(chunk) {
                body.push(chunk);
            });
            // finalize response from RASA 
            res.on('end', function() {
                try {
                    const bodyStr = Buffer.concat(body).toString();
                    console.info("Response from RASA: "+bodyStr);
                    body = JSON.parse(bodyStr);
                } catch(e) {
                    reject(e);
                }
                // process the response from RASA
                // response from RASA is an array of statements followed by a question
                // we concatenate the statements first 
                let statement = "";
                let i=0;
                while(i<body.length-1) {
                    statement += " "+body[i++].text;
                }
                // final element is the actual question from RASA
                const question = body[i].text;

                // for POST or PUT send the data received from RASA

                // make request to Voicegain to get sid and wss

                const vgReq = https.request(optionsVoicegain, (res) => {
                    if (res.statusCode < 200 || res.statusCode >= 300) {
                        console.warn(`VG error response: `+res.statusCode);
                        resolve(xmlResponseFromLambda( bodyForTwilioErrorResponse("Bad response from Voicegain: code "+res.statusCode) ));
                    }
                    var vgBody = [];
                    // assemble data received from RASA
                    res.on('data', function(chunk) {
                        vgBody.push(chunk);
                        console.info('chunk: '+chunk);
                    });
                    // finalize response from VG 
                    res.on('end', function() {
                        try {
                            const bodyStr = Buffer.concat(vgBody).toString();
                            console.info("Response from VG: "+bodyStr);
                            vgBody = JSON.parse(bodyStr);
                        } catch(e) {
                            reject(e);
                        }
                        // process response from voicegain
                        // we are looking for wss
                        const audio = vgBody.audio;
                        const stream =  audio.stream;
                        const websocketUrl = stream.websocketUrl;
                        const sessions = vgBody.sessions;
                        const session = sessions[0];
                        const sessionId =  session.sessionId;

                        console.info("websocketUrl: "+websocketUrl);
                        // pass the good response to resolve
                        resolve(xmlResponseFromLambda( bodyForTwilioResponse(csid, sequence, websocketUrl, statement, question) ));
                    });
                });
                vgReq.on('error', (e) => {
                    resolve(xmlResponseFromLambda( bodyForTwilioErrorResponse("Error invoking Voicegain: "+e.message) ));
                });    
                // send the request
                vgReq.write(JSON.stringify(bodyForVgRequest(csid, sequence)));
                vgReq.end();


            });
        });
        rasaReq.on('error', (e) => {
            resolve(xmlResponseFromLambda( bodyForTwilioErrorResponse("Error invoking Rasa: "+e.message) ));
        });
        // send the request
        const rasaReqStr = JSON.stringify(rasaReqBody);
        console.info("To RASA: "+rasaReqStr);
        rasaReq.write(rasaReqStr);
        rasaReq.end();
    };

}

function bodyForVgRequest(csid, sequence) {
    let body = {};
    body.sessions = [];
    let session = {};
    session.asyncMode = "REAL-TIME";
    session.callback = {};
    session.callback.uri 
    = "https://dqe7mrw2jh.execute-api.us-east-2.amazonaws.com/default/twilioVoicegainRasa1?seq="+(sequence+1)+"&csid="+csid;
    session.content = {};
    session.content.full = [];
    session.content.full.push("transcript");
    body.sessions.push(session);
    body.audio = {};
    body.audio.source = {};
    body.audio.source.stream = {};
    body.audio.source.stream.protocol = "TWIML";
    body.audio.format = "PCMU";
    body.audio.rate = 8000;
    body.audio.channels = "mono";
    body.audio.capture = false;
    body.settings = {};
    body.settings.asr = {};
    body.settings.asr.startInputTimers = false;
    body.settings.asr.confidenceThreshold = 0.25;
    body.settings.asr.noInputTimeout = 5000;
    body.settings.asr.completeTimeout = 2000;
    console.info("body for VG: "+JSON.stringify(body));
    return body;
}

function bodyForTwilioErrorResponse(errMsg) {
    let body = "";
    body += '<Response>\r\n'; 
    body += '  <Say voice="woman" language="en-US">'+errMsg+'</Say>\r\n';
    body += '  <Say voice="woman" language="en-US">Please call back later. Goodbye!</Say>\r\n';
    body += '  <Hangup/>\r\n';
    body += '</Response>\r\n';
    console.info("body for Twilio: "+body);
    return body;
}

function bodyForTwilioResponse(csid, sequence, websocketUrl, statementPrompt, questionPrompt) {
    let body = "";
    body += '<Response>\r\n';
    if(typeof statementPrompt !== 'undefined') {
        body += '  <Say voice="woman" language="en-US">'+statementPrompt+'</Say>\r\n';
    }
    body += '  <Connect>\r\n';
    body += '    <Stream url="'+websocketUrl+'">\r\n';
    body += '      <Parameter name="bargeIn" value ="enable"/>\r\n';
    body += '      <Parameter name="voice" value ="claire"/>\r\n';
    body += '      <Parameter name="prompt01" value ="'+questionPrompt+'"/>\r\n';
    body += '    </Stream>\r\n';
    body += '  </Connect>\r\n';
    body += '  <Redirect method="GET">'
    +'https://dqe7mrw2jh.execute-api.us-east-2.amazonaws.com/default/twilioVoicegainRasa1?seq='+(sequence+1)+"&amp;csid="+csid+'</Redirect>\r\n';
    body += '</Response>\r\n';
    console.info("body for Twilio: "+body);
    return body;
}

function xmlResponseFromLambda(xmlStr) {
    
    console.info("Response for Twilio: "+xmlStr);

    // tell AWS Lambda how to respond
    const response = {
        statusCode: 200,
        headers: {
            'Content-Type': 'application/xml',
        },
        body: xmlStr
    };
    return response;
}

function jsonResponseFromLambda(respBody) {
    const respBodyStr = JSON.stringify(respBody);
    console.info("Response for VG: "+respBodyStr);

    // tell AWS Lambda how to respond
    const response = {
        statusCode: 200,
        headers: {
            'Content-Type': 'application/json',
        },
        body: respBodyStr
    };
    return response;
}

function questionData(sequence, statementPrompt, questionPrompt) {

    let question = "";

    if(typeof statementPrompt != 'undefined') {
        question += '<Parameter name="prompt01" value="'+cleanupString(statementPrompt)+'"/>\r\n';
    }

    if(typeof questionPrompt != 'undefined') {
        question += '<Parameter name="prompt02" value="'+cleanupString(questionPrompt)+'"/>\r\n';
    }

    question += '<Parameter name="bargeIn" value ="enable"/>\r\n';

    return question;
}

function cleanupString(str) {
    return str.replace(/[\[\]]/g, '');
}

function handleVoicegainRequest(bodyStr, queryParams) {
    console.info("handle VG request: "+bodyStr);

    let body = JSON.parse(bodyStr);

    if(typeof queryParams.seq != 'undefined') {
        sequence = queryParams.seq;
    }
    console.info("Sequence: "+sequence);  
    if(typeof queryParams.csid != 'undefined') {
        csid = queryParams.csid;
    }
    console.info("    CSID: "+csid); 

    const promise = new Promise(function(resolve, reject) {

        try {
            const destparams = {
                Bucket: "jacek-lambda-1",
                Key: "LVR-"+csid+"-"+sequence,
                Body: bodyStr,
                ContentType: "application/json"
            };

            console.info("saving VG response to S3");
            const putResult = s3.putObject(destparams, function(err, data) {
                if (err) {
                    console.log(err, err.stack); // an error occurred
                    reject(err.message);
                }
                else {
                    console.log("S3 ok: "+data);           // successful response
                    resolve(jsonResponseFromLambda({stop:true}));
                }
              });
        } catch (error) {
            console.error(error);
            reject(error.message);
        } 
    });
    return promise;
}

function handleUnexpectedRequest(method) {
    console.warn("handle Unexpected request");
}
