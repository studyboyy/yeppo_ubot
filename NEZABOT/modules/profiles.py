from NEZABOT import *

__MODULE__ = "profiles"
__HELP__ = f"""
<b>『 bantuan untuk profile 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}setbio</code> [text]
  <b>• penjelasan:</b> untuk mengubah bio anda

  <b>• perintah:</b> <code>{PREFIX[0]}setname</code> [text]
  <b>• penjelasan:</b> untuk mengubah nama anda

  <b>• perintah:</b> <code>{PREFIX[0]}block</code> [reply to user]
  <b>• penjelasan:</b> untuk memblokir pengguna

  <b>• perintah:</b> <code>{PREFIX[0]}unblock</code> [reply to user]
  <b>• penjelasan:</b> untuk membuka blokir pengguna
"""


@CB.UBOT("setbio", sudo=False)
async def _(client, message):
    await set_bio(client, message)


@CB.UBOT("setname", sudo=False)
async def _(client, message):
    await setname(client, message)


@CB.UBOT("block", sudo=False)
async def _(client, message):
    await block_user_func(client, message)


@CB.UBOT("unblock", sudo=False)
async def _(client, message):
    await unblock_user_func(client, message)