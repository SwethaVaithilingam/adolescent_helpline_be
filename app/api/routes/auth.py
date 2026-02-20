from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.auth_service import signup_user, login_user
from app.schemas.auth import SignupRequest, SignupResponse, LoginRequest, LoginResponse
from app.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/signup", response_model=SignupResponse)
def signup(data: SignupRequest, db: Session = Depends(get_db)):
    try:
        age = signup_user(data, db)   # pass db
        return {"message": "Signup successful", "age": age}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    valid = login_user(data.phone, data.password, db)
    if not valid:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token({"phone": data.phone})

    return {"message": "Login successful",
            "access_token": token,
            "token_type": "bearer"}
