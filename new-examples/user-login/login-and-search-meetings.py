import requests
import json
import hashlib
import hmac

userName = "<your user email for the Voicegain account>"


password = input("Enter password for user " + userName + ": ")

login_url = "https://transcribe.ascalon.ai/auth-svc/auth/login"

login_body = {
    "email": userName,
    "password": password,
    "from": "TranscribeApp",
    "passwordFormat": "plain"
}

login_headers = {
    "Content-Type": "application/json"
}

def computeMAC(message, api_key, auth_token, nonce):
    hmac_sha256 = hmac.new(auth_token.encode(), message.encode(), hashlib.sha256)
    hex = hmac_sha256.hexdigest()
    return f"signature={hex},sessionId={api_key},nonce={nonce}"

response = requests.post(login_url, json=login_body, headers=login_headers)

print(response.status_code)
# print(response.json())

data = response.json()

stok = data['stok']
nonces = data['nonce'] ## a list of nonces
permission = data['permission']
api = data['api']
details = data['details']
account_id = data['account']['id']
# account_accountId = data['account']['accountId']
# account_webName = data['account']['webName']
# account_postalAddress = data['account']['postalAddress']
# account_webNameLowercase = data['account']['webNameLowercase']
# account_dateCreated = data['account']['dateCreated']
# account_bucketId = data['account']['bucketId']
# account_termsAcceptedBy = data['account']['termsAcceptedBy']
# account_billingAccountId = data['account']['billingAccountId']
# account_creator = data['account']['creator']
# account_paymentMethodCreated = data['account']['paymentMethodCreated']
# account_businessName = data['account']['businessName']
# account_billingStyle = data['account']['billingStyle']
# account_type = data['account']['type']
# account_inactivityLogoutThreshold = data['account']['inactivityLogoutThreshold']
# account_referrer = data['account']['referrer']
# account_notes = data['account']['notes']
# account_deleted = data['account']['deleted']
# account_color = data['account']['color']
# account_timeZone = data['account']['timeZone']
# account_dateFormat = data['account']['dateFormat']
# account_weekStartsOn = data['account']['weekStartsOn']
# account_timeFormat = data['account']['timeFormat']
# account_maxPersistenceCloud = data['account']['maxPersistenceCloud']
# account_status = data['account']['status']
# account_transcribeSecondsUsed = data['account']['transcribeSecondsUsed']
# account_transcribeStorageUsed = data['account']['transcribeStorageUsed']
# account_endTimeOfCurrentBillingPeriod = data['account']['endTimeOfCurrentBillingPeriod']
# account_limits = data['account']['limits']
# account_pciDss = data['account']['pciDss']
# account_formatters = data['account']['formatters']
# account_longTermRedaction = data['account']['longTermRedaction']
email = data['email']
userId = data['userId']
#passwordChangeRequired = data['passwordChangeRequired']
#clientSideProperties = data['clientSideProperties']
contextId = data['contextId']



print("stok: " + stok)
print("api: " + api)
print("userId: " + userId)
print("account_id: " + account_id)

nonce = nonces.pop()

print("nonce: " + nonce)

emailPlusApiKey = email.lower() + api

print("emailPlusApiKey: " + emailPlusApiKey)

hmac_sha256 = hmac.new(stok.encode(), emailPlusApiKey.encode(), hashlib.sha256)
auth_token = hmac_sha256.hexdigest()

print("auth_token: " + auth_token)


search_url = "https://transcribe.ascalon.ai/ascalon-web-api/asr/meeting/search"

search_body = {
  "type" : "OrQuery",
  "disjuncts" : [
    {
      "type" : "TxtSearchTerm",
      "field" : "TEXT",
      "txtQuery" : "java"
    },
    {
      "type" : "TxtSearchTerm",
      "field" : "TEXT",
      "txtQuery" : "computer"
    }
  ]
}

# computer the authrization header without which the request will fail
mac = computeMAC(json.dumps(search_body), api, auth_token, nonces.pop())
print("mac: " + mac)

search_headers = {
    "Content-Type": "application/json",
    "Authorization": "MAC " + mac,
}

response = requests.post(search_url, json=search_body, headers=search_headers)

print(response.status_code)
# print(response.json())

search_results = response.json()

print("Search results:")

for result in search_results:
    print("-----------label:", result["label"])
    print("meetingSessionId:", result["meetingSessionId"])
    print("       contextId:", result["contextId"])
    print("         creator:", result["creator"])


# logout
print("Logging out")

logout_url = "https://transcribe.ascalon.ai/auth-svc/auth/logout"

logout_body = {
}

# computer the authrization header without which the request will fail
mac = computeMAC(json.dumps(logout_body), api, auth_token, nonces.pop())
print("mac: " + mac)

logout_headers = {
    "Content-Type": "application/json",
    "Authorization": "MAC " + mac,
}

response = requests.post(logout_url, json=logout_body, headers=logout_headers)

print(response.status_code)
# print(response.json())

data = response.json()
