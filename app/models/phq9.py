from sqlalchemy import Column, Integer, String, JSON, DateTime
from app.core.database import Base
from sqlalchemy.sql import func

class Phq9Result(Base):
    __tablename__ = "phq9_results"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String(15), index=True, nullable=False)
    answers = Column(JSON, nullable=False)
    total_score = Column(Integer, nullable=False)
    severity = Column(String(255), nullable=False)

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