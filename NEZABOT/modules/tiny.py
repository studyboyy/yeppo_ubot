from NEZABOT import *
from PIL import Image

__MODULE__ = "tiny"
__HELP__ = f"""
<b>『 bantuan untuk tiny 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}tiny</code> [reply to sticker]
  <b>• penjelasan:</b> untuk merubah sticker menjadi kecil
"""

def text_set(text):
    lines = []
    if len(text) <= 55:
        lines.append(text)
    else:
        all_lines = text.split("\n")
        for line in all_lines:
            if len(line) <= 55:
                lines.append(line)
            else:
                k = len(line) // 55
                lines.extend(line[((z - 1) * 55) : (z * 55)] for z in range(1, k + 2))
    return lines[:25]


@CB.UBOT("nulis", sudo=False)
async def handwrite(client, message):
    if message.reply_to_message:
        naya = message.reply_to_message.text
    else:
        naya = message.text.split(None, 1)[1]
    nan = await eor(message, "Processing...")
    try:
        img = Image.open("pyrogram/template.jpg")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("pyrogram/default.ttf", 30)
        x, y = 150, 140
        lines = text_set(naya)
        line_height = font.getsize("hg")[1]
        for line in lines:
            draw.text((x, y), line, fill=(1, 22, 55), font=font)
            y = y + line_height - 5
        file = "nulis.jpg"
        img.save(file)
        if os.path.exists(file):
            await message.reply_photo(
                photo=file, caption=f""
            )
            os.remove(file)
            await nan.delete()
    except Exception as e:
        return await message.reply(e)

@CB.UBOT("tiny", sudo=False)
async def _(client, message):
    await tiny_cmd(client, message)
