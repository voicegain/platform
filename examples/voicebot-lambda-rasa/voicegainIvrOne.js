// pick one according to the protocol you will use
const https = require('https');
const http = require('http');

exports.handler = async (event, context) => {

// for switching between mock and real RASA back-end     
// https://my-rasa-app.smartmock.io/flight
// http://ec2-18-224-xxx-yy.us-east-2.compute.amazonaws.com:5005/webhooks/rest/webhook

    // options for making http request to RASA api
    const optionsMock = {
        hostname: 'my-rasa-app.smartmock.io',
        port: 443,
        path: '/flight',
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

    const options = optionsRasa;
    const httpInvoker = http;

   // initial message to RASA - it will trigger the "how can i help you question"
   const sayHiToRasa = "Hi";
   // final message to RASA
   const sayByeToRasa = "Goodbye"; 
   // message to RASA in the middle of the dialogue
   // will be overwritten by actual response captured by voicegain
   let messageForRasa = "none";

   console.info("START "+JSON.stringify(event));

   // get parameters from incoming AWS Lambda request
   const method = event.requestContext.http.method; // POST, PUT, or DELETE expected
   const queryParams = event.queryStringParameters;
   const bodyStr = event.body;
   const body = JSON.parse(bodyStr);
   const sid = body.sid; // Voicegain session id
   const seq = body.sequence; // sequence within single voicegain session

   console.info("method="+method);
   console.info("   sid="+sid);
   
   // local (customer) session id defaults to AWS request id
   let csid = context.awsRequestId;
   let vuiResult = "ERROR";

   // init response to be sent back to Voicegain 
   const respBody = {};
   respBody.sid = sid;
   
   if(method == 'POST') { // start of session
       respBody.sequence = seq;
       messageForRasa = sayHiToRasa;
   }
   else if (method == 'PUT') { // mid session
       respBody.sequence = queryParams.seq; // sequence is obtained from query param 
       csid = queryParams.csid; // customer session id from query param
       
       // search events for input, i.e. answer
       const events = body.events;

       for(const event of events) {
           if(event.type == "input") {
               vuiResult = event.vuiResult;
               // only in case of match we will send data to RASA
               if(vuiResult == "MATCH") {
                   const vuiAlt = event.vuiAlternatives[0];
                   const utt = vuiAlt.utterance;
                   // set message to RASA based on the utterance captured by Voicegain
                   messageForRasa = utt; 
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

   respBody.csid = csid;

   if(messageForRasa == 'none') {
       if(vuiResult=='NOINPUT') {
           respBody.question = questionData(respBody.sequence, "I did not hear you", "Please speak");
       }
       else if(vuiResult=='NOMATCH') {
           respBody.question = questionData(respBody.sequence, "I did not get it", "Can you say it again");
       }
       const promise = new Promise(function(resolve, reject) {
           resolve(responseFromLambda(respBody));
       });
       return promise;
   }
   else {
       // Promise that we will return back to AWS Lambda 
       const promise = new Promise(function(resolve, reject) {

           // init request to be sent to RASA
           let rasaReq = {};
           rasaReq.sender = "voicegain-"+csid; // sender name unique to this session
           rasaReq.message = messageForRasa; // the message for RASA
           console.info("Message for RASA: "+messageForRasa);

           // function that will send request to RASA and process the response
           const req = httpInvoker.request(options, (res) => {
               if (res.statusCode < 200 || res.statusCode >= 300) {
                   return reject(new Error('statusCode=' + res.statusCode));
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

                   // now fill in the data for the response to be sent back to Voicegain
                   if(method=='DELETE') {
                       // acknowledge termination
                       respBody.termination = "normal";
                   }
                   else {
                       // for POST or PUT send the data received from RASA
                       respBody.question = questionData(respBody.sequence, statement, question)
                   }
                   // pass the good response to resolve
                   resolve(responseFromLambda(respBody));
               });
           });
           req.on('error', (e) => {
               reject(e.message);
           });
           // send the request
           req.write(JSON.stringify(rasaReq));
           req.end();
       });
       return promise;  
   }
}

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

function questionData(sequence, statementPrompt, questionPrompt) {
   // for POST or PUT send the data received from RASA
   let question = {};
   // in Voicegain each question needs a name 
   question.name = "answer"+sequence;
   // non-bargeinable intro prompt
   if(statementPrompt!="") {
       question.text = cleanupString(statementPrompt); 
   }
   question.audioResponse = {};
   // now the bargineable 
   question.audioResponse.questionPrompt = cleanupString(questionPrompt);
   // some standard timeouts
   question.audioResponse.noInputTimeout = 5000;
   question.audioResponse.completeTimeout = 2000;
   // set the voice
   question.audioProperties = {}; 
   question.audioProperties.voice = "catherine";
   return question;
}

function cleanupString(str) {
   return str.replace(/[\[\]]/g, '');
}
