from NEZABOT import *

__MODULE__ = "sosmed"
__HELP__ = f"""
<b>『 bantuan untuk sosmed 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}sosmed</code> [link]
  <b>• penjelasan:</b> untuk mendownload media dari facebook/tiktok/instagram/twitter/youtube

  <b>• perintah:</b> <code>{PREFIX[0]}song</code> [song title]
  <b>• penjelasan:</b>  untuk mendownload music yang diinginkan

  <b>• perintah:</b> <code>{PREFIX[0]}vsong</code> [song title]
  <b>• penjelasan:</b> untuk mendownload video yang diinginkan
"""


@CB.UBOT("sosmed", sudo=False)
async def _(client, message):
    await sosmed_cmd(client, message)


@CB.UBOT("vsong", sudo=False)
async def _(client, message):
    await vsong_cmd(client, message)


@CB.UBOT("song", sudo=False)
async def _(client, message):
    await song_cmd(client, message)
