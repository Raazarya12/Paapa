from info import DATABASE_URI

# Bot information
SESSION = 'Media_search'
USER_SESSION = 'User_Bot'
API_ID = 29127726
API_HASH = 'b25483bdec0d64a73899ee8ede66cd40'
BOT_TOKEN = '6949780397:AAFcrsLdqgqShfIyYvHY8Du01TIEPQfEmHs'
USERBOT_STRING_SESSION = ''

# Bot settings
CACHE_TIME = 300
USE_CAPTION_FILTER = False

# Admins, Channels & Users
ADMINS = [1985196029]
CHANNELS = [-1001430858047]
AUTH_USERS = []
AUTH_CHANNEL = None

# MongoDB information
DATABASE_NAME = 'Telegram'
COLLECTION_NAME = 'channel_files'  # If you are using the same database, then use different collection name for each bot

#temp dict for storing the db uri which will be used for storing user, chat and file infos
tempDict = {'indexDB': DATABASE_URI}
