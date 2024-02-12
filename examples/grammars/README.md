scripts in this deirectory:
* **recognize-alphanumeric.py** - does alphanumeric recognition using one of the grammars in grxml directory, uses audio from Recordings
* **uk-postcodes-benchmark.py** - run a benchmark for UK postocdes recognition using grammar in uk-postcodes-jjsgf.json
* **sync-reco-inline-grammar-jsgf-spanish.py** - simple example for Spanish recognition using grammar in JJSGF format
* **sync-reco-inline-grammar-grxml-english.py** - example of English zip code recognition using GRXML grammar from an S3 url

These scripts require ffmpeg to be installed.
Windows installation:
1. Download pakcages & executable files from https://ffmpeg.org/download.html
2. Unzip the files and rename the folder to "ffmpeg"
3. Move the folder into the root of C: drive
4. Run CMD as administrator and run: setx /m PATH "C:\ffmpeg\bin;%PATH%"
5. Restart your computer and verify installation with: ffmpeg -version

Linux installation:
Run one of the following commands as appropriate for your Linux Distribution:
sudo apt install ffmpeg         [On Debian, Ubuntu and Mint]
sudo yum install ffmpeg         [On RHEL/CentOS/Fedora and Rocky/AlmaLinux]
sudo emerge -a sys-apps/ffmpeg  [On Gentoo Linux]
sudo apk add ffmpeg             [On Alpine Linux]
sudo pacman -S ffmpeg           [On Arch Linux]
sudo zypper install ffmpeg      [On OpenSUSE]    
sudo pkg install ffmpeg         [On FreeBSD]