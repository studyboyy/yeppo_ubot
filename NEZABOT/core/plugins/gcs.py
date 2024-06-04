import asyncio
from gc import get_objects

from pyrogram.enums import ChatType
from pyrogram.errors.exceptions import FloodWait

from NEZABOT import *
from NEZABOT.config import *
from NEZABOT.core.function.emoji import emoji

def get_message(message):
    msg = (
        message.reply_to_message
        if message.reply_to_message
        else ""
        if len(message.command) < 2
        else " ".join(message.command[1:])
    )
    return msg

async def get_broadcast_id(client, query):
    chats = []
    chat_types = {
        "group": [ChatType.GROUP, ChatType.SUPERGROUP],
        "users": [ChatType.PRIVATE],
    }
    async for dialog in client.get_dialogs():
        if dialog.chat.type in chat_types[query]:
            chats.append(dialog.chat.id)

    return chats

async def broadcast_group_cmd(client, message):
    msg = await message.reply(emoji("proses") + f"**sedang memproses mohon bersabar**...")

    send = get_message(message)
    if not send:
        return await msg.edit(emoji("gagal") + f"**mohon balas sesuatu atau ketik sesuatu!**")

    chats = await get_broadcast_id(client, "group")
    blacklist = await get_chat(client.me.id)

    done = 0
    for chat_id in chats:
        if chat_id in blacklist:
            continue
        elif chat_id in BLACKLIST_CHAT:
            continue

        try:
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except Exception:
            pass

    return await msg.edit(f"**pesan broadcast anda terkirim ke** `{done}` **group**" + emoji("done"))    
    


async def broadcast_users_cmd(client, message):
    msg = await message.reply(emoji("proses") + f"**sedang memproses mohon bersabar**...")

    send = get_message(message)
    if not send:
        return await msg.edit(emoji("gagal") + f"**mohon balas sesuatu atau ketik sesuatu!**")

    chats = await get_broadcast_id(client, "users")

    done = 0
    for chat_id in chats:
        if chat_id == client.me.id:
            continue
        

        try:
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            if message.reply_to_message:
                await send.copy(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except Exception:
            pass

    return await msg.edit(f"**pesan broadcast anda terkirim ke** `{done}` **group**" + emoji("done"))    


async def send_msg_cmd(client, message):
    if message.reply_to_message:
        chat_id = (
            message.chat.id if len(message.command) < 2 else message.text.split()[1]
        )
        try:
            if client.me.id != bot.me.id:
                if message.reply_to_message.reply_markup:
                    x = await client.get_inline_bot_results(
                        bot.me.username, f"get_send {id(message)}"
                    )
                    return await client.send_inline_bot_result(
                        chat_id, x.query_id, x.results[0].id
                    )
        except Exception as error:
            return await message.reply(error)
        else:
            try:
                return await message.reply_to_message.copy(chat_id)
            except Exception as t:
                return await message.reply(f"{t}")
    else:
        if len(message.command) < 3:
            return await message.reply("ketik yang bener")
        chat_id, chat_text = message.text.split(None, 2)[1:]
        try:
            return await client.send_message(chat_id, chat_text)
        except Exception as t:
            return await message.reply(f"{t}")


async def send_inline(client, inline_query):
    _id = int(inline_query.query.split()[1])
    m = next((obj for obj in get_objects() if id(obj) == _id), None)
    if m:
        await client.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=[
                InlineQueryResultArticle(
                    title="get send!",
                    reply_markup=m.reply_to_message.reply_markup,
                    input_message_content=InputTextMessageContent(
                        m.reply_to_message.text
                    ),
                )
            ],
        )
        
        
async def gcast_inline(client, inline_query):
    get_id = int(inline_query.query.split(None, 1)[1])
    m = [obj for obj in get_objects() if id(obj) == get_id][0]
    buttons, text = await gcast_create_button(m)
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get button!",
                    reply_markup=buttons,
                    input_message_content=InputTextMessageContent(text),
                )
            )
        ],
    )
