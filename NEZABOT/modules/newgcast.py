from NEZABOT import *
from pyrogram.enums import ChatType, ChatMemberStatus
from NEZABOT.core.database.saved import get_chat


__MODULE__ = "gcast new"
__HELP__ = f"""
<b>『 bantuan untuk gcastnew 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}bc</code> gc balas ke pesan
  <b>• penjelasan:</b> gc[grup], adm[khusus admin], pv [private chat]

"""

def get_message(message):
    msg = (
        message.reply_to_message
        if message.reply_to_message
        else ""
        if len(message.command) < 2
        else " ".join(message.command[1:])
    )
    return msg

cnt = "<emoji id=5211112665237175703>✅</emoji>"
ex = "<emoji id=5852812849780362931>❌</emoji>"
brs = "<emoji id=5210935111289159311>🔘</emoji>"

@CB.UBOT("bc", sudo=True)
async def _(c, m):
    done = 0
    gagal = 0
    if len(m.command) != 2:
        await m.reply(f"**<emoji id =5929358014627713883>❌</emoji> mohon gunakan format: bc [gc adm pv] **")
        return
    send = get_message(m)
    if not send:
        await m.reply_text(f"<emoji id=5911461474315802019>⭐</emoji> **mohon balas ke pesan** !", quote=True)
        return
    if not m.reply_to_message:
        await m.reply_text(f"<emoji id=5911461474315802019>⭐</emoji> **mohon balas ke pesan** !", quote=True)
        return
    blacklist = await get_chat(c.me.id)
    try:
        if m.command[1] == "gc":
            Haku = await m.reply(f"<emoji id=6010111371251815589>⏳</emoji> **sedang memproses**...")
            async for dialog in c.get_dialogs():
                if dialog.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
                    chat_id = dialog.chat.id
                    await asyncio.sleep(0.1)
                    if chat_id not in blacklist:
                        try:
                            await send.copy(chat_id)
                            done += 1
                        except Exception:
                            gagal += 1
                            pass

            await Haku.edit(f"""{brs} **berhasil menjalankan broadcast ke seluruh grup**
<blockquote>{cnt}**berhasil** : {done} **grup**</blockquote>
<blockquote>{ex}**gagal** : {gagal} **grup**</blockquote>
**powered by : **<a href=tg://user?id={c.me.id}>{c.me.first_name} {c.me.last_name or ''}</a>""")

        elif m.command[1] == "pv":
            Haku = await m.reply(f"<emoji id=6010111371251815589>⏳</emoji> **sedang memproses**...")
            async for dialog in c.get_dialogs():
                if dialog.chat.type == ChatType.PRIVATE:
                    chat_id = dialog.chat.id
                    await asyncio.sleep(0.1)
                    if chat_id not in blacklist:
                        try:
                            await send.copy(chat_id)
                            done += 1
                        except Exception:
                            pass

            await Haku.edit(
                f"<emoji id =5465277190453085073>🤖</emoji> **berhasil mengirim ke {done} chat pribadi** <emoji id=5798623990436074786>✅</emoji>\n\n"
                f"<emoji id =5465277190453085073>🤖</emoji> **powered by NEZABOT** <emoji id =5895583431194054511>🌟</emoji>\n")

        elif m.command[1] == "adm":
            Haku = await m.reply(f"<emoji id=6010111371251815589>⏳</emoji> **sedang memproses**...")
            async for dialog in c.get_dialogs():
                if dialog.chat.type in (ChatType.SUPERGROUP, ChatType.GROUP):
                    chat_id = dialog.chat.id
                    await asyncio.sleep(0.1)
                    try:
                        member = await c.get_chat_member(chat_id, "me")
                        if member.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER):
                            await send.copy(chat_id)
                            done += 1
                    except Exception:
                        pass
            await Haku.edit(
                f"<emoji id =5465277190453085073>🤖</emoji> **berhasil mengirim ke {done} khusus admin** <emoji id=5798623990436074786>✅</emoji>\n\n"
                f"<emoji id =5465277190453085073>🤖</emoji> **powered by NEZABOT** <emoji id =5895583431194054511>🌟</emoji>\n")


    except IndexError:
        await m.reply(f"<emoji id =5929358014627713883>❌</emoji>**mohon gunakan bc gc/adm/pv balas ke pesan**")