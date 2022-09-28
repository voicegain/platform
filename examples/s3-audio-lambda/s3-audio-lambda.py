import json
import boto3
import urllib.parse
import urllib3

s3 = boto3.client('s3')

voicegainJwt = "<your context JWT here>"
voicegainUrl = "https://api.ascalon.ai/v1/asr/transcribe/async"
myAuthConf = "<name of the authConf with the private key>"
headers = {"Authorization" : voicegainJwt, "Content-Type" : "application/json"}

def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))
    if(event.get("Records") is not None):
        records = event.get("Records")
        try:
            for record in records:
                bucket = record['s3']['bucket']['name']
                key = urllib.parse.unquote_plus(record['s3']['object']['key'], encoding='utf-8')

                url = s3.generate_presigned_url(
                    'get_object',
                    Params={'Bucket': bucket, 'Key': key},
                    ExpiresIn=3600)

                vgRequest = {
                    "sessions" : [{
                        "asyncMode" : "OFF-LINE",
                        "audioChannelSelector" : 'mix',
                        "vadMode" :"normal",
                        "content" : {"full" : ["words"]},

                        # this will send it to the portal which is fine for testing
                        # for prod you would likely configure a callback
                        "portal" : {"label" : bucket +"-"+ key, "persist" : 3600000},

                        "metadata" : [
                            {"name" : "bucket", "value" : bucket},
                            {"name" : "key", "value" : key},
                        ]
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

                http = urllib3.PoolManager()

                print("Making request to: " + voicegainUrl)

                asr_response_raw = http.urlopen("POST", voicegainUrl, headers=headers, body=json.dumps(vgRequest))

                print("response code from VG: " + str(asr_response_raw.status))
                if(asr_response_raw.status == 200):
                    decoded_r = asr_response_raw.data.decode("utf8")
                    print("response body from VG: " + str(decoded_r))
                    return {
                        'statusCode': 200,
                        'body': json.dumps('OK')
                    }
                else:
                    return {
                        'statusCode': 200,
                        'body': json.dumps('OK but Voicegain request returned code ' + str(asr_response_raw.status))
                    }


        except Exception as e:
            eStr = str(e)
            print("Exception: "+eStr)
            return {
                'statusCode': 500,
                'body': json.dumps(eStr)
            }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps('No resource')
        }