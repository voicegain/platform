#!/bin/bash

# script to list available audio devices

echo "Voicegain Audio Daemon: List Audio Devices"
JSON=audio-daemon-config.json
echo "Starting Daemon with -i option"
./java-launch-audio-daemon.sh --json $JSON -i --log info --avc on
