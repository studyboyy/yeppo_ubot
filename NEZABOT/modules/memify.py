from NEZABOT import *

__MODULE__ = "memefy"
__HELP__ = f"""
<b>『 bantuan untuk memify 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}mmf</code> [text]
  <b>• penjelasan:</b> balas ke sticker atau foto akan di ubah menjadi sticker teks meme yang di tentukan
"""


@CB.UBOT("mmf|memify", sudo=True)
async def _(client, message):
    await memify_cmd(client, message)
