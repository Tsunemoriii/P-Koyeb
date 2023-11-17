import os


API_HASH = os.environ.get("API_HASH", "fc1bce8441f3c90b719bc86098137a3d")
API_ID = int(os.environ.get("API_ID", 25697264))
AUTH_USERS = list(filter(lambda x: x, map(int, os.environ.get("AUTH_USERS", "5672065955 1432756163 682111519 1446111611").split())))
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://SonicOtakus:otakusonic@cluster0.lfpjg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001191707498))


# Bot tokens
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6054245957:AAHPD4Rrlt05HpdMEQnRVSjx6AIgJJ35oDE")
BOT_TOKEN_2 = os.getenv("BOT_TOKEN_2", "6051155351:AAFTIzVQEytmfPAFZX7OCH60hkP3hCmoQE4")
BOT_TOKEN_3 = os.getenv("BOT_TOKEN_3", "6722197684:AAExVaNGi0MO1nzY9fi4Sv0nfNl9cpdPcYw")
BOT_TOKEN_4 = os.getenv("BOT_TOKEN_4", "6917972682:AAFZZx47GWw60zl1JzZ4ryfSWWHaKuKfIME")
BOT_TOKEN_5 = os.getenv("BOT_TOKEN_5", "6985172423:AAGpV8817eRrxDjF-NUGfuy3FUnoUWr49xU")

# channel usernames for force subscribe (without @)
MAIN_CHANNEL = os.environ.get("MAIN_CHANNEL", "Hanimes_Otaku")
MAIN_CHANNEL_2 = os.getenv("MAIN_CHANNEL_2", "Hanimes_Otaku")
MAIN_CHANNEL_3 = os.getenv("MAIN_CHANNEL_3", "One_Piece_Film_Z_Movie")
MAIN_CHANNEL_4 = os.getenv("MAIN_CHANNEL_4","One_Piece_Film_Gold_Movie")
MAIN_CHANNEL_5 = os.getenv("MAIN_CHANNEL_5", "Film_Gold_One_Piece")

# shortener api keys
SHORTENER_API = os.environ.get("SHORTENER_API", "60e33b784ffac4382a553666021940b5d777bcd2")
SHORTENER_API_2 = os.environ.get("SHORTENER_API_2", "60e33b784ffac4382a553666021940b5d777bcd2")
SHORTENER_API_3 = os.environ.get("SHORTENER_API_3", "60e33b784ffac4382a553666021940b5d777bcd2")
SHORTENER_API_4 = os.environ.get("SHORTENER_API_4", "60e33b784ffac4382a553666021940b5d777bcd2")
SHORTENER_API_5 = os.environ.get("SHORTENER_API_5", "60e33b784ffac4382a553666021940b5d777bcd2")

# shortener api urls
SHORTENER_WEB = os.environ.get("SHORTENER_WEB", "https://publicearn.com/api?api={0}&url={1}")
SHORTENER_WEB_2 = os.environ.get("SHORTENER_WEB_2", "https://publicearn.com/api?api={0}&url={1}")
SHORTENER_WEB_3 = os.environ.get("SHORTENER_WEB_3", "https://publicearn.com/api?api={0}&url={1}")
SHORTENER_WEB_4 = os.environ.get("SHORTENER_WEB_4", "https://publicearn.com/api?api={0}&url={1}")
SHORTENER_WEB_5 = os.environ.get("SHORTENER_WEB_5", "https://publicearn.com/api?api={0}&url={1}")

# double short url and api
DOUBLE_SHORT = True    # write False to turn off
DOUBLE_SHORT_WEB = os.environ.get("DOUBLE_SHORT_WEB", "https://link2paisa.com/api?api={0}&url={1}")
DOUBLE_SHORT_API = os.environ.get("DOUBLE_SHORT_API", "636de537452baa8a215b0813f3dfb1a30ef76278")

# original link
ORIGINAL_LINK = False    # write True to send original link

# Fill bot token, main channel, shortener api, shortener web accordingly.
# bot token 1 will only work with main channel 1 and shortener api 1
# and shortener web 1 will work with shortener api 1 only.
# and so on.
