### dial out to a  phone numbe rusing Twilion and connect the call to Telephony Bot on its SIP address

import os
from twilio.rest import Client
import configparser

cfg = configparser.ConfigParser()
cfg.read("config.ini")

account_sid = cfg.get("DEFAULT", "TWILIO_ACCOUNT_ID")
auth_token = cfg.get("DEFAULT", "TWILIO_AUTH_TOKEN")
from_phone = cfg.get("DEFAULT", "FROM_PHONE")
tel_bot_sip_uri = cfg.get("DEFAULT", "TEL_BOT_SIP_URI")

#to_phone = '+18174002096'
# Wells-Fargo
to_phone = '+18008693557'

print(f'Sip uri: {tel_bot_sip_uri}', flush=True )

twiml = f'<Response> <Dial> <Sip>{tel_bot_sip_uri};transport=tcp?x-mycustomheader=foo</Sip> </Dial> <Say voice="woman" language="en-US">Bye</Say> </Response>'

client = Client(account_sid, auth_token)
call = client.calls.create(
                        twiml=twiml,
                        to=to_phone,
                        from_=from_phone
                    )

print(f'Call SID: {call.sid}')
