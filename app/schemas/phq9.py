from pydantic import BaseModel, conint, conlist

from typing import List
AnswerType = conint(ge=0, le=3)
class Phq9Request(BaseModel):
    answers: conlist(AnswerType, min_length=9, max_length=9)


class Phq9Response(BaseModel):
    total_score: int
    severity: str

class Config:
    from_attributes = True
