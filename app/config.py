import os
from dotenv import load_dotenv

load_dotenv()

# App settings
APP_ENV = os.getenv("APP_ENV", "development")
APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
APP_PORT = int(os.getenv("APP_PORT", 8000))

# DEBUG should be a boolean
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

# Or set DEBUG based on APP_ENV
# DEBUG = APP_ENV == "development"

# Database settings
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./app.db")