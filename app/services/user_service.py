from datetime import date
from sqlalchemy.orm import Session
from app.models.user import User


def calculate_age(dob: date) -> int:
    today = date.today()
    return today.year - dob.year - (
        (today.month, today.day) < (dob.month, dob.day)
    )


def update_user_profile(current_user: User, data, db: Session):

    current_user.full_name = data.name
    current_user.dob = data.dob
    current_user.student_class = data.student_class
    current_user.school_name=data.school_name
    current_user.district = data.district

    db.commit()
    db.refresh(current_user)

    # 🔥 dynamically calculate age
    age = calculate_age(current_user.dob)

    return current_user
