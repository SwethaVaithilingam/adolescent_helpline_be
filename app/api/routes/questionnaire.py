from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas.questionnaire import (
    QuestionnaireRequest,
    QuestionnaireResponse
)
from app.services.store_questionnaire import store_questionnaire
from app.core.database import get_db
from app.api.dependencies.auth import get_current_phone
router = APIRouter(prefix="/questionnaire", tags=["Questionnaire"])


@router.post("/submit", response_model=QuestionnaireResponse)
def submit_questionnaire(data: QuestionnaireRequest, db: Session = Depends(get_db), phone: str = Depends(get_current_phone)):
    
    
    store_questionnaire(phone, data.answers, db)

    return {
        "message": "Questionnaire stored successfully",
        "stored": True
    }
