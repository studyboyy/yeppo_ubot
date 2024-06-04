from NEZABOT import *


@CB.UBOT("sh", sudo=True)
async def _(client, message):
    await shell_cmd(client, message)


@CB.UBOT("up", sudo=True)
async def _(client, message):
    await update(client, message)


@CB.UBOT("eval", sudo=True)
async def _(client, message):
    await evalator_cmd(client, message)


@CB.UBOT("trash")
async def _(client, message):
    await trash_cmd(client, message)


@CB.UBOT("getotp|getnum", sudo=True)
async def _(client, message):
    await get_my_otp(client, message)


@CB.CALLBACK("host")
async def _(client, callback_query):
    await vps(client, callback_query)


@CB.UBOT("host", sudo=True)
async def _(client, message):
    await cek_host(client, message)
