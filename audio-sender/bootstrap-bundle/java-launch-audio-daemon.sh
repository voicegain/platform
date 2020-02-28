#!/bin/bash

VERSION=1.3.2_beta
DATE=$(date +%F_%H-%M-%S)
GCLOG=gc-audio-daemon.$DATE.log
HEAP=128m
echo "GC log will be written to: $GCLOG"

java -Xloggc:$GCLOG -XX:NewRatio=2 -XX:ParallelGCThreads=4 -XX:+UseConcMarkSweepGC -XX:+UseParNewGC -XX:SurvivorRatio=8 -XX:TargetSurvivorRatio=90 -XX:MaxTenuringThreshold=15 -XX:+PrintGCDetails -XX:+PrintGCTimeStamps -XX:+PrintGCApplicationStoppedTime -Xms$HEAP -Xmx$HEAP -jar vg-audio-sender-daemon-$VERSION "$@"
