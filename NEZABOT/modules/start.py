from .. import *


@CB.UBOT("ping", sudo=True)
@ubot.on_message(filters.user(USER_ID) & filters.command("cping", "") & ~filters.me)
async def _(client, message):
    await ping_cmd(client, message)


@CB.BOT("start")
async def _(client, message):
    await start_cmd(client, message)