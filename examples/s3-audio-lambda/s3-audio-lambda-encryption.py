import json
import boto3
import urllib.parse
import urllib3

s3 = boto3.client('s3')
sqs = boto3.client('sqs')
http = urllib3.PoolManager()

voicegainJwt = "<your context JWT here>"
asrTranscribeUrl = "https://api.voicegain.ai/v1/asr/transcribe/async"
dataAudioUrl = "https://api.voicegain.ai/v1/data/audio"
myAuthConf = "<name of the authConf with the private key>"
headers = {"Authorization" : voicegainJwt, "Content-Type" : "application/json"}

# it's sqs queue url, you need to copy url from your sqs
sqsUrl = "https://sqs.eu-central-1.amazonaws.com/321296667966/test-common-queue"
preassignUrlExpirationTime = 3600

def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    if(event.get("Records") is not None):
        records = event.get("Records")
        try:
            records = event.get("Records")
            eventType = getEventType(records)
            print("Event type is " + eventType)
            if(eventType == 'S3'):
                for record in records:
                    processRecord(record)
            elif(eventType == 'SQS'):
                for record in records:
                    print(str(record['body']))
                    processRecord(json.loads(str(record['body'])))

        except Exception as e:
            eStr = str(e)
            print("Exception: " + eStr)
            return {
                'statusCode': 500,
                'body': json.dumps(eStr)
            }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('No resource')
        }

    return {
        'statusCode': 200,
        'body': json.dumps('OK')
    }

def processRecord(record):
    bucket = record['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(record['s3']['object']['key'], encoding='utf-8')
    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket, 'Key': key},
        ExpiresIn=120)

    audioRequest = {
        "name": key,
        "description": "File from S3",
        #todo find out contentType
        "contentType": "audio/wav",
        #It's possible to change to "enhanced" encryption
        "encryption": "standard",
        "audio": {
            "source": {
                "fromUrl": {
                    "url": url,
                    "fetchTimeout": 20000
                    # "authConf": myAuthConf
                }
            }
        }
    }

    print("Making request to: " + dataAudioUrl)
    audioDataResponse = http.urlopen("POST", dataAudioUrl, headers=headers, body=json.dumps(audioRequest))
    print("response code from VG: " + str((audioDataResponse).status))
    if(audioDataResponse.status == 429):
        retryAfter = getRetryAfterValue(audioDataResponse)
        sendMessageToSQS(record, retryAfter)
        return

    objectId = str(json.loads(audioDataResponse.data.decode("utf-8")).get("objectId"))
    print("objectId is: " + objectId)


    headMetadata = s3.head_object(Bucket=bucket, Key=key)
    lastModified = str(headMetadata.get('LastModified'))
    objectMetadata = headMetadata.get('Metadata')

    requestMetadata = []
    requestMetadata.append({"name" : "bucket", "value" : bucket})
    requestMetadata.append({"name" : "key", "value" : key})
    requestMetadata.append({"name" : "lastModified", "value" : lastModified})

    if objectMetadata:
        for key in objectMetadata.keys():
            requestMetadata.append({"name" : key, "value" : objectMetadata.get(key)})

    vgRequest = {
        "sessions" : [{
            "asyncMode" : "OFF-LINE",
            "audioChannelSelector" : 'mix',
            "vadMode" :"normal",
            "content" : {"full" : ["words"]},

            # this will send it to the portal which is fine for testing
            # for prod you would likely configure a callback
            "portal" : {"label" : bucket +"-"+ key, "persist" : 3600000},

            "metadata": requestMetadata
        }],
        "audio" :{
            "source" :{
                "dataStore": {
                    "uuid": objectId
                }
            },
            "channels" : "mono"
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

    print("Making request to: " + asrTranscribeUrl)

    asr_response_raw = http.urlopen("POST", asrTranscribeUrl, headers=headers, body=json.dumps(vgRequest))

    if(asr_response_raw.status == 429):
        retryAfter = getRetryAfterValue(asr_response_raw)
        sendMessageToSQS(record, retryAfter)

    print("response code from VG: " + str(asr_response_raw.status))
    if(asr_response_raw.status == 200):
        decoded_r = asr_response_raw.data.decode("utf8")
        print("response body from VG: " + str(decoded_r))


def getEventType(records):
    if records[0]['eventSource'] == 'aws:s3':
        return 'S3'
    elif records[0]['eventSource'] == 'aws:sqs':
        # "eventSource": "aws:sqs"
        return 'SQS'


def getRetryAfterValue(vgResponse):
    header = vgResponse.headers
    print("Header: " + str(header))
    retryAfter = int(header.get("Retry-After"))
    print("RetryAfter is: " + str(retryAfter))
    if (retryAfter > 900):
        retryAfter = 900
    return retryAfter


def sendMessageToSQS(record, retryAfter):
    response = sqs.send_message(
        QueueUrl=sqsUrl,
        DelaySeconds=retryAfter,
        MessageBody = json.dumps(record)
    )
    print("Message successfully send to sqs, MessageId:" + response['MessageId'])