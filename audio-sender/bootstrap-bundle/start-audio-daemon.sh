#!/bin/bash

# Use this script to start Voicegain Audio Sender Daemon
# once running you can kill it using kill command (the process id is printed after the daemon is started)

echo "Starting Voicegain Audio Daemon"

DATE=$(date +%F_%H-%M-%S)
APPLOG=audio-daemon.$DATE.log

# Source value may have to be modified to match the correct Audio Input Device
SOURCE=5

JSON=audio-daemon-config.json

echo "Starting Daemon in background with log redirected to "+$APPLOG
./java-launch-audio-daemon.sh --json $JSON --source $SOURCE --log info --avc on > $APPLOG &

ps -aef | grep java

echo "Tailing log from: $APPLOG"
tail -100f $APPLOG
