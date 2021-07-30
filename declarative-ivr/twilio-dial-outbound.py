import os
from twilio.rest import Client

# simple script to dial a number from Twilio and then bridge it to a Voicegain SIP endpoint 
 
# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC054c13f4xxxxxxxxxxxxxxxb04f2f710160'
auth_token = 'c36eca6axxxxxxxxxxxxxxxx8d900f6ec'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        twiml='<Response> \
    <Dial>        <Sip>sip:673a8342-b0exxxxxxxxxxxxxxxxx87c18b8ca3ba@fs001.voicegain.ai:5080;transport=tcp?x-mycustomheader=foo</Sip>   </Dial> \
    <Say voice="woman" language="en-US">Bye</Say> \
</Response>',
                        to='+18174xxxxx096',
                        from_='+146xxxxx554'
                    )

print(call.sid)