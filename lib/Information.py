from .library import *

admin_user_id = 1868180475 #<--- آیدی ادمین
api_id = 11795206 #<--- آی پی آی آیدی
api_hash = '53768e7ecd4406e4d88464d71a30165a' #<--- ای پی آی هش
helper_username = 'sohancoin_bot' #<--- یوزر ربات هلپر بدون @
bot_token = '7723117220:AAHD5dmGJvY9NMKZ8xyVWqk-eJHGTFJsu4A' #<--- توکن ربات هلپر

client_id = '01e7dc6b41c3471b94efe87abeb05919'
client_secret = '4f5f93af1ced4b0d9ba8440606803639'

client = TelegramClient('TRself-MT', api_id, api_hash)
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
