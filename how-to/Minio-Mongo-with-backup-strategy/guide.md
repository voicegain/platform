# <a id="top"></a> Setup Minio (S3 compatible) Object Store and MongoDB with reliable backup strategy
Step by step guide how to deploy Minio and Mongo Docker containers to systems (Baremetal or VM) and a recommended backup approach
----
**Prerequisites:**
* Dedicated backup storage system that can be accessed via SSH.
* Either one or two systems running Ubuntu 20.04 (You can run both Minio and Mongo containers on a single system if needed. This may work with Ubuntu 22.04 but we are using 20.04 for this guide.)

## <a id="toc"></a>Table of Contents
- [Step 0: Critical Storage Requirements](#before)
- [Step 1: Install Packages and initial SSH config](#step1)
- [Step 2: Minio setup and backup solution](#step2)
- [Step 3: MongoDB setup and backup solution](#step3)

## <a name="before"></a>Step 0: Critical Storage Requirements

**Dedicated Remote Backup Storage Recommendation:**  
Each of the Minio and MongoDB container will have their own local dedicated storage on their respective system(s). The backup solutions in this guide aim to provide reliable application consistent backups that can resist corruption in the case of an enexpected system fault. This assumes that you have SSH access to a system that has reliable storage redundancy via some technology such as RAID or Ceph, etc...

On the remote backup storage system, you will create a directory for minio and a directory for mongodb backups. This need to be writtable by your user. The directories should be on a redundant or regularly backedup partition/disk.

For this guide we will suppose that the user: `ubuntu` has mounted backup drives to `/home/ubuntu/backups/minio` and `/home/ubuntu/backups/mongodb`

Specific configuration and storage requirements for the docker systems will be addressed under their respective application below. However, you can review the following chart to determine the ideal size of the local storage volumes for each application based on your expected usage:

![storagechart](minioandmongo-storage.png)

## <a name="step1"></a>Step 1: Install Packages and initial SSH config
If you are using a single system for both Minio and MongoDB then simply run all of the following commands within your terminal, otherwise, the prerequsites have been broken down in to General, Minio-Specific, and MongoDB-Specific.

**General Prerequisites:**
* **NOTE:** *After running the following block of commands (ending with `usermod -aG docker ${USER}`) you must log out and log back in in order for your user to be able to run docker commands without requiring sudo.*
<pre>
sudo apt update ; sudo apt install apt-transport-https ca-certificates curl rsync software-properties-common -y && curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - && sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable" && sudo apt install docker-ce -y && sudo usermod -aG docker ${USER}
</pre>

**Minio System Prerequisites:**
<pre>
sudo apt update ; sudo apt install sshfs -y
curl https://dl.min.io/client/mc/release/linux-amd64/mc \
  --create-dirs \
  -o $HOME/minio-binaries/mc

chmod +x $HOME/minio-binaries/mc
export PATH=$PATH:$HOME/minio-binaries/
echo "export PATH=$PATH:$HOME/minio-binaries/" >> ~/.bashrc
</pre>

**MongoDB System Prerequisites:**
<pre>
sudo apt update ; sudo apt install lvm2 xfsprogs mongodb-clients
</pre>

## <a name="step2"></a>Step 2: Minio setup and backup solution

**Minio Storage Requirements**
In the case of Minio there are no special requirements. However, it is a best practice to have a dedicated partition to be mounted in the container. This can avoid issues with the underlying host system in the event that the disk fills. 


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

## <a name="step3"></a>Step 3: MongoDB setup and backup solution


**MongoDB Storage Requirements**
The Docker container for Mongodb will be mounting a local drive for storage. This partition MUST be an LVM 
