repeat.py checks for presence of <item repeat="N"/> elements directly under <one-off>

Such grammars are currenlty not processed correctly by Voicegain ASR.

It is necessary to wrap <item repeat="N"/> into additional <item> so that none of the items directly under <one-of> has a a repeat.

BTW, the -o option is still being worked on. It will generate a grammar with the wrapping <item>s inserted where needed.

<pre>
usage: repeat.py [-h] [-i INPUT] [-o OUTPUT]

Finds <items> with a repeat attribute, that are direct children of <one-of> elements. It can also correct the mistake and output new grammar to a file.

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        the input file to check
  -o OUTPUT, --output OUTPUT
                        the output file to save the corrected input file
</pre>