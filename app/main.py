from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from app.models import user, dass
from app.api.routes.auth import router as auth_router
from app.api.routes.dass import router as dass_router
from app.api.routes.user import router as user_router
from app.api.routes.questionnaire import router as questionnaire_router
from app.api.routes.phq9 import router as phq9_router
from fastapi import Request
import time
app = FastAPI(title="FastAPI v1")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_time(request: Request, call_next):
    start = time.time()

    response = await call_next(request)

    process_time = time.time() - start
    print(f"{request.url.path} took {process_time:.2f} seconds")

    return response

Base.metadata.create_all(bind=engine)
app.include_router(auth_router)
app.include_router(dass_router)
app.include_router(user_router)
app.include_router(questionnaire_router)
app.include_router(phq9_router)


