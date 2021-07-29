import json
import base64
import requests

telnyx_app_id = "<telnyx applicatio id>"
telnyx_APIAuthKey_fromPortal = "<telnyx APIAuthKey>"
telnyx_phone = "<telnyx phone starting with +1>"
headers = {"Content-Type" : "application/json", "Accept" : "application/json", "Authorization" : "Bearer "+telnyx_APIAuthKey_fromPortal}

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    body = None
    event_type = None
    call_control_id = None
    client_state = None
    if(event.get('body') is not None):
        #decoded = base64.b64decode(event['body'])
        #print('Decoded: '+str(decoded))
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
    
    query = event.get("queryStringParameters")
    if (query is not None):
        rtpIp = query.get("rtpIp")
        if(rtpIp is not None): 
            port1 = query.get("port1")
            port2 = query.get("port2")
            dial = query.get("dial")
            dial_expanded = dial
            if(dial is not None):
                for digit in "0123456789":
                    dial_expanded = dial_expanded.replace(digit, digit+' ')
            print("IP: "+rtpIp+" ports: "+port1+","+port2+",  dial="+dial)
            if(event_type == 'call.answered'):
                print('call answered')

                # telnyx_response = requests.post( 'https://api.telnyx.com/v2/calls/{}/actions/fork_start'.format(call_control_id),
                #     headers=headers,
                #     json={"rx": "udp:"+rtpIp+":"+port1, "tx": "udp:"+rtpIp+":"+port2})
                # print(telnyx_response)
                # print(telnyx_response.json())
                
                
                telnyx_response = requests.post( 'https://api.telnyx.com/v2/calls/{}/actions/speak'.format(call_control_id),
                    headers=headers,
                    json={"payload": "Welcome to our test. Dialing number: "+dial_expanded, "voice": "female", "language": "en-US"})
                print(telnyx_response)
                print(telnyx_response.json())
            if(event_type == 'call.speak.ended'):
                print('speak ended, dialing '+dial)
                telnyx_response = requests.post( 'https://api.telnyx.com/v2/calls',
                    headers=headers,
                    json={"connection_id": telnyx_app_id, "to": "+1"+dial, "from": telnyx_phone})
                print(telnyx_response)
                print(telnyx_response.json())      
                new_call_data = telnyx_response.json().get('data')
                if(new_call_data is not None):
                    new_call_control_id = new_call_data.get('call_control_id')
                    print('new_call_control_id='+new_call_control_id)
                    telnyx_response = requests.post( 'https://api.telnyx.com/v2/calls/{}/actions/bridge'.format(call_control_id),
                        headers=headers,
                        json={"call_control_id": new_call_control_id, "client_state" : base64.b64encode(new_call_control_id.encode('ascii')).decode('ascii')})
                    print(telnyx_response)
                    print(telnyx_response.json())           
            if(event_type == 'call.bridged'):
                if(client_state is not None):
                    print('client_state encoded='+client_state)
                    base64_bytes = client_state.encode("ascii")
                    sample_string_bytes = base64.b64decode(base64_bytes)
                    client_state = sample_string_bytes.decode("ascii")
                    print('client_state decoded='+client_state)
                    
                    # print('stopping fork')
    
                    # telnyx_response = requests.post( 'https://api.telnyx.com/v2/calls/{}/actions/fork_stop'.format(call_control_id),
                    #     headers=headers,
                    #     json={})
                    # print(telnyx_response)
                    # print(telnyx_response.json())
                    
                    print('restarting fork')
    
                    telnyx_response = requests.post( 'https://api.telnyx.com/v2/calls/{}/actions/fork_start'.format(client_state),
                        headers=headers,
                        json={"rx": "udp:"+rtpIp+":"+port1, "tx": "udp:"+rtpIp+":"+port2})
                    print(telnyx_response)
                    print(telnyx_response.json())
                    
            print("good")
            return {
                "statusCode":200,
                "headers" : {'Content-Type': 'application/json'},
                "body":json.dumps({'result':'OK'})
                }
        else:
            print("no rtpIP")
            return {
            "statusCode":200,
            "headers" : {'Content-Type': 'application/json'},
            "body":json.dumps({'result':'no rtp'})
            }        
    else:
        print("no query data")
        return {
            "statusCode":200,
            "headers" : {'Content-Type': 'application/json'},
            "body":json.dumps({'result':'no query'})
            }