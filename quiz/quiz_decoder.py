import json
from typing import Any, Dict
from model import Question, Answer

class QuizDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj: Dict[str, Any]) -> Any:
        if "answers" in obj:
            return Question(**obj)
        if "answer" in obj:
            return Answer(**obj)
        return obj
