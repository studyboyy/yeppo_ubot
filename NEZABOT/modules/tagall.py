
__MODULE__ = "tagall"
__HELP__ = f"""
<b>『 bantuan untuk tagall 』</b>

  <b>• perintah:</b> <code>all</code> [pesan - rep_pesan]
  <b>• penjelasan:</b> untuk tagall kesemua member grup

  <b>• perintah:</b> <code>batal</code>
  <b>• penjelasan:</b> untuk menghentikan tagall
"""

import asyncio
from random import shuffle

from NEZABOT import *

tagallgcid = {}

@CB.UBOT("all", sudo=True)
async def tagall_cmd(client, message):
    msg = await message.reply("silahkan tunggu", quote=True)
    if client.me.id in tagallgcid and message.chat.id in tagallgcid[client.me.id]:
        return await msg.edit(
            "sedang menjalankan perintah silahkan coba lagi nanti atau gunakan perintah <code>batal</code>"
        )
    if client.me.id not in tagallgcid:
        tagallgcid[client.me.id] = set()

    tagallgcid[client.me.id].add(message.chat.id)

    text = message.text.split(None, 1)[1] if len(message.text.split()) != 1 else ""
    users = [
    f"[{member.user.first_name}](tg://user?id={member.user.id})"
        async for member in message.chat.get_members()
        if not (member.user.is_bot or member.user.is_deleted)
    ]
    shuffle(users)
    m = message.reply_to_message or message
    await msg.delete()
    for output in [users[i : i + 5] for i in range(0, len(users), 5)]:
        if (
            client.me.id not in tagallgcid
            or message.chat.id not in tagallgcid[client.me.id]
        ):
            break
        await m.reply(
            f"{text}\n\n{' '.join(output)}", quote=bool(message.reply_to_message)
        )
        await asyncio.sleep(2)

    if client.me.id in tagallgcid and message.chat.id in tagallgcid[client.me.id]:
        tagallgcid[client.me.id].remove(message.chat.id)
        if not tagallgcid[client.me.id]:
            del tagallgcid[client.me.id]

@CB.UBOT("batal", sudo=True)
async def batal_cmd(client, message):
    if (
        client.me.id not in tagallgcid
        or message.chat.id not in tagallgcid[client.me.id]
    ):
        return await message.reply(
            "sedang tidak ada perintah: <code>tagall</code> yang digunakan"
        )

    tagallgcid[client.me.id].remove(message.chat.id)
    if not tagallgcid[client.me.id]:
        del tagallgcid[client.me.id]

    await message.reply("ok, perintah tagall berhasil dibatalkan")
