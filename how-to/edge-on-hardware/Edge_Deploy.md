# <a id="top"></a>Deploy Voicegain On-Edge
Step by step guide how to deploy Voicegain Speech-to-Text Platform on your own Hardware or a VM.

NOTE 1: this guide was originally written for a bare hardware deployment. However, it can also be used for a deployment on a VM (e.g. provided by VMware). Some of the instructions are then irrelevant , e.g., Step 1.

NOTE 2: We also now support an install on a machine or a VM that has no GPU (thus CPU-only).

----
Under the hood:
This guide will have you do the following:
* Configure your server BIOS
* Install Ubuntu **LTS 20.04 Desktop** with custom Partitioning onto a server with NVIDIA CUDA Capable GPUs
  * If the machine or the VM has no GPU, you can alternatively use Ubuntu **LTS 20.04 Server**
  * NOTE: We have tested our install with Ubuntu 22.04 LTS and found that it does not run stable (there are frequent service restarts due to failed liveness probe even in presence on no load). So please **do not use Ubuntu 22.04**. We will continue troubleshooting Ubuntu 22.04 and will note here when it is safe to use.
* Provision your server using the Voicegain EZ Init script.
* Deploy the Voicegain Application to your environment. 

TODO: Manual provisioning requirements and steps to upload your preexisting kubeconfig file to the Voicegain Portal

## <a id="toc"></a>Table of Contents
- [Before you Start](#before)
- [Step 1: Configure your server BIOS](#step1)
- [Step 2: Boot to Installation Media](#step2)
- [Step 3: Configure Network](#step3)
- [Step 4: Configure Installation](#step4)
- [Step 5: Manually Create Partitions](#step5)
- [Step 6: Finalize Provisioning](#step6)
- [Step 7: Create Cluster on VoiceGain](#step7)
- [Step 8: Run EZInit Script](#step8)
- [Step 9: Reboot](#step9)
- [Step 10: Ensure Cluster is functional](#step10)
- [Step 11: Deploy Voicegain Application](#step11)
- [Step 12: Reboots, Notes and Caveats](#step12)
- [CRITICAL NOTE ON SYSTEM UPDATES](#updates)
- [Billing and Licensing](#license)

## <a name="before"></a>Before you Start 
In order to deploy Voicegain on Edge your account needs to have the Edge feature enabled - otherwise you will not see the relevant pages in the [Voicegain Web Console](https://www.voicegain.ai). Please contact support@voicegain.ai to have that enabled.

When you contact us we will ask you to describe your intended usage (e.g. offline transcription or MRCP ASR) so that we can enable an appropriate Edge configuration for your use case. If you are only exploring we can enable several generic configurations to allow you to test a variety of uses. For production use we will prepare a custom configuration that makes the best use of resources on your server(s). We will also configure port based licensing if desired (default is usage-based billing). 

## <a name="step1"></a>Step 1: Configure your Server BIOS 

*Step 1 is relevant only for a bare hardware deployment (not a VM).*

Boot your server and enter BIOS Configuration Menu: [Common Manufacturer BIOS Keys](https://www.tomshardware.com/reviews/bios-keys-to-access-your-firmware,5732.html#:~:text=BIOS%20Keys%20by%20Manufacturer%201%20ASRock%3A%20F2%20or,Lenovo%20%28ThinkPads%29%3A%20Enter%20then%20F1.%20More%20items...%20)

### UEFI settings
You will want to find the Boot Settings section of your BIOS and select UEFI rather than BIOS/Legacy.

Example of DELL UEFI Mode Selection:
![UEFI Mode Selection](./UEFI.png)

### 4G decoding
Most of modern (say made after 2015) motherboards have option “Above 4G decoding” in bios (or something similarly named), and it should be enabled for Nvidia data-center GPUs. It’s generally not enabled by default except for very recent servers, so it is necessary to verify that setting and enable it if needed. It could be difficult to find, it’s usually buried in the advanced PCI settings.

If not enabled the card will not be detected by Nvidia driver and you may see errors in the dmesg log

## <a name="step2"></a>Step 2: Boot to Installation Media

*Step 2 may have to be done differently if installing on a VM - the instructions below focus on bare hardware.*

If you have not already; you can download the Ubuntu 20 LTS Desktop Image [here](https://ubuntu.com/download/desktop). (If machine or VM has no GPU then you can alternatively use Ubuntu Server.)

You can burn the installation image on to DVD, however, we recommend creating a Bootable USB drive as it is faster and becoming the new standard.

Steps to creating a bootable Ubuntu USB Drive based on your current OS:

[Ubuntu](https://ubuntu.com/tutorials/create-a-usb-stick-on-ubuntu)

[Windows](https://ubuntu.com/tutorials/create-a-usb-stick-on-windows)

[MacOS](https://ubuntu.com/tutorials/create-a-usb-stick-on-macos)


[Generic Overall Guide](https://linuxhint.com/create_bootable_linux_usb_flash_drive/)

Insert the USB drive and ensure that your system will either prioritize USB Drive in the boot order, or otherwise, manually enter the UEFI One Time Boot Menu and boot from the USB Drive. 

When the Live Ubuntu system has booted select "Try Ubuntu" (NOT "Install Ubuntu")

## <a name="step3"></a>Step 3: Configure Network

The reason for choosing to "Try Ubuntu" is that you can manually configure your network settings before Installing. This saves a lot of time and heartbreak. 

Selecting the network icon in the top right you can then choose to edit the wired settings, click the gear icon and select the IPV4 tab and provide the static IP address of your new server and relevant network information.

![Wired Settings](./Edge-network1.png)
![IPv4 Settings](./Edge-network2.png)

Now you can toggle the Wired Network off and then back on for the new settings to take effect. 

Next, DoubleClick the "Install Ubuntu 20.xx.x LTS" icon on the desktop. 

## <a name="step4"></a>Step 4: Configure Installation

Choose your language/keyboard etc...

On the "Updates and Other Software" screen, select "Minimal Installation" and "Download updates while installing Ubuntu" and ensure that all other boxes are NOT checked (Third Party software). See Below:

![Install Settings](./4-1.png)

Then proceed with [Step 5](#step5)

## <a name="step5"></a>Step 5: Manually Create Partitions

In short, the spirit behind the partitions are as such: 
- EFI partition: Required 
- No Swap: Kubernetes requires swap to be off so no need to waste disk space here.
- Partition for NFS-Server: dynamically provisioned storage consumed by the k8s cluster.
 
Kubernetes doesn't support Swap, and the Storage should not impact the host system if it's ever filled. Detailed walk-through follows:

### Installation Type:
* On the "Installation Type" screen: Choose "Something else" and then "Continue"

![Something Else](./5-1.png)

### Partition Layout: 

* **NOTE:** *If this disk has previous partitions you will want to select the drive itself (usually /dev/sda) and then select "New Partition Table..." this WILL destroy all data previously on the disk.*

#### Allotment:

**Recommendation:** *We recommend using at least 250 GB for the / (root) partition and 750 GB (at least) for the storage partition `/nfs`. In the below example we are using a single 1TB Drive*

* **For Each Partition we create do the following:** Click on "**free space**" which should be the entire disk, and click on the "**+**" below to create your new partitions. 
The partitions will use the ext4 filesystem, and default settings such as "Primary" and their Location.

* Create a 535 MB Partition on your boot drive and chose "EFI System Partition" from the "Use as:" dropdown box.
![EFI System Partition](./5-2.png)

* Create a partition of 250,000MB keep the default radio button options and choose `/` (root) as the *Mount point*.

![Root Partition](./5-3.png)

* For the remaining ~750GB (or however much you have left over), create a new partition and manually type the *Mount point* as: `/nfs`  
**NOTE:** *Obviously this could also be done with multiple drives. Dedicating a device to `/` and another solely to `/nfs`. Another option would be to combine multiple partitions/disks into a single LVM for `/nfs`*

![NFS Partition](./5-4.png)

* **NOTE:** If this disk has previous partitions as discussed above be certain that the check boxes to *"format"* the partitions is checked for `/` and `nfs`.

![Ready to Install](./5-5.png)

Click **Install Now** -> Continue -> Continue and finish the remainder of the install (create user and password. Assign hostname, etc...). Choose to require password to log in, and restart the system when prompted (remove installation media or otherwise ensure that the boot drive is higher in the boot order).

**A NOTE ABOUT USERS:**

During the EZInit Script process a system user named `voicegain` will be created (if one does not already exist). The `voicegain` user will be used for interacting with and running the voicegain application. If this is going to be a single user system (you do not need multple user logins) then you can (if you wish) create the `voicegain` user yourself during the Ubuntu installation process. If this system will be accessed by multple people you may wish to simply create the first admin account during the Ubuntu installation and allow the EZInit script to generate the `voicegain` user. 

## <a name="step6"></a>Step 6: Finalize Provisioning

Your first boot into Ubuntu will prompt you to set up some features: Connecting online accounts, Livepatch and Help Ubuntu. Skip these steps or approve the default choices. (Naturally, you can choose to not send any data to Canonical)

You will likely also be prompted by the "Software Updater" to, well, update. Close out of this **without** updating. The packages will be updated during the cluster provisioning phase via our EZInitScript.

***OPTIONAL:*** At this time you may wish to install SSH server and complete the process over an SSH session. To do so open a terminal (either by right-clicking on the desktop and choosing to "Open in terminal" or you can search for Terminal from the Activites menu in the top left corner.

In the terminal execute: `sudo apt install openssh-server -y`

## <a name="step7"></a>Step 7: Create Cluster on VoiceGain
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

* **NOTE 1:** If you are installing on a machine or VM **without GPU** you need to append the following option to the EZInit Script  `-g false` or `--gpu false` ; otherwise the EZInit script will attempt to install Nvidia Cuda drivers and will fail.

* **NOTE 2:** Ubuntu 20 handles sudo commands differently than other distros and previous versions. It is **required** to run sudo while preserving the home directory:
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

NOTE: In principle this step is not needed if the machine or VM has no GPU. But it will not hurt to reboot either.

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
