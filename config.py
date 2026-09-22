
import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = "JOSA AI"
APP_VERSION = "1.0.0"

AI_NAME = os.getenv("AI_NAME", "JOSA")

AI_PERSONALITY = os.getenv(
    "AI_PERSONALITY",
    "Friendly, respectful, helpful, and supportive."
)

DATABASE_PATH = os.getenv(
    "DATABASE_PATH",
    "josa.db"
)
