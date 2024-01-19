from ub import clients, app

from pyrogram import filters
from pyrogram.types import Message
import config 

@app.on_message(filters.command("join") & filters.user(config.SUDOERS))
async def joinchat(app, m: Message):
  chat=m.text.split(" ", 1)[1]
  no=[]
  for client in clients:
    try:
      await client.join_chat(chat)
      await message.reply_text(f"{client.me.mention} joined @{chat}")
    except Exception as e:
      print(e)
      continue 
  await message.reply_text("Done")
