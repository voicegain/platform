# Examples of recognition using grammars

## Relevant Knowledge-Base Articles

* [Grammars Supported in /asr/recognize API](https://support.voicegain.ai/hc/en-us/articles/360045678932-Grammars-Supported-in-asr-recognize-API) - this also describes available buil-in grammars
  * GRXML
    * [Supported GRXML Syntax](https://support.voicegain.ai/hc/en-us/articles/360039777992-Supported-GRXML-Syntax)
    * [Sample GRXML Grammars](https://support.voicegain.ai/hc/en-us/articles/360046906211-Sample-GRXML-Grammars)
  * [JJSGF Grammars](https://support.voicegain.ai/hc/en-us/articles/360048936511-JJSGF-Grammars)
* [Grammar Caching](https://support.voicegain.ai/hc/en-us/articles/7987530013716-Grammar-Caching)
* Examples:
  * [Examples of Synchronous /asr/recognize API](https://support.voicegain.ai/hc/en-us/articles/360044558872-Examples-of-Synchronous-asr-recognize-API)
  * [Example of recognition with GRXML grammar of audio streamed via websocket](https://support.voicegain.ai/hc/en-us/articles/360047237552-Example-of-recognition-with-GRXML-grammar-of-audio-streamed-via-websocket)
  * [Continuous Recognition](https://support.voicegain.ai/hc/en-us/articles/360050327712-Continuous-Recognition)


## Older examples

We are converting them to new updates examples. Most of the old examples should work.

https://github.com/voicegain/platform/tree/master/examples/grammars


## /asr/recognize API

### sync-reco-grxml-url-en.py

Uses synchronous /asr/recognize API which returns recognition result in the response.

This script will run grammar-based recognition on all utterance audio files contained in INPUTFOLDER (see Configuration).

You can change the grammar used inside the script

**Note**, the first run will be slower, in particular when using a large grammar, because the grammar needs to be compiled. Subsequent runs will use a compiled grammar from a grammar cache.

**Configuration**

* Rename `config-example.ini` to `config.ini`
* Set values of `INPUTFOLDER` and `OUTPUTFOLDER`
  * Your utterance recording files will be in `INPUTFOLDER`
* Set JWT token, for more info see: https://support.voicegain.ai/hc/en-us/articles/360028023691-JWT-Authentication  

