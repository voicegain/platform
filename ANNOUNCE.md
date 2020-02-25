## February 15, 2020
* Minor release 1.3.1_beta is scheduled for 2/25/2020 between 6pm and 9pm CST.
  * Release notes are available [here](https://raw.githubusercontent.com/voicegain/platform/master/RELEASE.md)
  * This release fixes the two Known Issues listed below.

## February 8, 2020
* Known issues
  * (issue #283) SSO to Grafana analytics dashboard does not work 
  * (issue #284) Downloadable IVR-Proxy docker-compose has issues under load (multiple sessions) with UDP traffic crossing in and out of Docker Container. This causes silence packets inserted into MRCP audio stream within the jitter buffer. It also causes packet loss for outbound audio traffic to Voicegain cloud.</br>
  The IVR-Proxy works fine for single session, so that functionality can still be tested. 

## February 5, 2020
* Minor release 1.3.0_beta is scheduled for 2/5/2020 between 6pm and 9pm CST.
  * Release notes are available [here](https://raw.githubusercontent.com/voicegain/platform/master/RELEASE.md)

## January 13, 2020
* Release 1.2.2_beta scheduled for 4:50pm GMT has been completed. It fixes:
    - bug #181: Websockets control page not visible
    - bug #185: Unable to generate JWT from Portal



