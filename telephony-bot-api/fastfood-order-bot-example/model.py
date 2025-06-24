from pydantic import BaseModel
from typing import Optional, List, Union


class Prompt(BaseModel):
    text: str


class Question(BaseModel):
    text: str


class VuiAlternatives(BaseModel):
    utterance: str


class InputEvent(BaseModel):
    vuiResult: str
    vuiAlternatives: Optional[List[VuiAlternatives]] = None


class OtherEvent(BaseModel):
    pass


# Request model for POST
class TelephonyBotPostReq(BaseModel):
    sid: str


# Request model for PUT
class TelephonyBotPutReq(BaseModel):
    csid: str
    sid: str
    events: Optional[List[Union[InputEvent, OtherEvent]]] = None


# Request model for DELETE
class TelephonyBotDeleteReq(BaseModel):
    csid: str
    sid: str


# Response model for POST and PUT request
class TelephonyBotPostPutResp(BaseModel):
    csid: str
    sid: str
    prompt: Optional[Prompt] = None
    question: Optional[Question] = None


# Response model for DELETE request
class TelephonyBotDeleteResp(BaseModel):
    csid: str
    termination: str
