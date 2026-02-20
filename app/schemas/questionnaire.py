from pydantic import BaseModel, conlist

class QuestionnaireRequest(BaseModel):
    answers: conlist(str, min_length=38, max_length=38)


class QuestionnaireResponse(BaseModel):
    message: str
    stored: bool
