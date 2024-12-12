from dataclasses import dataclass, field
from typing import List, Tuple, ClassVar
from uuid import uuid4, UUID

@dataclass(eq=True, frozen=True)
class AIQuestion:
    question: str
    answers: List[str]
    correct: int
    explanation: str


@dataclass(eq=True, frozen=True)
class AIResponse:
    topic: str
    questions: List[AIQuestion]


@dataclass(eq=True, frozen=True)
class Answer:
    answer: str
    uuid: UUID = field(default_factory= lambda: uuid4())


@dataclass(eq=True, frozen=True)
class Question:
    question: str
    answers: List[Answer]
    correct: UUID
    explanation: str
    uuid: UUID = field(default_factory= lambda: uuid4())


@dataclass(eq=True, frozen=True)
class QuizResult:
    @dataclass(eq=True, frozen=True)
    class Summary:
        correct: int
        total: int
    
    @dataclass(eq=True, frozen=True)
    class UserAnswer:
        question_id: UUID
        answer_id: UUID
        valid: bool
    
    summary: Summary
    questions: List[Question]
    user_answers: List[UserAnswer]

