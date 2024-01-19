import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


BOT_TOKEN = getenv("BOT_TOKEN", "")
SESSION1 = getenv("SESSION1", "")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
