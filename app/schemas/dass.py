from pydantic import BaseModel, conint, conlist

AnswerType = conint(ge=0, le=3)

class Dass21Request(BaseModel):
    answers: conlist(AnswerType, min_length=21, max_length=21)


class Dass21Score(BaseModel):
    score: int
    level: str


class Dass21Response(BaseModel):
    depression: Dass21Score
    anxiety: Dass21Score
    stress: Dass21Score
