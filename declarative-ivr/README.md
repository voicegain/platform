# Declarative IVR

This folder contains an AWS Lambda python script that together with Voicegain Telephony Bot API offers an easy method for building simple to moderately complex IVRs. 

## The declarative YAML for specifying IVRs - actions

Below are examples of all available IVR actions:

### VOID
```
  type: VOID
  next: Welcome
```
Does not do anything except specifying next action to execute. Useful e.g. for joining multiple paths in the flow, or logically partitioning the flow.

### OUTPUT
```
  type: OUTPUT
  voice: catherine
  prompt: |
    Hello, this is a call from Santa North Pole, LLC. 
    We would like to ask you a few questions regarding your satisfaction with the recent visit from Santa. 
    It will not take more than two minutes.  
  next: AgreeToParticipate
```
Specifies the prompt to be played and the voice to use (if diferent from the default voice).
Prompt text supports variable substitution.

### INPUT
```
  type: INPUT
  name: agreeToParticipate
  voice: catherine
  prompt: 'Would you like to participate now, or would you rather have us call you later.'
  bargeIn: true
  grammar: 
  - participate
  noInputMax: 1
  noMatchMax: 1
  confirmation:
    threshold: 0.33
    prompt: "Was it: ${agreeToParticipate} ?"
  fail: CallHealth
  next: ParticipateDecision  
```
Used to play a question prompt and gather input.
* More than one grammar is allowed. This makes it possible to handle both speech and DTMF input.
* semantic result of the grammar recognition will be assigned to a variable specified with `name`
* In case of NOINPUT or NOMATCH the specified number of re-prompts will be automatically performed.
* It is possible to do automatic confirmation question if confidence is below a set threshold
* in case of too many NOINPUT or NOMATCH  the specified  `fail` action will be executed.

### EVAL
```
  type: EVAL
  eval: "'${agreeToParticipate}'"
  case:
  - expr: "'${1}'=='now'"
    next: ParticipateNow
  - expr: "'${1}'=='later'"
    next: ParticipateLater
  next: ParticipateNever
```

Used to do expression evaluation and branching. Can reference variables collected during the IVR flow. External variables can be injected at the start of the session

The `case` expression allows for branching. It evaluates expressions in sequence and the first one evaluating to **true** will be taken. Special variable `${1}` can be used to reference the result of `eval`

Note tha you may modify the AWS Lambda python script and introduce your own functions and variables that may be used in EVAL.

### DISCONNECT
```
  type: DISCONNECT
  voice: catherine
  prompt: Thank you for your time, goodbye.
  reason: NORMAL
```
Plays the specified prompt and disconnects the call. Disconnect will result either in a hangup (is the call was a top level call) or a transfer back to the invoking call if the call was bridged from another call.

The `reason` will be stored in the session.

## The declarative YAML for specifying IVRs - special elements

The YAML has several special elements:

