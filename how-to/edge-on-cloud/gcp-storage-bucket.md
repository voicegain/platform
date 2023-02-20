# How to configure a Google Storage bucket

Voicegain Edge Deployment to Google VPC can either use (a) an internal storage (within Edge Kubernetes Cluster), or (b) it can use Google Storage via an S3 adapter.

We recommend option (b) because:
1. It will ensure that your data will survive, no matter what happens to the Kubernetes cluster and its persistent volumes.
2. You can set the HA parameters of Google Storage to your liking.
3. There is no limit on the size of the storage.
4. You can use Google GCP tools to monitor storage usage.

The steps to prepare Google Storage for use by Voicegain Edge Deployment are:
1. [Create a Service Account](#step1)
2. [Create a bucket](#step2)
3. [Assign Service Account permissions to that bucket](#step3)
4. [Get request endpoint and create HMAC key](#step4)
5. [(optional) VPC Service Controls](#step5)

## <a name="step1"></a>Create a Service Account

This is done from GCP **IAM & Admin** under the Project in which you want to have the bucket.
* (+) Create Service Account
  * set the name
  * do not set any project access grants
  * do not grant user access
* There is no need to generate the key here, however, see [step4](#step4)

## <a name="step2"></a>Create a bucket

This is done from GCP **Cloud Storage** under the Project in which you want to have the bucket.
* Goto Buckets - > (+) Create
* Give bucket a name 
  * We recommend you use your domain name in the bucket name, e.g., mybucket1.acme.com -- see [Domain-named bucket verification](https://cloud.google.com/storage/docs/domain-name-verification?authuser=3&_ga=2.17559549.-514936252.1656353780)
* Choose from the storage options based on your needs (e.g. is is prod, or test)
* Choose Standard storage class
* Choose Uniform access control
* Choose the protection and encryption settings based on your needs

## <a name="step3"></a>Assign Service Account permissions to that bucket

After creating the bucket we can assign permission to access it to the Service Account we created in [step1](#step1)
* Have the name of the service account ready
* Click on the name of the bucket in the bucket list
* Choose Permissions tab
* Choose (+) Grant Access
* Enter the name of the Service Account into the *New principals* box
* Select Storage Admin role - even though it says "Full control of GCS resources" because it is assigned to a Bucket and not to a Project it will allow only opertations on the specified Bucket.
* Click Save

## <a name="step4"></a>Get request endpoint and create HMAC key

This is done from the Settings page of the **Google Storage**.

Under Setting you can see the Request Endpoint URL that you will need to provide to Voicegain.

Creating HMAC key
* under *Service account HMAC* you will need to click (+) Create a Key for Another Service Account.
* then select the Service Account created in [step1](#step1)
* click Create Key
* from the next page you will need to copy Access key and the Secret - you will share those with Voicegain.

Voicegain will incorporate the url and the key in your custom Edge Configuration, which you will be able to deploy from the Voicegain Web Console.


## <a name="step5"></a>VPC Service Controls

Using VPC Service Controls you can require access to your Google Storage Bucket to be only allowed from e.g. your Edge Kubernetes cluster. This is an additional protection in case the Service Account we created in [step1](#step1) were compromised. 
