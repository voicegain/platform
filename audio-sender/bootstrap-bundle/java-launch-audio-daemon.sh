#!/bin/bash

# helper script to run the vg-audio-sender-daemon jar file

VERSION=1.30.1
DATE=$(date +%F_%H-%M-%S)
GCLOG=gc-audio-daemon.$DATE.log
HEAP=128m
echo "GC log will be written to: $GCLOG"

java -Xlog:gc:$GCLOG -Xms$HEAP -Xmx$HEAP -XX:+UseG1GC -XX:MaxGCPauseMillis=5 -jar vg-audio-sender-daemon-$VERSION.jar "$@"
