import asyncio
import os

from gc import get_objects
from time import time
from pyrogram import Client, filters
from pyrogram.errors import RPCError
from pyrogram.types import *
from pyrogram import *
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                            InlineQueryResultArticle, InputTextMessageContent)

from NEZABOT import *
from NEZABOT.core.function.emoji import emoji

async def nyolongnih(client, message):
    try:
        await message.edit(emoji("proses") + f"**Procesing...**")
        link = get_arg(message)
        msg_id = int(link.split("/")[-1])
        if "t.me/c/" in link:
            try:
                chat = int("-100" + str(link.split("/")[-2]))
                dia = await client.get_messages(chat, msg_id)
            except RPCError:
                await message.edit(emoji("gagal") + f"**sepertinya terjadi kesalahan**")
        else:
            try:
                chat = str(link.split("/")[-2])
                dia = await client.get_messages(chat, msg_id)
            except RPCError:
                await message.edit(emoji("gagal") + f"**sepertinya terjadi kesalahan**")
        anjing = dia.caption or None
        if dia.text:
            await dia.copy(message.chat.id)
            await message.delete()
        if dia.photo:
            anu = await client.download_media(dia)
            await client.send_photo(message.chat.id, anu, anjing)
            await message.delete()
            os.remove(anu)
        
        if dia.video:
            anu = await client.download_media(dia)
            await client.send_video(message.chat.id, anu, anjing)
            await message.delete()
            os.remove(anu)
        
        if dia.audio:
            anu = await client.download_media(dia)
            await client.send_audio(message.chat.id, anu, anjing)
            await message.delete()
            os.remove(anu)
        
        if dia.voice:
            anu = await client.download_media(dia)
            await client.send_voice(message.chat.id, anu, anjing)
            await message.delete()
            os.remove(anu)
        
        if dia.document:
            anu = await client.download_media(dia)
            await client.send_document(message.chat.id, anu, anjing)
            await message.delete()
            os.remove(anu)
        else:
            await message.edit(emoji("gagal") + f"**sepertinya terjadi kesalahan**")
    except Exception as e:
        await message.reply_text(e)