# Grammar Processor

==========================================

This is a library for creating grammars in [JJSGF](https://support.voicegain.ai/hc/en-us/articles/360048936511-JJSGF-Grammars) format from a set of sentences. 


```python
sentences_to_jjsgf_grammar(sentences)
```

, where sentences is a python list, creates a JJSGF grammar from the sentences (near-shortest grammar).


__________
The following methods are used to process the grammar:

```python
generateBaseGrammar(sentences)
```

generates ABNF-style grammar from the sentences.

```python
get_jjsgf(grammar)
```
builds unprocessed JJSGF-formatted grammar from above ABNF.


```python
fix_jjsgf(jjsgf)
```

Takes JJSGF grammar and optimizes by removing repeated rules and combining where possible iteratively.



