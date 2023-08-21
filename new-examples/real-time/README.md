This directory contains sample Python scripts that demonstrate real-time transcription using Voicegain API.

Scripts with `ffmpeg` in their name can transcode from any audio format to format suitable for streaming over websocket.

* rt-2chn-simulated-twiml-f32.py - streaming 2 files (left/right) through a websocket using simulated TWIML (Twilio Media Streams) protocol, files are in 32-bit Floating Point PCM format
* rt-2chn-simulated-twiml-pcmu.py - streaming 2 files (left/right) through a websocket using simulated TWIML (Twilio Media Streams) protocol, files are in 32-bit PCMU (ulaw) format
* rt-websocket-1chn-ffmpeg.py - streaming a mono file using websocket, results are returned over another websocket in word-by-word mode
* rt-websocket-2chn-ffmpeg.py - streaming a stereo file using websocket, results are returned 2 other websockets in word-by-word mode
* rt-websocket-2chn-segment-ffmpeg.py - streaming a stereo file using websocket, results are returned 2 other websockets in segment-by-segment mode 
* rt-websocket-polling-ffmpeg-bulk.py - streaming a mono file using websocket, results are returned via polling (this method can process multiple files) 
  Note: if file is stereo, in this configuration the transcript will be of the merged audio. We will add a two-channel model example soon.
* rt-websocket-transceiver-2chn-ffmpeg.py - streaming a stereo file using websocket, results are returned over the same websocket in word-by-word mode
* rt-websocket-transceiver-2chn-segment-ffmpeg.py - streaming a stereo file using websocket, results are returned over the same websocket in segment-by-segment mode

Note: sentence-by-sentence has been discontinued as of Release 1.88.0 and replaced by segment-by-segment.