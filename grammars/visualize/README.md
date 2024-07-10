# Grammar Processor

==========================================

This is a library for processing grammars in [GRXML] (https://www.w3.org/TR/speech-grammar) format and [JJSGF](https://support.voicegain.ai/hc/en-us/articles/360048936511-JJSGF-Grammars) format, creating railroad diagrams representing all possible outcomes of the grammar.

Diagrams
--------
Each of these files, grxmlprocessor.py and jjsgfprocessor.py, contain their own unique ways of parsing the different styles of grammar.


grxmlprocessor.py
----------
Constructing a set of diagrams for a grxml grammar contains one function call, for example

```python
grxmlToRailroad("zip_code_no_refs.grxml")  
```

,where zip_code_no_refs.grxml is found at https://support.voicegain.ai/hc/en-us/articles/360046906211-Sample-GRXML-Grammars, will creates files with name {rule name}.svg. As an example, ROOT.svg from this grammar is shown:


![ROOT (63)](https://github.com/codemstrneel/grammarprocessor/assets/41355538/b16b7b3f-c395-40f7-bcde-a20b159bb149)


__________
The following methods are used to process the grxml:

```python
extract_rules(xml_string)  
```

This method takes in a string and returns a processed dictionary with key of the rule name between < and > delimeters and the content of the rule, with tags between !! and !! delimeters as a result. As an example, the tensPlace rule from the Zip Code grammar is as follows:

'\<tensPlace\>': '(twenty  !!out.tensPlace="2";!! | thirty  !!out.tensPlace="3";!! | forty  !!out.tensPlace="4";!! | fifty  !!out.tensPlace="5";!! | sixty  !!out.tensPlace="6";!! | seventy  !!out.tensPlace="7";!! | eighty  !!out.tensPlace="8";!! | ninety  !!out.tensPlace="9";!!)'


```python
createDiagram(rules) 
```

takes a set of rules in the above format and writes to a series of svg files with file name {rule_name}.svg




jjsgfprocessor.py
----------

Constructing a set of diagrams for a grxml grammar contains one function call, for example

```python
jjsgfToRailroad("jjsgfComplex.txt")  
```

where jjsgfComplex.txt is 
[jjsgfComplex.txt](https://github.com/user-attachments/files/15980416/jjsgfComplex.txt). , This writes to a series of files {rule_name}.svg which contains the content of the railroad diagram. As an example, root.svg from this grammar is shown:


![root (64)](https://github.com/codemstrneel/grammarprocessor/assets/41355538/ae2b2bd8-ce7f-411b-afe2-a894d433b322)




The following methods are used to process the JJSGF::

```python
extract_rules(jjsgf_string)  
```

This method takes in a string and returns a processed dictionary with key of the rule name between < and > delimeters and the content of the rule, with tags between !! and !! delimeters as a result. As an example, the yes_phrase rule from the jjsgfComplex grammar is as follows:

'<yes_phrase>': '([sure|ok] ([<yes> [<yes>]] <yes> ))'


```python
createDiagram(rules) 
```

takes a set of rules in the above format and writes to a series of svg files with file name {rule_name}.svg

