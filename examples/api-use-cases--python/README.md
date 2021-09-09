# Overview

These 4 examples are similar in that they all use **async** api and also use **polling** to obtain the result of transcription. Here are the differences: 
* async-off-line-from-url.py - OFF-LINE trancription of audio file retrieved from URL
* async-off-line-via-file-upload.py - OFF-LINE trancription of audio file uploaded using /data API (multipart/form-data)
retrieved from URL - this example processes a single file and shows details of all polling request
* async-off-line-via-file-upload-bulk.py - this is similar to the example above but processes all files from a directory (the name of which you set inside the script) and stores only the final results in text format (no intermediate polling results are stored). This is a handy script to process a lot of files in offline mode. Note: it submits 1 file at a time so it is not optimized for throughput.  
* async-off-line-2-chn-via-data-upload-bulk.py - same as the script above except for being configured to process 2-channel audio (stereo files where left and right channels contain different speakers)
* async-real-time-word-tree.py - REAL-TIME transcription of audio file retrieved from URL. It uses the word-tree output which provides more recognition alternatives/hypotheses.
* async-real-time-from-websocket-with-polling.py - REAL-TIME transcription of audio file streamed via a websocket. The transcript results (incremental and full) are retrieved via polling. This script is setup to process all audio input files from input directory and report results in a single text file. It transcodes input audio files to a format suitable for websocket streaming, e.g. mulaw. 

# Install
To run these scripts you will need Python (we have tested the scripts using python 3.8). You will need to install the required dependencies using `pip`.

The last script requires **ffmpeg**. This [video](https://www.youtube.com/watch?v=HmoCT7Km0wo) may be useful for Windows 10 users in demonstrating how to setup Git Bash, Python, and FFMpeg.  
