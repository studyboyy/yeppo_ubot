from NEZABOT import *

__MODULE__ = "global"
__HELP__ = f"""
<b>『 bantuan untuk global 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}gban</code> [user_id/username/reply to user]
  <b>• penjelasan:</b> untuk banned user dari semua group chat 

  <b>• perintah:</b> <code>{PREFIX[0]}ungban</code> [user_id/username/reply to user]
  <b>• penjelasan:</b> untuk unbanned user dari semua group chat

  <b>• perintah:</b> <code>{PREFIX[0]}listgban</code>
  <b>• penjelasan:</b> untuk melihat daftar pengguna gban.
"""


@CB.UBOT("gban", sudo=True)
@ubot.on_message(filters.user(DEVS) & filters.command("cgban", "") & ~filters.me)
async def _(client, message):
    await global_banned(client, message)


@CB.UBOT("ungban", sudo=True)
async def _(client, message):
    await cung_ban(client, message)


@CB.UBOT("listgban", sudo=True)
async def _(client, message):
    await gbanlist(client, message)
