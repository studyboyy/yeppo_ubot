from NEZABOT import *
from pyrogram.raw.functions.contacts import AddContact

@CB.UBOT("svkon", sudo=True)
async def _(client, message):
    jancok = message.reply_to_message
    if not jancok:
        return await message.reply_text("<emoji id=6113872536968104754>❎</emoji><b> mohon reply ke pengguna</b>")
    chat_id = await client.resolve_peer(peer_id=jancok.from_user.id)
    cx = await client.invoke(
        AddContact(
            id = chat_id,
            first_name = jancok.from_user.first_name,
            last_name = jancok.from_user.last_name or "",
            phone = "",
    ))
    hasil = cx.users[0].contact
    if hasil:
        await message.reply_text(f"<emoji id=5850633746583129853>✅</emoji> berhasil menyimpan contact dengan nama {jancok.from_user.first_name}")
    else:
        await message.reply_text("<emoji id=6113872536968104754>❎</emoji><b> terjadi kesalahan</b>")