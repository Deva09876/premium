from pyrogram.types import Message
from ub import app

@app.on_message(filters.command("start"))
async def start(app, m: Message):
  await m.reply_text("I'm Alive")
