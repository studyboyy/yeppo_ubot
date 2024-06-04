from NEZABOT import *

__MODULE__ = "translate"
__HELP__ = f"""
<b>『 bantuan untuk translate 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}tr</code> [reply/text]
  <b>• penjelasan:</b> untuk menerjemahkan text

  <b>• perintah:</b> <code>{PREFIX[0]}bahasa</code>
  <b>• penjelasan:</b> untuk merubah bahasa translate

  note : atur bahasa dahulu untuk menggunakan fitur ini
"""

@CB.UBOT("tr|tl", sudo=False)
async def _(client, message):
    await tr_cmd(client, message)


@CB.UBOT("bahasa", sudo=False)
async def _(client, message):
    await set_lang_cmd(client, message)


@CB.INLINE("^ubah_bahasa")
@INLINE.QUERY
async def _(client, inline_query):
    await ubah_bahasa_inline(client, inline_query)


@CB.CALLBACK("^set_bahasa")
@INLINE.DATA
async def _(client, callback_query):
    await set_bahasa_callback(client, callback_query)
