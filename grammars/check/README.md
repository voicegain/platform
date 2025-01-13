repeat.py checks for presence of <item repeat="N"/> elements directly under <one-off>

Such grammars are currenlty not processed correctly by Voicegain ASR.

It is necessary to wrap <item repeat="N"/> into additional <item> so that none of the items directly under <one-of> has a a repeat.

BTW, the -o option is still being worked on. It will generate a grammar with the wrapping <item>s inserted where needed.