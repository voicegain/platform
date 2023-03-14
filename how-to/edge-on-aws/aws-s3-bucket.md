# How to create S3 bucket for use with Voicegain Edge Deployment

## Creating and S3 bucket

Once your account is setup login to your aws console https://console.aws.amazon.com and select S3 from services menu.

![Select s3](./choose-s3-service.png)

Click Create Bucket 

![Click Create Bucket](./click-create-bucket.png)

Provide bucket information - note you will need to select a globally unique name - we suggest you append your company name to the end of the bucket name, e.g. "my-s3-bucket.acme"

![Bucket settings part1](./create-s3-bucket-p1.png)

and

![Bucket settings part2](./create-s3-bucket-p2.png)

## Generating AWS Access Key ID and Secret Access Key

We will use a Key that is designated to this S3 bucket. First we need to go to IAM

![AWS IAM](./aws-select-iam.png)

### Create a policy to access the bucket

Here we will first create a policy that will give access only to the previoucly created bucket

![IAM Create Policy](./iam-create-policy.png)

We will define policy in JSON, of course replace `my-s3-bucket` with the name of your target S3 bucket.

![Policy JSON](./bucket-policy-json.png)

<pre>
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": [
                "arn:aws:s3:::my-s3-bucket",
                "arn:aws:s3:::my-s3-bucket/*"
            ]
        }
    ]
}
</pre>

On the "Review policy" page just give it a name and click Create Policy

You will see the new created policy in the Policy list

![New Policy](./our-s3-policy.png)

## Create a user with the policy

Now we need to create a User to which we will assign the S3 polci and the key.

In IAM, we go to Users and click Add users

![Add User](./aws-add-user.png)

We give user a name and give **no** access to AWS Console

![Give user a name](./give-s3-user-name.png)

We choose "Attach policies directly" and select the policy that we created in the previous step.

![Attach policy](./aws-user-attach-policy.png)

On the next page we click Create user

## Generare a key for the user

Then we go back to the User list and select our new created user (click on the user name)

![Select new user](./aws-select-new-user.png)

On the page that opens, we click on "Create access key"

![Click Create access key](./s3-new-user.png)

On the next page we select Other and click Next

On the next page provide a meaningful description and click "Create access key"

![Name the key](./provide-key-name.png)

Now copy the key and click Done

![Copy key](./key-generated.png)