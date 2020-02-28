#!/bin/bash
CODE_NAME=ascalon
DEPLOYMENT=dev
VG_VER=1.3.2_beta
echo "Setup for Voicegain Audio Sender Daemon ver. $VG_VER"

echo "Checking java version"

if type -p java; then
    echo "Found java executable in PATH"
    _java=java
elif [[ -n "$JAVA_HOME" ]] && [[ -x "$JAVA_HOME/bin/java" ]];  then
    echo "Found java executable in JAVA_HOME"
    _java="$JAVA_HOME/bin/java"
else
    echo "No Java. Please install Java 9"
    exit
fi

if [[ "$_java" ]]; then
    version=$("$_java" -version 2>&1 | awk -F '"' '/version/ {print $2}')
    version1=$(echo "$version" | awk -F. '{printf("%03d%03d",$1,$2);}')
    echo "Installed Java version $version ($version1)"
    if [ $version1 -ge 001009 ]; then
        echo "OK - Java version is 1.9 or higher"
    else         
        echo "Java version is lower than 1.9 - Please install Java 9"
        exit
    fi
fi

echo "Downloading Voicegain Audio Sender Daemon"
wget -N --backups=0 wget https://f002.backblazeb2.com/file/$CODE_NAME-cdn/vg-audio-sender-daemon-$VG_VER.jar
echo "Downloading java launch script"
wget -N --backups=0 https://raw.githubusercontent.com/voicegain/platform/$DEPLOYMENT/audio-sender/bootstrap-bundle/java-launch-audio-daemon.sh
chmod u+x java-launch-audio-daemon.sh
echo "Downloading daemon start script"
wget -N --backups=0 https://raw.githubusercontent.com/voicegain/platform/$DEPLOYMENT/audio-sender/bootstrap-bundle/start-audio-daemon.sh
chmod u+x start-audio-daemon.sh
echo ""
echo "Setup done.
echo ""
echo "You can launch Voicegain Audio Daemon by running"
echo " ./start-audio-daemon.sh
echo ""

