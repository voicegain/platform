# <a id="top"></a>Deploy Voicegain On-Edge
Step by step guide how to deploy Voicegain Speech-to-Text Platform on your own Hardware or a VM.

NOTE 1: this guide was originally written for a bare hardware deployment. However, it can also be used for a deployment on a VM (e.g. provided by VMware). Some of the instructions are then irrelevant , e.g., Step 1.

NOTE 2: We also now support an install on a machine or a VM that has no GPU (thus CPU-only).

----
Under the hood:
This guide will have you do the following:
* Configure your server BIOS
* Install Ubuntu **Server 24.04 LTS** with custom Partitioning onto a server with NVIDIA CUDA Capable GPUs (support for non-GPU/CPU-Only also available. See [Step 8](#step8) for --gpu flag)
* Provision your server using the Voicegain EZ Init script.
* Deploy the Voicegain Application to your environment. 

TODO: Manual provisioning requirements and steps to upload your preexisting kubeconfig file to the Voicegain Portal

## <a id="toc"></a>Table of Contents
- [Before you Start](#before)
- [Step 1: Configure your server BIOS](#step1)
- [Step 2: Boot to Installation Media](#step2)
- [Step 3: Configure Installation](#step4)
- [Step 4: Configure Network](#step3)
- [Step 5: Manually Create Partitions](#step5)
- [Step 6: Finalize Configuration and Provisioning](#step6)
- [Step 7: Create Cluster on VoiceGain](#step7)
- [Step 8: Run EZInit Script](#step8)
- [Flags and Arguments](#flags)
- [Step 9: Reboot](#step9)
- [Step 10: Ensure Cluster is functional](#step10)
- [Step 11: Deploy Voicegain Application](#step11)
- [Step 12: Reboots, Notes and Caveats](#step12)
- [CRITICAL NOTE ON SYSTEM UPDATES](#updates)

## <a name="before"></a>Before you Start 
In order to deploy Voicegain on Edge your account needs to have the Edge feature enabled - otherwise you will not see the relevant pages in the [Voicegain Web Console](https://www.voicegain.ai). Please contact support@voicegain.ai to have that enabled.

When you contact us we will ask you to describe your intended usage (e.g. offline transcription or MRCP ASR) so that we can enable an appropriate Edge configuration for your use case. If you are only exploring we can enable several generic configurations to allow you to test a variety of uses. For production use we will prepare a custom configuration that makes the best use of resources on your server(s). We will also configure port based licensing if desired (default is usage-based billing). 

Ensure that this node will have access to an NTP Clock endpoint. By default, this requires port 123 UDP. Ubuntu will use systemd-timesyncd connected to ntp.ubuntu.com. If you will be using your own NTP server update your configuration accordingly.

## <a name="step1"></a>Step 1: Configure your Server BIOS 

*Step 1 is relevant only for a bare hardware deployment (not a VM). Proceed to [Step 2](#step2) if manually installing on VM. If the VM was autoprovisioned with Ubuntu Server 24.04 proceed to [Step 5](#step5) to ensure storage partitions are configured correctly.*

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

If you have not already; you can download the Ubuntu 24.04 LTS Server Image [here](https://releases.ubuntu.com/24.04.2/ubuntu-24.04.2-live-server-amd64.iso).

You can burn the installation image on to DVD, however, we recommend creating a Bootable USB drive as it is faster and becoming the new standard.

Steps to creating a bootable Ubuntu USB Drive based on your current OS:

[Ubuntu](https://ubuntu.com/tutorials/create-a-usb-stick-on-ubuntu)

[Windows](https://ubuntu.com/tutorials/create-a-usb-stick-on-windows)

[MacOS](https://ubuntu.com/tutorials/create-a-usb-stick-on-macos)


[Generic Overall Guide](https://linuxhint.com/create_bootable_linux_usb_flash_drive/)

Insert the USB drive and ensure that your system will either prioritize USB Drive in the boot order, or otherwise, manually enter the UEFI One Time Boot Menu and boot from the USB Drive. 


 

## <a name="step3"></a>Step 3: Configure Installation

Choose your language/keyboard etc...

On the "Choose type of install" screen, select "Ubuntu Server" and and leave other options unchecked. See Below:

![Install Settings](https://github.com/user-attachments/assets/bc1b9695-35f8-473a-938a-5c6ee9671c07)

### Networking ###
This guide assumes you will be statically assigning a dedicated IP address to your K8s node. 

Determine Network Interface if you do not already know it by the interface that doesn't have a "not connected" note, and highlight it, press enter and select "Edit IPv4"
![Network Interfaces](https://github.com/user-attachments/assets/0d5f2b18-1219-4156-9081-c88524315064)


Then define the IPv4 configuration as it pertains to your network:
![IPv4 Settings](https://github.com/voicegain/platform/assets/14049448/6d66bb1d-a200-425e-be44-5b6f5b16f49d)

After selecting next, if you require use of an HTTP Proxy you can configure it here.

This guide was written with the Installer Version 24.04.2. You may be prompted to update the installer to a new version. Ideally this should pose any issues, however, it is not unheard of for an installer update to break some unforeseen functionality. You may choose to update the isntaller, but if you encounter an issue you may consider installing without updating the installer.
![Installer Selection](https://github.com/user-attachments/assets/09670b73-8410-46de-a722-35031f8dd6d0)



## <a name="step5"></a>Step 5: Manually Create Partitions

In short, the spirit behind the partitions are as such: 
- EFI partition: Required 
- **No Swap**: Kubernetes requires swap to be off so no need to waste disk space here.
- Partition for **NFS**: dynamically provisioned persistent storage consumed by the k8s cluster.
- Partition for **/var/lib**: The majority of runtime data is stored in /var/lib/containerd and /var/lib/kubelet so /var/lib/ is partitioned separately to avoid filling the / (root) filesystem and rendering the system system inaccessible. 
- Partition for **/var/log**: prevent overactive logs from filling root filesystem and rendering the system inaccessible. 
 
Kubernetes requires Swap to be disabled. The NFS persistent volumes, k8s runtime, and log storage should not impact the host system if they're ever filled. Detailed walk-through follows:

### Guided storage configuration:
* On the "Guided storage configuration" screen: Choose "Custom storage layout" and then "Done"
![Server-Guided-Storage](https://github.com/user-attachments/assets/618ec654-7555-4652-ae61-43c198617954)


### Recommended Partitioning for Ubuntu Installation:

For disk sizes of **1TB, 2TB, and 4TB**, the following partitioning scheme is recommended:

| Mount Point   | 1TB  | 2TB  | 4TB  |
|--------------|------|------|------|
| `/boot/efi`  | 1.05G | 1.05G | 1.05G |
| `/`          | 64G  | 96G  | 128G  |
| `/var/lib`   | 256G  | 384G  | 512G  |
| `/var/log`   | 48G   | 64G   | 96G  |
| `/nfs`       | Remainder | Remainder | Remainder |

- `/boot/efi` is always **1.05GB**.
- The **root (`/`)** partition size increases as disk capacity grows.
- `/var/lib` is partitioned to avoid k8s runtime from filling the **root (`/`)**
- `/var/log` is allocated for logging purposes.
- `/nfs` uses the remaining space.

#### Partitioning: 
* **NOTE:** *If this disk has previous partitions you will want to select the drive itself (show by UUID and size) and then select "Reformat" this WILL destroy all data previously on the disk. If this disk had an existing LVM volume group you will need to delete the LVM Volume Group before you can "Reformat"*

- **/boot/efi** : Hightlight the intended disk and select "Use as boot device"
![Use As Boot Device](https://github.com/user-attachments/assets/7ee93016-9b05-4b73-be97-2681bed8fe37)

* **For Each Subsequent Partition we create; do the following:** scroll down and highlight "**free space**" which should be the entire disk, hit enter and select "Add GPT Partition". Enter the size and mount point using the table above as a guide.

- **root (`/`)** : Add GPT Partition, Populate Size according to table above. Leave it as ext4 format and the Mount point should be  '/' a.k.a. the root partition. Create.
![root partition](https://github.com/user-attachments/assets/ce6538c0-5513-4dd2-a38f-6a41fd1622e2)

- **/var/lib** : Add GPT Partition, Populate Size according to table above. Leave it as ext4 format and select Mount as "/var/lib". Create.
 ![var-lib](https://github.com/user-attachments/assets/34a103e4-41ed-4336-b921-4dae976e4318)

- **/var/log** : Add GPT Partition, Populate Size according to table above. Leave it as ext4 format and select Mount as "Other" and enter `var/log` (the / will already be prepended so it should read as `/var/log`). Create.
![var-log](https://github.com/user-attachments/assets/916fca17-7f20-43dd-9d46-ebac8faa65aa)

- **/nfs** : Add GPT Partition, Leave size empty to utilize the remaining disk space. Leave it as ext4 format and select Mount as "Other and enter `nfs` (as the / is already prepended). Create.
 ![nfs](https://github.com/user-attachments/assets/67ae468c-5c67-46b1-8225-e0339fe17158)

**NOTE:** *Indeed, this could also be done with multiple drives. Dedicating a device to `/` and another solely to `/nfs`. Another option would be to combine multiple partitions/disks into a single LVM for `/nfs`*

![Filesystem Summary](https://github.com/user-attachments/assets/3c563985-e448-45a9-9b8e-4e4592a43acd)

 **Continue** -> (If disk was previously formated you will need to confirm the destructive action) -> Profile Configuration 

## <a name="step6"></a>Step 6: Finalize Configuration and Provisioning
**A NOTE ABOUT USERS:**

During the EZInit Script process a system user named `voicegain` will be created (if one does not already exist). The `voicegain` user will be used for interacting with and running the voicegain application. If this is going to be a single user system (you do not need multple user logins) then you can (if you wish) create the `voicegain` user yourself during the Ubuntu installation process. If this system will be accessed by multple people you may wish to simply create the first admin account during the Ubuntu installation and allow the EZInit script to automatically generate the `voicegain` user. 

![User Creation](https://github.com/voicegain/platform/assets/14049448/6b994fe6-ae4a-4a48-8264-05cbd889cf96)
Click Continue.

** Upgrade to Ubuntu Pro **: If you are subscribed to Ubuntu Pro you may enable it in this step. Continue.

** SSH configuration **: On this page you can choose to install OpenSSH server, which in most cases is ideal, unless you will have direct access to the system as needed. Depending on your existing conditions and requirements you can choose the default of Allowing password authentication over SSH, or you can Import an SSH Key if your environment requires it. Click Done. 

* **IMPORTANT: Featured Server Snaps** Do not install anything from the "Freatured server snaps" page. Snap uses different versios of software with custom configuration locations and this will break the intended functionality of our cluster.

* Click DONE to begin the Installation

* Reboot and remove the installation media. 
 
***OPTIONAL:*** If you did not choose to install OpenSSH Server during the provisioning phase, time you may wish to install it now and complete the process over an SSH session. 

In the terminal execute: `sudo apt install openssh-server -y`

This will automatically start the server and update the local firewall to permit SSH connections over port 22.

## <a name="step7"></a>Step 7: Create Cluster on VoiceGain
> **System Provisioning Considerations:** As we are now using Ubuntu Server; there is not a Desktop Environment by default. As such, we will be using SSH so we can copy and paste into our terminal. For the sake of simplicity; the guide is assuming that you are on a Desktop with a browser and SSH access to the Edge Cluster. 

1. On your desktop system; go to: https://console.voicegain.ai
2. If you do not have a developer account, you would need to sign up first. Detailed instructions are provided [here](https://www.voicegain.ai/post/how-to-signup-for-a-developer-account-and-start-using-voicegain-voice-ai).
3. Log in to the console and go to the "[Edge Deployment](https://console.voicegain.ai/specific/edge-deployments)" view. Click "**+ ADD**" and name your Cluster and choose **EZ Setup**.

![Add new Edge Deployment](https://github.com/user-attachments/assets/7895a046-c1b5-49f6-99a3-ca514e57bfa1)

4. Find your newly created cluster in the Edge Deployment list and Load it by clicking the button to the right of the entry (left of the Delete/Trash button) 
![Load Cluster](https://github.com/user-attachments/assets/107c82ca-3bf1-4129-a607-acc6e53d69e4)




5. Define the Connection parameters relevant to your circumstance. Ideally your Edge Deployment will be in your DMZ or "Edge" and, as such, is reachable from the internet. If so, choose the top radio button: "Reachable from internet" and provide the IP Address or Fully Qualified Domain Name as well as the K8S API port (by default this is 6443). Alternatively, if you do not have a DMZ or the ability to add a pinhole in your firewall; you should choose: "Set up control tunnel". Then Click "**Apply**" and "**> Next**"
> **What is the control tunnel?:** In order to connect to systems behind a strict Firewall your Edge system will leverage autossh to establish an SSH tunnel with our network over the HTTPS (port 443) protocol. This is a non interactive shell session that solely creates a reverse port forward so that we can reach your Kubernetes API from within our network.
![Connection Parameters](https://github.com/user-attachments/assets/2b94a6bb-7893-4001-821f-7eac52389ab2)

6. Click "**Generate**" and then "**Copy**". You now have the Command script in your clipboard. 
![Generate Command Script](https://github.com/user-attachments/assets/64b772ed-9856-47ca-92c6-3edcb5c300af)


## <a name="step8"></a>Step 8: Run EZInit Script

The EZInitCommand provided above should look something like: 

``` wget --content-disposition --backups=3 https://api.voicegain.ai/v1/cluster/singleUse/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxxx/initScript/EZInitScript && sudo --preserve-env=HOME bash voicegain-init.sh ```

> **What is `--preserve-env=HOME`?** As of Ubuntu 20; Ubuntu handles `sudo` commands differently than other distros and previous versions. It is **required** to run sudo while preserving the home directory in order for the install to pertain to the correct user.

<a name="flags"></a>  
## FLAGS and ARGUMENTS
* **GPU Operator Mode (`--gpu|-g`):** Controls how GPU support is configured. Use -g false (or --gpu false) to install Nvidia drivers directly on the host. Default (true) uses the GPU-Operator to manage driver deployment.
* **CPU Only (No GPU) (`--cpu|-c`):** Use this flag for CPU-only installations. Disables all GPU-related installations (both host drivers and GPU-Operator). Cannot be used with `--gpu`.
* **Multi-node (`--multi|-m`) [DEPRECATED]:** By default the EZInit script assumes a single node cluster is being deployed. In order to receive follow-up instructions and commands for multi-node clusters provide the -m or --multi flag [DEPRECATED]
* **Custom NFS (`--server|-s` and `--nfsdir|-d`):** By default the local server 127.0.0.1 and the /nfs directory are set for dynamic storage provisioning. If you have another NFS server within your network you can provide the IP via the -s 8.8.8.8 or --server 8.8.4.4 arguments. If you have a different local partition you wish to serve from you can provide the -d /mystorage or --nfsdir /storage arguments. (replacing 8.8.8.8, 8.8.4.4, /mystroage, and /storage with your destinations)
* **Legacy Mode (`--legacy|-l`):** Enables compatibility mode for older systems and Kubernetes versions
* **Existing Cluster (`--exists|-x`):** Allows management of pre-existing clusters, including reset options
* **Verbose Mode (`--verbose|-v`):** Enables detailed output during installation and configuration
* **Help (`--help|-h`):** Displays usage information and available options

Paste the copied EZInit Command into a terminal/ssh session on the Edge System, **Defaults are generally correct unless instucted otherwise by your Voicegain Contact.** and hit enter and provide your password for sudo when prompted. 



![EZInitScript](./8-1.png)

The script will check to see if the `voicegain` user exists and create it if not. If the script is not being ran by the `voicegain` user it will ask you to proceed with the following steps:

```
sudo su -
su voicegain
vginstall
```

**INFO:** if the EZInit script is used to create the `voicegain` user, it will be created as a system user with passwordless sudo and no password. **This user cannot log into the system directly or remotely**. The script will then be copied to the system user directory `/opt/voicegain/bin/` and aliased as `vginstall`

## <a name="step9"></a>Step 9: Reboot
 
### The details: 
#### Why Reboot?
In principle this step is not needed if the default GPU-Operator is installed or if the machine or VM has no GPU. If the Voicegain Installer was executed with the --gpu=false flag, it will have installed NVIDIA drivers to the host. Requireing a reboot in order to load the required kernel modules. In any event; it will not hurt to reboot.

#### Single-Node Cluster
If this is a single node cluster, press any key when prompted to reboot. Congrats! Your cluster is configured!

#### Multi-Node Cluster
IF you are setting up a multi-node cluster (via the --multi flag) **DO NOT YET REBOOT...**

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

![Deploy1](https://github.com/user-attachments/assets/85400741-c2d9-4033-b2f0-2fdc762a26ec)
![Deploy2](./11-1-2.png)
![Deploy3](https://github.com/user-attachments/assets/4ef78b38-843a-4096-94ce-bf137a9a799e)

- Monitor the progress on the terminal session we created in step 10.
- Check the status on the Console to see when the deployment is finished, then you can click the link to open your local portal.

![Portal](./11-2.png)
- Choose "Login" and use your Voicegain credentials

![Login](https://github.com/user-attachments/assets/ad94e8a8-1717-4989-9710-7239066e9f9f)


- Now you can test your new deployment. 
  - On the home page click on the "Run test" button on the Function Tests card.
    ![Run test](https://github.com/user-attachments/assets/cf8a6ba9-dc57-4498-b220-7c659f6a55e8)


  - If you chose an off-line acoustic model you can also test by uploading a file for transcription.

![Transcribe](https://github.com/user-attachments/assets/7298ea6c-4bce-489c-ad2c-37804c8a70e5)


## <a name="step12"></a>Step 12: Reboots, Notes and Caveats

NTP: **Ensure that this node will have access to an NTP Clock endpoint. By default, this requires port 123 UDP. Ubuntu will use systemd-timesyncd connected to ntp.ubuntu.com. If you will be using your own NTP server update your configuration accordingly.** Timeskew can cause many seemingly unrelated issues. 

First Reboot: The EZInit script has enabled all required services for the cluster to start automatically upon reboot. After rebooting the system you may need to wait up to 10 minutes for all of the individual components to start and settle. 

voicegain user: The cluster configuration is ran as the non-root user who ran the EZInit script. If you require other users on the system to have access to the kubectl command line tool you will want to copy the kubernetes configuration file to their home directory. 

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

Goto: [top of document](#top)
