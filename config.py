import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7575487741:AAGVL1WMiHr5j88NIPx2EQD4CBsTPzZHP3s")
API_ID = int(os.environ.get("API_ID", "28203009")) # Defaulting to "0" as int for safety if not set
API_HASH = os.environ.get("API_HASH", "c385478ec9a0c322964bdd56175cef7b")
ADMINS = int(os.environ.get("ADMINS", "6401029823")) # Defaulting to "0" as int for safety
DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002547260781") # Will be an empty string if not set
