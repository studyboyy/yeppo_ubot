import importlib
import random
from datetime import datetime, timedelta

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone

from NEZABOT import *


async def login_cmd(client, message):
    info = await message.reply("<b>tunggu sebentar...</b>", quote=True)
    if len(message.command) < 3:
        return await info.edit(
            f"<code>{message.text}</code> <b>hari - string pyrogram</b>"
        )
    try:
        ub = Ubot(
            name=f"ubot_{random.randrange(999999)}",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=message.command[2],
        )
        await ub.start()
        for mod in loadModule():
            importlib.reload(importlib.import_module(f"NEZABOT.modules.{mod}"))
        now = datetime.now(timezone("asia/Jakarta"))
        expire_date = now + timedelta(days=int(message.command[1]))
        await set_expired_date(ub.me.id, expire_date)
        await add_ubot(
            user_id=int(ub.me.id),
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=message.command[1],
        )
        buttons = [
            [
                InlineKeyboardButton(
                    "📁 cek masa aktif 📁",
                    callback_data=f"cek_masa_aktif {ub.me.id}",
                )
            ],
        ]
        await bot.send_message(
            LOGS_MAKER_UBOT,
            f"""
<b>❏ CHIHOODBOT diaktifkan</b>
<b> ├ akun:</b> <a href=tg://user?id={ub.me.id}>{ub.me.first_name} {ub.me.last_name or ''}</a> 
<b> ╰ id:</b> <code>{ub.me.id}</code>
""",
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True,
        )
        return await info.edit(
            f"<b>✅ berhasil login di akun: <a href='tg://user?id={ub.me.id}'>{ub.me.first_name} {ub.me.last_name or ''}</a></b>"
        )
    except Exception as error:
        return await info.edit(f"<code>{error}</code>")


async def restart_cmd(client, message):
    msg = await message.reply("<b>tunggu sebentar</b>", quote=True)
    if message.from_user.id not in ubot._get_my_id:
        return await msg.edit(
            f"<b>anda tidak bisa menggunakan perintah ini. dikarenakan anda bukan pengguna @{bot.me.username}</b>"
        )
    for X in ubot._ubot:
        if message.from_user.id == X.me.id:
            for _ubot_ in await get_NEZABOTs():
                if X.me.id == int(_ubot_["name"]):
                    try:
                        ubot._ubot.remove(X)
                        ubot._get_my_id.remove(X.me.id)
                        UB = Ubot(**_ubot_)
                        await UB.start()
                        for mod in loadModule():
                            importlib.reload(
                                importlib.import_module(f"NEZABOT.modules.{mod}")
                            )
                        return await msg.edit(
                            f"<b>✅ restart berhasil dilakukan {UB.me.first_name} {UB.me.last_name or ''} | {UB.me.id}</b>"
                        )
                    except Exception as error:
                        return await msg.edit(f"<b>{error}</b>")
