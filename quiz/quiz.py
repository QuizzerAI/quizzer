from typing import List, Dict
from model import Question, Answer
from uuid import UUID

class Quiz:
    questions: List[Question]
    user_answers: Dict[UUID, UUID]

    def __init__(self, questions: List[Question]):
        self.questions = questions
        self.user_answers = {}

    def get_question(self, index: int) -> Question:
        return self.questions[index]

    def answer_question(self, question: Question, answer: Answer):
        self.user_answers[question.uuid] = answer.uuid
    
    def grade(self) -> int:
        score = 0
        for question_id in self.user_answers:
            question = [q for q in self.questions if q.uuid == question_id][0]
            answer_id = self.user_answers[question_id]
            answer = [a for a in question.answers if a.uuid == answer_id][0]
            if answer.uuid == question.correct:
                score += 1
        return score
