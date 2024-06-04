from NEZABOT import *

__MODULE__ = "memes"
__HELP__ = f"""
<b>『 bantuan untuk memes 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}memes</code> [text]
  <b>• penjelasan:</b> untuk membuat stiker memes random
"""


@CB.UBOT("mms|memes", sudo=True)
async def _(client, message):
    await memes_cmd(client, message)
