from NEZABOT import *


@CB.BOT("login", FILTERS.OWNER)
@CB.UBOT("login", sudo=False)
@CB.OWNER
async def _(client, message):
    await login_cmd(client, message)   
    
@CB.BOT("restart")
async def _(client, message):
    await restart_cmd(client, message)
