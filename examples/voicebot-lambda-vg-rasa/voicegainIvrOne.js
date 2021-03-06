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
// end of endpoint configuration

// external requireds
const https = require('https');
const http = require('http');

// chose how to connect to RASA
const options = optionsRasa;
const httpInvoker = http;

/////////////////////
// Lambda Entry Point
/////////////////////
exports.handler = async (event, context) => {

    // initial message to RASA - it will trigger the "how can i help you" question
    const sayHiToRasa = "Hi";
    // final message to RASA
    const sayByeToRasa = "Goodbye"; 

    // message to RASA in the middle of the dialogue
    // will be overwritten by actual response captured by voicegain
    let messageForRasa = "none";

    console.info("START "+JSON.stringify(event)); // debug

    // get parameters from incoming AWS Lambda request
    const method = event.requestContext.http.method; // POST, PUT, or DELETE expected
    const queryParams = event.queryStringParameters;
    const bodyStr = event.body;
    const body = JSON.parse(bodyStr);
    const sid = body.sid; // Voicegain session id
    const seq = body.sequence; // sequence within single Voicegain session

    console.info("method="+method);
    console.info("   sid="+sid);
    
    // local (customer) session id defaults to AWS request id
    let csid = context.awsRequestId;
    let vuiResult = "ERROR"; // speech recognition status (VUI = voice UI)

    // initialize response to be sent back to Voicegain 
    const respBody = { sid : sid };
    
    if(method == 'POST') { // start of session
        respBody.sequence = seq;
        messageForRasa = sayHiToRasa;
    }
    else if (method == 'PUT') { // mid session
        respBody.sequence = queryParams.seq; // sequence is obtained from query param 
        csid = queryParams.csid; // customer session id also from query param
        
        // search voicegain IVR events for input, i.e. answer
        const events = body.events;

        for(const event of events) {
            if(event.type == "input") {
                vuiResult = event.vuiResult;
                // only in case of match we will send data to RASA
                if(vuiResult == "MATCH") {
                    // workaround for a bug in Voicegain 1.17.0
                    if(typeof event.vuiAlternatives == 'undefined') {
                        vuiResult == "NOMATCH";
                    }
                    else {
                        const vuiAlt = event.vuiAlternatives[0]; // pick the top alternative
                        // set message to RASA based on the utterance captured by Voicegain
                        messageForRasa = vuiAlt.utterance; 
                    }
                }
                break;
            }
        }
    } 
    else { // assuming end session (DELETE)
        respBody.sequence = queryParams.seq;
        csid = queryParams.csid;
        messageForRasa = sayByeToRasa;
    }

    // set the local sid in the response
    respBody.csid = csid;

    if(messageForRasa == 'none') {
        // speech recognition returned no utterance
        if(vuiResult=='NOINPUT') {
            // generic reprompt in case of no input
            respBody.question = questionData(respBody.sequence, "I did not hear you", "Please speak");
        }
        else if(vuiResult=='NOMATCH') {
            // generic reprompt in case of no match
            respBody.question = questionData(respBody.sequence, "I did not get it", "Can you say it again");
        }
        // just return the generic reprompt to VG
        return new Promise(function(resolve, reject) {
            resolve(responseFromLambda(respBody));
        });
    }
    else {
        // Promise that we will return back to AWS Lambda 
        const promise = new Promise(function(resolve, reject) {

            // request to be sent to RASA
            let rasaReq = {
                sender : "voicegain-"+csid, // sender name unique to this session
                message : messageForRasa // the message for RASA - this is the recognized utterance
            };
            console.info("Message for RASA: "+messageForRasa);

            // function that will send request to RASA and process the response
            const req = httpInvoker.request(options, (res) => {
                if (res.statusCode < 200 || res.statusCode >= 300) {
                    // TODO: add error message to say
                    return reject(new Error('statusCode=' + res.statusCode));
                }
                var body = [];
                // assemble http data received from RASA
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

                    // now fill in the data for the response to be sent back to Voicegain
                    if(method=='DELETE') {
                        // acknowledge termination
                        respBody.termination = "normal";
                        // note: we are ignoring whatever RASA may have returned
                    }
                    else {
                        // for POST or PUT send the data received from RASA
                        respBody.question = questionData(respBody.sequence, statement, question);
                    }
                    // send the good response via resolve
                    resolve(responseFromLambda(respBody));
                });
            });
            req.on('error', (e) => {
                // TODO: add error message to say
                reject(e.message);
            });
            // send the request
            const rasaReqStr = JSON.stringify(rasaReq);
            console.info("To RASA: "+rasaReqStr);
            req.write(rasaReqStr);
            req.end();
        });
        return promise;  
    }
}

// package response into what Lambda understands
function responseFromLambda(respBody) {
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

// generate question data response for VG
function questionData(sequence, statementPrompt, questionPrompt) {
    // for POST or PUT send back the data received from RASA
    let question = {
        // in Voicegain each question needs a name 
        name : "answer"+sequence,
        audioResponse : {
            // the bargineable question prompt 
            questionPrompt : cleanupString(questionPrompt),
            // some standard timeouts
            noInputTimeout : 5000,
            // complete timeout may be reduced to give faster responses
            completeTimeout : 2000 
        },
        // set the voice, can be commented out if the default is to be used
        audioProperties : { voice : "catherine"}
    };

    if(statementPrompt!="") {
        // non-bargeinable intro prompt
        question.text = cleanupString(statementPrompt); 
    }   
    return question;
}

// sometimes RASA message strings have brackets, need to remove them
function cleanupString(str) {
    return str.replace(/[\[\]]/g, '');
}
