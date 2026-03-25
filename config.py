import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Base paths
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"

# SMTP Configuration
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")

if not SENDER_EMAIL or not SENDER_PASSWORD:
    # We don't raise an error immediately on import to allow dry-runs/testing without credentials
    print("WARNING: SENDER_EMAIL or SENDER_PASSWORD environment variables are not set.")

# App Configuration
DELAY_BETWEEN_EMAILS_SECONDS = int(os.getenv("DELAY_BETWEEN_EMAILS_SECONDS", 5))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", 3))

# File Paths
INPUT_EXCEL_PATH = os.getenv("INPUT_EXCEL_PATH", str(DATA_DIR / "input_emails.xlsx"))
OUTPUT_EXCEL_PATH = os.getenv("OUTPUT_EXCEL_PATH", str(DATA_DIR / "log.xlsx"))
