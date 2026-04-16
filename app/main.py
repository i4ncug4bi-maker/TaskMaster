from dotenv import load_dotenv
load_dotenv()


from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routers.tasks import router as tasks_router
from app.routers.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TaskMaster API",
    version="0.3.0",
    description="Professional TaskMaster API (FastAPI + DB + Auth).",
)

app.include_router(tasks_router, prefix="/tasks")
app.include_router(auth_router, prefix="/auth")
