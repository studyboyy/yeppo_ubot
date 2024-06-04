import os

DEVS = [
    5089916692,
    1938616056,
]
API_ID = int(os.getenv("API_ID", "4848003"))

API_HASH = os.getenv("API_HASH", "24dd5f08012ca7461d14ce9741871afd")

BOT_TOKEN = os.getenv("BOT_TOKEN", "")

OWNER_ID = int(os.getenv("OWNER_ID", "1938616056"))

USER_ID = list(map(int,os.getenv("USER_ID", "5089916692 1938616056",).split(),))

LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-100"))

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1001854052937 -1001473548283").split()))

MAX_BOT = int(os.getenv("MAX_BOT", "100"))

COMMAND = os.getenv("COMMAND", ".")

OPENAI_KEY = os.getenv("OPENAI_KEY")

PREFIX = COMMAND.split()

MONGO_URL = os.getenv(
    "MONGO_URL",
    "",
)
