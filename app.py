
from contextlib import asynccontextmanager

from fastapi import FastAPI
from pydantic import BaseModel, Field

from config import APP_NAME, APP_VERSION, AI_NAME
from database import initialize_database, get_profile


@asynccontextmanager
async def lifespan(app: FastAPI):
    initialize_database()
    print("JOSA database is ready.")
    yield


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    lifespan=lifespan
)


class ProfileRequest(BaseModel):
    display_name: str = Field(default="", max_length=100)
    ai_name: str = Field(default="JOSA", max_length=100)
    bio: str = Field(default="", max_length=2000)
    goals: str = Field(default="", max_length=4000)


@app.get("/")
async def home():
    return {
        "app": APP_NAME,
        "version": APP_VERSION,
        "ai_name": AI_NAME,
        "status": "online",
        "message": "Welcome to JOSA AI!"
    }


@app.get("/api/status")
async def status():
    return {
        "ai": AI_NAME,
        "status": "active",
        "backend": "FastAPI",
        "database": "connected"
    }


@app.get("/api/profile")
async def profile():
    return get_profile()


@app.get("/api/health")
async def health():
    return {
        "status": "healthy",
        "service": "JOSA AI Backend"
    }
    
