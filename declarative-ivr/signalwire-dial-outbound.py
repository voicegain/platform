import os
import requests
from requests.auth import HTTPBasicAuth
from signalwire.rest import Client as signalwire_client

sw_project = '<your SignalWire Project Id>'
sw_token = '<your SignalWire Token>'
sw_space = '<your SignalWire space, e.g. acme.signalwire.com>'
sw_phone = '+1<your SignalWire phone number>'

phone = '+1<phone you will dial>'
voicegain_sip = 'sip:<voicegain sip address for your Telephone Bot application>:5080;transport=tcp'

custom_sip_headers = '?x-mycustomheader=foo'

# most of the code is setting up the LaML code in the LaML bin
# unlike in Twilio API, we cannot pass LaML text to a new call, we can only pass a url
# uploading LaML to a LaML bin will give us a Url 

laml_name = "dial_voicegain_sip_v1" # name of the LaML bin where we will store LaML to be executed on the call

laml='<Response> \n \
        <Say voice="woman" language="en-US">dialing now</Say> \n \
        <Dial> <Sip>{}{}</Sip> </Dial> \n \
        <Say voice="woman" language="en-US">we are done. good bye</Say> \n \
    </Response>'.format(voicegain_sip, custom_sip_headers),

print("check if LaML bin exists", flush=True)

sw_response = requests.get( 'https://{}/api/laml/2010-04-01/Accounts/{}/LamlBins?Name={}'.format(sw_space, sw_project, laml_name),
    auth = HTTPBasicAuth(sw_project, sw_token)
    )
print(sw_response)
print(sw_response.json()) 

laml_bins = sw_response.json().get('laml_bins')
laml_bin = None
laml_bin_uri = None
laml_request_url = None

if(laml_bins is not None and len(laml_bins)>0):
    # get the 1st one
    laml_bin = laml_bins[0]
    print("LaML bin: "+str(laml_bin), flush=True)
    laml_bin_uri = laml_bin.get('uri')
    print("LaML bin URI: "+str(laml_bin_uri), flush=True)

if(laml_bin_uri is None):
    print("Does not exist yet. Uploading LaML: {}".format(laml), flush=True)

    sw_response = requests.post( 'https://{}/api/laml/2010-04-01/Accounts/{}/LamlBins.JSON'.format(sw_space, sw_project),
        auth = HTTPBasicAuth(sw_project, sw_token),
        data={  "Name": laml_name,
                "Contents" : laml }
        )
    print(sw_response)
    print(sw_response.json()) 
else:
    print("Already exists. Updating LaML: {}".format(laml), flush=True)
    sw_response = requests.post( 'https://{}{}'.format(sw_space, laml_bin_uri),
        auth = HTTPBasicAuth(sw_project, sw_token),
        data={  "Name": laml_name,
                "Contents" : laml }
        )
    print(sw_response)
    print(sw_response.json())    

laml_request_url = sw_response.json().get('request_url')
print("LaML request URL: "+str(laml_request_url), flush=True)

# test LAML Url
sw_response = requests.get( laml_request_url)
print(sw_response)
print("LaML to be used:")
print(sw_response.text, flush=True) 

# client client object and dial the call
client = signalwire_client(sw_project, sw_token, signalwire_space_url = sw_space)

# dial the call and pass the url of the LaML bin
print("dialing: "+phone, flush=True)

call = client.calls.create(
                        url=laml_request_url,
                        to=phone,
                        from_=sw_phone
                    )

print(call.sid)
