@echo OFF

echo "Starting Voicegain Audio Daemon"

set TIME1=%date:/=-%
set TIME2=%time::=-%
set TIME=%TIME1%_%TIME2: =0%
set DATE=%TIME:~4,18%
set APPLOG=audio-daemon.%DATE%.log

::Source value may have to be modified to match the correct Audio Input Device
set SOURCE=5

set JSON=audio-daemon-config.json

echo "Starting Daemon in background with log redirected to %APPLOG%"
java-launch-audio-daemon.bat %JSON% %SOURCE% %APPLOG% 

::tasklist /fi "imagename eq vg-audio-sender-daemon-1.30.1.jar"

::echo "Tailing log from %APPLOG%"
::more %APPLOG%
pause