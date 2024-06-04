from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone
from NEZABOT.core.function.emoji import emoji
from NEZABOT import *
from NEZABOT.config import USER_ID
# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 ℙℝ𝔼𝕄𝕀𝕌𝕄 #
# ========================== #


async def prem_user(client, message):
    Tm = await message.reply(emoji("proses") + "<b>processing . . .</b>")
    if message.from_user.id not in await get_seles():
        return await Tm.edit(
            emoji("gagal") + "Untuk menggunakan perintah ini anda harus menjadi reseller terlebih dahulu"
        )
    user_id, get_bulan = await extract_user_and_reason(message)
    if not user_id:
        return await Tm.edit(f"<b>{message.text} user_id/username - bulan</b>")
    try:
        get_id = (await client.get_users(user_id)).id
    except Exception as error:
        return await Tm.edit(error)
    if not get_bulan:
        get_bulan = 1
    premium = await get_prem()
    if get_id in premium:
        return await Tm.edit(f"**dia sudah bisa membuat CHIHOODBOT**" + emoji("done"))
    added = await add_prem(get_id)
    if added:
        now = datetime.now(timezone("asia/Jakarta"))
        expired = now + relativedelta(months=int(get_bulan))
        await set_expired_date(get_id, expired)
        await Tm.edit(
            emoji("done") + f" {get_id} telah di aktifkan selama {get_bulan} bulan, silahkan buat CHIHOODBOT di @{bot.me.username}"
        )
        await bot.send_message(
            OWNER_ID,
            f"• {message.from_user.id} ─> {get_id} •",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "👤 profil",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                        InlineKeyboardButton(
                            "profil 👤", callback_data=f"profil {get_id}"
                        ),
                    ],
                ]
            ),
        )
    else:
        await Tm.delete()
        await message.edit(emoji("gagal") + "terjadi kesalahan yang tidak diketahui")


async def unprem_user(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply(emoji("proses") + "<b>processing . . .</b>")
    if not user_id:
        return await Tm.edit(
            emoji("gagal") + "<b>balas pesan pengguna atau berikan user_id/username</b>"
        )
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    delpremium = await get_prem()
    if user.id not in delpremium:
        return await Tm.edit(emoji("gagal") + "<b>tidak ditemukan</b>")
    removed = await remove_prem(user.id)
    if removed:
        await Tm.edit(emoji("done") + f"<b> {user.mention} berhasil dihapus</b>")
    else:
        await Tm.delete()
        await message.edit(emoji("gagal") + "terjadi kesalahan yang tidak diketahui")


async def get_prem_user(client, message):
    text = ""
    count = 0
    for user_id in await get_prem():
        try:
            user = await bot.get_users(user_id)
            count += 1
            userlist = f"• {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"{userlist}\n"
    if not text:
        await message.reply(emoji("gagal") + "tidak ada pengguna yang ditemukan")
    else:
        await message.reply(text)


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝔹𝕃𝔸ℂ𝕂𝕃𝕀𝕊𝕋 #
# ========================== #


async def add_blaclist(client, message):
    Tm = await message.edit(emoji("proses") + "<b>tunggu sebentar . . .</b>")
    chat_id = message.chat.id
    blacklist = await get_chat(client.me.id)
    if chat_id in blacklist:
        return await Tm.edit("group ini sudah ada dalam blacklist" + emoji("done"))
    add_blacklist = await add_chat(client.me.id, chat_id)
    if add_blacklist:
        await Tm.edit(f"{message.chat.title} berhasil ditambahkan ke daftar hitam" + emoji("done"))
    else:
        await Tm.edit("terjadi kesalahan yang tidak diketahui" + emoji("gagal"))
        await asyncio.sleep(2)
    return await Tm.delete()


async def del_blacklist(client, message):
    Tm = await message.edit(emoji("proses") + "<b>tunggu sebentar . . .</b>")
    try:
        if not get_arg(message):
            chat_id = message.chat.id
        else:
            chat_id = int(message.command[1])
        blacklist = await get_chat(client.me.id)
        if chat_id not in blacklist:
            return await Tm.edit(emoji("bintang") + f"{message.chat.title} tidak ada dalam daftar hitam")
        del_blacklist = await remove_chat(client.me.id, chat_id)
        if del_blacklist:
            await Tm.edit(f"{chat_id} berhasil dihapus dari daftar hitam" + emoji("done"))
        else:
            await Tm.edit("terjadi kesalahan yang tidak diketahui" + emoji("gagal"))
    except Exception as error:
        await Tm.edit(error)
        await asyncio.sleep(2)
    return await Tm.delete()


async def get_blacklist(client, message):
    Tm = await message.edit(emoji("proses") + "<b>tunggu sebentar . . .</b>")
    msg = emoji("bintang") + f"<b>• total blacklist {len(await get_chat(client.me.id))}</b>\n\n"
    for X in await get_chat(client.me.id):
        try:
            get = await client.get_chat(X)
            msg += f"<b>• {get.title} | <code>{get.id}</code></b>\n"
        except:
            msg += f"<b>• <code>{X}</code></b>\n"
    await message.edit(msg)


async def rem_all_blacklist(client, message):
    msg = await message.edit(emoji("proses") + "<b>sedang memproses....</b>", quote=True)
    get_bls = await get_chat(client.me.id)
    if len(get_bls) == 0:
        return await msg.edit(emoji("bintang") + "<b>daftar hitam anda kosong</b>")
    for X in get_bls:
        await remove_chat(client.me.id, X)
    await msg.edit("<b>semua daftar hitam telah berhasil dihapus</b>" + emoji("done"))


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 ℝ𝔼𝕊𝔼𝕃𝕃𝔼ℝ #
# ========================== #


async def seles_user(client, message):
    if message.from_user.id not in USER_ID:
        return await message.reply(f"❌Untuk menggunakan perintah ini anda harus menjadi admin terlebih dahulu")
    user_id = await extract_user(message)
    Tm = await message.reply(emoji("proses") + "<b>tunggu sebentar . . .</b>")
    if not user_id:
        return await Tm.edit(
            emoji("gagal") + "<b>balas pesan pengguna atau berikan user_id/username</b>"
        )
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    reseller = await get_seles()
    if user.id in reseller:
        return await Tm.edit("sudah menjadi reseller.")
    added = await add_seles(user.id)
    if added:
        await add_prem(user.id)
        await Tm.edit(emoji("done") + f"<b> {user.mention} teleh menjadi reseller</b>")
    else:
        await Tm.delete()
        await message.edit("terjadi kesalahan yang tidak diketahui" + emoji("gagal"))


async def unseles_user(client, message):
    if message.from_user.id not in USER_ID:
        return await message.reply(f"❌Untuk menggunakan perintah ini anda harus menjadi admin terlebih dahulu")
    user_id = await extract_user(message)
    Tm = await message.reply(emoji("proses") + "<b>tunggu sebentar . . .</b>")
    if not user_id:
        return await Tm.edit(
            emoji("gagal") + "<b>balas pesan pengguna atau berikan user_id/username</n>"
        )
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    delreseller = await get_seles()
    if user.id not in delreseller:
        return await Tm.edit(emoji("bintang") + "tidak ditemukan")
    removed = await remove_seles(user.id)
    if removed:
        await remove_prem(user.id)
        await Tm.edit(f"{user.mention} berhasil dihapus" + emoji("done"))
    else:
        await Tm.delete()
        await message.edit("terjadi kesalahan yang tidak diketahui" + emoji("gagal"))


async def get_seles_user(cliebt, message):
    if message.from_user.id not in USER_ID:
        return await message.reply(f"❌Untuk menggunakan perintah ini anda harus menjadi admin terlebih dahulu")
    text = ""
    count = 0
    for user_id in await get_seles():
        try:
            user = await bot.get_users(user_id)
            count += 1
            user = f"• {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"{user}\n"
    if not text:
        await message.edit("tidak ada pengguna yang ditemukan" + emoji("gagal"))
    else:
        await message.edit(text)


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝔼𝕏ℙ𝕀ℝ𝔼𝔻 #
# ========================== #


async def expired_add(client, message):
    if message.from_user.id not in USER_ID:
        return await message.reply(f"❌Untuk menggunakan perintah ini anda harus menjadi admin terlebih dahulu")
    Tm = await message.reply(emoji("proses") + "<b>processing . . .</b>")
    user_id, get_day = await extract_user_and_reason(message)
    if not user_id:
        return await Tm.edit(f"<b>{message.text} user_id/username - hari</b>")
    try:
        get_id = (await client.get_users(user_id)).id
    except Exception as error:
        return await Tm.edit(error)
    if not get_day:
        get_day = 30
    now = datetime.now(timezone("asia/Jakarta"))
    expire_date = now + timedelta(days=int(get_day))
    await set_expired_date(user_id, expire_date)
    await Tm.edit(emoji("bintang") + f"{get_id} telah diaktifkan selama {get_day} hari." + emoji("done"))


async def expired_cek(client, message):
    if message.from_user.id not in USER_ID:
        return await message.reply(f"❌Untuk menggunakan perintah ini anda harus menjadi admin terlebih dahulu")
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply("pengguna tidak temukan" + emoji("gagal"))
    expired_date = await get_expired_date(user_id)
    if expired_date is None:
        await message.reply(f"{user_id} belum diaktifkan." + emoji("gagal"))
    else:
        remaining_days = (expired_date - datetime.now()).days
        await message.reply(
            f"{user_id} aktif hingga {expired_date.strftime('%d-%m-%Y %H:%M:%S')}. sisa waktu aktif {remaining_days} hari."
        )


async def un_expired(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply(emoji("proses") + "</b>memproses. . .</b>")
    if not user_id:
        return await Tm.edit("<b>user tidak ditemukan</b>" + emoji("gagal"))
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    await rem_expired_date(user.id)
    return await Tm.edit(emoji("done") + f"<b> {user.id} expired telah dihapus</b>")


async def bcast_cmd(_, message):
    if message.from_user.id not in USER_ID:
        return
    
    if message.reply_to_message:
        x = message.reply_to_message.id
        y = message.chat.id
    
    if len(message.command) > 1:
        return await message.reply(
            "<b>Silakan sertakan pesan atau balas pesan yang ingin disiarkan.</b>"
        )

    kntl = 0
    mmk = []
    jmbt = len(await get_served_users())
    babi = await get_served_users()
    for xx in babi:
        mmk.append(int(xx["user_id"]))
    if USER_ID in mmk:
        mmk.remove(USER_ID)
    for i in mmk:
        try:
            m = (
                await bot.forward_messages(i, y, x)
                if message.reply_to_message
                else await bot.send_message(i, y, x)
            )
            kntl += 1
        except:
            pass
    return await message.reply(
        emoji("done") + f"** Berhasil mengirim pesan ke `{kntl}` pengguna, dari `{jmbt}` pengguna.**",
    )
