from NEZABOT import *

__MODULE__ = "ϙuotly"
__HELP__ = f"""
<b>『 bantuan untuk quotly 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}q</code> [reply to text]
  <b>• penjelasan:</b> untuk merubah text menjadi sticker
"""


@CB.UBOT("q", sudo=True)
async def _(client, message):
    await quotly_cmd(client, message)
