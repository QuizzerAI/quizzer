import json
from typing import Any
from model import Answer, Question
from uuid import UUID

class QuizPackEncoder(json.JSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, UUID):
            return obj.hex
        if isinstance(obj, Answer):
            return obj.__dict__
        if isinstance(obj, Question):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)
