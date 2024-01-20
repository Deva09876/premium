from pyrogram import filters
from pyrogram.types import Message
from ub import app, clients

@app.on_message(filters.command("start"))
async def start(app, m: Message):
  await m.reply_text("I'm Alive\n\n")
  for client in clients:
    await m.reply_text(f"{client.me.mention} is alive")
