from sqlalchemy import Column, Integer, String, JSON, DateTime
from datetime import datetime
from app.core.database import Base
from sqlalchemy.sql import func

class Dass21Result(Base):
    __tablename__ = "dass21_results"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String(15), index=True)

    answers = Column(JSON)

    depression_score = Column(Integer)
    depression_level = Column(String(50))

    anxiety_score = Column(Integer)
    anxiety_level = Column(String(50))

    stress_score = Column(Integer)
    stress_level = Column(String(50))

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