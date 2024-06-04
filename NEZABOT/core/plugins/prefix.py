from NEZABOT import *


async def setprefix(client, message):
    Tm = await message.reply("memproses...", quote=True)
    if len(message.command) < 2:
        return await Tm.edit(f"<code>{message.text}</code> simbol prefix")
    else:
        ub_prefix = []
        for prefix in message.command[1:]:
            if prefix.lower() == "none":
                ub_prefix.append("")
            else:
                ub_prefix.append(prefix)
        try:
            client.set_prefix(message.from_user.id, ub_prefix)
            await set_pref(message.from_user.id, ub_prefix)
            parsed_prefix = " ".join(f"<code>{prefix}</code>" for prefix in ub_prefix)
            return await Tm.edit(f"<b>✅ prefix telah diubah ke: {parsed_prefix}</b>")
        except Exception as error:
            return await Tm.edit(str(error))


async def change_emot(client, message):
    try:
        msg = await message.reply("memproses...", quote=True)

        if not client.me.is_premium:
            return await msg.edit(
                "<b>untuk menggunakan perintah ini akun anda haru premium terlebih</b>"
            )

        if len(message.command) < 3:
            return await msg.edit("<b>tolong masukkan query dan valeu nya</b>")

        query_mapping = {"pong": "EMOJI_PING", "uptime": "EMOJI_UPTIME", "mention": "EMOJI_MENTION"}
        command, mapping, value = message.command[:3]

        if mapping.lower() in query_mapping:
            query_var = query_mapping[mapping.lower()]
            emoji_id = None
            if message.entities:
                for entity in message.entities:
                    if entity.custom_emoji_id:
                        emoji_id = entity.custom_emoji_id
                        break

            if emoji_id:
                await set_vars(client.me.id, query_var, emoji_id)
                await msg.edit(
                    f"<b>✅ <code>{query_var}</code> berhasil di setting ke:</b> <emoji id={emoji_id}>{value}</emoji>"
                )
            else:
                await msg.edit("<b>tidak dapat menemukan emoji premium</b>")
        else:
            await msg.edit("<b>mapping tidak ditemukan</b>")

    except Exception as error:
        await msg.edit(str(error))
