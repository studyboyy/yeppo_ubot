
__MODULE__ = "logs"
__HELP__ = """
bantuan untuk group logs

• perintah: <code>{0}logger</code> [on/off]
• penjelasan: untuk mengaktifkan atau menonaktifkan grup log.

- <code>{0}logger on</code> ->  mengaktifkan grup log.
- <code>{0}logger off</code> ->  menonaktifkan grup log.
"""



import asyncio
from pyrogram.enums import *
from pyrogram.errors import FloodWait
from pyrogram.types import *
from NEZABOT import *
from pyrogram.errors.exceptions.not_acceptable_406 import UserRestricted
from pyrogram.errors.exceptions.bad_request_400 import ChannelPrivate


async def create_botlog(client):
    name = "NEZA-UserBot Logs"
    desc = "Jangan Keluar Dari Grup Log Ini\n\nPowered by: neza-userbot"
    group = await client.create_supergroup(name, desc)
    nt = wget.download("https://telegra.ph//file/e8314103e98de10e242ac.jpg")
    photo_video = {"video": nt} if nt.endswith(".mp4") else {"photo": nt}
    kntl = group.id
    await client.set_chat_photo(kntl, **photo_video)
    await client.send_message(
        kntl,
        f"**Group Log Berhasil Dibuat\n\nKamu keluar dari sini aku cabulin rame2!!!**",
    )
    
async def get_log(client):
    name = "NEZA-UserBot Logs"
    async for dialog in client.get_dialogs():
        if dialog.chat.title == name:
            return dialog.chat
    return None

@ubot.on_message(
  filters.group
  & filters.mentioned
  & filters.incoming
  & ~filters.bot
  & ~filters.via_bot
)
async def _(client, message):
    log = await get_log(client)
    cek = await get_log_group(client.me.id)
    if not cek:
        return
    user = f"[{message.from_user.first_name} {message.from_user.last_name or ''}](tg://user?id={message.from_user.id})"
    message_link = message.link
    text = f"""
📨 <b>TAGS MESSAGE</b>
• <b>Logs:</b> <code>{client.me.first_name}</code>
• <b>Group:</b> <code>{message.chat.title}</code>
• <b>Dari :</b> <code>{user}</code>
• <b>Pesan:</b> <code>{message.text}</code>

• <b>Tautan Grup:</b> [Disini]({message_link})
"""
    try:
        await client.send_message(
            log.id,
            text,
            disable_web_page_preview=True,
        )
    except FloodWait as e:
        await asyncio.sleep(e.value)
        await client.send_message(
            log.id,
            text,
            disable_web_page_preview=True,
        )

@ubot.on_message(
  filters.private
  & filters.incoming
  & ~filters.me
  & ~filters.bot
  & ~filters.service
)
async def _(client, message):
    log = await get_log(client)
    cek = await get_log_group(client.me.id)

    if cek is None:
        return  # Tindakan yang sesuai jika hasil get_log_group adalah None

    if message.chat.id == 777000:
        return  # Tindakan yang sesuai jika id chat adalah 777000

    async for x in client.search_messages(message.chat.id, limit=1):
        if log and hasattr(log, 'id'):
            try:
                await x.forward(log.id)
            except ChannelPrivate:
                pass
        else:
            print("Objek log tidak diinisialisasi dengan benar.")


@CB.UBOT("logger", sudo=True)
async def _(client, message):
    try:
        xx = await message.reply(f"**Processing...**")
        cek = get_arg(message)
        logs = await get_log_group(client.me.id)
        if cek.lower() == "on":
            if not logs:
                await set_log_group(client.me.id, logger=True)
                await create_botlog(client)
                ajg = await get_log(client)
                babi = await client.export_chat_invite_link(int(ajg.id))
                return await xx.edit(f"**Log Group Berhasil Diaktifkan :\n\n{babi}**")
            else:
                return await xx.edit(f"**Log Group anda Sudah aktif.**")
        if cek.lower() == "off":
            if logs:
                await del_log_group(client.me.id)
                ajg = await get_log(client)
                await client.delete_supergroup(int(ajg.id))
                return await xx.edit(f"**Log Group Berhasil Dinonaktifkan.**")
            else:
                return await xx.edit(f"**Log Group anda Sudah Dinonaktifkan.**")
        else:
            return await xx.edit(
                f"**Format yang anda berikan salah. silahkan gunakan <code>{message.text} on/off</code>**"
            )
    except UserRestricted:
        await del_log_group(client.me.id)
        await xx.edit(f"anda tidak bisa membuat group!")