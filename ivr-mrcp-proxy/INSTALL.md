## Steps to get IVR-Proxy sender running on Windows (inside Docker)

1. Log into [Voicegain ACP](https://portal.voicegain.ai)
1. If you do not have an account, [sign up](https://portal.voicegain.ai/signup) for an account. Select the IVR feature to get access to the IVR tools in the portal. You may also select additional features that you require.
1. Once logged into the portal, select a Context in the drop down menu in the header. You may also create a new context.
1. In the side menu, under Settings -> Web ASR -> ASR Recognition Settings choose the Real-Time model that has "ivr" in its name, e.g. "voicegain-rt-ivr-en-us:11"
1. Also in the side menu, go to IVR -> MRCP proxy.
1. Enter the IP address of the machine where the proxy will be installed. 
1. A link to download the IVR proxy bootstrap configuration should appear. Copy the link into a new browser tab and download the configuration file (.tar).
1. Install Docker Desktop on the Windows machine if it is not installed already. On older machines, virtualization may need to be enabled on the computer to get Docker running successfully. Visit the [Docker Desktop install page](https://docs.docker.com/docker-for-windows/install/) or use this [direct download link](https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe) to download Docker Desktop.
1. Extract the contents of the IVR proxy file (.tar) into a desired location.
1. Using Powershell or an equivalent command line shell, change directories into the extracted folder.
1. Once in the directory, run the command "docker-compose up".
1. IVR-Proxy sender should now be running.
1. To stop it use Ctrl+C and then type "docker-compose down".
