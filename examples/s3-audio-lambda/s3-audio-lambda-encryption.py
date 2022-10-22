import json
import boto3
import urllib.parse
import urllib3
from enum import Enum
from botocore.exceptions import ClientError
import time

s3 = boto3.client('s3')
sqs = boto3.client('sqs')
http = urllib3.PoolManager()
dynamodb = boto3.resource('dynamodb')
dynamoDbTableName = "VoicegainRateLimit"
table = dynamodb.Table(dynamoDbTableName)

voicegainJwt = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJodHRwczovL2FwaS52b2ljZWdhaW4uYWkvdjEiLCJzdWIiOiIzOTBlYmRhNy1iZDAwLTQzMGQtOTI3My02NTE3Y2Q1NjA3ZjMifQ.QP7Q7CR9BlebO4OH9u9l8HqsG_hXFOCGKry5eWtAQ9g"
asrTranscribeUrl = "https://api.voicegain.ai/v1/asr/transcribe/async"
dataAudioUrl = "https://api.voicegain.ai/v1/data/audio"
myAuthConf = "<name of the authConf with the private key>"
headers = {"Authorization" : voicegainJwt, "Content-Type" : "application/json"}

# it's sqs queue url, you need to copy url from your sqs
sqsUrl = "https://sqs.us-east-2.amazonaws.com/921245439331/voicegain-rate-limit-queue"
preassignUrlExpirationTime = 120
eventTypeS3 = "S3"
eventTypeSQS = "SQS"

class Status(Enum):
    PENDING = 1
    PROCESSED = 2
    RETIRED = 3

def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    if(event.get("Records") is not None):
        records = event.get("Records")
        try:
            records = event.get("Records")
            eventType = getEventType(records)
            print("Event type is " + eventType)
            if(eventType == eventTypeS3):
                for record in records:
                    processRecord(record, eventType)
            elif(eventType == eventTypeSQS):
                for record in records:
                    print(str(record['body']), eventType)
                    processRecord(json.loads(str(record['body'])), eventType)

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

def processRecord(record, eventType):
    bucket = record['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(record['s3']['object']['key'], encoding='utf-8')

    retryCounter = 1
    objectId = None
    if(eventType == eventTypeSQS):
        if('retryCounter' in record):
            retryCounter = int(record['retryCounter']) + 1
        if('audioId' in record):
            objectId = record['audioId']

    if(eventType == eventTypeSQS):
        try:
            saveToDynamoDb(key, retryCounter, Status.PENDING.name)
        except ClientError as e:
            if e.response['Error']['Code']=='ConditionalCheckFailedException':
                print("Item is already processed: " + key)
                return

    if(objectId is None):
        objectId = saveAudio(bucket, key, record, retryCounter)
    if objectId is not None:
        print("objectId is: " + objectId)
        transcribeAudio(bucket, key, objectId, record, eventType, retryCounter)


def saveAudio(bucket, key, record, retryCounter):
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
        sendMessageToSQS(record, retryAfter, retryCounter, None)
        saveToDynamoDb(key, retryCounter, Status.PENDING.name)
        return None
    objectId = str(json.loads(audioDataResponse.data.decode("utf-8")).get("objectId"))
    return objectId


def transcribeAudio(bucket, key, objectId, record, eventType, retryCounter):
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
        sendMessageToSQS(record, retryAfter, retryCounter, objectId)
        saveToDynamoDb(key, retryCounter, Status.PENDING.name)
    print("response code from VG: " + str(asr_response_raw.status))
    if(asr_response_raw.status == 200):
        decoded_r = asr_response_raw.data.decode("utf8")
        print("response body from VG: " + str(decoded_r))
        if(eventType == eventTypeSQS):
            saveToDynamoDb(key, -1, Status.PROCESSED.name)

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


def sendMessageToSQS(record, retryAfter, retryCounter, audioId):
    record.update({"retryCounter": retryCounter})
    if audioId is not None:
        record.update({"audioId": audioId})
    response = sqs.send_message(
        QueueUrl=sqsUrl,
        DelaySeconds=retryAfter,
        MessageBody = json.dumps(record)
    )
    print("Message successfully send to sqs, MessageId:" + response['MessageId'])

def saveToDynamoDb(id, retryCounter, status):
    Item={
        'id': id,
        'retryCounter': retryCounter,
        'status': status,
        'created': int(time.time() + 24*60*60) #current time + 1 day, using for dynamoDb ttl
    }
    table.put_item(Item=Item,  ConditionExpression="attribute_not_exists(id)")