from typing import List
from model import Question, Answer, AIResponse

def pack(response: AIResponse) -> List[Question]:
    questions: List[Question] = []
    for question in response.questions:
        answers: List[Answer] = []
        for answer in question.answers:
            answers.append(Answer(answer))
        correct: Answer = answers[question.correct]
        questions.append(Question(question.question, answers, correct.uuid, question.explanation))
    return questions
