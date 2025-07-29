# config.py

import os
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = os.getenv("CITY", "Lecco")
UNITS = os.getenv("UNITS", "metric")  # fallback se non definito

EMAIL_CONFIG = {
    "sender": os.getenv("EMAIL_SENDER"),
    "recipient": os.getenv("EMAIL_RECIPIENT"),
    "smtp_server": os.getenv("EMAIL_SMTP_SERVER", "smtp.gmail.com"),
    "port": int(os.getenv("EMAIL_SMTP_PORT", 587)),
    "password": os.getenv("EMAIL_PASSWORD"),
}
