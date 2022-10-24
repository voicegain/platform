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

voicegainJwt = "<your context JWT here>"
asrTranscribeUrl = "https://api.voicegain.ai/v1/asr/transcribe/async"
myAuthConf = "<name of the authConf with the private key>"
headers = {"Authorization" : voicegainJwt, "Content-Type" : "application/json"}
# it's sqs queue url, you need to copy url from your sqs
sqsUrl = "<SQS url>"
preassignUrlExpirationTime = 3600
eventTypeS3 = "S3"
eventTypeSQS = "SQS"

class Status(Enum):
    PENDING = 1
    PROCESSED = 2
    RETIRED = 3

def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    if(event.get("Records") is not None):
        try:
            records = event.get("Records")
            eventType = getEventType(records)
            print("Event type is " + eventType)
            if(eventType == eventTypeS3):
                for record in records:
                    processRecord(record, eventType)
            elif(eventType == eventTypeSQS):
                for record in records:
                    print(str(record['body']))
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
    if(eventType == eventTypeSQS):
        if('retryCounter' in record):
            retryCounter = int(record['retryCounter']) + 1

    if(eventType == eventTypeSQS):
        try:
            saveToDynamoDb(key, retryCounter, Status.PENDING.name)
        except ClientError as e:
            if e.response['Error']['Code']=='ConditionalCheckFailedException':
                print("Item is already processed: " + key)
                return

    url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket, 'Key': key},
        ExpiresIn=preassignUrlExpirationTime)

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
                "fromUrl" : {
                    "url" : url,
                    "authConf" : myAuthConf
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
        sendMessageToSQS(record, retryAfter, retryCounter)
        # saveToDynamoDb(key, retryCounter, Status.PENDING.name)

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


def sendMessageToSQS(record, retryAfter, retryCounter):
    record.update({"retryCounter": retryCounter})
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