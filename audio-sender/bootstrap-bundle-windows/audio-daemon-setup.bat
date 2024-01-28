@echo OFF

set CODE_NAME=voicegain
set DEPLOYMENT=master
set VG_VER=1.30.1
echo "Setup for voigain Audio Sender Daemon ver. %VG_VER%"

echo "Checking wget"

IF exist "%SystemRoot%\System32\wget.exe" (
    echo "Found wget executable in PATH"
    set _wget=%SystemRoot%\System32\wget.exe
) ELSE (
    echo "Please install wget - See README.md for more info"
    pause
    exit
)

::While testing, the script couldn't execute the wget command if the wget.exe file wasn't in the same folder
::This checks if the wget.exe file is in the same folder as the script
IF exist "%CD%\wget.exe" (
    echo "Found wget executable in daemon folder"
) ELSE (
    echo "Please place wget executable in daemon folder"
    pause
    exit
)

echo "Checking java version"

IF exist "C:\Program Files\Common Files\Oracle\Java\javapath\java.exe" (
    echo "Found java executable in PATH"
    set JAVA_HOME=C:\Program Files\Common Files\Oracle\Java\javapath
    set _java=%JAVA_HOME%\java.exe
) ELSE (
    echo "No Java. Please install Java 9"
    pause
    exit
)

PATH C:\Program Files\Common Files\Oracle\Java\javapath
for /f tokens^=2-5^ delims^=.-_^" %%j in ('java -fullversion 2^>^&1') do set "jver=%%j%%k%%l%%m"

IF %jver% LSS 19000 (
    echo "Java version is lower than 1.9 - Please install Java 9"
    pause
    exit
) ELSE (
    echo "OK - Java version is 1.9 or higher"
)

echo ""
echo "Downloading Voicegain Audio Sender Daemon"
wget "https://s3.us-east-2.amazonaws.com/files.public.voicegain.ai/vg-audio-sender-daemon-%VG_VER%.jar"
echo ""
echo "Downloading java launch script"
wget "https://raw.githubusercontent.com/voicegain/platform/%DEPLOYMENT%/audio-sender/bootstrap-bundle/java-launch-audio-daemon.bat"
echo ""
echo "Downloading list audio devices script"
wget "https://raw.githubusercontent.com/voicegain/platform/%DEPLOYMENT%/audio-sender/bootstrap-bundle/list-audio-devices.bat"
echo ""
echo "Downloading daemon start script"
wget "https://raw.githubusercontent.com/voicegain/platform/%DEPLOYMENT%/audio-sender/bootstrap-bundle/start-audio-daemon.bat"
echo ""
echo "Setup done."
echo ""
echo "You can view available audio devices by running"
echo "list-audio-devices.sh"
echo ""
echo "You can launch Voicegain Audio Daemon by running"
echo "start-audio-daemon.sh"
echo ""
pause