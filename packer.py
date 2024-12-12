#!/usr/bin/python3
from typing import List, Dict, Any
from uuid import uuid4, UUID
from model import Question, Answer, AIResponse, AIQuestion
import json

class AIDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj: Dict[str, Any]) -> Any:
        if "name" in obj:
            return AIResponse(**obj)
        if "answers" in obj:
            return AIQuestion(**obj)
        return obj

class QuizPackEncoder(json.JSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, UUID):
            return obj.hex
        if isinstance(obj, Answer):
            return obj.__dict__
        if isinstance(obj, Question):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

def pack(response: AIResponse) -> List[Question]:
    questions: List[Question] = []
    for question in response.questions:
        answers: List[Answer] = []
        for answer in question.answers:
            answers.append(Answer(answer))
        correct: Answer = answers[question.correct]
        questions.append(Question(question.question, answers, correct.uuid, question.explanation))
    return questions

if __name__ == "__main__":
    import sys
    
    ai_response_string: str = ""

    for line in sys.stdin:
        ai_response_string += line

    ai_response: AIResponse = AIResponse(**json.loads(ai_response_string, cls=AIDecoder))
    questions: List[Question] = pack(ai_response)
    print(json.dumps([q.__dict__ for q in questions], indent=4, cls=QuizPackEncoder))