from NEZABOT import *
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid

__MODULE__ = "zombies"
__HELP__ = f"""
<b>『 bantuan untuk zombies 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}zombies</code>
  <b>• penjelasan:</b> untuk mengeluarkan akun terhapus digrup anda.
"""

@CB.UBOT("zombies", sudo=False)
async def zombies_cmd(client, message):
    try:
        chat_id = message.chat.id
        deleted_users = []
        banned_users = 0
        Tm = await message.reply("<code><emoji id =5803403369913520877>🔍</emoji>sedang memeriksa</code>")
        async for i in client.get_chat_members(chat_id):
            if i.user.is_deleted:
                deleted_users.append(i.user.id)
        if len(deleted_users) > 0:
            for deleted_user in deleted_users:
                try:
                    banned_users += 1
                    await message.chat.ban_member(deleted_user)
                except Exception:
                    pass
            await Tm.edit(f"<b>berhasil mengeluarkan {banned_users} akun terhapus <emoji id=5798623990436074786>✅</emoji></b>")
        else:
            await Tm.edit("<b><emoji id =5929358014627713883>❌</emoji> tidak ada akun terhapus di group ini</b>")
    except ChannelInvalid:
        await Tm.edit(f"**<emoji id =5929358014627713883>❌</emoji> Gunakan Di Grup**")