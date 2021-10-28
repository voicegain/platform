# <a id="top"></a>Deploy Voicegain into AWS
Step by step guide how to deploy Voicegain Speech-to-Text Platform into AWS
----
Under the hood:
This guide will have you do the following:
* Create an AWS Kubernetes cluster with GPU’s
* Authorize Voicegain to authenticate with your cluster by editing the aws-auth configmap and uploading your kubeconfig file to the Voicegain Console

At step 4 we describe the option of using Vacuum CLI tool. This tool is not yet publicly available. We will modify this document as soon as we make it available with instructions on how  to download it.

## <a id="toc"></a>Table of Contents
- [Step 1: Request GPUs from AWS](#step1)
- [Step 2: Create a User](#step2)
- [Step 3: Create Roles](#step3)
- [Step 4: Choose Between Automated or Manual K8s Setup](#step4)
- [Step 5: Create Cluster](#step5)
- [Step 6: Create NodeGroup](#step6)
- [Step 7: Install Kubectl](#step7)
- [Step 8: Install and Configure awscli](#step8)
- [Step 9: Get kubeconfig](#step9)
- [Step 10: Give Voicegain Access to K8s](#step10)
- [Step 11: Upload kubeconfig to Voicegain](#step11)
- [Step 12: Allow Access to Voicegain Cloud on AWS](#step12)
- [Step 13: Start Deployment of Chosen Features](#step13)
- [Step 14: Wait for Deployment to Finish](#step14)
- [Step 15: Start Using Voicegain in AWS](#step15)

## <a id="step1"></a>Step 1: Request GPUs from AWS

This may take a while so it is smart to do this at the very beginning

## <a id="step2"></a>Step 2: Create a User

Under IAM: 
* Create a user with Console Access* and Programmatic API access and save your "access key ID" and "secret access key"
* Create a password<sup>*</sup> and identify a default regions such as ‘us-east-2’ (For simplicity you can provide full AWS service/resource access by adding user to a Group with AdministratorAccess)

<sup>*</sup> NOTE: Console Access and Password creation not required for Vacuum CLI users.

![IAM Create Group](./IAM-create-group.png)

![Add User Step 1](./add-user.png)

![Add User Step 2](./add-user-2.png)

![Add User Step 3](./add-user-3.png)

## <a id="step3"></a>Step 3: Create Roles

### Method A

1. Create Amazon EKS worker node role in IAM console: [see AWS User Guide](https://docs.aws.amazon.com/eks/latest/userguide/worker_node_IAM_role.html)
2. Create Amazon EKS Service role in IAM console: [see AWS User Guide](https://docs.aws.amazon.com/eks/latest/userguide/service_IAM_role.html)

![Create Role Step 1](./create-role.png)

![Create Role Step 2](./create-role-2.png)

Caveat: The EKS Role will not appear available in Cluster Creation until you either completely refresh the page or close and renavigate to Cluster Creation. (Navigating away and back to Cluster Creation has not ever worked in all of our tests.)

Alternatively, you can create Roles using method B

### Method B

Create a role in Amazon IAM with the following 5 policies:
* [AmazonEKSClusterPolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonEKSClusterPolicy$jsonEditor)
* AmazonEKSServicePolicy
* [AmazonEKSWorkerNodePolicy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy$jsonEditor)
* [AmazonEKS_CNI_Policy](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy$jsonEditor)
* [AmazonEC2ContainerRegistryReadOnly](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly$jsonEditor)

With the following Trust Relationship:
```javascript
{
  "Version": "2020-01-01",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "eks.amazonaws.com",
          "ec2.amazonaws.com"
        ]
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

## <a id="step4"></a>Step 4: Choose Between Automated or Manual K8s Setup

Either:

### Provision Amazon K8S cluster using Vacuum tool

**Recommended:** Set up ‘vacuum’ tool on your administration system, you will need your AWS credentials, EKS Worker Role, and subnet IDs from AWS.

Create Edge Cluster via Voicegain Console and retrieve ClusterID, then  
<pre>
vacuum k8s provision -t cluster_name -u Cluster_ID
</pre>

Then skip to [Step 12](#step12)

### Provision Amazon K8S cluster manually

Sign out of AWS Console and Sign In with the IAM User created in Step one. You will sign in with your Account ID, Username, and password.

Then proceed with [Step 5](#step5)

## <a id="step5"></a>Step 5: Create Cluster 

Create Cluster w/ EKSServiceRole:

![Create Cluster](./create-cluster.png)

## <a id="step6"></a>Step 6: Create NodeGroup

Create NodeGroup

![Node Group](./node-group.png)

When creating the NodeGroups, Voicegain will require GPU’s, thus choose the Amazon Linux 2 GPU Enabled (AL2_x86_64)) AMI type and a g4dn EC2 Instance Type. 
Minimum 2xlarge (32 GiB memory) w/ minimum 2 nodes.

## <a id="step7"></a>Step 7: Install Kubectl

Local system setup, install Kubectl following [these instructions from kubernetes website](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

## <a id="step8"></a>Step 8: Install and Configure awscli

Install and configure awscli:

If using Python: 
<pre>
python -m pip install awscli --user
aws configure
</pre>
You can test for successful configuration with:
<pre>
aws eks list-clusters
</pre>

## <a id="step9"></a>Step 9: Get kubeconfig

Retreive kubernetes configuration file:
<pre>
aws eks update-kubeconfig –name YOUR_CLUSTER_NAME
</pre>
And test access with the following:  
<pre>
kubectl get nodes
</pre>

## <a id="step10"></a>Step 10: Give Voicegain Access to K8s

Provide Voicegain with access to the Kubernetes (k8s) cluster:

Create a file on the local system named voicegain-auth.yaml with the following content:
<pre>
data:
  mapUsers: |
    - userarn: arn:aws:iam::977776626189:user/VoicegainAgent
      username: vg_user
      groups:
        - system:masters
</pre>
And patch the aws-auth configmap with the following command:
<pre>
kubectl -n kube-system patch cm aws-auth --patch "$(< voicegain-auth.yaml )"
</pre>

## <a id="step11"></a>Step 11: Upload kubeconfig to Voicegain

If you are using Vacuum the kubeconfig will be automatically submitted to Voicegain Cloud.

If not, you will have to install the Voicegain API access libraries (at this point please send email to support@voicegain.ai to obtain them) and use your JWT token to upload your kubeconfig file, now located at `~/.kube/confg` to the Voicegain Cloud using PUT https://api.voicegain.ai/v1/cluster/{uuid} - request body has to contain `k8sConfig` field.

You can also copy/paste kubeconfig file via the Web Console - into the Configuration edit box
![Paste kubeconfig into Web Console](./Edge-config-connection.PNG) 

## <a id="step12"></a>Step 12: Allow Access to Voicegain Cloud on AWS

Allow access to Voicegain Cloud on AWS by editing the Cluster’s Security-Group (Inbound Rules):

![EKC Cluster Configuration](./eks-cluster-config.png)

![Cluster Security Group](./cluster-security-group.png)

Add a new Inbound Rule w/ Custom TCP Port 31680 and Source of “My IP” (or any IP’s you want to be able to reach your cluster management console):

![Edit Inbound Rules](./edit-inbound-rules.png)

## <a id="step13"></a>Step 13: Start Deployment of Chosen Features

From the [Voicegain Console](https://console.voicegain.ai "Voicegain Cloud Console"), choose the build version, the configuration, and the model type you wish to utilize and press `(Re)Build Cluster` button at the bottom of the page. 

![Choose the build version](./Edge-config-config-version.PNG)

![Choose the configuration and model type](./Edge-config-config-config.PNG)

## <a id="step14"></a>Step 14: Wait for Deployment to Finish

You can watch the progress of your cluster deployment via:
<pre>
watch `kubectl get po`
</pre>

## <a id="step15"></a>Step 15: Start Using Voicegain in AWS

Once the deployment has settled, follow the Customer-console link on your Edge Deployment page on [console.voicegain.ai](https://console.voicegain.ai "Voicegain Cloud Console") , log in, and begin transcribing! 

All done!

---
Goto: [top of document](#top)
