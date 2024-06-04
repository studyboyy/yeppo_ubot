from pyrogram import Client, enums, filters
from pyrogram.types import Message
import asyncio
from NEZABOT import *
from NEZABOT.core.database.saved import get_chat
from pyrogram.enums import ChatType, ChatMemberStatus
from NEZABOT.core.function.emoji import emoji

from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant

async def join(client: Client, message: Message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply(emoji("proses") + "memproꜱeꜱ...")
    try:
        await xxnx.edit(emoji("done") + f"berhaꜱil bergabung ke chat id `{Man}`")
        await client.join_chat(Man)
    except Exception as ex:
        await xxnx.edit(emoji("gagal") + f"ERROR: \n\n{str(ex)}")


async def leave(client: Client, message: Message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    xxnx = await message.reply(emoji("proses") + f"**sedang memproꜱeꜱ**...")
    if message.chat.id in BLACKLIST_CHAT:
        return await xxnx.edit(emoji("gagal") + f"perintah ini dilarang digunakan di group ini")
    try:
        await xxnx.edit_text(emoji("bintang") + f" {client.me.first_name} **telah meninggalkan grup ini, bye!!**")
        await client.leave_chat(Man)
    except Exception as ex:
        await xxnx.edit_text(emoji("gagal") + f"ERROR: \n\n{str(ex)}")


async def kickmeallch(client: Client, message: Message):
    Man = await message.reply(emoji("proses") + f"**global leave dari channel**...")
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type == ChatType.CHANNEL:
            chat = dialog.chat.id
            member = await client.get_chat_member(chat, "me")
            if member.status not in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                try:
                    await client.leave_chat(chat)
                    done += 1
                except Exception:
                    pass
    await Man.edit(f"**berhasil keluar dari {done}**" + emoji("done"))