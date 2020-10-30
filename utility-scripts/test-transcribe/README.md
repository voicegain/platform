# What it does #
`test-trascribe.py` takes an audio file (or files) and transcribes it (them) using Voicegain STT API and (optionally) using Google STT API.</br>
If reference transcripts are provided then it will compute and report WER in an HTML formated report.</br>
If reference transcripts are not provided then it will do a diff of Voicegain vs Google transcription.

# How to use #
Copy `test-trascribe.py` to a directory of your choice. Additionally, you need two other directories (may be subdirectories of where `test-trascribe.py` is) - one for input audio files and one for the output results.

The input consists of:
* *.wav files - all wav files in the input directory will be transcribed. These may be mono or stereo files - for stereo files we assume that left and right channel mau contain different spoken audio, like e.g. recordings from a telephone platform where one channel is inbound and the other channels is outbound.
* *-reference.txt files - these are (optional) reference transcripts for each audio file

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
