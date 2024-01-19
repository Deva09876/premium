from ub import clients, app

from pyrogram import filters
from pyrogram.types import Message
import config 

@app.on_message(filters.command("join") & filters.user(config.SUDOERS))
async def joinchat(app, m: Message):
  
