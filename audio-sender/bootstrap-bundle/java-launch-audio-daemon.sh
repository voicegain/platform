#!/bin/bash

VERSION=1.3.2_beta
DATE=$(date +%F_%H-%M-%S)
GCLOG=gc-audio-daemon.$DATE.log
HEAP=128m
echo "GC log will be written to: $GCLOG"

java -Xlog:gc:$GCLOG -Xms$HEAP -Xmx$HEAP  -XX:MaxGCPauseMillis=5 -jar vg-audio-sender-daemon-$VERSION.jar "$@"
