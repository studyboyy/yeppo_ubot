from NEZABOT import *

__MODULE__ = "info"
__HELP__ = f"""
<b>『 bantuan untuk info 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}info</code> [user_id/username/reply to users]
  <b>• penjelasan:</b> untuk mendapatkan info pengguna telegram dengan deskripsi lengkap

  <b>• perintah:</b> <code>{PREFIX[0]}cinfo</code> [chat_id/username/reply to chat]
  <b>• penjelasan:</b> untuk mendapatkan info group/channel dengan deskripsi lengkap
"""


@CB.UBOT("whois|info", sudo=False)
async def _(client, message):
    await info_cmd(client, message)


@CB.UBOT("cwhois|cinfo", sudo=False)
async def _(client, message):
    await cinfo_cmd(client, message)
