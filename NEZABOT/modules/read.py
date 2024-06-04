from NEZABOT import *

__MODULE__ = "baca"
__HELP__ = f"""
<b>『 bantuan untuk baca 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}baca</code>
  <b>• penjelasan:</b> untuk membaca semua pesan yang belum terbaca
"""
from pyrogram import Client, idle, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.types import ChatMember
from pyrogram.errors.exceptions import UserNotParticipant

@CB.UBOT("baca", sudo=True)
async def baca_read(client, message):
    Mai = await message.reply_text(f"Proccesing...")
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == ChatType.PRIVATE:
            user_id = dialog.chat.id
            anjai = await client.read_chat_history(user_id)
            if anjai:
                done += 1
    await Mai.edit_text(f"Berhasil Membaca Pesan Dari : {done} User✅")
