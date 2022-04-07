# Configuring AWS S3 for use with Voicegain Edge Deployment

## Step 1: Create S3 bucket

[AWS Instructions for bucket creation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html)

You can create s3 bucket from the [AWS S3 Console](https://console.aws.amazon.com/s3/)

Some relevant settings:
* Object Ownership: ACLs disabled / Bucket owner enforced
* Block public access: Block **all** public access
* Bucket Versioning: disabled


If the voicegain Edge is also running on AWS, it's better to create a bucket in the same region as the Edge Deployment.

 ## Step 2: Create IAM policy

 [AWS Instructions for access policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html)

 You can create the required policy from the [AWS IAM Console](https://console.aws.amazon.com/iam/)

Choose: Policies -> Create Policy -> JSON


Replace BUCKET-NAME with you actual bucket name.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::BUCKET-NAME",
                "arn:aws:s3:::BUCKET-NAME/*"
            ]
        }
    ]
}
```

## Step 3: Create a user

Create a user, and attach the policy created in Step 2 to the user. Get access key and secret key of the new user

 You can do this from the [AWS IAM Console](https://console.aws.amazon.com/iam/)

## Step 4: Provide information to Voicegain

Soon you will be able to enter it into Voicegain Web Console. For now you will need to communicate this information directly to Voicegain (via email, chat, etc).

* Server URL: https://s3.<REGION>.amazonaws.com
* Bucket name: bucket name created in Step 2
* Access Key and Secret Key: keys created in Step 3