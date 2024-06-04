from NEZABOT import *

__MODULE__ = "kang"
__HELP__ = f"""
<b>『 bantuan untuk kang 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}kang</code> [reply to image/sticker]
  <b>• penjelasan:</b> untuk menambahkan dan costum emoji sticker ke sticker pack

  <b>note:</b> untuk membuat paket ꜱtiker baru gunakan angka di belakang !kang.
  <b>example:</b> <code>kang 2</code> untuk membuat dan menyimpan ke paket ꜱtiker ke-2</b>
"""

@CB.UBOT("kang", sudo=False)
async def _(client, message):
    await kang_cmd(client, message)
