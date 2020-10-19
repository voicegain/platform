/**
The MIT License

Copyright (c) Voicegain.

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
*/

// start of endpoint configuration
const optionsMock = {
    hostname: 'rasa-nlu.app.mock.io',
    port: 443,
    path: '/flight/start',
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    }
};

const optionsRasa = {
    hostname: 'ec2-18-224-xxx-yy.us-east-2.compute.amazonaws.com',
    port: 5005,
    path: '/webhooks/rest/webhook',
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    }
};    

const optionsVoicegain =  {
    hostname: 'api.voicegain.ai',
    port: 443,
    path: '/v1/asr/transcribe/async',
    method: 'POST',
    headers: {
        'Authorization' : 'Bearer <JWT Token Here>',
        'Content-Type': 'application/json'
     }
}; 

const lambdaCallbackUrl = "https://dqe7mrxxxx.execute-api.us-east-2.amazonaws.com/default/twilioVoicegainRasa1?seq=";
const s3bucket = "my-bucket-lambda-1";
// end of endpoint configuration

// external requireds
const AWS = require('aws-sdk');
const https = require('https');
const http = require('http');
const s3 = new AWS.S3();

// chose how to connect to RASA
const options = optionsRasa;
const httpInvoker = http;

// initial message to RASA - it will trigger the "how can i help you question"
const sayHiToRasa = "Hi";

// keeps track of session and the turn in the session 
let csid = "no-csid";
let sequence = 0;

/////////////////////
// Lambda Entry Point
/////////////////////
exports.handler = async (event, context) => {

    console.info("START "+JSON.stringify(event)); // debug

    // get parameters from incoming AWS Lambda request
    const method = event.requestContext.http.method; // POST, PUT, or DELETE expected
    const queryParams = event.queryStringParameters;
    const bodyStr = event.body;
    console.info("method="+method);

    if(method == "GET") {
        // Android makes callbacks using GET
        return handleAndroidRequest(context, queryParams);
    }
    else if (method == "POST") {
        // Voicegain makes callbacks using POST
        return handleVoicegainRequest(bodyStr, queryParams);
    }
    else {
        return handleUnexpectedRequest(method);
    }
}

// Android callback handler
// it has two flows
// 1) for initial request at start of session
// 2) for subsequent requests within session - it needs to wait for data from Voicegain
//
function handleAndroidRequest(context, queryParams) {
    console.info("handle Android request: "+queryParams.seq);

    if(typeof queryParams.seq != 'undefined') {
        // we are already in a session - turn sequence is provided
        sequence = parseInt(queryParams.seq, 10);
    }
    console.info("Sequence: "+sequence);    

    // local (customer) session id defaults to AWS request id
    csid = context.awsRequestId;
    if(typeof queryParams.csid != 'undefined') {
        // for session in progress use csid from the query parameter
        csid = queryParams.csid;
    }
    console.info("    CSID: "+csid);  

    // initiate recognition status and recognized utterance
    let vgRecoStatus = "ERROR"; // recognition result status
    let messageForRasa = "none"; // recognized utterance - it will be sent as answer to RASA

    const promise = new Promise(function(resolve, reject) {
        if(sequence == 0) { // start of session
            console.info("START of session");
            // start of session, say "Hi" to RASA
            messageForRasa = sayHiToRasa;
            handleRasaThenVG(messageForRasa, vgRecoStatus, resolve, reject);
        }
        else  { // mid session
            console.info('waiting for data from Voicegain');
            try {
                const params = {
                    Bucket: s3bucket,
                    Key: s3key(csid, sequence),
                };
                s3.waitFor('objectExists', params, function (err, metadata) {  
                    if (err) {  
                        // waiting failed
                        console.log(err, err.stack);
                        reject(err.message);  
                    } else {  
                        // object exists -> now get it
                        console.info("S3 obj exists: "+JSON.stringify(metadata));  // debug
                        s3.getObject(params, function(err, data) {
                            if (err) {
                                console.warn("failed to get from s3");
                                console.log(err, err.stack); // an error occurred
                                reject(err.message);
                            }
                            else {
                                const strBody = data.Body.toString();
                                console.log("S3 ok: "+strBody);           // successful response
                                const dataBody = JSON.parse(strBody);
                                const result = dataBody.result;
                                vgRecoStatus = result.status; // recognition status
                                console.info("Result Status: "+vgRecoStatus);
        
                                if(vgRecoStatus == 'MATCH') {
                                    // workaround for a bug in Voicegain 1.17.0
                                    if(typeof result.transcript == 'undefined') {
                                        vgRecoStatus == 'NOMATCH';
                                    }
                                    else {
                                        messageForRasa = result.transcript; // recognized utterance
                                    }
                                }
                                
                                handleRasaThenVG(messageForRasa, vgRecoStatus, resolve, reject);
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

// accomplishes the following
// 1) send message to RASA and get a response
function handleRasaThenVG(messageForRasa, vuiResult, resolve, reject) {
    if(messageForRasa == 'none') {
        if(vuiResult=='NOINPUT') {
            voicegainThenAndroid(resolve, reject, "I did not hear you", "Please speak");
        }
        else if(vuiResult=='NOMATCH') {
            voicegainThenAndroid(resolve, reject, "I did not get it", "Can you say it again");
        }
    }
    else {
        // request to be sent to RASA
        let rasaReqBody = {
            sender : "voicegain-"+csid, // sender name unique to this session
            message : messageForRasa // the message for RASA
        };
        console.info("Message for RASA: "+messageForRasa);

        // function that will send request to RASA and process the response
        const rasaReq = httpInvoker.request(options, (res) => {
            if (res.statusCode < 200 || res.statusCode >= 300) {
                console.warn(`RASA error response: `);
                // say the error message and hang up
                resolve(jsonResponseFromLambda( bodyForAndroidErrorResponse("Bad response from Rasa: code "+res.statusCode) ));
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

                // make request to Voicegain to start recognition
                // and the return response to Android
                voicegainThenAndroid(resolve, reject, statement, question);

            });
        });
        rasaReq.on('error', (e) => {
            // say the error message and hang up
            resolve(jsonResponseFromLambda( bodyForAndroidErrorResponse("Error invoking Rasa: "+e.message) ));
        });
        // send the request
        const rasaReqStr = JSON.stringify(rasaReqBody);
        console.info("To RASA: "+rasaReqStr);
        rasaReq.write(rasaReqStr);
        rasaReq.end();
    }

}

// make request to Voicegain to start recognition
// and the return response to Android
function voicegainThenAndroid(resolve, reject, statement, question) {
    const vgReq = https.request(optionsVoicegain, (res) => {
        if (res.statusCode < 200 || res.statusCode >= 300) {
            console.warn(`VG error response: `+res.statusCode);
            // say the error message and hang up
            resolve(jsonResponseFromLambda( bodyForAndroidErrorResponse("Bad response from Voicegain: code "+res.statusCode) ));
        }
        var vgBody = [];
        // assemble data received from VG
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
            // we are looking for websocket url so that Android can stream audio to it
            const audio = vgBody.audio;
            const stream =  audio.stream;
            const websocketUrl = stream.websocketUrl;

            console.info("websocketUrl: "+websocketUrl);
            // have resolve return the response to Android
            resolve(jsonResponseFromLambda( bodyForAndroidResponse(csid, sequence, websocketUrl, statement, question) ));
        });
    });
    vgReq.on('error', (e) => {
        // say the error message and hang up
        resolve(jsonResponseFromLambda( bodyForAndroidErrorResponse("Error invoking Voicegain: "+e.message) ));
    });    
    // send the request
    vgReq.write(JSON.stringify(bodyForVgRequest(csid, sequence)));
    vgReq.end();

}

// Generate body for Voicegain request to start transcription
function bodyForVgRequest(csid, sequence) {
    let body = {};
    body.sessions = [{
        asyncMode : "REAL-TIME",
        callback : { uri : lambdaCallbackUrl+(sequence+1)+"&csid="+csid },
        content : { full : ["transcript"] }
    }];
    body.audio = {
        source : { stream : { protocol : "TWIML"} },
        format : "PCMU",
        rate : 8000,
        channels : "mono",
        capture : false
    };
    body.settings = {
        asr : {
            startInputTimers : false,
            confidenceThreshold : 0.25,
            noInputTimeout : 5000,
            completeTimeout : 2000
        }
    };

    console.info("body for VG: "+JSON.stringify(body));
    return body;
}

// Generate response for Android in case of an error
function bodyForAndroidErrorResponse(errMsg) {
    let body = [
        { say : cleanupString(errMsg) },
        { say : 'Please call back later. Goodbye!'} 
    ];
    return body;
}

// Generate response for Android which 
// 1) optionally says something
// 2) makes a <Connect><Stream> request to Voicegain 
function bodyForAndroidResponse(csid, sequence, websocketUrl, statementPrompt, questionPrompt) {
    let body = [];
    if(typeof statementPrompt !== 'undefined') {
        let say = { say : cleanupString(statementPromp };
        body.push(say);
    }
    const stream = {
        url : websocketUrl,
        parameters : [
            {name : bargeIn, value : enable},
            {name : voice, value : claire},
            {name : prompt01, value : cleanupString(questionPrompt)}
        ]
    }; 
    body.push(stream);
    const redirect = {
        method : GET,
        url : lambdaCallbackUrl+(sequence+1)+"&amp;csid="+csid
    }
    body.push(redirect);
    return body;
}

// json response from Lambda
function jsonResponseFromLambda(respBody) {
    const respBodyStr = JSON.stringify(respBody);
    console.info("Response for VG: "+respBodyStr);

    // tell AWS Lambda how to respond
    const response = {
        statusCode: 200,
        headers: { 'Content-Type': 'application/json' },
        body: respBodyStr
    };
    return response;
}

// sometimes RASA message strings have brackets
function cleanupString(str) {
    return str.replace(/[\[\]]/g, '');
}

// Handle callback from Voicegain recognition
// this will just store callback payload from Voicegain into S3 for this csid and sequence
function handleVoicegainRequest(bodyStr, queryParams) {
    console.info("handle VG request: "+bodyStr);

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
                Bucket: s3bucket,
                Key: s3key(csid, sequence),
                Body: bodyStr,
                ContentType: "application/json"
            };

            console.info("saving VG response to S3");
            s3.putObject(destparams, function(err, data) {
                if (err) {
                    console.log(err, err.stack); // an error occurred
                    reject(err.message);
                }
                else {
                    console.log("S3 ok: "+data);           // successful response
                    // tell Voicegain that we are done processing callback
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

// just in case
function handleUnexpectedRequest(method) {
    console.warn("handle Unexpected request");
    return new Promise(function(resolve, reject) {
        reject("Do not know how to handle: "+method);
    });
}

// single place to compose key to s3 
function s3key(csid, sequence) {
    return "LVR-"+csid+"-"+sequence;
}
