import asyncio
import os

from NEZABOT import *
from NEZABOT.core.function.emoji import emoji

async def memify_cmd(client, message):
    if not message.reply_to_message:
        return await message.reply(emoji("gagal") + "balas ke pesan foto atau sticker!")
    reply_message = message.reply_to_message
    if not reply_message.media:
        return await message.reply(emoji("gagal") + "balas ke pesan foto atau sticker")
    file = await client.download_media(reply_message)
    Tm = await message.reply(emoji("proses") + "processing . . .")
    text = get_arg(message)
    if len(text) < 1:
        return await Tm.edit(emoji("gagal") + f"harap ketik {PREFIX[0]}mmf text")
    meme = await add_text_img(file, text)
    await asyncio.gather(
        Tm.delete(),
        client.send_sticker(
            message.chat.id,
            sticker=meme,
            reply_to_message_id=message.id,
        ),
    )
    os.remove(meme)
