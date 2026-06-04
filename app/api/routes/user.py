from fastapi import APIRouter, Depends
from app.schemas.user import ProfileResponse, UpdateProfileRequest
from app.api.dependencies.user_profile import get_current_user
from app.models.user import User
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.auth_service import calculate_age

from app.services.user_service import update_user_profile
router = APIRouter(prefix="/user", tags=["User"])


@router.get("/profile", response_model=ProfileResponse)
def get_profile(current_user: User = Depends(get_current_user)):
    age =calculate_age(current_user.dob)
    return {
        "name": current_user.full_name,
        "dob": current_user.dob,
        "phone": current_user.phone,
        "age": age,
        "student_class": current_user.student_class,
        "school_name":current_user.school_name,
        "district": current_user.district,
    }

@router.put("/profile", response_model=ProfileResponse)
def edit_profile(
    data: UpdateProfileRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated_user = update_user_profile(current_user, data, db)

    age = calculate_age(updated_user.dob)

    return {
        "name": updated_user.full_name,
        "dob": updated_user.dob,
        "phone": updated_user.phone,
        "age": age,
        "student_class": updated_user.student_class,
        "school_name":updated_user.school_name,
        "district": updated_user.district,
    }
