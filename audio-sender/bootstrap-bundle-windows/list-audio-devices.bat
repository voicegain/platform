@echo OFF

echo "Voicgain Audio Daemon: List Audio Devices"
set JSON=audio-daemon-config.json
echo "Startig Daemon"
java-launch-audio-daemon.bat %JSON%
pause