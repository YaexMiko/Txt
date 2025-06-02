# DON'T add anything here just add in render's secret or env section 
from os import environ
from config import API_ID, API_HASH, BOT_TOKEN
API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
