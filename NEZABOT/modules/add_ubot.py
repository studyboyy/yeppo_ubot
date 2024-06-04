from NEZABOT import *


@CB.CALLBACK("pler")
async def _(client, callback_query):
    await ohaja(client, callback_query)


@CB.CALLBACK("bahan")
async def _(client, callback_query):
    await need_api(client, callback_query)


@CB.CALLBACK("memek")
async def _(client, callback_query):
    await bikin_memek(client, callback_query)


@CB.CALLBACK("bahan")
async def _(client, callback_query):
    await need_api(client, callback_query)


@CB.CALLBACK("memek")
async def _(client, callback_query):
    await bikin_memek(client, callback_query)


@CB.CALLBACK("bahan")
async def _(client, callback_query):
    await need_api(client, callback_query)


@CB.CALLBACK("bayar_dulu")
async def _(client, callback_query):
    await payment_NEZABOT(client, callback_query)


@CB.CALLBACK("add_ubot")
async def _(client, callback_query):
    await bikin_ubot(client, callback_query)


@CB.CALLBACK("cek_ubot")
@CB.BOT("getubot")
async def _(client, message):
    if message.from_user.id == OWNER_ID:
        await cek_ubot(client, message)
    else:
        await message.reply("Maaf, hanya pemilik bot yang dapat mengakses ini.")


@CB.CALLBACK("^(get_otp|get_phone|get_faktor|ub_deak|deak_akun)")
async def _(client, callback_query):
    await tools_NEZABOT(client, callback_query)


@CB.CALLBACK("cek_masa_aktif")
async def _(client, callback_query):
    await cek_NEZABOT_expired(client, callback_query)


@CB.CALLBACK("del_ubot")
async def _(client, callback_query):
    await hapus_ubot(client, callback_query)

    
@CB.CALLBACK("^(prev_ub|next_ub)")
async def _(client, callback_query):
    await next_prev_ubot(client, callback_query)
