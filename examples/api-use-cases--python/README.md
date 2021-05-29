These three examples are similar in that they all use async api and also use polling to obtain the result of transcription. Here are the differences: 
* async-off-line-from-url.py - OFF-LINE trancription of audio file retrieved from URL
* async-off-line-via-file-upload.py - OFF-LINE trancription of audio file uploaded using /data API (multipart/form-data)
* async-real-time-word-tree.py - REAL-TIME transcription of audio file retrieved from URL. It uses the word-tree output which provides more recognition alternatives/hypotheses.
