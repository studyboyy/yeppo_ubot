import asyncio
from datetime import datetime
from gc import get_objects
from time import time
from NEZABOT import bot, ubot
from pyrogram.errors.exceptions.bad_request_400 import UserBannedInChannel
from pyrogram.raw.functions import Ping
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from NEZABOT import *


async def send_msg_to_owner(client, message):
    if message.from_user.id == OWNER_ID:
        return
    else:
        buttons = [
            [
                InlineKeyboardButton(
                    "👤 profil", callback_data=f"profil {message.from_user.id}"
                ),
                InlineKeyboardButton(
                    "jawab 💬", callback_data=f"jawab_pesan {message.from_user.id}"
                ),
            ],
        ]
        await client.send_message(
            OWNER_ID,
            f"<a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>\n\n<code>{message.text}</code>",
            reply_markup=InlineKeyboardMarkup(buttons),
        )

from pyrogram.errors.exceptions.bad_request_400 import ReactionInvalid

async def ping_cmd(client, message):
    try:
        start = datetime.now()
        await client.invoke(Ping(ping_id=0))
        end = datetime.now()
        uptime = await get_time((time() - start_time))
        delta_ping = round((end - start).microseconds / 10000, 2)
        emot_1 = await get_vars(client.me.id, "EMOJI_PING")
        emot_2 = await get_vars(client.me.id, "EMOJI_UPTIME")
        emot_3 = await get_vars(client.me.id, "EMOJI_MENTION")
        emot_pong = emot_1 if emot_1 else "5172484558305625218"
        emot_uptime = emot_2 if emot_2 else "5210935111289159311"
        emot_mention = emot_3 if emot_3 else "5856956664292315353"
        if client.me.is_premium:
            _ping = f"""
<b><emoji id={emot_pong}>⭐</emoji> pong:</b> <code>{str(delta_ping).replace('.', ',')} ms</code>
<b><emoji id={emot_uptime}>🔘</emoji> date:</b> <code>{str(uptime).replace('.', ',')} ms</code>
<b><emoji id={emot_mention}>✉️</emoji> neza-userbot:</b> <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a>
    """
        else:
            _ping = f"""
<b>🏓 pong:</b> <code>{str(delta_ping).replace('.', ',')} ms</code>
<b>⏱ date: <code>{uptime}</code></b>
<b>⚜ neza-userbot:</b> <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a>
    """
        await message.reply_text(_ping)
    except UserBannedInChannel:
        pass

async def start_cmd(client, message):
    await add_served_user(message.from_user.id)
    await send_msg_to_owner(client, message)
    if len(message.command) < 2:
        buttons = Button.start(message)
        msg = MSG.START(message)
        await message.reply(msg, reply_markup=InlineKeyboardMarkup(buttons))
    else:
        txt = message.text.split(None, 1)[1]
        msg_id = txt.split("_", 1)[1]
        send = await message.reply("<b>tunggu sebentar...</b>")
        if "secretMsg" in txt:
            try:
                m = [obj for obj in get_objects() if id(obj) == int(msg_id)][0]
            except Exception as error:
                return await send.edit(f"<b>❌ error:</b> <code>{error}</code>")
            user_or_me = [m.reply_to_message.from_user.id, m.from_user.id]
            if message.from_user.id not in user_or_me:
                return await send.edit(
                    f"<b>❌ pesan ini bukan untukmu <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>"
                )
            else:
                text = await client.send_message(
                    message.chat.id,
                    m.text.split(None, 1)[1],
                    protect_content=True,
                    reply_to_message_id=message.id,
                )
                await send.delete()
                await asyncio.sleep(120)
                await message.delete()
                await text.delete()
        elif "copyMsg" in txt:
            try:
                m = [obj for obj in get_objects() if id(obj) == int(msg_id)][0]
            except Exception as error:
                return await send.edit(f"<b>❌ error:</b> <code>{error}</code>")
            id_copy = int(m.text.split()[1].split("/")[-1])
            if "t.me/c/" in m.text.split()[1]:
                chat = int("-100" + str(m.text.split()[1].split("/")[-2]))
            else:
                chat = str(m.text.split()[1].split("/")[-2])
            try:
                get = await client.get_messages(chat, id_copy)
                await get.copy(message.chat.id, reply_to_message_id=message.id)
                await send.delete()
            except Exception as error:
                await send.edit(error)
