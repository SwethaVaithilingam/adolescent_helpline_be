from sqlalchemy.orm import Session
from app.models.questionnaire import Questionnaire

def store_questionnaire(phone: str, answers: list, db: Session):

    # Check if record already exists
    record = db.query(Questionnaire).filter(Questionnaire.phone == phone).first()

    # Prepare answer dictionary
    data = {}
    for i in range(38):
        data[f"q{i+1}"] = answers[i]

    if record:
        # UPDATE existing record
        for key, value in data.items():
            setattr(record, key, value)

    else:
        # INSERT new record
        record = Questionnaire(phone=phone, **data)
        db.add(record)

    db.commit()
    db.refresh(record)

    return True
