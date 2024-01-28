# Steps to get Audio Sender Daemon running (Linux version)#
Version 1.7.0 

## Install ##

Run 

`chmod u+x audio-daemon-setup.sh`

to make the setup script executable, then run the script:

`./audio-daemon-setup.sh`

If the script reports no **wget** present then please install it.
Here are example commands for installing wget on Ubuntu or Debian:

```
sudo apt-get update
sudo apt-get install -y wget
```

### Java install if necessary ###

If the script reports no Java 9 present then please install Java 11 if avaiable or Java 9, if 11 is not available for your Linux version.

Here are example install commands for Ubuntu or Debian:

```
sudo apt-get update
sudo apt-get install -y galternatives openjdk-11-jre
```
or
```
sudo apt-get update
sudo apt-get install -y galternatives openjdk-9-jre
```

Verify Java install running:

`java -version`

Once correct java is installed, rerun `./audio-daemon-setup.sh` 


## Check Audio Devices ##

Run this command to list the audio devices:

`./list-audio-devices.sh`

Pick the number next to the correct input device and change the `SOURCE` parameter in `start-audio-daemon.sh` to that value.


## Check/Modify the configuration ##

Configuration is in the json file. 

Normally no changes are needed, but the configuration can always be modified for specific use case.


## Launch Audio Daemon ##

`./start-audio-daemon.sh`

