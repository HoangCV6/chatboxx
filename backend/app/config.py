import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DB_URL")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")