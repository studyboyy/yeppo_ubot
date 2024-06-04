from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardMarkup, InlineQueryResultArticle,                            InputTextMessageContent, InlineKeyboardButton)
from datetime import datetime
import pytz

from NEZABOT import *

hadir_list = []

def get_hadir_list():
    return "\n".join([f"👤 {user['mention']} - {user['jam']}" for user in hadir_list])
    
async def absen_command(c, m):
    user_id = m.from_user.id
    mention = m.from_user.mention
    timestamp = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%d-%m-%Y")
    jam = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%H:%M:%S")

    hadir_list.append({"user_id": user_id, "mention": mention, "jam": jam})
    hadir_text = get_hadir_list()
    try:
        x = await c.get_inline_bot_results(bot.me.username, "absen_in")
        if x.results:
            await m.reply_inline_bot_result(x.query_id, x.results[0].id)
        else:
            await m.reply("Tidak ada hasil inline bot.")
    except asyncio.TimeoutError:
        await m.reply("Waktu habis dalam mendapatkan hasil inline bot.")
    except Exception as e:
        await m.reply(f"Terjadi kesalahan: {e}")
        
        
async def clear_absen_command(c, m):
    hadir_list.clear()

    await m.reply("Semua absen berhasil dihapus.")
        
        
async def absen_query(c, iq):
    user_id = iq.from_user.id
    mention = iq.from_user.mention
    timestamp = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%d-%m-%Y")
    jam = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%H:%M:%S")
    hadir_list.append({"user_id": user_id, "mention": mention, "jam": jam})
    hadir_text = get_hadir_list()

    text = f"**ABSEN TANGGAL:**\n{timestamp}\n\n**LIST ABSEN:**\n{hadir_text}\n\n"
    buttons = [[InlineKeyboardButton("Hadir", callback_data="absen_hadir")]]
    keyboard = InlineKeyboardMarkup(buttons)
    await c.answer_inline_query(
        iq.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="💬",
                    input_message_content=InputTextMessageContent(text),
                    reply_markup=keyboard
                )
            )
        ],
    )
    
async def hadir_callback(c, cq):
    user_id = cq.from_user.id
    mention = cq.from_user.mention
    timestamp = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%d-%m-%Y")
    jam = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%H:%M:%S")
    if any(user['user_id'] == user_id for user in hadir_list):
        await cq.answer("anda sudah melakukan absen sebelumnya.", show_alert=True)
    else:
        hadir_list.append({"user_id": user_id, "mention": mention, "jam": jam})
        hadir_text = get_hadir_list()
        text = f"**ABSEN TANGGAL:**\n{timestamp}\n\n**LIST ABSEN:**\n{hadir_text}\n\n"
        buttons = [[InlineKeyboardButton("Hadir", callback_data="absen_hadir")]]
        keyboard = InlineKeyboardMarkup(buttons)
        await cq.edit_message_text(text, reply_markup=keyboard)