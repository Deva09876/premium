import asyncio
import importlib
from pyrogram import Client, idle
from ub.modules import ALL_MODULES
from ub import clients, app, ids

async def start_bot():
    for all_module in ALL_MODULES:
        importlib.import_module(f"ub.modules.{all_module}")
    print(f"Successfully loaded {len(ALL_MODULES)}.")
    print("Bot Started")
    await idle()
    try:
        await app.stop()
    except:
        pass
    for client in clients:
        try:
            await client.stop()
        except:
            pass
    print("» Stopping Bot!   GoodBye")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(start_bot())
