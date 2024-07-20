import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
TELEGRAM_API_KEY = os.getenv('TELEGRAM_API_KEY')
RADIUS = os.getenv('RADIUS')
