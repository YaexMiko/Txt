import os
from os import environ

# Bot Configuration
API_ID = int(environ.get("API_ID", "28614709"))  # Replace with your API ID
API_HASH = environ.get("API_HASH", "f36fd2ee6e3d3a17c4d244ff6dc1bac8")  # Replace with your API Hash
BOT_TOKEN = environ.get("BOT_TOKEN", "8049166513:AAFmB5M8Qz6uboPYXPiS9PBX3FrQAZbjHA4")  # Replace with your Bot Token

# Owner Configuration
OWNER_ID = int(environ.get("OWNER_ID", "7970350353"))  # Replace with your Telegram User ID
OWNER_USERNAME = environ.get("OWNER_USERNAME", "@Yae_X_Miko")  # Your username

# Channel Configuration
CHANNEL_ID = environ.get("CHANNEL_ID", "-1002607772171")  # Your channel ID
LOG_CHANNEL = environ.get("LOG_CHANNEL", "-1002607772171")  # Log channel ID

# Bot Settings
BOT_NAME = environ.get("BOT_NAME", "TXT Extractor Bot")
BOT_USERNAME = environ.get("BOT_USERNAME", "@Hhhnybot")

# File Paths
COOKIES_FILE_PATH = environ.get("COOKIES_FILE_PATH", "youtube_cookies.txt")
DOWNLOAD_DIR = environ.get("DOWNLOAD_DIR", "./downloads/")

# Default Tokens (if needed)
DEFAULT_PW_TOKEN = ""

# Web Server Configuration (for deployment)
WEBHOOK = environ.get("WEBHOOK", False)
PORT = int(environ.get("PORT", 8080))
HOST_URL = environ.get("HOST_URL", "your_render_url") #If you are running in render

# Photo URLs
START_PHOTO = "https://telegra.ph/file/37985c408b1b7c817cbd6-4b850ca6f02b6eae30.jpg"
DEFAULT_THUMB = "https://i.postimg.cc/dVY9nL63/IMG-20250426-130510-655.jpg"

# Credit
DEVELOPER = "@Yae_X_Miko"

# Validation
if not API_ID or not API_HASH or not BOT_TOKEN:
    print("❌ Error: Please set API_ID, API_HASH, and BOT_TOKEN in environment variables or config.py")
    exit(1)

print("✅ Configuration loaded successfully!")
