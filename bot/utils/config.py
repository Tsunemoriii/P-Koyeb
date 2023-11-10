import os


API_HASH = os.environ.get("API_HASH", "fc1bce8441f3c90b719bc86098137a3d")
API_ID = int(os.environ.get("API_ID", 25697264))
AUTH_USERS = list(filter(lambda x: x, map(int, os.environ.get("AUTH_USERS", "5672065955 1432756163 682111519 1446111611").split())))
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://SonicOtakus:otakusonic@cluster0.lfpjg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001191707498))


# Bot tokens
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6054245957:AAHPD4Rrlt05HpdMEQnRVSjx6AIgJJ35oDE")
BOT_TOKEN_2 = os.getenv("BOT_TOKEN_2", "6051155351:AAFTIzVQEytmfPAFZX7OCH60hkP3hCmoQE4")
BOT_TOKEN_3 = os.getenv("BOT_TOKEN_3", "6086088634:AAH-OOsdwcbDJ4dFC5B1NsskaR7uCCoLyPc")
BOT_TOKEN_4 = os.getenv("BOT_TOKEN_4", "6225070483:AAE6dKan-ump5yNVhXbva1OkAJ0UQNXbu7I")
BOT_TOKEN_5 = os.getenv("BOT_TOKEN_5", "5990317516:AAEg4lkBRp1WgqWT8b3U6pG1QKTUIas15DQ")

# channel usernames for force subscribe (without @)
MAIN_CHANNEL = os.environ.get("MAIN_CHANNEL", "Hanimes_Otaku")
MAIN_CHANNEL_2 = os.getenv("MAIN_CHANNEL_2", "Hanimes_Otaku")
MAIN_CHANNEL_3 = os.getenv("MAIN_CHANNEL_3", "Hanimes_Otaku")
MAIN_CHANNEL_4 = os.getenv("MAIN_CHANNEL_4","Channel_No_Four")
MAIN_CHANNEL_5 = os.getenv("MAIN_CHANNEL_5", "Channel_No_Five")

# shortener api keys
SHORTENER_API = os.environ.get("SHORTENER_API", "dcddbca543e209dd3f79cfbae6b1dd52cb3ec595")
SHORTENER_API_2 = os.environ.get("SHORTENER_API_2", "dcddbca543e209dd3f79cfbae6b1dd52cb3ec595")
SHORTENER_API_3 = os.environ.get("SHORTENER_API_3", "dcddbca543e209dd3f79cfbae6b1dd52cb3ec595")
SHORTENER_API_4 = os.environ.get("SHORTENER_API_4", "dcddbca543e209dd3f79cfbae6b1dd52cb3ec595")
SHORTENER_API_5 = os.environ.get("SHORTENER_API_5", "23eb5dd17ac140282cad623f70635f2ba0820f4d")

# shortener api urls
SHORTENER_WEB = os.environ.get("SHORTENER_WEB", "https://moneykamalo.com/api?api={0}&url={1}")
SHORTENER_WEB_2 = os.environ.get("SHORTENER_WEB_2", "https://moneykamalo.com/api?api={0}&url={1}")
SHORTENER_WEB_3 = os.environ.get("SHORTENER_WEB_3", "https://moneykamalo.com/api?api={0}&url={1}")
SHORTENER_WEB_4 = os.environ.get("SHORTENER_WEB_4", "https://moneykamalo.com/api?api={0}&url={1}")
SHORTENER_WEB_5 = os.environ.get("SHORTENER_WEB_5", "https://paisakamalo.in/api?api={0}&url={1}")

# double short url and api
DOUBLE_SHORT = True    # write False to turn off
DOUBLE_SHORT_WEB = os.environ.get("DOUBLE_SHORT_WEB", "https://onepagelink.in/api?api={0}&url={1}")
DOUBLE_SHORT_API = os.environ.get("DOUBLE_SHORT_API", "c75a81ba04af2e8f1bb88ffbb70085305d19f618")

# original link
ORIGINAL_LINK = False    # write True to send original link

# Fill bot token, main channel, shortener api, shortener web accordingly.
# bot token 1 will only work with main channel 1 and shortener api 1
# and shortener web 1 will work with shortener api 1 only.
# and so on.
