import json
import base64
import requests
import time

# Example Lambda function that shows how to dial a number from Telnyx and then bridge it to Voicegain SIP Endpoint
# You can invoke it by making http GET request (with the "phone" parameter) to the AWS url for this Lambda function 

telnyx_application_id = "<Telnyx application id (connection id) >"
telnyx_APIAuthKey_fromPortal = "<Telnyx API Auth Key>"
telnyx_phone = "+1<Telnyx phone number>"

voicegain_sip = 'sip:<voicegain sip address for the application you want to dial>:5080' 

headers = {"Content-Type" : "application/json", "Accept" : "application/json", "Authorization" : "Bearer "+telnyx_APIAuthKey_fromPortal}

print('Loading function') 


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    method = event['requestContext']['http']['method']
    domainName = event['requestContext']['domainName']
    path = event['requestContext']['http']['path']
    print("Method="+method+", domain="+domainName+", path="+path)
    url = "https://"+domainName+path
    print("url="+url)
    query = event.get("queryStringParameters")
    if(method == 'GET'):
        # GET request triggers the outbound call to the specified phone
        
        if (query is None):
            # missing the phone parameter
            return {
            "statusCode":400,
            "headers" : {'Content-Type': 'application/json'},
            "body":json.dumps({'result':'need phone parameter'})
            }              
        else:
            phone = query.get("phone")
            print('dialing '+phone) 
            telnyx_response = requests.post( 'https://api.telnyx.com/v2/calls',
                headers=headers,
                json={  "connection_id": telnyx_application_id, 
                        "to": "+1"+phone, 
                        "from": telnyx_phone, 
                        "webhook_url" : url+"?leg=A"} # we label the outbound leg A in the webhook requests
                )
            print(telnyx_response)
            print(telnyx_response.json()) 
            
            return {
            "statusCode":200,
            "headers" : {'Content-Type': 'application/json'},
            "body":json.dumps({'result':'outbound dialied ok'})
            }    
    elif(method == 'POST'):
        # this is webhook invocation by Telnyx
        print("Telnyx webhook POST")
        body = None
        event_type = None
        call_control_id = None
        client_state = None
        if(event.get('body') is not None):
            body = json.loads(event['body'])
            print('Body: '+str(body))
        if(body is not None):
            data = body.get('data')
            if(data is not None):
                event_type = data.get('event_type')
                print('-->EVENT_TYPE: '+str(event_type))
                payload = data.get('payload')
                if(payload is not None):
                    print('Payload: '+str(payload))
                    call_control_id = payload.get('call_control_id')
                    client_state = payload.get("client_state")
                    
        leg = query.get("leg")
                    
        if(leg == 'A'):
            print('Outbound leg')
            
            if(event_type == 'call.answered'):
                print('call answered')
                # acknowledge that call was answered by saying 'one moment'
                telnyx_response = requests.post( 'https://api.telnyx.com/v2/calls/{}/actions/speak'.format(call_control_id),
                    headers=headers,
                    json={"payload": "one moment", "voice": "female", "language": "en-US"})
                print(telnyx_response)
                print(telnyx_response.json())
                
            if(event_type == 'call.speak.ended'):
                print('speak ended, dialing '+voicegain_sip)
                # once the 'one moment' prompt finishes playing we dial the Voicegain SIP endpoint
                
                telnyx_response = requests.post( 'https://api.telnyx.com/v2/calls',
                    headers=headers,
                    json={  "connection_id": telnyx_application_id, 
                            "to": voicegain_sip, 
                            "from": telnyx_phone, 
                            "webhook_url" : url+"?leg=B", 
                            "custom_headers" : [{"name" : "x-my-custom-telnyx-header", "value" : "some_value"}]} # you can pass info to Voicegain using custom SIP headers
                    )

                print(telnyx_response)
                print(telnyx_response.json()) 
                
                # get the data for the new dialed leg
                new_call_data = telnyx_response.json().get('data');
                if(new_call_data is not None):
                    new_call_control_id = new_call_data.get('call_control_id')
                    print('new_call_control_id='+new_call_control_id)
                    
                    time.sleep(1)
                    print('bridging the call legs')
                    telnyx_response = requests.post( 'https://api.telnyx.com/v2/calls/{}/actions/bridge'.format(call_control_id),
                        headers=headers,
                        json={  "call_control_id": new_call_control_id, 
                                "client_state" : base64.b64encode(new_call_control_id.encode('ascii')).decode('ascii')} # just an illustration how you can pass info between the legs of the call
                        )
                    print(telnyx_response)
                    print(telnyx_response.json())       
                    print('call bridged')
        
        if(leg == 'B'):
            print('SIP leg')
            # we could print some debuggin info from the SIP leg here 
            
        return {
            "statusCode":200,
            "headers" : {'Content-Type': 'application/json'},
            "body":json.dumps({'result':'OK'})
            }
    else:
        print("wrong http method")
        return {
            "statusCode":400,
            "headers" : {'Content-Type': 'application/json'},
            "body":json.dumps({'result':'bad request'})
            }    
    
