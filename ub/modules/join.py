from ub import clients, app

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import UserAlreadyParticipant, InviteRequestSent
import config 

@app.on_message(filters.command("join") & filters.user(config.SUDOERS))
async def joinchat(app, m: Message):
  k=0
  if len(m.command) < 2:
    return await m.reply("Give Chat Username or link")
  else:
    chat=m.text.split(" ", 1)[1]
  for client in clients:
    try:
      await client.join_chat(chat)
      k+=1
      await m.reply_text(f"{client.me.mention} joined")
    except UserAlreadyParticipant:
      await m.reply_text(f"{client.me.mention} is already participant")
      k+=1
    except InviteRequestSent:
      await m.reply_text(f"{client.me.mention} has sent request to join")
      k+=1
    except Exception as e:
      await m.reply_text(f"{e}")
      continue
  await m.reply_text(f"Done \n {k} account successfully joined")
