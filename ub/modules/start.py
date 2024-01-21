from pyrogram import filters
from pyrogram.types import Message
from ub import app, clients

@app.on_message(filters.command("start"))
async def start(app, m: Message):
  k=0
  await m.reply_text("I'm Alive\n\n")
  for client in clients:
    k+=1
  await m.reply(f"Out Of {len(clients)} Clients, {k} Are Alive!")
