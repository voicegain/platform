import requests, time, os, json, re
import configparser

cfg = configparser.ConfigParser()
cfg.read("config.ini")
configSection = cfg.get("DEFAULT", "CONFIG")
protocol = cfg.get(configSection, "PROTOCOL")
hostPort = cfg.get(configSection, "HOSTPORT")
JWT = cfg.get(configSection, "JWT")
urlPrefix = cfg.get(configSection, "URLPREFIX")
outputFolder = cfg.get("DEFAULT", "OUTPUTFOLDER")
inputFolder = cfg.get("DEFAULT", "INPUTFOLDER")
inputFile = cfg.get("DEFAULT", "INPUTFILE")

print(f"CONFIG: {configSection}")
print(f"inputFolder: {inputFolder}")
print(f"inputFile: {inputFile}")

filesToProcess = 5

if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

host = f"{protocol}://{hostPort}/{urlPrefix}"

# Load text file from inputFile
inputFilePath = os.path.join(inputFolder, inputFile)
with open(inputFilePath, 'r') as file:
    text_content = file.read()

print(f"Loaded text content from {inputFilePath}:\n{text_content}")

headers = {"Authorization":JWT}

body = {
    "text": text_content,
    "speakers": ["Speaker 1", "Speaker 2"],
    "formatters" : [
        {
            "type": "redact",
            "parameters": {
                "SSN": "[SSN]",
                "PHONE": "partial",
                "CC": "partial",
                "ZIP" : "[ZIP]",
                "PERSON": "partial",
                "DMY": "[DMY]",
                "CVV" : "[CVV]",
                "ADDRESS": "partial",
            }
        }
        # , {
        #     "type": "regex",
        #     "parameters": {
        #         "mask": "[CODE]",
        #         "options" : "IA",
        #         "pattern": "[1-9][0-9]{3}[ ]?[a-zA-Z]{2}"
        #     }
        # }
    ],
    "debug": {"level": "7"}  
}

url = "{}/text/redact".format(host)

print(f"making request {url}...", flush=True)
response_raw = requests.post(url, json=body, headers=headers)
if(response_raw.status_code != 200):
    print("unexpected response code {} for asr request".format(response_raw.status_code), flush=True)
    print(response_raw, flush=True)
    print(response_raw.text, flush=True)
    print("EXIT", flush=True)
    exit()

response = response_raw.json()

print(f"response: {response}", flush=True)

print("Redacted text:")
print(response.get("redactedText"), flush=True)

# Extract and print redactions
redactions = response.get("redactions", [])
print("\nRedactions:")
for redaction in redactions:
    print(f"Type: {redaction['type']}, Pattern: {redaction['pattern']},\n\tOriginal: {redaction['originalValue']}\n\tRedacted: {redaction['redactedValue']}", flush=True)