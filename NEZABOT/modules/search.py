from NEZABOT import *

__MODULE__ = "search"
__HELP__ = f"""
<b>『 bantuan untuk search 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}bing</code> or <code>{PREFIX[0]}pic</code> [query]
  <b>• penjelasan:</b> untuk mencari photo random dari google

  <b>• perintah:</b> <code>{PREFIX[0]}gif</code> [query]
  <b>• penjelasan:</b> untuk mencari gift/animation random dari google
"""


@CB.UBOT("bing|pic", sudo=False)
async def _(client, message):
    await pic_bing_cmd(client, message)


@CB.UBOT("gif", sudo=False)
async def _(client, message):
    await gif_cmd(client, message)
