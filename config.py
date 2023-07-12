import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), ".env")

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class ApiTelegram:
    API_ID = int(os.environ["API_ID"])
    API_HASH = os.environ["API_HASH"]


class SettingsBot:
    BOT_TOKEN = os.environ["BOT_TOKEN"]
    DATABASE = os.environ["DATABASE"]


class InfoID:
    ADMIN_ID = int(os.environ["ADMIN_ID"])




