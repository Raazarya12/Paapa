from info import DATABASE_URI

# Bot information
SESSION = 'Media_search'
USER_SESSION = 'User_Bot'
API_ID = 20932503
API_HASH = '4742289cfae50c92d8de04b4daae2c64'
BOT_TOKEN = '7826147450:AAGY3iRWqNf3D_ZRfbJocQhJDo9Tk1T5eWc'
USERBOT_STRING_SESSION = ''

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False

# Admins, Channels & Users
ADMINS = [6655462760]
CHANNELS = [-1002342348023]
AUTH_USERS = []
AUTH_CHANNEL = None

# MongoDB information
DATABASE_NAME = 'Telegram'
COLLECTION_NAME = 'channel_files'  # If you are using the same database, then use different collection name for each bot

#temp dict for storing the db uri which will be used for storing user, chat and file infos
tempDict = {'indexDB': DATABASE_URI}
