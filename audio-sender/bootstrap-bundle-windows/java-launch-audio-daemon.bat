@echo OFF

set VERSION=1.30.1
set HEAP=128m

set ARGC=0
FOR %%x IN (%*) DO Set /A ARGC+=1

IF %ARGC%==1 GOTO one
IF %ARGC%==3 GOTO two

:one

set TIME1=%date:/=-%
set TIME2=%time::=-%
set TIME=%TIME1%_%TIME2: =0%
set DATE=%TIME:~4,18%
set GCLOG=gc-audio-daemon.%DATE%.log

echo "GC log will be written to: %GCLOG%"

java -Xlog:gc:%GCLOG% -Xms%HEAP% -Xmx%HEAP% -XX:+UseG1GC -XX:MaxGCPauseMillis=5 -jar vg-audio-sender-daemon-%VERSION%.jar --json %1 -i --log info --avc on
pause
GOTO end

:two

set TIME1=%date:/=-%
set TIME2=%time::=-%
set TIME=%TIME1%_%TIME2: =0%
set DATE=%TIME:~0,18%
set GCLOG=gc-audio-daemon.%DATE%.log

echo "GC log will be written to: %GCLOG%"

java -Xlog:gc:%GCLOG% -Xms%HEAP% -Xmx%HEAP% -XX:+UseG1GC -XX:MaxGCPauseMillis=5 -jar vg-audio-sender-daemon-%VERSION%.jar >> %3 2>&1 --json %1 --source %2

:end
