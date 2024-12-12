#!/usr/bin/python3
import json
from typing import Any, Dict, List
from model import Question, Answer
from uuid import UUID

class QuizDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj: Dict[str, Any]) -> Any:
        if "answers" in obj:
            return Question(**obj)
        if "answer" in obj:
            return Answer(**obj)
        return obj

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

if __name__ == "__main__":
    bold = "\033[1m"
    red = "\033[91m"
    green = "\033[92m"
    end = "\033[0m"

    def get_input() -> List[Question]:
        import sys
        question_list_string: str = ""
        for line in sys.stdin:
            question_list_string += line
        sys.stdin = open('/dev/tty')
        return json.loads(question_list_string, cls=QuizDecoder)
    
    quiz = Quiz(get_input())

    def ask_question(quiz: Quiz, index: int):
        question = quiz.get_question(index)
        print()
        print(bold + question.question + end)
        print()
        for i, answer in enumerate(question.answers):
            print(f"{bold}  {i}:{end} {answer.answer}")
        print()
        answer = int(input("Answer: "))
        quiz.answer_question(question, question.answers[answer])

    def review_quiz(quiz: Quiz):
        result = quiz.grade()
        print(f"Score: {result}/{len(quiz.questions)}\n")
        for question in quiz.questions:
            answer_id = quiz.user_answers[question.uuid]
            answer = [a for a in question.answers if a.uuid == answer_id][0]
            correct_answer = [a for a in question.answers if a.uuid == question.correct][0]
            is_correct = answer == correct_answer
            answer_color = green if is_correct else red
            print(bold + question.question + end)
            print(bold + f"Correct answer: {correct_answer.answer}" + end)
            print(answer_color + bold + f"Your answer: {answer.answer}" + end)
            print(f"Explanation: {question.explanation}")
            print()
        print(f"Score: {result}/{len(quiz.questions)}\n")

    for i in range(len(quiz.questions)):
        ask_question(quiz, i)

    print()
    print()
    
    review_quiz(quiz)