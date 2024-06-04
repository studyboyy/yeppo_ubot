import asyncio

from pyrogram.enums import UserStatus
import random
from NEZABOT import *
from NEZABOT.core.function.emoji import emoji
from asyncio import sleep

async def invite_cmd(client, message):
    mg = await message.reply(emoji("bintang") + "<b>menambahkan pengguna!</b>")
    if len(message.command) < 2:
        return await mg.delete()
    user_s_to_add = message.text.split(" ", 1)[1]
    if not user_s_to_add:
        await mg.edit(
            emoji("bintang") + "<b>beri saya pengguna untuk ditambahkan! periksa menu bantuan untuk info lebih lanjut!</b>"
        )
        return
    user_list = user_s_to_add.split(" ")
    try:
        await client.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except Exception as e:
        return await mg.edit(f"{e}")
    await mg.edit(emoji("bintang") + f"<b>berhasil ditambahkan {len(user_list)} ke grup ini</b>" + emoji("done"))


invite_id = []


async def inviteall_cmd(client, message):
    Tm = await message.reply(emoji("proses") + "<b>processing . . .</b>")
    if len(message.command) < 3:
        await message.delete()
        return await Tm.delete()
    try:
        chat = await client.get_chat(message.command[1])
    except Exception as error:
        return await Tm.edit(error)
    if message.chat.id in invite_id:
        return await Tm.edit_text(
            emoji("proses") + f"sedang menginvite member silahkan coba lagi nanti atau gunakan perintah: <code>{PREFIX[0]}cancel</code>"
        )
    else:
        done = 0
        failed = 0
        invite_id.append(message.chat.id)
        await Tm.edit_text(emoji("bintang") + f"mengundang anggota dari {chat.title}")
        async for member in client.get_chat_members(chat.id):
            stats = [
                UserStatus.ONLINE,
                UserStatus.OFFLINE,
                UserStatus.RECENTLY,
                UserStatus.LAST_WEEK,
            ]
            if member.user.status in stats:
                try:
                    await client.add_chat_members(message.chat.id, member.user.id)
                    done = done + 1
                    await asyncio.sleep(int(message.command[2]))
                except Exception:
                    failed = failed + 1
                    await asyncio.sleep(int(message.command[2]))
        invite_id.remove(message.chat.id)
        await Tm.delete()
        return await message.reply(
            f"""
emoji("done") + <b> <code>{done}</code> anggota yang berhasil diundang</b>
emoji("gagal") + <b> <code>{failed}</code> anggota yang gagal diundang</b>
"""
        )


async def cancel_cmd(client, message):
    if message.chat.id not in invite_id:
        return await message.reply_text(
            emoji("gagal") + f"sedang tidak ada perintah: <code>{PREFIX[0]}inviteall</code> yang digunakan"
        )
    try:
        invite_id.remove(message.chat.id)
        await message.reply_text(emoji("bintang") + "ok inviteall berhasil dibatalkan" + emoji("done"))
    except Exception as e:
        await message.reply_text(e)

async def ongjir_cmd(client, message):
    emoji = "<emoji id=6278555627639801385>✅</emoji>"
    try:
        await message.reply(f"active {emoji} !")
    except:
        pass

async def devsreact_cmd(client, message):
    try:
        emoji = ["🔥", "👻", "❤️‍🔥", "🗿", "😈"]
        random_emoji = random.choice(emoji)
        chat = message.chat.id
        id = message.id
        await sleep(1)
        await client.send_reaction(chat_id=chat, message_id=id, emoji=random_emoji)
    except:
        pass