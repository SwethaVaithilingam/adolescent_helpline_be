from fastapi import FastAPI
from app.core.database import Base, engine
from app.models import user, dass
from app.api.routes.auth import router as auth_router
from app.api.routes.dass import router as dass_router
from app.api.routes.user import router as user_router
from app.api.routes.questionnaire import router as questionnaire_router
from app.api.routes.phq9 import router as phq9_router

app = FastAPI(title="FastAPI v1")
Base.metadata.create_all(bind=engine)
app.include_router(auth_router)
app.include_router(dass_router)
app.include_router(user_router)
app.include_router(questionnaire_router)
app.include_router(phq9_router)


