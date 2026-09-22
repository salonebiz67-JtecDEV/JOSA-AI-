
from fastapi import FastAPI
from config import APP_NAME, APP_VERSION, AI_NAME

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)


@app.get("/")
def home():
    return {
        "app": APP_NAME,
        "version": APP_VERSION,
        "ai_name": AI_NAME,
        "status": "online",
        "message": "Welcome to JOSA AI!"
    }


@app.get("/api/status")
def status():
    return {
        "ai": AI_NAME,
        "status": "active",
        "backend": "FastAPI"
    }
  
