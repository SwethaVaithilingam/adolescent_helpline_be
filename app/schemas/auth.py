from pydantic import BaseModel, validator, Field
from datetime import date
import re


# ---------- Signup ----------
class SignupRequest(BaseModel):
    full_name: str = Field(..., min_length=2, max_length=50)
    dob: date
    phone: str
    password: str = Field(..., min_length=6)
    student_class: str
    district: str = Field(..., min_length=2, max_length=50)

    # Validate Indian phone number
    @validator("phone")
    def validate_phone(cls, v):
        if not re.match(r'^[6-9]\d{9}$', v):
            raise ValueError("Invalid Indian phone number")
        return v

    # Validate name (alphabets and spaces only)
    @validator("full_name")
    def validate_name(cls, v):
        v = v.strip()
        if not re.match(r'^[A-Za-z ]+$', v):
            raise ValueError("Name must contain only alphabets and spaces")
        return v

    # Validate district (alphabets and spaces only)
    @validator("district")
    def validate_district(cls, v):
        v = v.strip()
        if not re.match(r'^[A-Za-z ]+$', v):
            raise ValueError("District must contain only alphabets and spaces")
        return v

    # Validate age (example: 10–19 years)
    @validator("dob")
    def validate_age(cls, v):
        today = date.today()
        age = today.year - v.year - (
            (today.month, today.day) < (v.month, v.day)
        )

        if age < 10 or age > 19:
            raise ValueError("Age must be between 10 and 19 years")
        return v


class SignupResponse(BaseModel):
    message: str

class SendOtpRequest(BaseModel):
    phone: str

    @validator("phone")
    def validate_phone(cls, v):
        if not re.match(r'^[6-9]\d{9}$', v):
            raise ValueError("Invalid Indian phone number")
        return v


class VerifyOtpRequest(BaseModel):
    phone: str
    otp: str

    @validator("phone")
    def validate_phone(cls, v):
        if not re.match(r'^[6-9]\d{9}$', v):
            raise ValueError("Invalid Indian phone number")
        return v
# ---------- Login ----------
class LoginRequest(BaseModel):
    phone: str
    password: str

    # Optional: Validate phone format in login too
    @validator("phone")
    def validate_phone(cls, v):
        if not re.match(r'^[6-9]\d{9}$', v):
            raise ValueError("Invalid Indian phone number")
        return v


class LoginResponse(BaseModel):
    message: str
    access_token: str
