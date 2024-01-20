from ub import clients, app

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import UserAlreadyParticipant, InviteRequestSent
import config 

@app.on_message(filters.command("join") & filters.user(config.SUDOERS))
async def joinchat(app, m: Message):
  if len(m.command) < 2:
    return await msg.reply("Give Chat Username Without @")
  else:
    chat=m.text.split(" ", 1)[1]
  for client in clients:
    try:
      await client.join_chat(chat)
      await m.reply_text(f"{client.me.mention} joined @{chat}")
    except UserAlreadyParticipant:
      await m.reply_text(f"{client.me.mention} is already participant in @{chat}")
    except InviteRequestSent:
      await m.reply_text(f"{client.me.mention} has sent request to join @{chat}")
    except Exception as e:
      await m.reply_text(f"{e}")
      continue
  await m.reply_text("Done")
