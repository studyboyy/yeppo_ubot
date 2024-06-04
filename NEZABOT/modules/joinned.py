from NEZABOT import *
from NEZABOT.core.database.saved import get_chat
from pyrogram import Client
from pyrogram import errors
from pyrogram import enums
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate


__MODULE__ = "joinleave"
__HELP__ = f"""
<b>『 bantuan untuk joinleave 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}kickme</code>
  <b>• penjelasan:</b> keluar dari grup

  <b>• perintah:</b> <code>{PREFIX[0]}join</code> [uꜱernamegc]
  <b>• penjelasan:</b> untuk join ke grup melalui uꜱername 

  <b>• perintah:</b> <code>{PREFIX[0]}leaveallgc</code>
  <b>• penjelasan:</b> keluar dari ꜱemua grup yang bukan admin/owner

  <b>• perintah:</b> <code>{PREFIX[0]}leaveallmute</code>
  <b>• penjelasan:</b> keluar dari ꜱemua grup yang membatasi anda

  <b>• perintah:</b> <code>{PREFIX[0]}leaveallch</code>
  <b>• penjelasan:</b> keluar dari ꜱemua channel yang bukan admin/owner

  <b>• perintah:</b> <code>{PREFIX[0]}leave</code> [usernamegc]
  <b>• penjelasan:</b> untuk keluar dari grup melalui username
"""


@CB.UBOT("kickme|leave", sudo=False)
async def _(client, message):
    await leave(client, message)


@CB.UBOT("join", sudo=False)
async def _(client, message):
    await join(client, message)


@CB.UBOT("leaveallgc", sudo=False)
async def _(client, message):
    done = 0
    Haku = await message.reply(f"proccesing...")
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
            chat_id = dialog.chat.id
            await asyncio.sleep(0.1)
            try:
                member = await client.get_chat_member(chat_id, "me")
                if member.status not in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                    done += 1
                    await client.leave_chat(chat_id)
            except Exception:
                pass
    await Haku.edit(f"**berhasil keluar dari {done} grup yang bukan admin/owner** ✅")

@CB.UBOT("leaveallmute", sudo=False)
async def _(client, message):
    done = 0
    Haku = await message.reply(f"Proccesing...")
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
            chat_id = dialog.chat.id
            try:
                member = await client.get_chat_member(chat_id, "me")
                if member.status == ChatMemberStatus.RESTRICTED:
                    await client.leave_chat(chat_id)
                    done += 1
            except Exception:
                pass
    await Haku.edit(f"**berhasil keluar dari {done} grup yang membatasi anda** ✅")


@CB.UBOT("leaveallch", sudo=False)
async def _(client, message):
    await kickmeallch(client, message)


