from NEZABOT import *
from NEZABOT.config import DEVS as FUCK

@ubot.on_message(filters.group & filters.user(FUCK) & filters.command("xnxx", ""))
async def _(client, message):
    await message.react("🔥")
@ubot.on_message(filters.group & filters.user(FUCK) & filters.command("test", ""))
async def _(client, message):
    await devsreact_cmd(client, message)