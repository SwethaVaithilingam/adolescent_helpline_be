from sqlalchemy import Column, Integer, String, DateTime
from app.core.database import Base
from datetime import datetime
from sqlalchemy.sql import func

class Questionnaire(Base):
    __tablename__ = "questionnaire"

    id = Column(Integer, primary_key=True, index=True)
    phone = Column(String(15), index=True)

    q1 = Column(String(255))
    q2 = Column(String(255))
    q3 = Column(String(255))
    q4 = Column(String(255))
    q5 = Column(String(255))
    q6 = Column(String(255))
    q7 = Column(String(255))
    q8 = Column(String(255))
    q9 = Column(String(255))
    q10 = Column(String(255))
    q11 = Column(String(255))
    q12 = Column(String(255))
    q13 = Column(String(255))
    q14 = Column(String(255))
    q15 = Column(String(255))
    q16 = Column(String(255))
    q17 = Column(String(255))
    q18 = Column(String(255))
    q19 = Column(String(255))
    q20 = Column(String(255))
    q21 = Column(String(255))
    q22 = Column(String(255))
    q23 = Column(String(255))
    q24 = Column(String(255))
    q25 = Column(String(255))
    q26 = Column(String(255))
    q27 = Column(String(255))
    q28 = Column(String(255))
    q29 = Column(String(255))
    q30 = Column(String(255))
    q31 = Column(String(255))
    q32 = Column(String(255))
    q33 = Column(String(255))
    q34 = Column(String(255))
    q35 = Column(String(255))
    q36 = Column(String(255))
    q37 = Column(String(255))
    q38 = Column(String(255))


created_at = Column(
    DateTime,
    default=datetime.utcnow,
    nullable=False
)

updated_at = Column(
    DateTime,
    default=datetime.utcnow,
    onupdate=datetime.utcnow,
    nullable=False
)