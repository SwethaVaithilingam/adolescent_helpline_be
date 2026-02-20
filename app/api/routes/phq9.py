from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.phq9 import Phq9Request, Phq9Response
from app.services.phq9_service import calculate_phq9_score, store_phq9
from app.api.dependencies.auth import get_current_phone

router = APIRouter(
    prefix="/phq9",
    tags=["PHQ9"]
)


@router.post("/submit", response_model=Phq9Response)
def submit_phq9(data: Phq9Request, db: Session = Depends(get_db),phone: str = Depends(get_current_phone)):

    if len(data.answers) != 9:
        raise HTTPException(status_code=400, detail="PHQ-9 requires exactly 9 answers")

    result = calculate_phq9_score(data.answers)

    store_phq9(phone, data.answers, result, db)

    return result
