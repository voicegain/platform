# Setup and Configure Linphone to make call to SIP URI
Linphone is a popular open-source VoIP (Voice over IP) software that allows users to make voice and video calls using the SIP (Session Initiation Protocol). Here's a detailed guide on how to make a call to a SIP URI without registration using the Linphone desktop application:

### Prerequisites

1. **Linphone Installation:**
   - Ensure you have Linphone installed on your desktop. You can download it from the [official Linphone website](https://www.linphone.org/technical-corner/linphone/downloads).

### Steps to Make a Call to a SIP URI Without Registration

1. **Open Linphone:**
   - Launch the Linphone application on your desktop.

2. **Access the Settings:**
   - Go to the `Preferences` or `Settings` menu. This can typically be found in the `Linphone` menu on macOS or under the `Tools` menu on Windows/Linux.

3. **Configure SIP Account:**
   - Since you want to make calls without registration, you don’t need to configure a SIP account for registration. However, you should ensure that Linphone can make outbound SIP calls.
   - If prompted to add an account, you can skip this step.

4. **Disable Registration:**
   - Navigate to the `SIP Accounts` section.
   - If there’s an existing account, select it and ensure the option for “Register on startup” or “Enable registration” is disabled. This prevents Linphone from attempting to register with a SIP server.

5. **Check Network Settings:**
   - Ensure that your network settings allow SIP traffic. Sometimes firewalls or network configurations can block SIP traffic.

6. **Initiate a Call to a SIP URI:**
   - In the main Linphone window, locate the `Address` or `Call` field.
   - Enter the SIP URI of the contact you want to call. The format should be `sip:username@domain`.
     - For example, `df3d29f1-856d-470d-887d-445f01541dcb@fs1lab.ascalon.ai;transport=tcp`.
   - Click the `Call` button (usually represented by a green phone icon).

7. **Monitor the Call Status:**
   - Linphone will attempt to initiate the call to the SIP URI without registering to a SIP server.
   - You will see the call status in the main window. If the SIP URI is correct and the contact is reachable, the call should go through.

8. **End the Call:**
   - Once the conversation is over, you can end the call by clicking the red phone icon.

### Additional Tips

- **SIP Proxy:**
  - If the SIP URI requires a specific SIP proxy to be used, you can configure this in the `Network` settings of Linphone. Go to `Preferences` > `Network` and set the `Outbound proxy`.

- **Debugging:**
  - If the call doesn’t go through, check the logs for any error messages. Linphone logs can be accessed through the `Help` or `Tools` menu under `Log Output` or `Debug`.

- **Firewall and NAT:**
  - Ensure that your firewall or NAT (Network Address Translation) settings are properly configured to allow SIP traffic. Ports 5060 (UDP/TCP) and 5061 (TLS) are commonly used for SIP.

- **Audio and Video Settings:**
  - Make sure your audio and video devices are correctly configured in Linphone. Go to `Preferences` > `Audio` and `Video` to select the correct input/output devices.

By following these steps, you should be able to make calls to a SIP URI using Linphone without needing to register with a SIP server. This is useful for direct SIP calls where the calling and receiving parties have publicly reachable SIP URIs.

Once the dialplan is ready, you need to develop an application that listens for incoming HTTP requests and passes back the WebSocket URL to FreeSWITCH for live streaming. You can use the provided sample web service application vg_asr_service.py.

