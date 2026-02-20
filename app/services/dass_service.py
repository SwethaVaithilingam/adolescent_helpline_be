from sqlalchemy.orm import Session
from app.models.dass import Dass21Result


def store_dass21(phone: str, answers: list, results: dict, db: Session):

    existing_record = (
        db.query(Dass21Result)
        .filter(Dass21Result.phone == phone)
        .first()
    )

    if existing_record:
        # UPDATE existing record
        existing_record.answers = answers
        existing_record.depression_score = results["depression"]["score"]
        existing_record.depression_level = results["depression"]["level"]
        existing_record.anxiety_score = results["anxiety"]["score"]
        existing_record.anxiety_level = results["anxiety"]["level"]
        existing_record.stress_score = results["stress"]["score"]
        existing_record.stress_level = results["stress"]["level"]

        # updated_at will auto-update because of onupdate=func.now()

        db.commit()
        db.refresh(existing_record)
        return existing_record

    else:
        # CREATE new record
        record = Dass21Result(
            phone=phone,
            answers=answers,
            depression_score=results["depression"]["score"],
            depression_level=results["depression"]["level"],
            anxiety_score=results["anxiety"]["score"],
            anxiety_level=results["anxiety"]["level"],
            stress_score=results["stress"]["score"],
            stress_level=results["stress"]["level"],
        )

        db.add(record)
        db.commit()
        db.refresh(record)
        return record

def calculate_dass21(answers: list):
    depression_idx = [2,4,9,12,15,16,20]
    anxiety_idx = [1,3,6,8,14,18,19]
    stress_idx = [0,5,7,10,11,13,17]

    def total(indexes):
        return sum(answers[i] for i in indexes) * 2

    depression_score = total(depression_idx)
    anxiety_score = total(anxiety_idx)
    stress_score = total(stress_idx)

    def level(score, ranges):
        for limit, label in ranges:
            if score <= limit:
                return label

    depression_level = level(depression_score, [
        (9, "Normal"), (13, "Mild"), (20, "Moderate"),
        (27, "Severe"), (100, "Extremely Severe")
    ])

    anxiety_level = level(anxiety_score, [
        (7, "Normal"), (9, "Mild"), (14, "Moderate"),
        (19, "Severe"), (100, "Extremely Severe")
    ])

    stress_level = level(stress_score, [
        (14, "Normal"), (18, "Mild"), (25, "Moderate"),
        (33, "Severe"), (100, "Extremely Severe")
    ])

    return {
        "depression": {"score": depression_score, "level": depression_level},
        "anxiety": {"score": anxiety_score, "level": anxiety_level},
        "stress": {"score": stress_score, "level": stress_level},
    }
