from pydantic import BaseModel
from datetime import date
from typing import Optional

class UpdateProfileRequest(BaseModel):
    name: Optional[str] = None
    dob: Optional[date] = None
    student_class: Optional[str] = None
    school_name:Optional[str]=None
    district: Optional[str] = None

class ProfileResponse(BaseModel):
    name: str
    dob: date
    phone: str
    age: int
    student_class: str
    school_name:str
    district: str
