import csv
import json
from google.cloud import firestore

# Load GCP credentials
credentials_path = "./voicegain-prod-2a6e4e07b085.json"
with open(credentials_path) as cred_file:
    credentials = json.load(cred_file)

# Initialize Firestore client
db = firestore.Client.from_service_account_json(credentials_path)

# Function to get captured audio ID from Firestore
def get_captured_audio_id(session_id):
    # Query Firestore for the document with the given sessionId
    query = db.collection('web_api_session').where('sessionId', '==', session_id).limit(1)
    results = query.stream()
    
    for doc in results:
        return doc.to_dict().get('capturedAudio')
    
    print(f"No document found for session ID: {session_id}")
    return None

# Load aivr2asr.csv and retrieve captured audio IDs
csv_file_path = "./aivr2asr.csv"
output_csv_file_path = "./aivr2asr2audio.csv"

with open(csv_file_path, mode='r') as infile, open(output_csv_file_path, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile)
    writer = csv.writer(outfile)
    writer.writerow(['aivr_sid', 'channel', 'asr_sid', 'audio_id'])
    
    for row in reader:
        aivr_sid = row['aivr_sid']
        asr_sid_left = row['asr_sid_L']
        asr_sid_right = row['asr_sid_R']
        
        print(f"Retrieving captured audio ID for ASR session ID (left): {asr_sid_left}")
        captured_audio_left = get_captured_audio_id(asr_sid_left)
        print(f"Captured audio ID (left): {captured_audio_left}")
        writer.writerow([aivr_sid, 'L', asr_sid_left, captured_audio_left])
        
        print(f"Retrieving captured audio ID for ASR session ID (right): {asr_sid_right}")
        captured_audio_right = get_captured_audio_id(asr_sid_right)
        print(f"Captured audio ID (right): {captured_audio_right}")
        writer.writerow([aivr_sid, 'R', asr_sid_right, captured_audio_right])