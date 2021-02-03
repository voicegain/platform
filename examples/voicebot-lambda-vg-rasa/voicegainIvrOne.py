'''
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
'''


import json, re, urllib3

options = {
    "url" : 'http://ec2-18-224-xxx-xx.us-east-2.compute.amazonaws.com:5005/webhooks/rest/webhook',
    "headers" : {
        'Content-Type': 'application/json'
    }
};  

# sometimes RASA message strings have brackets, need to remove them
def cleanupString(str):
    return re.sub(f"[\[\]]", '', str)

# generate question data response for VG
def questionData(sequence, statementPrompt, questionPrompt):
    # for POST or PUT send back the data received from RASA
    question = {
        # in Voicegain each question needs a name 
        "name" : "answer"+str(sequence),
        "audioResponse" : {
            # the bargineable question prompt 
            "questionPrompt" : cleanupString(questionPrompt),
            # some standard timeouts
            "noInputTimeout" : 5000,
            # complete timeout may be reduced to give faster responses
            "completeTimeout" : 2000
        },
        # set the voice, can be commented out if the default is to be used
        "audioProperties" : { "voice" : "catherine"}
    }

    if statementPrompt != "":
        # non-bargeinable intro prompt
        question['text'] = cleanupString(statementPrompt)   

    return question

# package response into what Lambda understands
def responseFromLambda(respBody):
    respBodyStr = json.dumps(respBody)
    print("Response for VG: "+respBodyStr)
    # tell AWS Lambda how to respond
    response = {
        "statusCode" : 200,
        "headers" : {
            'Content-Type': 'application/json',
        },
        "body" : respBodyStr
    }
    return response

def lambda_handler(event, context):
    #initial message to RASA - it will trigger the "how can i help you" question
    sayHiToRasa = "Hi"
    # final message to RASA
    sayByeToRasa = "Goodbye" 

    # message to RASA in the middle of the dialogue
    # will be overwritten by actual response captured by voicegain
    messageForRasa = "none"

    print("START   event "+json.dumps(event))   # debug
    
    method = event['requestContext']['http']['method']

    queryParams = event.get('queryStringParameters')
    bodyStr = event['body']
    body = json.loads(bodyStr)
    sid = body['sid']; # Voicegain session id
    seq = body.get('sequence') # sequence within single Voicegain session

    if seq is None:
        seq = 0

    print('method: '+method)
    print('   sid: '+sid)
    print('   seq: '+str(seq))

    # local (customer) session id defaults to AWS request id
    csid = context.aws_request_id
    vuiResult = "ERROR" # speech recognition status (VUI = voice UI)

    # initialize response to be sent back to Voicegain 
    respBody = { "sid" : sid }

    if method == 'POST': # start of session
        respBody['sequence'] = seq
        messageForRasa = sayHiToRasa
    elif (method == 'PUT'): # mid session
        respBody['sequence'] = queryParams['seq'] # sequence is obtained from query param 
        csid = queryParams['csid'] # customer session id also from query param
        
        # search voicegain IVR events for input, i.e. answer
        events = body['events']

        for event in events:
            if event['type'] == "input":
                vuiResult = event['vuiResult']
                # only in case of match we will send data to RASA
                if vuiResult == "MATCH":
                    # workaround for a bug in Voicegain 1.17.0
                    if event.get('vuiAlternatives') is None:
                        vuiResult == "NOMATCH"
                    else:
                        vuiAlt = event['vuiAlternatives'][0]; # pick the top alternative
                        # set message to RASA based on the utterance captured by Voicegain
                        messageForRasa = vuiAlt['utterance'] 
                break
    else:
        # assuming end session (DELETE)
        respBody['sequence'] = queryParams['seq']
        csid = queryParams['csid']
        messageForRasa = sayByeToRasa
    
    # set the local sid in the response
    respBody['csid'] = csid

    if messageForRasa == 'none':
        # speech recognition returned no utterance        
        if vuiResult=='NOINPUT':
            # generic reprompt in case of no input            
            respBody['question'] = questionData(respBody.sequence, "I did not hear you", "Please speak")
        elif vuiResult=='NOMATCH':
            # generic reprompt in case of no match
            respBody['question'] = questionData(respBody.sequence, "I did not get it", "Can you say it again")
        
        # just return the generic reprompt to VG
        return responseFromLambda(respBody)
    else:
        # request to be sent to RASA
        rasaReq = {
            "sender" : "voicegain-"+csid, # sender name unique to this session
            "message" : messageForRasa # the message for RASA - this is the recognized utterance
        }
        print("Message for RASA: "+messageForRasa)
        http = urllib3.PoolManager()

        rasa_response = http.urlopen("POST", options['url'], headers=options['headers'], body=json.dumps(rasaReq))
        print("Response from RASA: "+str(rasa_response))
        decoded_r = rasa_response.data.decode("utf8")
        print("Response from RASA: "+str(decoded_r))
        body = json.loads(decoded_r)

        # process the response from RASA
        # response from RASA is an array of statements followed by a question
        # we concatenate the statements first 
        statement = ""
        i=0
        while i<len(body)-1:
            statement += " "+body[i]['text']
            i  += 1
        print("RASA statement: "+statement)
        # final element is the actual question from RASA
        question = body[i]['text']
        print("RASA  question: "+question)

        # now fill in the data for the response to be sent back to Voicegain
        if method=='DELETE':
            # acknowledge termination
            respBody['termination'] = "normal"
            # note: we are ignoring whatever RASA may have returned                        
        else:
            # for POST or PUT send the data received from RASA
            respBody['question'] = questionData(respBody['sequence'], statement, question)
        
        # send the good response via resolve
        return responseFromLambda(respBody)