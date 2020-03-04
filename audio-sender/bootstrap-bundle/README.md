## Steps to get Audio Sender Daemon running ##
Version 1.3.3_beta (dev)

### Install ###

Run 

 chmod u+x audio-daemon-setup.sh

to make the setup script executable, then run the script:

 ./audio-daemon-setup.sh


If the script reports no Java 9 present then please install it using e.g. these commands (Ubuntu)

sudo apt-get update
sudo apt-get install -y galternatives openjdk-9-jre

Verify install running:

java -version

Once correct java is installed, rerun ./audio-daemon-setup.sh 

### Check install ###

### Check/ Modify the configuration ###

It will be in the json file. 

You may have to change the SOURCE parameter in start-audio-daemon.sh

### Run Audio Daemon ###

./start-audio-daemon.sh

