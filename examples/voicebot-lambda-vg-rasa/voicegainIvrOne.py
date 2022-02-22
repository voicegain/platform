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

# these are the options for the web request to the Bot
options = {
    "url" : 'http://ec2-18-xxxxxx-98.us-east-2.compute.amazonaws.com:5005/webhooks/rest/webhook',
    #"url" : 'https://anxxxxxy3.execute-api.us-east-2.amazonaws.com/default/EchoBot',
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
            "noInputTimeout" : 5005,
            # complete timeout may be reduced to give faster responses
            "completeTimeout" : 1001
        },
        # set the voice, can be commented out if the default is to be used
        "audioProperties" : { "voice" : "catherine"}
    }

    if statementPrompt != "":
        # non-bargeinable intro prompt
        question['text'] = cleanupString(statementPrompt)   

    return question

# package response into what AWS Lambda understands
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
    #initial message to the Bot - it will trigger the "how can i help you" question
    sayHiToBot = "Hi"
    # final message to the Bot
    sayByeToRasa = "Goodbye" 

    # message to the Bot in the middle of the dialogue
    # will be overwritten by actual response captured by Voicegain
    messageForBot = "none"

    # Extract method and sid from received Lambda request 
    print("START   event "+json.dumps(event))   # debug
    
    method = event['requestContext']['http']['method']

    queryParams = event.get('queryStringParameters')
    bodyStr = event['body']
    body = json.loads(bodyStr)
    sid = body['sid']; # Voicegain session id
    seq = 0 # initial value

    print('method: '+method) # POST, PUT, DELETE
    print('   sid: '+sid)
    print('   seq: '+str(seq))

    # local (customer) session id defaults to AWS request id
    csid = context.aws_request_id
    vuiResult = "ERROR" # speech recognition status (VUI = voice UI)

    # initialize response to be sent back to Voicegain 
    respBodyForVG = { "sid" : sid }

    if method == 'POST': # start of session
        respBodyForVG['sequence'] = seq
        messageForBot = sayHiToBot
    elif (method == 'PUT'): # mid session
        respBodyForVG['sequence'] = queryParams['seq'] # sequence is obtained from query param 
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
                        messageForBot = vuiAlt['utterance'] 
                break
    else:
        # assuming end session (DELETE)
        respBodyForVG['sequence'] = queryParams['seq']
        csid = queryParams['csid']
        messageForBot = sayByeToRasa
    
    # set the local sid in the response
    respBodyForVG['csid'] = csid

    if messageForBot == 'none':
        # speech recognition returned no utterance        
        if vuiResult=='NOINPUT':
            # generic reprompt in case of no input            
            respBodyForVG['question'] = questionData(respBodyForVG.sequence, "I did not hear you", "Please speak")
        elif vuiResult=='NOMATCH':
            # generic reprompt in case of no match
            respBodyForVG['question'] = questionData(respBodyForVG.sequence, "I did not get it", "Can you say it again")
        
        # just return the generic reprompt to VG
        return responseFromLambda(respBodyForVG)
    else:
        # request to be sent to Bot
        sender = "voicegain-"+csid # sender name unique to this session
        statement, question = make_bot_request(sender, messageForBot)

        # now fill in the data for the response to be sent back to Voicegain
        if method=='DELETE':
            # acknowledge termination
            respBodyForVG['termination'] = "normal"
            # note: we are ignoring whatever RASA may have returned                        
        else:
            # for POST or PUT send the data received from RASA
            respBodyForVG['question'] = questionData(respBodyForVG['sequence'], statement, question)
        
        # send the good response via resolve
        return responseFromLambda(respBodyForVG)

# This function make a request to the Bot logic
# inputs are (this is what we are sending to the Bot):
# * sender : some unique identifier of this conversation session
# * messageForBot : this is what voicegain recognized as a response to the question
# outputs are (this is what we receive from the Bot):
# * statement : this is the prompt or prompts that will be played suing TTS to the caller - may be empty
# * question : this is the question that follows the (optional) prompt(s)
#
# The implementation below is specific for RASA Bot
# You will need to change this if you wan to use a different Bot framework
def make_bot_request(sender, messageForBot):
    rasaReq = {
            "sender" : sender,
            "message" : messageForBot # the message for RASA - this is the recognized utterance
        }
    print("Message for RASA: "+messageForBot)
    http = urllib3.PoolManager()

    rasa_response = http.urlopen("POST", options['url'], headers=options['headers'], body=json.dumps(rasaReq))
    print("    Raw response from RASA: "+str(rasa_response))
    decoded_r = rasa_response.data.decode("utf8")
    print("Decoded response from RASA: "+str(decoded_r))
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
    return statement,question
        