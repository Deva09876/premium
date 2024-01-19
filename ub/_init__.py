from pyrogram import Client
from config import SUDO_USERS, OWNER_ID, BOT_TOKEN, SESSION1, SESSION2, SESSION3, SESSION4, SESSION5, SESSION6, SESSION7, SESSION8, SESSION9, SESSION10, SESSION11, SESSION12, SESSION13, SESSION14, SESSION15, SESSION16, SESSION17, SESSION18, SESSION19, SESSION20 
from datetime import datetime
import time
from aiohttp import ClientSession

StartTime = time.time()
START_TIME = datetime.now()
CMD_HELP = {}
SUDO_USER = SUDO_USERS
clients = []
ids = []

SUDO_USERS.append(OWNER_ID)
aiosession = ClientSession()

API_ID = "6435225"
API_HASH = "4e984ea35f854762dcde906dce426c2d"

if not BOT_TOKEN:
   print("WARNING: BOT TOKEN NOT FOUND PLZ ADD ⚡")   

app = Client(
    name="app",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True,
)

if SESSION1:
   print("Client1: Found.. Starting..📳")
   client1 = Client(name="one", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION1, plugins=dict(root="Zaid/modules"))
   clients.append(client1)

if SESSION2:
   print("Client2: Found.. Starting.. 📳")
   client2 = Client(name="two", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION2, plugins=dict(root="Zaid/modules"))
   clients.append(client2)

if SESSION3:
   print("Client3: Found.. Starting.. 📳")
   client3 = Client(name="three", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION3, plugins=dict(root="Zaid/modules"))
   clients.append(client3)

if SESSION4:
   print("Client4: Found.. Starting.. 📳")
   client4 = Client(name="four", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION4, plugins=dict(root="Zaid/modules"))
   clients.append(client4)

if SESSION5:
   print("Client5: Found.. Starting.. 📳")
   client5 = Client(name="five", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION5, plugins=dict(root="Zaid/modules"))
   clients.append(client5)

if SESSION6:
   print("Client6: Found.. Starting.. 📳")
   client6 = Client(name="six", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION6, plugins=dict(root="Zaid/modules"))
   clients.append(client6)

if SESSION7:
   print("Client7: Found.. Starting.. 📳")
   client7 = Client(name="seven", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION7, plugins=dict(root="Zaid/modules"))
   clients.append(client7)

if SESSION8:
   print("Client8: Found.. Starting.. 📳")
   client8 = Client(name="eight", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION8, plugins=dict(root="Zaid/modules"))
   clients.append(client8)

if SESSION9:
   print("Client9: Found.. Starting.. 📳")
   client9 = Client(name="nine", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION9, plugins=dict(root="Zaid/modules"))
   clients.append(client9)

if SESSION10:
   print("Client10: Found.. Starting.. 📳")
   client10 = Client(name="ten", api_id=API_ID, api_hash=API_HASH, session_string=STRING_SESSION10, plugins=dict(root="Zaid/modules")) 
   clients.append(client10)
