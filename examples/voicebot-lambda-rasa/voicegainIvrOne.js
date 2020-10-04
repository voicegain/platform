const https = require('https');
const http = require('http');

exports.handler = async (event, context) => {
// https://my-rasa-app.smartmock.io/flight
// http://ec2-18-224-xxx-yy.us-east-2.compute.amazonaws.com:5005/webhooks/rest/webhook

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

    const sayHiToRasa = "Hi";
    const sayByeToRasa = "Goodbye";
    let messageForRasa = "none";

    console.info("START "+JSON.stringify(event));

    const method = event.requestContext.http.method;
    const queryParams = event.queryStringParameters;
    const bodyStr = event.body;
    const body = JSON.parse(bodyStr);
    const sid = body.sid;
    const seq = body.sequence;
    let csid = context.awsRequestId;

    console.info("method="+method);
    console.info("   sid="+sid);

    const respBody = {};
    respBody.sid = sid;
    
    if(method == 'POST') { // start of session
        respBody.sequence = seq;
        messageForRasa = sayHiToRasa;
    }
    else if (method == 'PUT') { // mid session
        respBody.sequence = queryParams.seq;
        csid = queryParams.csid;
        // search events for input, i.e. answer

        const events = body.events;

        messageForRasa = "I am lost";

        for(const event of events) {
            if(event.type == "input") {
                const vuiAlt = event.vuiAlternatives[0];
                const utt = vuiAlt.utterance;
                messageForRasa = utt;
                break;
            }
        }
    } 
    else { // assuming end session
        respBody.sequence = queryParams.seq;
        csid = queryParams.csid;
        messageForRasa = sayByeToRasa;
    }

    respBody.csid = csid;

    const promise = new Promise(function(resolve, reject) {

        let rasaReq = {};
        rasaReq.sender = "voicegain-"+csid;
        rasaReq.message = messageForRasa;
        console.info("Message for RASA: "+messageForRasa);

        const req = httpInvoker.request(options, (res) => {
            if (res.statusCode < 200 || res.statusCode >= 300) {
                return reject(new Error('statusCode=' + res.statusCode));
            }
            var body = [];
            res.on('data', function(chunk) {
                body.push(chunk);
            });
            res.on('end', function() {
                try {
                    const bodyStr = Buffer.concat(body).toString();
                    console.info("Response from RASA: "+bodyStr);
                    body = JSON.parse(bodyStr);
                } catch(e) {
                    reject(e);
                }

                // response from RASA is an array of statements followed by a question

                let statement = "";
                let i=0;
                while(i<body.length-1) {
                    statement += " "+body[i++].text;
                }

                const question = body[i].text;

                if(method=='DELETE') {
                    respBody.termination = "normal";
                }
                else {
                    respBody.question = {};
                    respBody.question.name = "answer"+respBody.sequence;
                    respBody.question.text = statement+". "+question;
                    respBody.question.audioResponse = {};
                    respBody.question.audioResponse.bargeIn = true;
                    respBody.question.audioResponse.noInputTimeout = 5000;
                    respBody.question.audioResponse.completeTimeout = 2000;
                }
                const respBodyStr = JSON.stringify(respBody);
                console.info("Response for VG: "+respBodyStr);

                const response = {
                    statusCode: 200,
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: respBodyStr
                };
                resolve(response);
              });
          });
          req.on('error', (e) => {
            reject(e.message);
          });
          // send the request
          //do the request
          req.write(JSON.stringify(rasaReq));
          req.end();

        
    });
    return promise;
       
};
