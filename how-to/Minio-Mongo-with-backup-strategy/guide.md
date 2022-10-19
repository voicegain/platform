![image](https://user-images.githubusercontent.com/14049448/195718717-b86e8529-0758-45a5-b88a-e787633f30ad.png)


# <a id="top"></a> Setup Minio (S3 compatible) Object Store and MongoDB with reliable backup strategy
Step by step guide how to deploy Minio and Mongo Docker containers to systems (Baremetal or VM) and a recommended backup approach
----
**Prerequisites:**
* Dedicated backup storage system that can be accessed via SSH.
* Either one or two systems running Ubuntu 20.04 (You can run both Minio and Mongo containers on a single system if needed. This may work with Ubuntu 22.04 but we are using 20.04 for this guide.)

## <a id="toc"></a>Table of Contents
- [Step 0: Critical Storage Requirements](#before)
- [Step 1: Install Packages and initial SSH config](#step1)
- [Step 2: Minio and backup solution](#step2)
- [Step 3: MongoDB and backup solution](#step3)

## <a name="before"></a>Step 0: Critical Storage Requirements

**Dedicated Remote Backup Storage Recommendation:**  
Each of the Minio and MongoDB container will have their own local storage on their respective systems. The backup solutions in this guide aim to provide reliable application consistent backups that can resist corruption in the case of an enexpected system fault. This assumes that you have SSH access to a system that has reliable storage redundancy via some technology such as RAID or Ceph, etc...

**MongoDB Storage Requirements**
The Docker container for Mongodb will be mounting a local drive for storage. This partition MUST be an LVM in order for our backup solution to work. Furthermore, the !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

**Minio Storage Requirements**
In the case of Minio there are no special requirements. However, it is a best practice to have a dedicated partition to be mounted in the container. This can avoid issues with the underlying host system in the event that the disk fills. 

![storagechart](minioandmongo-storage.png)

## <a name="step1"></a>Step 1: Install Packages and initial SSH config

These guides will take you through the basics and provide resources and links do provider documentation on how to create a kubernetes cluster appropriate for our application. When you have completed creating your GPU enabled k8s cluster please proceed with [Step 2](#step2)

* [AWS Specific Steps](aws-specific-steps.md)  
* GCP: Coming Soon  
* Oracle: Coming Soon 

## <a name="step2"></a>Step 2: Create Voicegain service account on your Cluster
Many cloud providers take a unique approach to authenticating and interacting with your k8s cluster. In many cases this may require authentication or roles on the Cloud account level. This following step will create a kubernetes specific service account for Voicegain so to ensure a uniform experience as well on not requiring any access to your Cloud account. We will only be interacting directly with the Kubernetes API endpoint with a kubernetes cluster role.

You will want to copy and paste the entire code block below into the terminal of your linux system that has kubectl configued and connected to your new cluster as outlined in our Cloud Specific Guides:. 
<pre>
kubectl -n kube-system create serviceaccount voicegain-manage
kubectl create clusterrolebinding voicegain-manage --clusterrole=cluster-admin --serviceaccount=kube-system:voicegain-manage
TOKENNAME=`kubectl -n kube-system get serviceaccount/voicegain-manage -o jsonpath='{.secrets[0].name}'`
CA=$(kubectl get -n kube-system secret/$TOKENNAME -o jsonpath='{.data.ca\.crt}')
TOKEN=$(kubectl get -n kube-system secret/$TOKENNAME -o jsonpath='{.data.token}' | base64 --decode)
SERVER_URL=$(kubectl cluster-info | head -n1 |awk '/Kubernetes/ {print $NF}'| sed 's/\x1B\[[0-9;]\{1,\}[A-Za-z]//g')

echo "
apiVersion: v1
kind: Config
clusters:
- name: vg-edge-cluster
  cluster:
    certificate-authority-data: ${CA}
    server: ${SERVER_URL}
contexts:
- name: vg-edge-context
  context:
    cluster: vg-edge-cluster
    user: vg-edge-user
current-context: vg-edge-context
users:
- name: vg-edge-user
  user:
    token: ${TOKEN}
" > vg_kubeconfig.yaml
</pre>

