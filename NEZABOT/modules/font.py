from NEZABOT import *

__MODULE__ = "font"
__HELP__ = f"""
<b>『 bantuan untuk font 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}font</code> [reply/text]
  <b>• penjelasan:</b> untuk merubah text font dengan tampilan yang berbeda
"""


@CB.UBOT("font", sudo=True)
async def _(client, message):
    await font_message(client, message)


@CB.INLINE("^get_font")
@INLINE.QUERY
async def _(client, inline_query):
    await font_inline(client, inline_query)


@CB.CALLBACK("^get")
@INLINE.DATA
async def _(client, callback_query):
    await font_callback(client, callback_query)


@CB.CALLBACK("^next")
@INLINE.DATA
async def _(client, callback_query):
    await font_next(client, callback_query)


@CB.CALLBACK("^prev")
@INLINE.DATA
async def _(client, callback_query):
    await font_prev(client, callback_query)
