from datetime import date
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.auth import SignupRequest
from passlib.context import CryptContext

# otp_store = {}

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def calculate_age(dob: date) -> int:
    today = date.today()
    return today.year - dob.year - (
        (today.month, today.day) < (dob.month, dob.day)
    )

# def generate_otp():
#     return str(random.randint(100000, 999999))


# def save_otp(phone: str, otp: str):
#     otp_store[phone] = otp


# def verify_saved_otp(phone: str, otp: str):
#     saved = otp_store.get(phone)

#     if saved is None:
#         return False
#     if saved != otp:
#         return False
#     del otp_store[phone]
#     return True

def signup_user(data: SignupRequest, db: Session):

    existing = db.query(User).filter(User.phone == data.phone).first()
    if existing:
        raise ValueError("User already exists")

    age = calculate_age(data.dob)

    hashed_password = pwd_context.hash(data.password)

    new_user = User(
        full_name=data.full_name,
        dob=data.dob,
        phone=data.phone,
        password=hashed_password,
        student_class=data.student_class,
        school_name=data.school_name,
        district=data.district
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return age


def login_user(phone: str, password: str, db: Session):
    user = db.query(User).filter(User.phone == phone).first()

    if not user:
        return False

    if not pwd_context.verify(password, user.password):
        return False

    return True
