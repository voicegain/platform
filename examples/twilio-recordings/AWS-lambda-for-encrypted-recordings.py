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

import json
import base64
from urllib.parse import parse_qs
import urllib3

voicegainJwt = "<your context JWT here>"
voicegainUrl = "https://api.ascalon.ai/v1/asr/transcribe/async"
myAuthConf = "<name of the authConf with the private key>"
expectedPublicKeyId = '<name of the public encryption key of twilio e.g. CR3b14a554c3da35a72e6ff6b1585c2cff'

headers = {"Authorization":voicegainJwt, "Content-Type" : "application/json"}

def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    if(event.get("resource") is not None):
        if(event.get('body') is not None):
            try:    
                rawRequest = event['body']
                
                print("Raw request: "+rawRequest)
                
                request = base64.b64decode(rawRequest).decode('utf-8')
                
                print("Request: "+request)
                
                twilioParams = parse_qs(request)
                
                print(json.dumps(twilioParams))
                
                if(twilioParams.get("RecordingStatus") is not None):
                    twilioRecordingStatus = twilioParams["RecordingStatus"][0];
                    print("Recording Status: "+twilioRecordingStatus)
                    
                    if(twilioRecordingStatus == "completed"):                
                    
                        encryptionDetailsJson = twilioParams.get("EncryptionDetails")
                        
                        if(encryptionDetailsJson is not None):
                            print("Recording is encrypted")
                        
                            encryptionDetails = json.loads(encryptionDetailsJson[0])
                            
                            print(json.dumps(encryptionDetails))
                            
                            publicKeyId = encryptionDetails.get('public_key_sid')
                            
                            if(expectedPublicKeyId == publicKeyId):
                                print("Public key Id matches")
    
                                twilioRecordingUrl = twilioParams["RecordingUrl"][0] + ".json"
                                print("Recording URL: "+twilioRecordingUrl)
                                
                                twilioRecordingChannels = twilioParams["RecordingChannels"][0];
                                print("Recording Channels: "+twilioRecordingChannels)
                                
                                formatChannels = "mono"
                                audioChannelSelector = "mix"
                                if(twilioRecordingChannels=="2"):
                                    formatChannels = "stereo"
                                    audioChannelSelector = "two-channel"
                                
                                twilioRecordingTrack = twilioParams["RecordingTrack"][0];
                                twilioRecordingSource = twilioParams["RecordingSource"][0]
                                twilioRecordingStartTime = twilioParams["RecordingStartTime"][0];
                                twilioRecordingDuration = twilioParams["RecordingDuration"][0];
                                twilioAccountSid = twilioParams["AccountSid"][0];
                                twilioCallSid = twilioParams["CallSid"][0];
                                twilioRecordingSid = twilioParams["RecordingSid"][0];
                                
                                vgRequest = {
                                    "sessions" : [{
                                        "asyncMode" : "OFF-LINE",
                                        "audioChannelSelector" : audioChannelSelector,
                                        "vadMode" :"normal",
                                        
                                        # this will send it to the portal which is fine for testing
                                        # for prod you would likely configure a callback
                                        "portal" : {"label" : "Foo", "persist" : 3600000},
                                        
                                        "diarization" : {"minSpeakers" : 1, "maxSpeakers" : 1},
                                        "metadata" : [
                                            {"name" : "twilioAccountSid",           "value" : twilioAccountSid},
                                            {"name" : "twilioCallSid",              "value" : twilioCallSid},
                                            {"name" : "twilioRecordingSid",         "value" : twilioRecordingSid},
                                            {"name" : "twilioRecordingStartTime",   "value" : twilioRecordingStartTime},
                                            {"name" : "twilioRecordingDuration",    "value" : twilioRecordingDuration},
                                            {"name" : "twilioRecordingSource",      "value" : twilioRecordingSource},
                                            {"name" : "twilioRecordingTrack",       "value" : twilioRecordingTrack},
                                            {"name" : "twilioRecordingChannels",    "value" : twilioRecordingChannels},
                                            {"name" : "twilioRecordingUrl",         "value" : twilioRecordingUrl}
                                        ]
                                    }],
                                    "audio" :{
                                        "source" :{
                                            "fromUrl" : {
                                                "url" : twilioRecordingUrl,
                                                "authConf" : myAuthConf
                                            }
                                        },
                                        "channels" : formatChannels
                                    },
                                    "settings" :{
                                        "asr" : {
                                            "languages" : ["en"]
                                        },
                                        "formatters" : [
                                            {"type" : "digits"}
                                        ]
                                    }
                                }
                            
                                http = urllib3.PoolManager()
        
                                print("Making request to: "+voicegainUrl )
                                
                                asr_response_raw = http.urlopen("POST", voicegainUrl, headers=headers, body=json.dumps(vgRequest))
        
                                print("response code from VG: "+str(asr_response_raw.status))
                                if(asr_response_raw.status == 200):
                                    decoded_r = asr_response_raw.data.decode("utf8")
                                    print("response body from VG: "+str(decoded_r))
                                    return {
                                        'statusCode': 200,
                                        'body': json.dumps('OK')
                                    }        
                                else:
                                    return {
                                        'statusCode': 200,
                                        'body': json.dumps('OK but Voicegain request returned code '+str(asr_response_raw.status))
                                    }                                       
                            else:
                                return {
                                    'statusCode': 400,
                                    'body': json.dumps('Unexpected public key Id: '+publicKeyId)
                                }                    
                        else:
                            return {
                                'statusCode': 400,
                                'body': json.dumps('Not an encrypted recording')
                            }                    
                    else:
                        print("Cannot invoke Voicegain API because recording is not complete")
                        return {
                            'statusCode': 200,
                            'body': json.dumps('OK but not completed')
                        }                              
                else:
                    return {
                        'statusCode': 200,
                        'body': json.dumps('No Twilio RecordingStatus')
                    }                        

            except Exception as e:
                eStr = str(e)
                print("Exception: "+eStr)
                return {
                    'statusCode': 500,
                    'body': json.dumps(eStr)
                }                
        else:
            return {
                'statusCode': 400,
                'body': json.dumps('No body')
            }                    
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('No resource')
        }
