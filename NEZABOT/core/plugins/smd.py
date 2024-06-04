import asyncio

from pyrogram.raw.functions.messages import DeleteHistory


async def sosmed_cmd(client, message):
    if len(message.command) < 2:
        return await message.reply(
            f"<code>{message.text}</code> link yt/ig/fb/tw/tiktok"
        )
    else:
        bot = "thisvidbot"
        link = message.text.split()[1]
        await client.unblock_user(bot)
        Tm = await message.reply("<code>processing . . .</code>")
        xnxx = await client.send_message(bot, link)
        await asyncio.sleep(10)
        try:
            sosmed = await client.get_messages(bot, xnxx.id + 2)
            await sosmed.copy(message.chat.id, reply_to_message_id=message.id)
            await Tm.delete()
        except Exception:
            await Tm.edit(
                "<b>video tidak ditemukan silahkan ulangi beberapA saat lagi</b>"
            )
        user_info = await client.resolve_peer(bot)
        return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
