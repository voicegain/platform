"""
The MIT License

Copyright (c) Voicegain.

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, TypedDict, Tuple
import logging
from string import Template
import time
import copy
import json
# Logger
# import sys
#
# logger = logging.getLogger()
# handler = logging.StreamHandler(sys.stdout)
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# handler.setFormatter(formatter)
# logger.addHandler(handler)
# logger.setLevel(logging.DEBUG)

ENTRY_STATE = "ENTRY"

S3_BUCKET_NAME = 'jacek-lambda-1'
JSON_IVR_DEF_KEY = 'outbound-survey-ivr_json_10'


def lambda_handler(event, context):
    """
    Handle lambda function
    :return:
    """
    logging.info(str(event))
    declarative_json = get_json(S3_BUCKET_NAME, JSON_IVR_DEF_KEY)
    declarative_bot_logic = DeclarativeBotLogic(declarative_json=declarative_json)
    body = json.loads(event['body'])
    method = event['httpMethod']
    logging.info('Body: ' + str(body))
    response_body, status_code = declarative_bot_logic.request_handler(body, method)
    return {
        "statusCode": status_code,
        "headers": {'Content-Type': 'application/json'},
        "body": json.dumps(response_body)
    }


def get_json(s3_bucket_name, json_ivr_def_key):
    """
    Read JSON from S3 bucket
    :return: declarative_json
    """
    import boto3
    t16 = time.time()
    s3_object = boto3.client('s3').get_object(Bucket=s3_bucket_name, Key=json_ivr_def_key)
    declarative_json = json.loads(s3_object['Body'].read().decode('utf-8'))
    elapsed_time = time.time() - t16
    logText = "Time spent in getJSON is " + str(elapsed_time) + " seconds"
    logging.info(logText)
    return declarative_json


class StateInformation:

    def __init__(self, sid: str, d: Optional[dict]):
        if d is None:
            d = dict()
        self._d = d
        self._sid = sid
        self._d["sid"] = self._sid
        if "csid" not in self._d:
            self._d["csid"] = f"Cust-{self._sid}"
        if "sequence" not in self._d:
            self._d["sequence"] = 0
        if "state" not in self._d:
            self._d["state"] = ENTRY_STATE
        if "noInputCount" not in self._d:
            self._d["noInputCount"] = 0
        if "noMatchCount" not in self._d:
            self._d["noMatchCount"] = 0

    def to_json(self) -> dict:
        if "sip" in self._d:
            del self._d["sip"]
        return self._d

    def reset_input(self):
        """
        Reset noInputCount, noMatchCount and vuiResult
        :return:
        """
        self._d["noInputCount"] = 0
        self._d["noMatchCount"] = 0
        self.vui_result = None

    def seq_add_one(self):
        current_seq = int(self._d["sequence"])
        current_seq += 1
        self._d["sequence"] = current_seq

    @property
    def sid(self) -> str:
        return self._sid

    @property
    def csid(self) -> str:
        return self._d["csid"]

    @property
    def sequence(self) -> int:
        return self._d["sequence"]

    @property
    def state(self) -> str:
        return self._d["state"]

    @state.setter
    def state(self, new_state):
        self._d["state"] = new_state

    @property
    def user_app_data(self) -> str:
        return self._d.get("userAppData")

    @user_app_data.setter
    def user_app_data(self, new_user_app_data):
        self._d["userAppData"] = new_user_app_data

    @property
    def vui_result(self):
        return self._d.get("vuiResult")

    @vui_result.setter
    def vui_result(self, new_result):
        if new_result:
            self._d["vuiResult"] = new_result
        else:
            if "vuiResult" in self._d:
                del self._d["vuiResult"]

    @property
    def no_input_count(self):
        return self._d["noInputCount"]

    def no_input_count_add_one(self):
        current_no_input_count = int(self._d["noInputCount"])
        current_no_input_count += 1
        self._d["noInputCount"] = current_no_input_count

    @property
    def no_match_count(self):
        return self._d["noMatchCount"]

    def no_match_count_add_one(self):
        current_no_match_count = int(self._d["noMatchCount"])
        current_no_match_count += 1
        self._d["noMatchCount"] = current_no_match_count


class LogicStateType(Enum):
    VOID = 1
    INPUT = 2
    OUTPUT = 3
    DISCONNECT = 4
    TRANSFER = 5
    EVAL = 6


class LogicState(ABC):

    def __init__(self, type: str, next: str = None, **kwargs):
        self._logic_type = LogicStateType[type]
        self._next = next

    @property
    def logic_type(self) -> LogicStateType:
        return self._logic_type

    @abstractmethod
    def run(self, body: dict, state_information: StateInformation) -> Optional[Tuple[dict, int]]:
        """

        :param body: request body
        :param state_information:
        :return:
        """
        pass

    @abstractmethod
    def ack(self, body: dict, state_information: StateInformation) -> None:
        pass


class InputLogicState(LogicState):
    """
    We exit this state when we get a match
    If it's NO_MATCH, or the confidence is lower than threshold, we reprompt.
    """

    def __init__(self,
                 global_default, global_grammars,
                 name: str, voice: str = None,
                 grammar: list = None,
                 prompt: str = None, nonBargeInPrompt: str = None,
                 noMatchMax: int = 2, noInputMax: int = 2,
                 waitMsec: int = None, noInputTimeout: int = None,
                 fail: str = None, confirmation: dict = None, **kwargs):
        super().__init__(**kwargs)
        self._global_default = global_default
        self._global_grammars = global_grammars
        self._name = name
        self._voice = voice
        self._grammar = grammar
        self._prompt = prompt
        self._non_barge_in_prompt = nonBargeInPrompt
        self._no_match_max = noMatchMax
        self._no_input_max = noInputMax
        self._wait_msec = waitMsec
        self._no_input_timeout = noInputTimeout
        self._fail = fail
        self._confirmation = confirmation

    def run(self, body: dict, state_information: StateInformation) -> Optional[Tuple[dict, int]]:
        """

        :param body: request body
        :param state_information:
        :return:
        """

        no_input_count = state_information.no_input_count
        no_match_count = state_information.no_match_count
        vui_result = state_information.vui_result

        prefix = ""

        match vui_result:
            case 'NOMATCH':
                # no-match
                if no_match_count < self._no_match_max:
                    prefix = self._global_default['prefixes']['noMatch'][no_match_count]
                    state_information.no_match_count_add_one()
                else:  # Case when there are more noMatch(es) than desired
                    state_information.state = self._fail
                    state_information.vui_result = 'ERROR'
                    return None
            case 'NOMATCH-CONF':
                if no_match_count < self._no_match_max:
                    prefix = self._global_default['repromtOnDisconfirm']
                    state_information.no_match_count_add_one()
                else:  # Case when there are more noMatch(es) than desired
                    state_information.state = self._fail
                    state_information.vui_result = 'ERROR'
                    return None
            case 'NOINPUT':
                # no-input
                if no_input_count < self._no_input_max:
                    prefix = self._global_default['prefixes']['noInput'][no_input_count]
                    state_information.no_input_count_add_one()
                else:  # Case when there are more noInput(s) than desired
                    state_information.state = self._fail
                    state_information.vui_result = 'ERROR'
                    return None
            case 'TO-CONFIRM':
                pass
            case _:
                # First time the function is called
                pass

        response = {
            "question": {
                "name": self._name,
                "audioResponse": {}
            }
        }

        if vui_result == 'TO-CONFIRM':
            response["question"]["text"] = self._confirmation['prompt']
        if (self._non_barge_in_prompt is not None) and (self._prompt is None):
            response["question"]["text"] = prefix + self._non_barge_in_prompt
        elif (self._non_barge_in_prompt is None) and (self._prompt is not None):
            response["question"]["audioResponse"]["questionPrompt"] = prefix + self._prompt
        elif (self._non_barge_in_prompt is not None) and (self._prompt is not None):
            response["question"]["text"] = prefix + self._non_barge_in_prompt
            response["question"]["audioResponse"]["questionPrompt"] = self._prompt
        else:
            response["question"]["text"] = ""

        if self._voice:
            response["question"]["audioProperties"] = {
                "voice": self._voice
            }

        if self._wait_msec:
            response["question"]["waitMsec"] = self._wait_msec

        if self._no_input_timeout:
            response["question"]["audioResponse"]["noInputTimeout"] = self._no_input_timeout

        if vui_result == 'TO-CONFIRM':
            response["question"]["audioResponse"]["grammar"] = [{"type": "BUILT-IN", "name": "boolean"}]
        else:
            if self._grammar:
                final_grammars = []
                for gr in self._grammar:
                    logging.info("gr type of: " + str(type(gr)))
                    if isinstance(gr, str):
                        # do a lookup of grammar by name
                        final_grammars.append(self._global_grammars[gr])
                    else:
                        # we have the grammar definition already
                        final_grammars.append(gr)
                response["question"]["audioResponse"]["grammar"] = final_grammars
        return response, 200

    def ack(self, body: dict, state_information: StateInformation) -> None:

        input_event = None
        if "events" in body:
            for event in body["events"]:
                if event["type"] == "input":
                    input_event = event
                    break

        if input_event:

            if state_information.vui_result == 'TO-CONFIRM':
                return self._ack_confirmation_func(input_event, state_information)

            match input_event['vuiResult']:
                case 'MATCH':
                    min_confidence = self._get_confidence_threshold_to_reprompt()
                    reco_conf = input_event['vuiAlternatives'][0].get('confidence')
                    grmr_name = input_event['vuiAlternatives'][0].get('grammar')
                    # we confirm only grammar recognition
                    if self._confirmation and ("prompt" in self._confirmation) and (grmr_name is not None) and (
                            (reco_conf is None) or reco_conf < min_confidence
                    ):
                        # need to confirm
                        state_information.vui_result = 'TO-CONFIRM'
                        return
                    else:
                        # This is executed if it's a match with confidence above threshold
                        state_information.state = self._next
                        state_information.reset_input()
                        return
                case 'NOMATCH':
                    state_information.vui_result = 'NOMATCH'
                    return
                case 'NOINPUT':
                    state_information.vui_result = 'NOINPUT'
                    return
                case _:
                    pass
        state_information.state = self._fail
        state_information.vui_result = "ERROR"
        return

    def _get_confidence_threshold_to_reprompt(self):
        """
        Retrieve confidence threshold
        :return:
        """
        if (not self._confirmation) or ('threshold' not in self._confirmation):
            return self._global_default['thresholds']['confirmation']
        return self._confirmation['threshold']

    def _ack_confirmation_func(self, input_event: dict, state_information: StateInformation) -> None:
        var_name = self._name + ".MEANING"
        if (input_event['vuiResult'] == 'MATCH') and (input_event.get(var_name) == "true"):
            state_information.state = self._next
            state_information.reset_input()
        else:  # MATCH with NO as a response or NOMATCH/NOINPUT - vuiResult is NOMATCH and state remains currState
            state_information.vui_result = 'NOMATCH-CONF'


class VoidLogicState(LogicState):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def run(self, body: dict, state_information: StateInformation) -> Optional[Tuple[dict, int]]:
        """

        :param body: request body
        :param state_information:
        :return:
        """
        state_information.state = self._next
        return None

    def ack(self, body: dict, state_information: StateInformation) -> None:
        raise NotImplementedError(f"VOID state doesn't support ACK")


class OutputLogicState(LogicState):
    def __init__(self, prompt, voice=None, dtmf=None, **kwargs):
        super().__init__(**kwargs)
        self._prompt = prompt
        self._voice = voice
        self._dtmf = dtmf

    def run(self, body: dict, state_information: StateInformation) -> Optional[Tuple[dict, int]]:
        """

        :param body: request body
        :param state_information:
        :return:
        """
        response = {
            "prompt": {
                "text": self._prompt
            }
        }
        if self._voice:
            response["prompt"]["audioProperties"] = {
                "voice": self._voice
            }

        if self._dtmf:
            response["prompt"]["dtmf"] = self._dtmf

        return response, 200

    def ack(self, body: dict, state_information: StateInformation) -> None:
        state_information.state = self._next


class EvalLogicState(LogicState):
    def __init__(self, eval, case, **kwargs):
        super().__init__(**kwargs)
        self._eval = eval
        self._case = case

    def run(self, body: dict, state_information: StateInformation) -> Optional[Tuple[dict, int]]:
        """

        :param body: request body
        :param state_information:
        :return:
        """
        logging.info(f"Eval expr={self._eval}")
        templ = Template(self._eval)
        afterSubst = templ.safe_substitute(**state_information.to_json())
        logging.info("After substitution: " + afterSubst)
        ans = eval(afterSubst)
        logging.info("Eval result: " + str(ans))
        for c in self._case:
            if self._check_expr(c['expr'], ans):
                next_state = c['next']
                state_information.state = next_state
                return None
        # If none of the expressions are satisfied, use the default next state
        state_information.state = self._next
        return None

    def ack(self, body: dict, state_information: StateInformation) -> None:
        raise NotImplementedError(f"EVAL state doesn't support ACK")

    @staticmethod
    def _check_expr(expr, ans):
        t12 = time.time()
        expr = expr.replace('${1}', ans)
        x = eval(expr)
        elapsed_time = time.time() - t12
        logText = "Expr: " + expr + " evaluated to " + str(x) + " :Time spent in checkExpr is " + str(
            elapsed_time) + " seconds"
        logging.info(logText)
        return x


class TransferLogicState(LogicState):
    def __init__(self, prompt, voice=None, phone=None, fail=None, **kwargs):
        super().__init__(**kwargs)
        self._prompt = prompt
        self._voice = voice
        self._phone = phone
        self._fail = fail

    def run(self, body: dict, state_information: StateInformation) -> Optional[Tuple[dict, int]]:
        """

        :param body: request body
        :param state_information:
        :return:
        """
        response = {
            "transfer": {
                "prompt": {
                    "text": self._prompt
                },
                "phone": self._phone['phoneNumber']
            }
        }
        if self._voice:
            response["transfer"]["prompt"]["audioProperties"] = {
                "voice": self._voice
            }
        return response, 200

    def ack(self, body: dict, state_information: StateInformation) -> None:
        if body['events'][-1]['outcome'] == 'success':  # Transfer is a success
            state_information.state = None  # TODO: END??
            return
        else:
            state_information.state = self._fail
            return


class DisconnectLogicState(LogicState):
    def __init__(self, prompt, reason=None, voice=None, **kwargs):
        super().__init__(**kwargs)
        self._prompt = prompt
        self._reason = reason
        self._voice = voice

    def run(self, body: dict, state_information: StateInformation) -> Optional[Tuple[dict, int]]:
        """

        :param body: request body
        :param state_information:
        :return:
        """
        response = {
            "disconnect": {
                "prompt": {
                    "text": self._prompt
                },
                "reason": self._reason
            }
        }
        if self._voice:
            response["disconnect"]["prompt"]["audioProperties"] = {
                "voice": self._voice
            }
        return response, 200

    def ack(self, body: dict, state_information: StateInformation) -> None:
        raise NotImplementedError(f"EVAL state doesn't support ACK")


class DeclarativeBotLogic:
    def __init__(self, declarative_json):
        self._declarative_json = declarative_json

    def request_handler(self, body, method):
        """
        Handle different requests.
        :param body:
        :param method: request type
        :return: main_response containing stateInformation
        """
        sid = body["sid"]
        if method == 'POST':
            user_app_data = body.get("userAppData")
            state_information = StateInformation(sid, None)
            if user_app_data:
                state_information.user_app_data = user_app_data

            _state_map = self._load_json(self._declarative_json, state_information.user_app_data)
            run_state_output = None
            while run_state_output is None:
                state = _state_map.get(state_information.state)
                if not state:
                    return self._get_error_response("Invalid state", "ERROR", "Invalid state", 500)
                run_state_output = state.run(body, state_information)
            response, response_code = run_state_output
            return self._main_response(response, state_information), response_code

        elif method == 'PUT':  # For all intermediate cases
            state_information = StateInformation(sid, body.get("vars"))
            _state_map = self._load_json(self._declarative_json, state_information.user_app_data)
            # ack
            state = _state_map[state_information.state]
            state.ack(body, state_information)
            # run next state
            run_state_output = None
            while run_state_output is None:
                state = _state_map.get(state_information.state)
                if not state:
                    return self._get_error_response("Invalid state", "ERROR", "Invalid state", 500)
                run_state_output = state.run(body, state_information)
            response, response_code = run_state_output
            return self._main_response(response, state_information), response_code

        elif method == 'DELETE':  # When the call ends naturally
            state_information = StateInformation(sid, body.get("vars"))
            return self._main_response(
                {"termination": "normal"},
                state_information
            ), 200

        else:
            logging.info('UNKNOWN')
            debug = "Invalid HTTP Request (Invalid Method) received at backend"
            detail = "Invalid HTTP Method",
            reason = "Invalid request"
            return self._get_error_response(debug, detail, reason, 400)

    @staticmethod
    def _load_json(declarative_json, use_app_data: str = None):
        if use_app_data:
            declarative_json = copy.deepcopy(declarative_json)
            user_app_data_list = use_app_data.split("&")
            for d in user_app_data_list:
                d_split_list = d.split("=")
                if len(d_split_list) != 2:
                    logging.warning(f"Invalid user app data {use_app_data}")
                    continue
                d_key_list = d_split_list[0].split(".")
                d_value = d_split_list[1]
                current_d = declarative_json
                for d_key in d_key_list[:-1]:
                    if d_key in current_d:
                        current_d = current_d[d_key]
                    else:
                        new_d = dict()
                        current_d[d_key] = new_d
                        current_d = new_d
                current_d[d_key_list[-1]] = d_value

        _state_map: TypedDict[str, LogicState] = dict()
        _default = declarative_json.get('DEFAULTS', {})
        _grammars = declarative_json.get("GRAMMARS", {})
        for key, value in declarative_json.items():
            if not isinstance(value, dict):
                continue
            state_type_str = value.get("type")
            if not state_type_str:
                continue
            state_type = LogicStateType[state_type_str]
            match state_type:
                case LogicStateType.INPUT:
                    _state_map[key] = InputLogicState(
                        global_default=_default,
                        global_grammars=_grammars,
                        **value)
                case LogicStateType.OUTPUT:
                    _state_map[key] = OutputLogicState(**value)
                case LogicStateType.VOID:
                    _state_map[key] = VoidLogicState(**value)
                case LogicStateType.EVAL:
                    _state_map[key] = EvalLogicState(**value)
                case LogicStateType.TRANSFER:
                    _state_map[key] = TransferLogicState(**value)
                case LogicStateType.DISCONNECT:
                    _state_map[key] = DisconnectLogicState(**value)
        return _state_map

    @staticmethod
    def _main_response(response_dict: dict, state_information: StateInformation):
        """

        :param response_dict:
        :param state_information:
        :return:
        """
        state_information.seq_add_one()
        temp = {
            "csid": state_information.csid,
            "sid": state_information.sid,
            "sequence": state_information.sequence,
            'vars': state_information.to_json()
        }
        response_dict.update(temp)
        return response_dict

    @staticmethod
    def _get_error_response(debug, detail, reason, code=400):
        errorResponse = {
            "debug": debug,
            "error": {
                "detail": detail,
                "reason": reason
            }
        }
        return errorResponse, code
