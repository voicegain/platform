from flask import Flask, request
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse the JSON body of the request
    data = request.get_json()
    
    if data:
        event = data.get('event')
        token = "XXXXXXXX"
        callid = data['data']['id'] if 'data' in data and 'id' in data['data'] else None

        # Basic Auth credentials
        username = "c7660d058ee878221d812f58cafcc9d6"
        password = token

        if event == 'call.created' and callid:
            print("Call Created -> callid:", callid)
            
            # Define the URL and payload for the contacts POST request
            contacts_url = "https://api.aircall.io/v1/contacts/250444238"
            contacts_payload = {
                "information": "Verified: FALSE\nMATCH Phone: 817-401-2196\nNO-MATCH: Address: 123 2nd North St, Dallas, TX 75038\nPARTIAL DoB: 12/5/1933\nCONFIRM Email: gary.jennings@acme.com"
            }
            
            # Define the URL and payload for the insight cards POST request
            insight_cards_url = f"https://api.aircall.io/v1/calls/{callid}/insight_cards"
            insight_cards_payload = {
                "contents": [
                    {
                        "type": "title",
                        "text": "Gary Jerry: Verified",
                        "link": "https://my-custom-crm.com"
                    },
                    {
                        "type": "shortText",
                        "label": "Account ID",
                        "text": "M690789",
                        "link": "https://my-custom-crm.com/6789"
                    },
                    {
                        "type": "shortText",
                        "label": "Intent",
                        "text": "Discuss Claim"
                    },
                    {
                        "type": "shortText",
                        "label": "DoB",
                        "text": "12 June 1999 (match)"
                    }    
                ]
            }

            # Make the POST request to contacts
            contacts_response = requests.post(contacts_url, json=contacts_payload, auth=HTTPBasicAuth(username, password))

            # Print the contacts response for debugging purposes
            print("Contacts response status code:", contacts_response.status_code)
            print("Contacts response body:", contacts_response.text)

            # Make the POST request to insight cards
            insight_cards_response = requests.post(insight_cards_url, json=insight_cards_payload, auth=HTTPBasicAuth(username, password))

            # Print the insight cards response for debugging purposes
            print("Insight cards response status code:", insight_cards_response.status_code)
            print("Insight cards response body:", insight_cards_response.text)

        elif event in ['call.ended', 'call.hangup', 'call.tagged'] and callid:
            # Define the URL and payload for the comments POST request
            comments_url = f"https://api.aircall.io/v1/calls/{callid}/comments"
            comments_payload = {
                "content": "Summary:\nCustomer confused about a denied claim.\nInformed that the claim is still being reviewed, it has not been denied.\nRequested to check in a week time."
            }

            # Make the POST request to comments
            comments_response = requests.post(comments_url, json=comments_payload, auth=HTTPBasicAuth(username, password))

            # Print the comments response for debugging purposes
            print("Comments response status code:", comments_response.status_code)
            print("Comments response body:", comments_response.text)
    
    return '', 200

if __name__ == '__main__':
    app.run(port=8080)
