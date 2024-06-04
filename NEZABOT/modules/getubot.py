from NEZABOT import *


@CB.UBOT("getubot", sudo=False)
@CB.OWNER
async def _(client, message):
    await getubot_cmd(client, message)


@CB.INLINE("^ambil_ubot")
async def _(client, inline_query):
    await getubot_query(client, inline_query)
