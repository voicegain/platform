# <a id="top"></a> WIP DRAFT: In Progess. Do not Refer to this as a guide.
Deploy Voicegain to Cloud Provider Managed Kubernetes Cluster
Step by step guide how to deploy Voicegain Speech-to-Text Platform on your Cloud Managed Kubernetes Cluster
----
Under the hood:
This guide will have you do the following:
* Create an Edge Cluster within the Voicegain Console
* Provide instructions to provision and setup Kubernetes (k8s) on popular Cloud Providers
* Connect Voicegain to your k8s cluster
* Deploy the Voicegain Application to your cloud. 

## <a id="toc"></a>Table of Contents
- [Before you Start](#before)
- [Step 1: Cloud Provider Specific Guides](#step1)
- [Step 2: Create Voicegain service account on your Cluster](#step2)
- [Step 3: Create Cluster on VoiceGain](#step3)
- [Step 4: Upload your Kubeconfig file to Voicegain](#step4)
- [Step 11: Deploy Voicegain Application](#step11)
- [Step 12: Reboots, Notes and Caveats](#step12)
- [CRITICAL NOTE ON SYSTEM UPDATES](#updates)
- [Billing and Licensing](#license)

## <a name="before"></a>Before you Start 
**Request GPU Access from your Cloud Provider:**
Many cloud providers, including AWS and GCP, require you to specifically request GPUs for your account. This process can take a few days to be processed so it's best to start this early.

**Voicegain Specific Steps:**
In order to deploy Voicegain on Edge your account needs to have the Edge feature enabled - otherwise you will not see the relevant pages in the [Voicegain Web Console](https://www.voicegain.ai). Please contact support@voicegain.ai to have that enabled.

When you contact us we will ask you to describe your intended usage (e.g. offline transcription or MRCP ASR) so that we can enable an appropriate Edge configuration for your use case. If you are only exploring we can enable several generic configurations to allow you to test a variety of uses. For production use we will prepare a custom configuration that makes the best use of resources on your server(s). We will also configure port based licensing if desired (default is usage-based billing). 

## <a name="step1"></a>Step 1: Cloud Provider Specific Guides

[AWS Specific Steps](aws-specific-steps.md)


## <a name="step2"></a>Step 2: Create Voicegain service account on your Cluster
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

## <a name="step4"></a>Step 4: Create Cluster on VoiceGain

1. Go to: https://console.voicegain.ai
2. If you do not have a developer account, you would need to sign up first. Detailed instructions are provided [here](https://www.voicegain.ai/post/how-to-signup-for-a-developer-account-and-start-using-voicegain-voice-ai).
3. Log in to the console and go to the "[Edge Deployment](https://console.voicegain.ai/specific/edge-deployments)" view. Click "**+ ADD**" and name your Cluster and choose **User-configured Kubernetes cluster**.

![Add new Edge Deployment](./Universal-1a.png)


3. Find your newly created cluster in the Edge Deployment list and Load it by clicking the button to the right of the entry (left of the Delete/Trash button) 
![Load Cluster](./Universal-1b.png)


4. 
5. 
6. 
7. Create Cluster on VoiceGain
> **System Provisioning Considerations:** For the sake of simplicity; the remainder of this guide will assume we are solely using the Ubuntu system we have just installed to complete all the remaining steps. However, it is entirely possible to complete this remotely. To do this, you would open a terminal and run `sudo apt install openssh-server -y`. You can, then, create the Cluster on the Voicegain portal from the system of your choosing and paste the EZInitCommand to the Ubuntu system over ssh.

1. On your new Ubuntu system: open Firefox and go to: https://console.voicegain.ai
2. If you do not have a developer account, you would need to sign up first. Detailed instructions are provided [here](https://www.voicegain.ai/post/how-to-signup-for-a-developer-account-and-start-using-voicegain-voice-ai).
3. Log in to the console and go to the "[Edge Deployment](https://console.voicegain.ai/specific/edge-deployments)" view. Click "**+ ADD**" and name your Cluster and choose **EZ Setup**.

![Add new Edge Deployment](./7-1.png)


3. Find your newly created cluster in the Edge Deployment list and Load it by clicking the button to the right of the entry (left of the Delete/Trash button) 
![Load Cluster](./7-2.png)


4. Define the Connection parameters relevant to your circumstance. Ideally your Edge Deployment will be in your DMZ or "Edge" and, as such, is reachable from the internet. If so, choose the top radio button: "Reachable from internet" and provide the IP Address or Fully Qualified Domain Name as well as the K8S API port (by default this is 6443). Alternatively, if you do not have a DMZ or the ability to add a pinhole in your firewall; you should choose: "Set up control tunnel". Then Click "**Apply**" and "**> Next**"
> **What is the control tunnel?:** In order to connect to systems behind a strict Firewall your Edge system will leverage autossh to establish an SSH tunnel with our network over the HTTPS (port 443) protocol. This is a non interactive shell session that solely creates a reverse port forward so that we can reach your Kubernetes API from within our network.
![Connection Parameters](./7-3.png)

5. Click "**Generate**" and then "**Copy**". You now have the Command script in your clipboard. 
![Generate Command Script](./7-4.png)

## <a name="step8"></a>Step 8: Run EZInit Script
Paste the copied Command Script into a terminal session on the Edge System, hit enter and provide your password for sudo when prompted. 

* **NOTE:** Ubuntu 20 handles sudo commands differently than other distros and previous versions. It is **required** to run sudo while preserving the home directory:
``` sudo --preserve-env=HOME bash voicegain-init.sh ``` 

![EZInitScript](./8-1.png)

The script will check to see if the `voicegain` user exists and create it if not. If the script is not being ran by the `voicegain` user it will ask you to proceed with the following steps:

```
sudo su -
su voicegain
vginstall
```

**INFO:** if the EZInit script is used to create the `voicegain` user, it will be created as a system user with passwordless sudo and no password. This user cannot log into the system directory or remotely. The script will then be copied to the system user directory `/opt/voicegain/bin/` and aliased as `vginstall`

## <a name="step9"></a>Step 9: Reboot

### The details: 
#### Why Reboot?
We are rebooting in order to ensure the Nvidia drivers are loaded into the kernel. This can be done manually, however, this is not always reliable as changes are made in future updates, and if you are logged in to the graphical interface this is even more complicated.

#### Single-Node Cluster
If this is a single node cluster, press any key when prompted to reboot (ignore MultiNodeEZWokerScript command).

#### Multi-Node Cluster
IF you are setting up a multi-node cluster DO NOT YET REBOOT...

The scope of this guide is focused on simple single node clusters, however, if you wish to have a mutli node cluster: 
- Follow steps 1 through 6 of this guide on the next system. 
- Copy the `MultiNodeEZWokerScript` command provided at the end of the EZInit script on the previous node.
- SSH into the next node and paste the copied command. 
- The output of each script will provide the command for the following node and prompt for a reboot. Do not reboot until the final node is provisioned. 
- Continue this process until you've provisioned your final node. Once the final node has been provisioned you can reboot all the nodes.

TLDR:
Install Ubuntu. Run EZInitScript. Run subsequent MultiNodeEZWorkerScript(s). Then Finally: Press any key in the terminal session of each node to Reboot. 

![Press the anykey](./9-1.png)

## <a name="step10"></a>Step 10: Ensure Cluster is Functional
Once rebooted, log in and open a terminal session and run the following commands: 

`kubectl cluster-info`

It should provide endpoints and confirmation that Kubernetes master and KubeDNS are both running.

`kubectl get po`

At the time of this writing we are using nfs-client-provisioner as our default storage class provider. So you should see a single pod in the Running state.
![Healthcheck](./10-1.png)

`watch kubectl get po`

And leave this session open and running, this will allow us to monitor the progress of the deployment in the following step

## <a name="step11"></a>Step 11: Deploy Voicegain Application
Repeat the process in [Step 7](#step7) to load your Cluster in the Voicegain Console

- Click on the Configuration Tab
- Select Build Version. Generally the most recent is recommended.
- Select one of the available Cluster Configurations (only ones compatible with you K8S cluster will be shown).
  - If you do not see a suitable configuration among the available choices please contact Voicegain support. 
- OPTIONAL: Enter Host Name for Web Edge Console access. This applies if your Edge system has a custom internal address or DNS name required to access it.
- (Ignore the external Storage settings. This applies to custom large configurations only.)
- Choose to (Re)Build cluster to begin the deployment

![Deploy1](./11-1-1.png)
![Deploy2](./11-1-2.png)
![Deploy3](./11-1-3.png)
- Monitor the progress on the terminal session we created in step 10.
- Check the status on the Console to see when the deployment is finished, then you can click the link to open your local portal.

![Portal](./11-2.png)
- Choose "Log In(Cloud)" and use your Voicegain credentials

![Login](./11-3.png)

- Now you can test your new deployment. 
  - On the home page click on the "Run test" button on the Function Tests card.
  - If you chose an off-line acoustic model you can also test by uploading a file for transcription.

![Transcribe](./11-4.png)

## <a name="step12"></a>Step 12: Reboots, Notes and Caveats

The EZInit script has enabled all required services for the cluster to start automatically upon reboot. After rebooting the system you may need to wait up to 10 minutes for all of the individual components to start and settle. 

The cluster configuration is ran as the non-root user who ran the EZInit script. If you require other users on the system to have access to the kubectl command line tool you will want to copy the kubernetes configuration file to their home directory. 

For example, you create a new user named 'bobert' who needs to be able to run kubectl commands and administer the cluster. After adding the user to Ubuntu (adduser or useradd). Run the following commands, making certain to assign the newly created user to the Newuser variable:
```
Newuser=bobert ### replace bobert with new user
Newhome=/home/${Newuser}
Newkube=${Newhome}/.kube
Newconfig=${Newkube}/config
sudo mkdir -p ${Newkube}
sudo cp /etc/kubernetes/admin.conf ${Newconfig}
sudo chown ${Newuser}. -R ${Newkube}
echo export KUBECONFIG=${Newconfig} | sudo tee -a ${Newhome}/.bashrc
```
## <a name="updates"></a>CRITICAL NOTE ON SYSTEM UPDATES

Frequently, versions of Nvidia-driver vs nvidia-container-runtime vs containerd vs etc... may cause the nvidia driver to no longer function with other components. As such, automatic system update has been disabled and **system-wide updates are highly discouraged**. Instead, individual packages should be updated as vulnerabilities are reported. System-wide updates may result in the cluster requiring reprovisioning from scratch.

Again: **system-wide updates are highly discouraged. Instead, individual packages should be updated as vulnerabilities are reported**

### All done!

---

## <a name="license"></a>Billing and Licensing

By default the Edge Setup will be deployed with usage based biling (per minute of the API time).

If you would rather be billed per port please contact us to setup a per port license for you Edge cluster.

All that we need is your account id, the name of the cluster that you would like to apply the license to (see image below), and of course the number of ports you would like to license.

![List of Edge Clusters with names](./Edge-clusters-list.PNG)


Goto: [top of document](#top)
