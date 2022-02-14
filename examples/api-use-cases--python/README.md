# Overview

These examples are similar in that they all use **async** api and also use **polling** to obtain the result of transcription. Here are the differences: 
* async-off-line-from-url.py - OFF-LINE transcription of audio file retrieved from URL
* async-off-line-from-url-two-channel-callback.py - OFF-LINE transcription of audio file retrieved from URL. It is assumed that the audio is 2-channel (stereo) with one speaker in left channel and second speaker in the right channel. The result of transcription will be submitted via callback.
* async-off-line-via-file-upload.py - OFF-LINE transcription of audio file uploaded using /data API (multipart/form-data)
retrieved from URL - this example processes a single file and shows details of all polling request
* async-off-line-via-file-upload-bulk.py - this is similar to the example above but processes all files from a directory (the name of which you set inside the script) and stores only the final results in text format (no intermediate polling results are stored). This is a handy script to process a lot of files in offline mode. Note: it submits 1 file at a time so it is not optimized for throughput.  
* async-off-line-2-chn-via-data-upload-bulk.py - same as the script above except for being configured to process 2-channel audio (stereo files where left and right channels contain different speakers). We are doing basically 2 offline transcriptions - one for left channel and one for right channel.
* async-real-time-word-tree.py - REAL-TIME transcription of audio file retrieved from URL. It uses the word-tree output which provides more recognition alternatives/hypotheses.
* async-real-time-from-websocket-with-polling.py - REAL-TIME transcription of audio file streamed via a websocket. The transcript results (incremental and full) are retrieved via polling. This script is setup to process all audio input files from input directory and report results in a single text file. It transcodes input audio files to a format suitable for websocket streaming, e.g. mulaw. 
* async-real-time-websocket-in-and-out.py - REAL-TIME transcription of audio file streamed via a websocket. Results (words) are received also using a websocket.
* edge-async-real-time-from-websocket-with-polling.py - similar to async-real-time-from-websocket-with-polling.py but adapted to run against edge deployment
* async-semi-real-time-via-file-upload.py - SEMI-REAL-TIME transcription - will work also on Edge either with Offline or Real-Time Model

# Install
To run these scripts you will need Python (we have tested the scripts using python 3.8). You will need to install the required dependencies using `pip`.

# JWT

All scripts need JWT token to be inserted in the specified place in the script, e.g.

```
...
## incremental polling interval
pollingInterval = 0.75

#voicegain
host = "api.voicegain.ai"
JWT = "<JWT obtained from the Voicegain Developer Console (https://console.voicegain.ai)>"

## ALL settings above this line ##
...
```

replace all the text between quotes with the JWT (do not leave <>).

Here are [instructions on how to obtain a JWT](https://support.voicegain.ai/hc/en-us/articles/360028023691-JWT-Authentication).

# Details of scripts
## Script: async-real-time-from-websocket-with-polling.py

Also applies to: edge-async-real-time-from-websocket-with-polling.py

### **Overview** 
This script performs REAL-TIME transcription of audio files streamed via a websocket. The transcript results (incremental and full) are retrieved via polling. This script is setup to process all audio input files from input directory (`input_path`) and report results in a single text file (`all_results_file`). 

For streaming the script uses ffmpeg to transcode input audio files to a format (`format`, `ffmpegFormat`) suitable for seding over websocket, e.g., to mulaw. ffmpeg is also used to change the sample rate to the target one (`sampleRate`)  

### **Install**
This script requires **ffmpeg**. This [video](https://www.youtube.com/watch?v=HmoCT7Km0wo) may be useful for Windows 10 users in demonstrating how to setup Git Bash, Python, and FFMpeg.  

### **Settings**

Various settings are in the top part of the python file.

You can also modify the body of the request. For example you can change `settings.asr.speechContext` from `normal` to `digits`, or you can enable/disable `settings.formatters`

### **Output**

Here is a sample output
```
writing all results to: output\all_results_2021-09-10_19-52-42.txt
AUDIO: ./m4a/2456786543215674_gy.m4a
        incremental:
                (2 fo)
                (245)
                (245678)
                (2456786)
                (245678654)
                (2456786543 TW)
                (2456786543215)
                (245678654321567)
        full:
                2456786543215674
AUDIO: ./m4a/4212345678901237.m4a
        incremental:
                (4 TW)
                (421 TW)
                (421234 f)
                (421234567)
                (4212345678 ni)
                (421234567890)
                (42123456789012 thr)
        full:
                4212345678901237

