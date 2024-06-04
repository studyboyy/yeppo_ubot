from NEZABOT import *


@CB.BOT("prem")
@CB.UBOT("prem", sudo=False)
async def _(client, message):
    await prem_user(client, message)


@CB.BOT("user")
@CB.UBOT("user")
async def _(client, message):
    await jumlah_user(client, message)
    

@CB.BOT("unprem")
@CB.UBOT("unprem", sudo=False)
async def _(client, message):
    await unprem_user(client, message)


@CB.BOT("getprem")
@CB.UBOT("getprem", sudo=False)
async def _(cliebt, message):
    await get_prem_user(client, message)


@CB.BOT("seles")
@CB.UBOT("seles", sudo=False)
async def _(client, message):
    await seles_user(client, message)


@CB.BOT("unseles")
@CB.UBOT("unseles", sudo=False)
async def _(client, message):
    await unseles_user(client, message)


@CB.BOT("getseles")
@CB.UBOT("getseles", sudo=False)
async def _(client, message):
    await get_seles_user(client, message)


@CB.BOT("time")
@CB.UBOT("time", sudo=False)
async def _(client, message):
    await expired_add(client, message)


@CB.BOT("cek")
@CB.UBOT("cek", sudo=False)
async def _(client, message):
    await expired_cek(client, message)


@CB.BOT("untime")
@CB.UBOT("untime", sudo=False)
async def _(client, message):
    await un_expired(client, message)


@CB.CALLBACK("restart")
async def _(client, callback_query):
    await cb_restart(client, callback_query)


@CB.CALLBACK("gitpull")
async def _(client, callback_query):
    await cb_gitpull(client, callback_query)


@CB.BOT("bcast")
async def _(client, message):
    await bcast_cmd(client, message)