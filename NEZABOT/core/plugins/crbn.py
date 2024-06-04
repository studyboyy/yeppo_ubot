from NEZABOT import *
from io import BytesIO
from NEZABOT.core.function.emoji import emoji

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


async def carbon_func(client, message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await message.delete()
    ex = await message.reply(emoji("proses") + f"**memproꜱeꜱ . . .**")
    carbon = await make_carbon(text)
    await ex.edit(emoji("upload") + f"**uploading . . .**")
    await asyncio.gather(
        ex.delete(),
        client.send_photo(
            message.chat.id,
            carbon,
            caption=f"<b>carboniꜱed by :</b>{client.me.mention}",
        ),
    )
    carbon.close()
