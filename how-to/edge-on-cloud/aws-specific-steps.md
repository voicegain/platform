# <a id="top"></a>AWS Specific Steps
Required Steps, AWS Provided documentation, and recommended best practices
----
**Overview:**
>* Create an AWS Kubernetes cluster with GPU’s and whitelist Voicegain IP's
>* Authorize Voicegain to authenticate by creating a Kubernetes Service Account

## <a id="toc"></a>Table of Contents
- [Step 1: Request GPUs from AWS](#step1)
- [Step 2: Create Cluster](#step2)
- [Step 3: Install Kubectl](#step3)
- [Step 4: Install and Configure awscli](#step4)
- [Step 5: Get kubeconfig](#step5)
TODO: - [Step 6: Give Voicegain Access to K8s](#step6)
- [Step 11: Upload kubeconfig to Voicegain](#step11)
- [Step 12: Allow Access to Voicegain Cloud on AWS](#step12)
- [Step 13: Start Deployment of Chosen Features](#step13)
- [Step 14: Wait for Deployment to Finish](#step14)
- [Step 15: Start Using Voicegain in AWS](#step15)

## <a id="step1"></a>Step 1: Request GPUs from AWS
In order to use GPUs you must request a Quota increase for them from AWS
The types (P type, G type/ On-demand, Spot instances) that you require are dependent on your Organizations needs.
AWS Link: [Instance Types](https://aws.amazon.com/ec2/instance-types/)

Be certain you are requesting them for the AWS Region you wish to run your cluster in.
AWS Link: [EC2 Quota Requests](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas)

## <a id="step2"></a>Step 2: Create Cluster

Link: [AWS Current Guide for Kubernetes Cluster creation](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html)
Link: [Creating Amazon EKS Cluster Role](https://docs.aws.amazon.com/eks/latest/userguide/service_IAM_role.html#create-service-role)
[Create Cluster](AWS-1a.png)

When you reach the "Cluster endpoint access" card in Cluster Creation; it is required that the API server enpoint is Publically available, 
however it is recommended that you limit access to your Organization's access IP and Voicegain's access IP. For security purposes this IP address is avaialble upon request. **Please contact Voicegain to receive the required Voicegain Access IP address.**

[Cluster endpoint access](AWS-2a.png)

Afterward you will need to create nodegroups for your GPU Instasnces for the cluster
Link: [Creating Amazon Node Group](https://docs.aws.amazon.com/eks/latest/userguide/create-managed-node-group.html)

## <a id="step3"></a>Step 3: Install Kubectl

Local system setup, install Kubectl following [these instructions from kubernetes website](https://kubernetes.io/docs/tasks/tools/install-kubectl/)

## <a id="step4"></a>Step 4: Install and Configure awscli

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
aws eks update-kubeconfig --name YOUR_CLUSTER_NAME
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

If you are using Vacuum the kubeconfig will be automatically submitted to Voicegain Cloud. Alternatively, you may use one of the following methods:

* You will have to install the Voicegain API access libraries (at this point please send email to support@voicegain.ai to obtain them) and use your JWT token to upload your kubeconfig file, now located at `~/.kube/confg` to the Voicegain Cloud using PUT https://api.voicegain.ai/v1/cluster/{uuid} - request body has to contain `k8sConfig` field.

* You can also copy/paste kubeconfig file via the Web Console - into the Configuration edit box

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
