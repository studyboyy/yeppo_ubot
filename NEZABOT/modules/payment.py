from NEZABOT import *


@CB.CALLBACK("^confirm")
async def _(client, callback_query):
    await confirm_callback(client, callback_query)


@CB.CALLBACK("^(kurang|tambah)")
async def _(client, callback_query):
    await tambah_or_kurang(client, callback_query)


@CB.CALLBACK("^(success|failed|home)")
async def _(client, callback_query):
    await success_failed_home_callback(client, callback_query)
