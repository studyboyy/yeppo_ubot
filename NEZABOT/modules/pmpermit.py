from NEZABOT import *

__MODULE__ = "pmpermit"
__HELP__ = """
bantuan untuk pmpermit

• perintah: <code>{0}antipm</code> [on atau off]
• penjelasan: untuk menghidupkan atau mematikan antipm

• perintah: <code>{0}setmsg</code> [balas atau berikan pesan]
• penjelasan: untuk mengatur pesan antipm.

• perintah: <code>{0}setlimit</code> [angka]
• penjelasan: untuk mengatur peringatan pesan blokir.

• perintah: <code>{0}ok</code>
• penjelasan: untuk menyetujui pesan.

• perintah: <code>{0}no</code>
• penjelasan: untuk menolak pesan.
"""



@CB.UBOT("antipm|pmpermit", sudo=True)
async def _(client, message):
    await permitpm(client, message)


@CB.UBOT("ok|a", sudo=True)
async def _(client, message):
    await approve(client, message)


@CB.UBOT("da|no", sudo=True)
async def _(client, message):
    await disapprove(client, message)


@CB.UBOT("setmsg", sudo=True)
async def _(client, message):
    await set_msg(client, message)


@CB.UBOT("setlimit", sudo=True)
async def _(client, message):
    await set_limit(client, message)


@ubot.on_message(
    filters.private & filters.incoming & ~filters.service & ~filters.me & ~filters.bot,group=1)
async def _(client, message):
    await handle_pmpermit(client, message)
