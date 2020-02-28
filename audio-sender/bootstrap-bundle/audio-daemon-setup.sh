#!/bin/bash
echo "Setup for Voicegain Audio Sender Daemon"

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