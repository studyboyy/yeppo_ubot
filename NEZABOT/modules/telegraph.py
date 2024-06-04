from NEZABOT import *

__MODULE__ = "telegraph"
__HELP__ = f"""
<b>『 bantuan untuk telegraph 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}tg</code> [reply media/text]
  <b>• penjelasan:</b> untuk mengapload media/text ke telegra.ph
"""


@CB.UBOT("tg", sudo=False)
async def _(client, message):
    await tg_cmd(client, message)
