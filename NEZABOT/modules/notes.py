from NEZABOT import *

__MODULE__ = "notes"
__HELP__ = f"""
<b>『 bantuan untuk notes 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}addnote</code> [note_name - reply]
  <b>• penjelasan:</b> untuk menyimpan sebuah catatan

  <b>• perintah:</b> <code>{PREFIX[0]}get</code> [note_name]
  <b>• penjelasan:</b> untuk mendapatkan catatan yang disimpan

  <b>• perintah:</b> <code>{PREFIX[0]}delnote</code> [note_name]
  <b>• penjelasan:</b> untuk menghapus catatan

  <b>• perintah:</b> <code>{PREFIX[0]}notes</code>
  <b>• penjelasan:</b> untuk melihat daftar catatan yang disimpan

  <b>note: untuk menggunakan button, gunakan format:</b>
  <code>text ~> button_text:button_url</code>
"""


@CB.UBOT("addnote", sudo=False)
async def _(client, message):
    await addnote_cmd(client, message)


@CB.UBOT("get", sudo=False)
async def _(client, message):
    await get_cmd(client, message)


@CB.INLINE("^get_notes")
@INLINE.QUERY
async def _(client, inline_query):
    await get_notes_button(client, inline_query)


@CB.UBOT("delnote", sudo=False)
async def _(client, message):
    await delnote_cmd(client, message)


@CB.UBOT("notes", sudo=False)
async def _(client, message):
    await notes_cmd(client, message)
