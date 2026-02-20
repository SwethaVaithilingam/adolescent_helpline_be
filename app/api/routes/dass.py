from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.dass_service import store_dass21,calculate_dass21
from app.core.database import get_db
from app.schemas.dass import Dass21Request,Dass21Response
from app.api.dependencies.auth import get_current_phone
router = APIRouter(prefix="/dass")
@router.post("/submit", response_model=Dass21Response)
def submit_dass21(data: Dass21Request,db: Session = Depends(get_db),phone: str = Depends(get_current_phone)):
    results = calculate_dass21(data.answers)
    store_dass21(phone, data.answers, results, db)
    return results