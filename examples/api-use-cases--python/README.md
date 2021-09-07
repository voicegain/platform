# Overview

These 4 examples are similar in that they all use **async** api and also use **polling** to obtain the result of transcription. Here are the differences: 
* async-off-line-from-url.py - OFF-LINE trancription of audio file retrieved from URL
* async-off-line-via-file-upload.py - OFF-LINE trancription of audio file uploaded using /data API (multipart/form-data)
* async-real-time-word-tree.py - REAL-TIME transcription of audio file retrieved from URL. It uses the word-tree output which provides more recognition alternatives/hypotheses.
* async-real-time-from-websocket-with-polling.py - REAL-TIME transcription of audio file streamed via a websocket. The transcript results (incremental and full) are retrieved via polling. This script is setup to process all audio input files from input directory and report results in a single text file.

# Install
To run these scripts you will need Python (we have tested the scripts using python 3.8). You will need to install the required dependencies using `pip`.

The last script requires ffmpeg. This [video](https://www.youtube.com/watch?v=HmoCT7Km0wo) may be useful for Windows 10 users in demonstrating how to setup Git Bash, Python, and FFMpeg.  
