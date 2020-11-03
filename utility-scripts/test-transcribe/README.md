# What it does #
`test-transcribe.py` takes an audio file (or files) and transcribes it (them) using Voicegain STT API and (optionally) using Google STT API.</br>
If reference transcripts are provided then it will compute and report WER in an HTML formated report.</br>
If reference transcripts are not provided then it will do a diff of Voicegain vs Google transcription.

# Setup #
Copy `test-transcribe.py` and `requirements.txt` to a directory of your choice. 
Additionally, you need two other directories (may be subdirectories of where `test-transcribe.py` is located) - one for input audio files and one for the output results.

The input to `test-transcribe.py` consists of:
* *.wav files - all wav files in the input directory will be transcribed. These may be mono or stereo files - for stereo files we assume that left and right channel mau contain different spoken audio, like e.g. recordings from a telephone platform where one channel is inbound and the other channels is outbound.
* *-reference.txt files - these are (optional) reference transcripts for each audio file
* *-reference-right.txt files - these are (optional) reference transcripts for each stereo audio file
* *-reference-left.txt files - these are (optional) reference transcripts for each stereo audio file

The output will contain:
* *-voicegain.txt - transcription of mono audio from Voicegain API
* *-voicegain.txt - transcription of mono audio from Voicegain API
* *.html - the WER and diff report for transcription of mono audio
* *-voicegain-left.txt - transcription of left channel of stereo audio from Voicegain API
* *-google-left.txt - transcription of left channel of stereo audio from Google API
* *-voicegain-right.txt - transcription of right channel of stereo audio from Voicegain API
* *-google-right.txt - transcription of right channel of stereo audio from Google API
* *-left.html - the WER and diff report for transcription of left channel of stereo audio 
* *-right.html - the WER and diff report for transcription of right channel of stereo audio 

Before you run `test-transcribe.py` install all required python dependencies using:
<pre>
pip install -r requirements.txt
</pre>

# How to run #

The command line to run `test-transcribe.py` looks as follows:
<pre>
python test-transcribe.py iYJhbGciOiJIUzI1NiIssrqcCI6IkpXVCJ9.eyJhdWQiOiJodHRwczovL2Fwspun32ljZWdhaW4uYWkvdjEiLCJzdWIiOiJiZDE0ZmQ5NC0wYdjj7aTRjOWEtODJlZS1jY2YwZGJlZjY3MjkifQ.K5hBcjZCksjaFXR7MWMclGKvuQeXFTFhvGSwmwoiA6z input/ output/ acme-dev-3093553eb66c.json default
</pre>
the components are:
* the JWT token - see this [helpdesk article on how to get JWT](https://support.voicegain.ai/hc/en-us/articles/360028023691-JWT-Authentication)
* the input directory
* the output directory
* optional file with Google Cloud credentials in json format - if missing then only Voicegain transcription will be done
* optional [type of Google speech-to-text recognizer to use](https://cloud.google.com/speech-to-text/pricing#pricing_table) - Standard or [Enhanced](https://cloud.google.com/speech-to-text/docs/enhanced-models)
  * value `default` will use Google Standard recognizer
  * value `video` will use Google Enhanced (Video) recognizer 

# Notes and Limitations #

Voicegain recognizer is run in OFF-LINE mode. Google recognizer is run in streaming mode.

* Google recognizer in streaming mode can process an audio file with **maximum 5 minutes length**.
* Because of the setup overhead for Voicegain OFF-LINE mode, for short files you will notice that Google recognizer processes them faster. However, larger audio files will benefit from faster processing of the OFF-LINE mode and they will be completed significantly faster than on Google.
* We will soon provide a version that allows you to process files larger than 5 minutes on Google - but it will require that files are first uploaded to Google Storage.

