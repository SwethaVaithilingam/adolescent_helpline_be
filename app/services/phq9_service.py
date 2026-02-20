from sqlalchemy.orm import Session
from app.models.phq9 import Phq9Result


def calculate_phq9_score(answers: list):
    total_score = sum(answers)

    if total_score <= 4:
        severity = "Minimal Depression"
    elif total_score <= 9:
        severity = "Mild Depression"
    elif total_score <= 14:
        severity = "Moderate Depression"
    elif total_score <= 19:
        severity = "Moderately Severe Depression"
    else:
        severity = "Severe Depression"

    return {
        "total_score": total_score,
        "severity": severity
    }


def store_phq9(phone: str, answers: list, result: dict, db: Session):
    record = Phq9Result(
        phone=phone,
        answers=answers,
        total_score=result["total_score"],
        severity=result["severity"]
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return record
