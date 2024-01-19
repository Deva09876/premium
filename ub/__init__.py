from pyrogram import Client
from pyrogram.errors import FloodWait
from config import BOT_TOKEN, SESSION1, SESSION2, SESSION3, SESSION4, SESSION5, SESSION6, SESSION7, SESSION8, SESSION9, SESSION10, SESSION11, SESSION12, SESSION13, SESSION14, SESSION15, SESSION16, SESSION17, SESSION18, SESSION19, SESSION20 
from datetime import datetime
import time, asyncio
from aiohttp import ClientSession

StartTime = time.time()
START_TIME = datetime.now()


clients = []

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
   client1 = Client(name="one", api_id=API_ID, api_hash=API_HASH, session_string=SESSION1)
   clients.append(client1)

if SESSION2:
   print("Client2: Found.. Starting.. 📳")
   client2 = Client(name="two", api_id=API_ID, api_hash=API_HASH, session_string=SESSION2)
   clients.append(client2)

if SESSION3:
   print("Client3: Found.. Starting.. 📳")
   client3 = Client(name="three", api_id=API_ID, api_hash=API_HASH, session_string=SESSION3)
   clients.append(client3)

if SESSION4:
   print("Client4: Found.. Starting.. 📳")
   client4 = Client(name="four", api_id=API_ID, api_hash=API_HASH, session_string=SESSION4)
   clients.append(client4)

if SESSION5:
   print("Client5: Found.. Starting.. 📳")
   client5 = Client(name="five", api_id=API_ID, api_hash=API_HASH, session_string=SESSION5)
   clients.append(client5)

if SESSION6:
   print("Client6: Found.. Starting.. 📳")
   client6 = Client(name="six", api_id=API_ID, api_hash=API_HASH, session_string=SESSION6)
   clients.append(client6)

if SESSION7:
   print("Client7: Found.. Starting.. 📳")
   client7 = Client(name="seven", api_id=API_ID, api_hash=API_HASH, session_string=SESSION7)
   clients.append(client7)

if SESSION8:
   print("Client8: Found.. Starting.. 📳")
   client8 = Client(name="eight", api_id=API_ID, api_hash=API_HASH, session_string=SESSION8)
   clients.append(client8)

if SESSION9:
   print("Client9: Found.. Starting.. 📳")
   client9 = Client(name="nine", api_id=API_ID, api_hash=API_HASH, session_string=SESSION9)
   clients.append(client9)

if SESSION10:
   print("Client10: Found.. Starting.. 📳")
   client10 = Client(name="ten", api_id=API_ID, api_hash=API_HASH, session_string=SESSION10) 
   clients.append(client10)

if SESSION11:
   print("Client11: Found.. Starting.. 📳")
   client11 = Client(name="eleven", api_id=API_ID, api_hash=API_HASH, session_string=SESSION11) 
   clients.append(client11)

if SESSION12:
   print("Client12: Found.. Starting.. 📳")
   client12 = Client(name="twelve", api_id=API_ID, api_hash=API_HASH, session_string=SESSION12)
   clients.append(client12)

if SESSION13:
   print("Client13: Found.. Starting.. 📳")
   client13 = Client(name="thirteenth", api_id=API_ID, api_hash=API_HASH, session_string=SESSION13)
   clients.append(client13)

if SESSION14:
   print("Client14: Found.. Starting.. 📳")
   client14 = Client(name="fourteen", api_id=API_ID, api_hash=API_HASH, session_string=SESSION14)
   clients.append(client14)

if SESSION15:
   print("Client15: Found.. Starting.. 📳")
   client15 = Client(name="fifteen", api_id=API_ID, api_hash=API_HASH, session_string=SESSION15)
   clients.append(client15)

if SESSION16:
   print("Client16: Found.. Starting.. 📳")
   client16 = Client(name="sixteen", api_id=API_ID, api_hash=API_HASH, session_string=SESSION16)
   clients.append(client16)

if SESSION17:
   print("Client17: Found.. Starting.. 📳")
   client17 = Client(name="seventeen", api_id=API_ID, api_hash=API_HASH, session_string=SESSION17)
   clients.append(client17)

if SESSION18:
   print("Client18: Found.. Starting.. 📳")
   client18 = Client(name="eighteen", api_id=API_ID, api_hash=API_HASH, session_string=SESSION18)
   clients.append(client18)

if SESSION19:
   print("Client19: Found.. Starting.. 📳")
   client19 = Client(name="nineteen", api_id=API_ID, api_hash=API_HASH, session_string=SESSION19)
   clients.append(client19)

if SESSION20:
   print("Client20: Found.. Starting.. 📳")
   client20 = Client(name="twenty", api_id=API_ID, api_hash=API_HASH, session_string=SESSION20) 
   clients.append(client20)


async def premium_bot():
    try:
        await app.start()
        print(f"Bot Started As {app.me.first_name}")
    except FloodWait as ex:
        print(e)
        await asyncio.sleep(ex.value)
    for client in clients:
       try:
          await client.start()
          print(f"Client started as {client.me.first_name}")
       except Exception as e:
          print(e)


asyncio.get_event_loop().run_until_complete(premium_bot())
