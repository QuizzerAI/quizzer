#!/usr/bin/python3
import sys
import json
from typing import List
from model import Question, AIResponse
from .ai_decoder import AIDecoder
from .quiz_pack_encoder import QuizPackEncoder
from .pack import pack

def get_input() -> str:
    result: str = ""
    for line in sys.stdin:
        result += line
    return result

def load_response() -> AIResponse:
    return AIResponse(**json.loads(get_input(), cls=AIDecoder))

def dump_questions(questions: List[Question]) -> str:
    return json.dumps([q.__dict__ for q in questions], indent=4, cls=QuizPackEncoder)

questions: List[Question] = pack(load_response())
string_of_questions: str = dump_questions(questions)
print(string_of_questions)