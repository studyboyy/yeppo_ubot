from asyncio import sleep

from pyrogram.raw.functions.messages import DeleteHistory, StartBot
from NEZABOT.core.function.emoji import emoji

async def limit_cmd(client, message):
    await client.unblock_user("SpamBot")
    bot_info = await client.resolve_peer("SpamBot")
    msg = await message.reply(emoji("proses") + "<code>processing . . .</code>" + emoji("bintang"))
    response = await client.invoke(
        StartBot(
            bot=bot_info,
            peer=bot_info,
            random_id=client.rnd_id(),
            start_param="start",
        )
    )
    await sleep(1)
    await msg.delete()
    status = await client.get_messages("SpamBot", response.updates[1].message.id + 1) 
    if status and hasattr(status, "text"):  # Pengecekan apakah status dan status.text valid
        pjg = len(status.text)
        print(pjg)
        if pjg <= 100:
            text = f"<emoji id=6278555627639801385>✅</emoji> **kabar baik, akun anda tidak dibatasi. anda bebas, sebebas burung yang terbang lepas** . <emoji id=5210935111289159311>🔘</emoji>"
            await client.send_message(message.chat.id, text)
            return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
        else:
            await status.copy(message.chat.id, reply_to_message_id=message.id)
            return await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
    else:
        print("Status tidak valid atau status.text tidak ada")
