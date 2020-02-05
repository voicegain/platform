## Steps to get IVR-Proxy sender running on Windows (inside Docker)

1. Log into [Voicegain ACP](portal.voicegain.ai)
2. If you do not have an account, sign up for an account. Select the IVR feature to get access to the IVR tools in the portal. You may also select additional features that you require.
3. Once logged into the portal, select a context in the drop down menu in the header. You may also create a new context.
4. Inside the selected context, select IVR then MRCP proxy in the side menu.
5. Enter the IP address of the machine where the proxy will be installed. 
6. A link to download the IVR proxy bootstrap configuration should appear. Copy the link into a new browser tab and download the configuration file (.tar).
7. Install Docker Desktop on the machine if it is not installed already. Virtualization may need to be enabled on the computer to get Docker running successfully. Visit the [Docker Desktop install page](https://docs.docker.com/docker-for-windows/install/) or use this [direct download link](https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe) to install Docker Desktop.
8. Extract the contents of the IVR proxy file (.tar) into a desired location.
9. Using any command line tool, change directories into the extracted folder.
10. Once in the directory, run the command "docker-compose up".
11. IVR-Proxy sender should now be running on the Windows machine.
