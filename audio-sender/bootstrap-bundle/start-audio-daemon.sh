#!/bin/bash
echo "Starting Voicegain Audio Daemon"

DATE=$(date +%F_%H-%M-%S)
APPLOG=audio-daemon.$DATE.log
SOURCE=2
JSON=audio-daemon-config.json

echo "Starting Daemon in background with log redirected to "+$APPLOG
./java-launch-audio-daemon.sh --json $JSON --source $SOURCE --log info --avc on > $APPLOG &

ps -aef | grep java

echo "Tailing log from: $APPLOG"
tail -100f $APPLOG
