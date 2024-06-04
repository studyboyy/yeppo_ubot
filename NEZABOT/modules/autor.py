from NEZABOT import *
import asyncio
from pyrogram.enums import ChatType

@CB.UBOT("asu", sudo=False)
async def asu(client, message):
    if len(message.command) < 2:  # Periksa apakah ada argumen setelah kata kunci 'asu'
        return await message.reply("gunakan asu balasan")
    x = await message.reply(f"proccesing...")
    done = 0
    gagal = 0
    anjir = " ".join(message.command[1:])  # Menggabungkan semua elemen setelah elemen pertama
    async for ngentod in client.get_dialogs():
        if ngentod.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
            pesan = client.get_chat_history(
                chat_id=ngentod.chat.id,
                limit=30,
                max_id=0)
            async for message in pesan:
                if message.mentioned:
                    try:
                        hai = await message.reply(f"{anjir}")
                        if hai:
                            done += 1
                    except:
                        gagal += 1
                        pass
    await x.edit(f"berhasil reply ke : {done} chat\ngagal reply ke : {gagal} chat")
