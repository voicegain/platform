#!/bin/bash
echo "Voicegain Audio Daemon: List Audio Devices"
JSON=audio-daemon-config.json
echo "Starting Daemon in background with log redirected to "+$APPLOG
./java-launch-audio-daemon.sh --json $JSON -i --log info --avc on