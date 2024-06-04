from NEZABOT import *
from pyrogram.raw.functions.messages import DeleteHistory
__MODULE__ = "clear"
__HELP__ = f"""
<b>『 bantuan untuk clear 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}clear</code>
  <b>• penjelasan:</b> untuk menghapus history
"""


@CB.UBOT("clear", sudo=True)
async def _(client, message):
    user_id = message.chat.id
    bot_info = await client.resolve_peer(user_id)
    await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))