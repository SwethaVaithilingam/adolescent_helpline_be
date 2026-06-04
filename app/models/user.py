from sqlalchemy import Column, Integer, String, DateTime,Date
from app.core.database import Base
from sqlalchemy.sql import func


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100))
    dob = Column(Date)
    phone = Column(String(15), unique=True, index=True)
    password = Column(String(100))
    student_class = Column(String(20))
    school_name=Column(String(50))
    district = Column(String(50))
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),   # automatically set when record created
        nullable=False
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()          # automatically updated on edit
    )