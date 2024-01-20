from ub import app
from pyrogram import filters, Client
import os
import re
import asyncio
import time
import config 
from pyrogram.types import Message

@app.on_message(filters.user(config.SUDOERS) & filters.command("clone"))
async def clone(app, msg: Message):
  session=message.text.split(" ", 1)[1]
  try:
    await msg.reply_text("Booting Your Client")
    client = Client(name="Clone", api_id=API_ID, api_hash=API_HASH, session_string=phone, plugins=dict(root="ub/modules"))
    await client.start()
    await msg.reply(f"Your Client Has Been Successfully As {client.me.first_name} ✅.")
  except Exception as e:
    await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
