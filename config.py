import os

from json_environ import Environ
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), ".env")



if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

json_env = Environ(path="./.env.json")


class ApiTelegram:
    API_ID = json_env("API_ID")
    API_HASH = json_env("API_HASH")


class SettingsBot:
    #   API ID/API HASH оставляю из файла .env, иначе для каждого профиля придётся создавать новового админ бота
    BOT_TOKEN = os.environ["BOT_TOKEN"]
    DATABASE = os.environ["DATABASE"]
    API_ID = os.environ["API_ID"]
    API_HASH = os.environ["API_HASH"]


class InfoID:
    NAME = os.environ["NAME"]
    ADMIN_ID = int(json_env("ADMIN_ID"))
    PHONE = json_env("PHONE")




