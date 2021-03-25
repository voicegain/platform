"""
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
"""

import json
import boto3
import time
from string import Template 

s3BucketName='jacek-lambda-1'
#jsonIvrDefKey='PizzaPizza_3_json_good'
jsonIvrDefKey='outbound-survey-ivr_json_10'
declarativeJSON = {}

def setErrorResponse(debug,detail,reason):
    errorResponse = {
        "debug":debug,
        "error":{
            "detail":detail,
            "reason":reason
        }
    }
    return errorResponse

def setNewStateInformation(stateInformation,seq,nextState,noInputCount,noMatchCount,vuiResult):
    newStateInformation =  stateInformation
    # newStateInformation = {
    #     "sid":stateInformation['sid'],
    #     "csid":stateInformation['csid'],
    #     "sequence":seq,
    #     "state":nextState,
    #     "noInputCount":noInputCount,
    #     "noMatchCount":noMatchCount,
    #     "vuiResult":vuiResult
    # }
    
    # let's merge instead
    
    newStateInformation['sequence'] = seq
    newStateInformation['state'] = nextState
    newStateInformation['noInputCount'] = noInputCount
    newStateInformation['noMatchCount'] = noMatchCount
    newStateInformation['vuiResult'] = vuiResult
    
    return newStateInformation

def finalResponse(statusCode,response,newStateInformation):
    return{
        "statusCode":statusCode,
        "body":response,
        "stateInformation":newStateInformation
    }


#VOID is simply a connecting function
def voidFunc(body,stateInformation):
    t1 = time.time()
    currState = stateInformation["state"]
    nextState = declarativeJSON[currState]["next"]
    funcType = declarativeJSON[nextState]["type"]
    seq = stateInformation["sequence"]
    noInputCount = stateInformation['noInputCount']
    noMatchCount = stateInformation['noMatchCount']
    vuiResult = stateInformation['vuiResult']
    newStateInformation = setNewStateInformation(stateInformation,seq,nextState,noInputCount,noMatchCount,vuiResult)
    elapsed_time = time.time() - t1
    logText = "Time spent in voidFunc is "+str(elapsed_time)+" seconds"
    print(logText)
    return getNormalFuncs(funcType,body,newStateInformation)

#This function handles OUTPUT states and returns response to Voicegain
def outputFunc(body,stateInformation):
    t2 = time.time()
    try:
        currState = stateInformation["state"]
        seq = int(stateInformation['sequence'])+1 #Update seq in functions which return a response
        noInputCount = stateInformation['noInputCount']
        noMatchCount = stateInformation['noMatchCount']
        vuiResult = stateInformation['vuiResult']
        newStateInformation = setNewStateInformation(stateInformation,seq,currState,noInputCount,noMatchCount,vuiResult)
        text = declarativeJSON[currState]['prompt']
        statusCode = 200
        response = {
            "csid": stateInformation['csid'],
            "sid":stateInformation['sid'],
            "sequence":seq,
            "prompt":{
                "text":text,
                "audioProperties":{
                    "voice":declarativeJSON[currState]['voice']
                }
            }
        }
    except Exception as e:
        statusCode = 500
        debug = "Something wrong with the outputFunc"
        detail = "outputFunc failed execution: exception="+str(e)
        reason = "Internal error"
        response = setErrorResponse(debug,detail,reason)
        newStateInformation = stateInformation
    elapsed_time = time.time() - t2
    logText = "Time spent in outputFunc is "+str(elapsed_time)+" seconds"
    print(logText)
    return finalResponse(statusCode,response,newStateInformation)

#This function acknowledges the completion of OUTPUT states
def ackOutputFunc(body,stateInformation):
    t3 = time.time()
    currState = stateInformation['state']
    nextState = getNextState(currState)
    funcType = declarativeJSON[nextState]['type']
    seq = stateInformation["sequence"]
    noInputCount = stateInformation['noInputCount']
    noMatchCount = stateInformation['noMatchCount']
    vuiResult = stateInformation.get('vuiResult')
    newStateInformation = setNewStateInformation(stateInformation,seq,nextState,noInputCount,noMatchCount,vuiResult)
    elapsed_time = time.time() - t3
    logText = "Time spent in ackOutputFunc is "+str(elapsed_time)+" seconds"
    print(logText)
    return getNormalFuncs(funcType,body,newStateInformation)

#This function handles INPUT states    
def inputFunc(body,stateInformation):
    
    t4 = time.time()
    currState = stateInformation['state']
    seq = int(stateInformation['sequence'])+1
    noInputCount = stateInformation['noInputCount']
    noMatchCount = stateInformation['noMatchCount']
    #By default, vuiResult in #saveS3 has value 'None'. So for the first time the inputFunc is invoked for a specific state, 
    #'else' condition becomes true and default prompt is played
    
    #If it is a NOMATCH
    if(stateInformation['vuiResult']=='NOMATCH' or stateInformation['vuiResult']=='NOMATCH-CONF'):
        noMatchCount = int(noMatchCount)+1
        
        if(noMatchCount <= declarativeJSON[currState]['noMatchMax']):
            if(stateInformation['vuiResult']=='NOMATCH'):
                #text = declarativeJSON[currState]['noMatch'][noMatchCount-1] #In case of normal NOMATCH
                text = declarativeJSON['DEFAULTS']['prefixes']['noMatch'][noMatchCount-1]+declarativeJSON[currState]['prompt']
            elif(stateInformation['vuiResult']=='NOMATCH-CONF'):
                text = declarativeJSON['DEFAULTS']['repromtOnDisconfirm']+declarativeJSON[currState]['prompt'] #In case of disconfirmation
            
        else: #Case when there are more noMatch(es) than desired
            nextState = declarativeJSON[currState]['fail']
            funcType = declarativeJSON[nextState]['type']
            seq = stateInformation["sequence"]
            noInputCount = stateInformation['noInputCount']
            noMatchCount = stateInformation['noMatchCount']
            vuiResult = 'ERROR'
            newStateInformation = setNewStateInformation(stateInformation,seq,nextState,noInputCount,noMatchCount,vuiResult)
            return getNormalFuncs(funcType,body,newStateInformation)
    
    #If it is NOINPUT
    elif(stateInformation['vuiResult']=='NOINPUT'):
        noInputCount = int(noInputCount)+1
        
        if(noInputCount <= declarativeJSON[currState]['noInputMax']):
            text = declarativeJSON['DEFAULTS']['prefixes']['noInput'][noInputCount-1]+declarativeJSON[currState]['prompt']

        else: #Case when there are more noInput(s) than desired
            nextState = declarativeJSON[currState]['fail']
            funcType = declarativeJSON[nextState]['type']
            seq = stateInformation["sequence"]
            noInputCount = stateInformation['noInputCount']
            noMatchCount = stateInformation['noMatchCount']
            vuiResult = 'ERROR'
            newStateInformation = setNewStateInformation(stateInformation,seq,nextState,noInputCount,noMatchCount,vuiResult)
            return getNormalFuncs(funcType,body,newStateInformation)
    
    #First time entry of INPUT state
    else:
        text = declarativeJSON[currState]['prompt'] #This is the default prompt
    try:
        vuiResult = stateInformation['vuiResult']
        newStateInformation = setNewStateInformation(stateInformation,seq,currState,noInputCount,noMatchCount,vuiResult)
        statusCode = 200
        grammars = declarativeJSON[currState].get('grammar')
        if(grammars is not None):
            finalGrammars = []
            for gr in grammars:
                print("gr type of: "+str(type(gr)))
                if (type(gr) == type("str")):
                    # do a lookup of grammar by name
                    finalGrammars.append( declarativeJSON['GRAMMARS'][gr] )
                else:
                    # we have the grammar definition already
                    finalGrammars.append( gr ) 
            response = {
                "csid": stateInformation['csid'],
                "sid":stateInformation['sid'],
                "sequence":seq,
                "question":{
                    "name":declarativeJSON[currState]['name'],
                    "text":text,
                    "audioProperties":{
                        "voice":declarativeJSON[currState]['voice']
                    },
                    "audioResponse":{
                        "bargeIn":declarativeJSON[currState]['bargeIn'],
                        "grammar": finalGrammars
                    }
                }
            }
        else:
            # no grammar - means large vocabulary recognition
            response = {
                "csid": stateInformation['csid'],
                "sid":stateInformation['sid'],
                "sequence":seq,
                "question":{
                    "name":declarativeJSON[currState]['name'],
                    "text":text,
                    "audioProperties":{
                        "voice":declarativeJSON[currState]['voice']
                    },
                    "audioResponse":{
                        "bargeIn":declarativeJSON[currState]['bargeIn']
                    }
                }
            }            
    except Exception as e:
        statusCode = 500
        debug = "Something wrong with the inputFunc"
        detail = "inputFunc failed execution: currState="+currState+" exception="+str(e),
        reason = "Internal error"
        response = setErrorResponse(debug,detail,reason)
        newStateInformation = stateInformation
    elapsed_time = time.time() - t4
    logText = "Time spent in inputFunc is "+str(elapsed_time)+" seconds"
    print(logText)
    return finalResponse(statusCode,response,newStateInformation)

def  getConfidence(declarativeJSON,currState):
    if(declarativeJSON[currState].get('confirmation')==None
    or declarativeJSON[currState]['confirmation'].get('threshold')==None):
        return declarativeJSON['DEFAULTS']['thresholds']['confirmation']
    return declarativeJSON[currState]['confirmation']['threshold']

#This function handles the callback from INPUT     
def ackInputFunc(body,stateInformation):
    
    t5 = time.time()
    currState = stateInformation['state']
    if(body['events'][1]['vuiResult'] == 'MATCH'):
        minConfidence = getConfidence(declarativeJSON,currState)
        recoConf = body['events'][1]['vuiAlternatives'][0].get('confidence')
        grmrName = body['events'][1]['vuiAlternatives'][0].get('grammar')
        # we confirm only grammar recognition
        if((grmrName is not None) and ((recoConf is None) or recoConf<minConfidence)):
            # need to confirm
            return confirmationFunc(body,stateInformation)            
        else:
            #This is executed if it's a match with confidence above threshold
            print("Recognition with High confidence")
            nextState = getNextState(currState)
            funcType = declarativeJSON[nextState]['type']
            seq = stateInformation["sequence"]
            newStateInformation = setNewStateInformation(stateInformation,seq,nextState,0,0,None)
            #keys in state information are set to 0 and None (basically reset) so that inputFunc starts fresh when next INPUT comes in
    
    elif(body['events'][1]['vuiResult'] == 'NOMATCH'): 
    #vuiResult set to NOMATCH, state remains currState, goes back to inputFunc and increments noMatch count   
        funcType = declarativeJSON[currState]['type']
        seq = stateInformation["sequence"]
        noInputCount = stateInformation['noInputCount']
        noMatchCount = stateInformation['noMatchCount']
        vuiResult = 'NOMATCH'
        newStateInformation = setNewStateInformation(stateInformation,seq,currState,noInputCount,noMatchCount,vuiResult)
        
    
    elif(body['events'][1]['vuiResult'] == 'NOINPUT'):
    #vuiResult set to NOMINPUT, state remains currState, goes back to inputFunc and increments noInput count   
        funcType = declarativeJSON[currState]['type']
        seq = stateInformation["sequence"]
        noInputCount = stateInformation['noInputCount']
        noMatchCount = stateInformation['noMatchCount']
        vuiResult = 'NOINPUT'
        newStateInformation = setNewStateInformation(stateInformation,seq,currState,noInputCount,noMatchCount,vuiResult)
        
    else:
    #Error state, passed to 'fail'
        nextState = declarativeJSON[currState]['fail']
        funcType = declarativeJSON[nextState]['type']
        seq = stateInformation["sequence"]
        noInputCount = stateInformation['noInputCount']
        noMatchCount = stateInformation['noMatchCount']
        vuiResult = 'ERROR'
        newStateInformation = setNewStateInformation(stateInformation,seq,nextState,noInputCount,noMatchCount,vuiResult)

    elapsed_time = time.time() - t5
    logText = "Time spent in ackInputFunc is "+str(elapsed_time)+" seconds"
    print(logText)
    return getNormalFuncs(funcType,body,newStateInformation)

#This function confirms the input from ackInput function
def confirmationFunc(body,stateInformation):
    t6 = time.time()
    try:
        currState = stateInformation['state']
        seq = int(stateInformation['sequence'])+1
        noInputCount = stateInformation['noInputCount']
        noMatchCount = stateInformation['noMatchCount']
        #vuiResult set to TO-CONFIRM to make sure next request that comes in is directed to ackConfirmationFunc
        #Grammar will be boolean
        vuiResult = 'TO-CONFIRM'
        newStateInformation = setNewStateInformation(stateInformation,seq,currState,noInputCount,noMatchCount,vuiResult)
        statusCode = 200
        response = {
            "csid": stateInformation['csid'],
            "sid":stateInformation['sid'],
            "sequence":seq,
            "question":{
                "name":declarativeJSON[currState]['name'],
                "text":declarativeJSON[currState]['confirmation']['prompt'], #This is ${phone.phone} in declarative JSON. How does the system know? Does Voicegain app store this?
                "audioProperties":{
                    "voice":declarativeJSON[currState]['voice']
                },
                "audioResponse":{
                    "bargeIn":declarativeJSON[currState]['bargeIn'],
                    "grammar":[{"type":"BUILT-IN","name":"boolean"}]
                }
            }
        }
    except Exception as e:
        statusCode = 500
        debug = "Something wrong with the confirmationFunc: exception="+str(e)
        detail = "confirmationFunc failed execution",
        reason = "Internal error"
        response = setErrorResponse(debug,detail,reason)
        newStateInformation = stateInformation
    elapsed_time = time.time() - t6
    logText = "Time spent in confirmationFunc is "+str(elapsed_time)+" seconds"
    print(logText)
    return finalResponse(statusCode,response,newStateInformation)

#This function acknowledges confirmation function    
def ackConfirmationFunc(body,stateInformation):

    t7 = time.time()
    currState = stateInformation['state']
    varName = declarativeJSON[currState]['name']+".MEANING"
    if((body['events'][1]['vuiResult'] == 'MATCH') and body['vars'][varName] == "true"): 
        nextState = getNextState(currState)
        funcType = declarativeJSON[nextState]['type']
        seq = stateInformation["sequence"]
        noInputCount = stateInformation['noInputCount']
        noMatchCount = stateInformation['noMatchCount']
        vuiResult = 'MATCH'
        newStateInformation = setNewStateInformation(stateInformation,seq,nextState,noInputCount,noMatchCount,vuiResult)
    else: #MATCH with NO as a response or NOMATCH/NOINPUT - vuiResult is NOMATCH and state remains currState
        funcType = declarativeJSON[currState]['type']
        seq = stateInformation["sequence"]
        noInputCount = stateInformation['noInputCount']
        noMatchCount = stateInformation['noMatchCount']
        vuiResult = 'NOMATCH-CONF'
        newStateInformation = setNewStateInformation(stateInformation,seq,currState,noInputCount,noMatchCount,vuiResult)
    elapsed_time = time.time() - t7
    logText = "Time spent in ackConfirmation is "+str(elapsed_time)+" seconds"
    print(logText)
    return getNormalFuncs(funcType,body,newStateInformation)

#This function disconnects the call from server side
def disconnectFunc(body,stateInformation):
    
    t8 = time.time()
    try:
        currState = stateInformation['state']
        seq = int(stateInformation['sequence'])+1
        noInputCount = stateInformation['noInputCount']
        noMatchCount = stateInformation['noMatchCount']
        vuiResult = stateInformation['vuiResult']
        newStateInformation = setNewStateInformation(stateInformation,seq,currState,noInputCount,noMatchCount,vuiResult)
        statusCode = 200
        response = {
            "csid": stateInformation['csid'],
            "sid":stateInformation['sid'],
            "sequence":seq,
            "disconnect":{
                "prompt":{
                    "text":declarativeJSON[currState]['prompt'],
                    "audioProperties":{
                        "voice":declarativeJSON[currState]['voice']
                    }
                },
                "reason":declarativeJSON[currState]['reason']
            }
        }
    except Exception as e:
        statusCode = 500
        debug = "Something wrong with the disconnectFunc: exception="+str(e)
        detail = "disconnectFunc failed execution",
        reason = "Internal error"
        response = setErrorResponse(debug,detail,reason)
        newStateInformation = stateInformation
    elapsed_time = time.time() - t8
    logText = "Time spent in disconnectFunc is "+str(elapsed_time)+" seconds"
    print(logText)
    return finalResponse(statusCode,response,newStateInformation)

#This function handles TRANSFER states    
def transferFunc(body,stateInformation):

    t9 = time.time()
    try:
        currState = stateInformation['state']
        seq = int(stateInformation['sequence'])+1
        #State remains currState
        noInputCount = stateInformation['noInputCount']
        noMatchCount = stateInformation['noMatchCount']
        vuiResult = stateInformation['vuiResult']
        newStateInformation = setNewStateInformation(stateInformation,seq,currState,noInputCount,noMatchCount,vuiResult)
        statusCode = 200
        response = {
            "csid": stateInformation['csid'],
            "sid":stateInformation['sid'],
            "sequence":seq,
            "transfer":{
                "prompt":{
                    "text":declarativeJSON[currState]['prompt'],
                    "audioProperties":{
                         "voice":declarativeJSON[currState]['voice']
                    }
                },
                "phone":declarativeJSON[currState]['prompt']
            }
        }
    except Exception as e:
        statusCode = 500
        debug = "Something wrong with the transferFunc: exception="+str(e)
        detail = "transferFunc failed execution",
        reason = "Internal error"
        response = setErrorResponse(debug,detail,reason)
        newStateInformation = stateInformation
    elapsed_time = time.time() - t9
    logText = "Time spent in transferFunc is "+str(elapsed_time)+" seconds"
    print(logText)
    return finalResponse(statusCode,response,newStateInformation)
    
#This function acknowledges the completion of Transfer states    
def ackTransferFunc(body,stateInformation):

    t10 = time.time()
    try:
        currState = stateInformation['state']
        if(body['events'][1]['outcome'] == 'success'): #Transfer is a success
            seq = int(stateInformation["sequence"])+1
            noInputCount = stateInformation['noInputCount']
            noMatchCount = stateInformation['noMatchCount']
            vuiResult = stateInformation['vuiResult']
            newStateInformation = setNewStateInformation(stateInformation,seq,currState,noInputCount,noMatchCount,vuiResult)
            statusCode = 200
            response = {
                "csid":stateInformation['csid'],
                "sid":stateInformation['sid'],
                "sequence":int(stateInformation['sequence'])+1
            }
    
        else: #Transfer failed - send to 'fail'
            nextState = declarativeJSON[currState]['fail']
            funcType = declarativeJSON[nextState]['type']
            seq = stateInformation["sequence"]
            noInputCount = stateInformation['noInputCount']
            noMatchCount = stateInformation['noMatchCount']
            vuiResult = stateInformation['vuiResult']
            newStateInformation = setNewStateInformation(stateInformation,seq,nextState,noInputCount,noMatchCount,vuiResult)
            return getNormalFuncs(funcType,body,newStateInformation)
    except Exception as e:
        statusCode = 500
        debug = "Something wrong with the ack transferFunc: exception="+str(e)
        detail = "transferFunc failed execution",
        reason = "Internal error"
        response = setErrorResponse(debug,detail,reason)
        newStateInformation = stateInformation
    elapsed_time = time.time() - t10
    logText = "Time spent in ackTransfer is "+str(elapsed_time)+" seconds"
    print(logText)
    return {
        "statusCode":statusCode,
        "body":response,
        "stateInformation":newStateInformation
    }
        
#When DELETE request comes in    
def endCall(body,stateInformation):

    t11 = time.time()
    try:
        statusCode = 200
        response = {
            "csid":stateInformation['csid'],
            "sid":stateInformation['sid'],
            "sequence":int(stateInformation['sequence'])+1,
            "termination":"normal"
        }
    except Exception as e:
        statusCode = 500
        debug = "Something wrong with the endCall: exception="+str(e)
        detail = "endCall failed execution",
        reason = "Internal error"
        response = setErrorResponse(debug,detail,reason)
    elapsed_time = time.time() - t11
    logText = "Time spent in endCall is "+str(elapsed_time)+" seconds"
    print(logText)
    newStateInformation = stateInformation
    return finalResponse(statusCode,response,newStateInformation)

def checkExpr(expr,ans):
    
    t12 = time.time()
    expr = expr.replace('${1}',ans)
    x = eval(expr)
    elapsed_time = time.time() - t12
    logText = "Expr: "+expr+" evaluated to "+str(x)+" :Time spent in checkExpr is "+str(elapsed_time)+" seconds"
    print(logText)
    return x

#To be further implemented by developer
def evalFunc(body,stateInformation):
    t13 = time.time()
    try:
        currState = stateInformation['state']
        evalExpr = declarativeJSON[currState]['eval']
        print("Eval "+currState+": expr="+evalExpr)
        templ = Template(evalExpr)
        print("State: "+json.dumps(stateInformation))
        afterSubst = templ.safe_substitute(**stateInformation)
        print("After substitution: "+afterSubst)
        ans = eval(afterSubst)
        ##ans = "'"+ans+"'"
        print("Eval result: "+str(ans))
        length = len(declarativeJSON[currState]['case'])
        for i in range(length):
            if(checkExpr(declarativeJSON[currState]['case'][i]['expr'],ans)):
                nextState = declarativeJSON[currState]['case'][i]['next'] 
                funcType = declarativeJSON[nextState]['type']
                seq = stateInformation["sequence"]
                noInputCount = stateInformation['noInputCount']
                noMatchCount = stateInformation['noMatchCount']
                vuiResult = stateInformation['vuiResult']
                newStateInformation = setNewStateInformation(stateInformation,seq,nextState,noInputCount,noMatchCount,vuiResult)
                return getNormalFuncs(funcType,body,newStateInformation)
        #If none of the expressions are satisfied, flow control reachs here
        nextState = getNextState(currState) 
        funcType = declarativeJSON[nextState]['type']
        seq = stateInformation["sequence"]
        noInputCount = stateInformation['noInputCount']
        noMatchCount = stateInformation['noMatchCount']
        vuiResult = stateInformation['vuiResult']
        newStateInformation = setNewStateInformation(stateInformation,seq,nextState,noInputCount,noMatchCount,vuiResult)
        elapsed_time = time.time() - t13
        logText = "Time spent in evalFunc is "+str(elapsed_time)+" seconds"
        print(logText)
        return getNormalFuncs(funcType,body,newStateInformation)
    except Exception as e:
        statusCode = 500
        debug = "Something wrong with the evalFunc: exception="+str(e)
        detail = "evalFunc failed execution",
        reason = "Internal error"
        response = setErrorResponse(debug,detail,reason)
        newStateInformation = stateInformation
    elapsed_time = time.time() - t13
    logText = "Time spent in evalFunc is "+str(elapsed_time)+" seconds"
    print(logText)
    return finalResponse(statusCode,response,newStateInformation)
    
#Start here
def main(event,context):
    print(str(event))
    t14 = time.time()
    getJSON()
    body = json.loads(event['body'])
    print('Body: '+str(body))
    if event['requestContext']['http']['method'] == 'POST':
        print('POST')
        state = 'ENTRY'
        csid = "Cust-"+body['sid'] 
        seq = 0
        stateInformation = {
            "sid":body['sid'],
            "csid":csid,
            "sequence":seq,
            "state":"ENTRY",
            "noInputCount":0,
            "noMatchCount":0,
            "vuiResult": None
        }
        funcType = declarativeJSON[state]['type']
        x = mainResponse(getNormalFuncs(funcType,body,stateInformation))
        elapsed_time = time.time() - t14
        logText = "Total time spent is "+str(elapsed_time)+" seconds"
        print(logText)
        print(x)
        return x

    elif event['requestContext']['http']['method'] == 'PUT': #For all intermediate cases
        print('PUT')
        stateInformation = getStateVars(body)
        if('TO-CONFIRM' == stateInformation.get('vuiResult')):
            print('need to confirm')
            x = mainResponse(ackConfirmationFunc(body,stateInformation))
            elapsed_time = time.time() - t14
            logText = "Total time spent is "+str(elapsed_time)+" seconds"
            print(logText)
            print(x)
            return x
        else:    
            state = stateInformation['state']
            funcType = declarativeJSON[state]['type']
            print('function type: '+funcType)
            x = mainResponse(getAckFuncs(funcType,body,stateInformation))
            elapsed_time = time.time() - t14
            logText = "Total time spent is "+str(elapsed_time)+" seconds"
            print(logText)
            print(x)
            return x    
    
    elif event['requestContext']['http']['method'] == 'DELETE': #When the call ends naturally
        print('DELETE')
        stateInformation = getStateVars(body)
        x = mainResponse(endCall(body,stateInformation))
        elapsed_time = time.time() - t14
        logText = "Total time spent is "+str(elapsed_time)+" seconds"
        print(logText)
        print(x)
        return x
    
    else:
        print('UNKNOWN')
        debug = "Invalid HTTP Request (Invalid Method) received at backend"
        detail = "Invalid HTTP Method",
        reason = "Invalid request"
        errorResponse = setErrorResponse(debug,detail,reason)
        response = {
            "statusCode":400,
            "body":errorResponse
        }
        return mainResponse(response)
    
#Responses with statusCode
def mainResponse(response):
    ## workaround - but we do not need to pass SIP headers back
    if(response['stateInformation'].get('sip') is not None ):
        response['stateInformation']['sip'] = None
        
    respBodyStr = json.dumps(response)
    print("Response for VG: "+respBodyStr)

    if(response['statusCode']==200): #Default statusCode = 200
        temp = {
            'vars':response['stateInformation']
        }
        response['body'].update(temp)
        return {
            "statusCode":200,
            "headers" : {'Content-Type': 'application/json'},
            "body":json.dumps(response['body'])
        }
    else: #Override 200 statusCode
        statusCode = response['statusCode']
        temp = {
                'vars':response['stateInformation']
            }
        response['body'].update(temp)
        return {
            "statusCode":statusCode,
            "headers" : {'Content-Type': 'application/json'},
            "body":json.dumps(response['body'])
        }

#Return JSON stored in #saveS3 - all the information about state    
def getStateVars(body):
    stateInformation = body['vars']
    print("State Vars -> "+str(stateInformation))
    return stateInformation

#Reads declarativeJSON from #saveS3
def getJSON():
    global declarativeJSON
    t16 = time.time()
    s3_object = boto3.client('s3').get_object(Bucket=s3BucketName,Key=jsonIvrDefKey)
    declarativeJSON = json.loads(s3_object['Body'].read().decode('utf-8'))
    elapsed_time = time.time() - t16
    logText = "Time spent in getJSON is "+str(elapsed_time)+" seconds"
    print(logText)
    return

#Directs request to functions based on funcType
def getNormalFuncs(funcType,body,stateInformation):
    if funcType == "INPUT":
        return inputFunc(body,stateInformation)
    elif funcType == "OUTPUT":
        return outputFunc(body,stateInformation)    
    elif funcType == "DISCONNECT":
        return disconnectFunc(body,stateInformation)
    elif funcType == "TRANSFER":
        return transferFunc(body,stateInformation)
    elif funcType == "EVAL":
        return evalFunc(body,stateInformation)
    elif funcType == "VOID":
        return voidFunc(body,stateInformation)
    else:
        debug = "Invalid funcType in getNormalFuncs"
        detail = "Invalid funcType",
        reason = "Internal error"
        errorResponse = setErrorResponse(debug,detail,reason)
        return{
            "statusCode":500,
            "body":errorResponse
        }
    
#Same as above, but for ackFuncs -- these handle callback responses from AIVR 
def getAckFuncs(funcType,body,stateInformation):
    if funcType == "INPUT":
        return ackInputFunc(body,stateInformation)
    elif funcType == "OUTPUT":
        return ackOutputFunc(body,stateInformation)    
    elif funcType == "TRANSFER":
        return ackTransferFunc(body,stateInformation)
    else:
        debug = "Invalid funcType in getAckFunc"
        detail = "Invalid funcType",
        reason = "Internal error"
        errorResponse = setErrorResponse(debug,detail,reason)
        return{
            "statusCode":500,
            "body":errorResponse
        }

def getNextState(currState):
    if(declarativeJSON.get(currState)==None):
        print("!! current state not in JSON definition: "+currState)
        return None
    nextStateName = declarativeJSON[currState]['next']
    if(declarativeJSON.get(nextStateName)==None):
        print("!! next state not in JSON definition: "+nextStateName)
        return None
    print("next state: "+nextStateName)
    return nextStateName