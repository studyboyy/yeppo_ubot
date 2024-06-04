from NEZABOT import *

__MODULE__ = "blacklist"
__HELP__ = """
<b>『 bantuan untuk blacklist chat 』</b>

  <b>• perintah:</b> <code>{0}addbl</code>
  <b>• penjelasan:</b> untuk memasukkan group ke daftar hitam supaya gcast kalian tidak masuk ke group [lakukan di group, selain di group bot tidak akan respon]

  <b>• perintah:</b> <code>{0}unbl</code>
  <b>• penjelasan:</b> untuk menghapus group dari daftar hitam agar gcast bisa masuk ke group  [lakukan di group, selain di group bot tidak akan respon]
  
  <b>• perintah:</b> <code>{0}rallbl</code>
  <b>• penjelasan:</b> untuk menghapus semua blacklist
  
  <b>• perintah:</b> <code>{0}listbl</code>
  <b>• penjelasan:</b> untuk memeriksa daftar blacklist group
"""
  
  
@CB.UBOT("addbl", sudo=True)
async def _(client, message):
    await add_blaclist(client, message)


@CB.UBOT("unbl", sudo=True)
async def _(client, message):
    await del_blacklist(client, message)


@CB.UBOT("rallbl", sudo=True)
async def _(client, message):
    await rem_all_blacklist(client, message)


@CB.UBOT("listbl", sudo=True)
async def _(client, message):
    await get_blacklist(client, message)
