import requests
import csv
from datetime import datetime
import configparser

# ...existing code...

CONFIG_FILE_PATH = 'config.ini'

# ...existing code...

def export_data(max_exported_call_id, jwt_token, host, per_page, consecutive, from_time):
    page_num = 1
    new_max_exported_call_id = max_exported_call_id
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    headers = {
        'Authorization': f'Bearer {jwt_token}'
    }

    while True:
        print(f"Fetching page {page_num}...", flush=True)
        ## within the loop we run constant value of afterCallId
        ## only the page gets incremented
        url = f"https://{host}/v1/sa/call?format=csv&per_page={per_page}&page={page_num}&afterCallId={max_exported_call_id}&consecutive={str(consecutive).lower()}&fromTime={from_time}"
        print(f"Making API request to: {url}", flush=True)  # Added print statement
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            print(f"Failed to fetch data: {response.status_code}", flush=True)
            break
        
        content = response.content.decode('utf-8')
        rows = list(csv.reader(content.splitlines()))
        
        if len(rows) <= 1:  # No data rows returned
            print("No more data rows returned.", flush=True)
            break
        
        print(f"Number of rows returned (excluding header): {len(rows) - 1}", flush=True)  # Added print statement
        
        file_name = f'export_{timestamp}_page_{page_num}.csv'
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        
        print(f"Saved data to {file_name}", flush=True)
        
        header = rows[0]
        call_id_index = header.index('callId')
        new_max_exported_call_id = rows[-1][call_id_index]  # Extract callId from the correct column
        page_num += 1

    return new_max_exported_call_id

# Load configuration
config = configparser.ConfigParser()
config.read(CONFIG_FILE_PATH)
environment = config['DEFAULT']['environment']
jwt_token = config[environment]['jwt_token']
host = config[environment]['host']

# Read max_exported_call_id, per_page, consecutive, and from_time from export.ini
try:
    max_exported_call_id = int(config['EXPORT']['max_exported_callid'])
except (configparser.NoSectionError, configparser.NoOptionError, ValueError):
    max_exported_call_id = 0

try:
    per_page = int(config['EXPORT']['per_page'])
except (configparser.NoSectionError, configparser.NoOptionError, ValueError):
    per_page = 1000  # Default value

try:
    consecutive = config.getboolean('EXPORT', 'consecutive')
except (configparser.NoSectionError, configparser.NoOptionError, ValueError):
    consecutive = True  # Default value

try:
    from_time = config['EXPORT']['from_time']
except (configparser.NoSectionError, configparser.NoOptionError):
    from_time = '2024-08-01T00:00:00Z'  # Default value

# Example usage:
print("Starting data export...", flush=True)
new_max_exported_call_id = export_data(max_exported_call_id, jwt_token, host, per_page, consecutive, from_time)
print("Data export completed.", flush=True)

# Save new_max_exported_call_id to config.ini
if 'EXPORT' not in config:
    config.add_section('EXPORT')
config['EXPORT']['max_exported_callid'] = str(new_max_exported_call_id)
with open(CONFIG_FILE_PATH, 'w') as configfile:
    config.write(configfile)
print(f"Updated max_exported_call_id to {new_max_exported_call_id}", flush=True)

# ...existing code...
