from NEZABOT import *

__MODULE__ = "ϙrcode"
__HELP__ = f"""
<b>『 bantuan untuk qrcode 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}qrGen</code> [text qrcode]
  <b>• penjelasan:</b> untuk merubah qrcode text menjadi gambar

  <b>• perintah:</b> <code>{PREFIX[0]}qrRead</code> [reply to media]
  <b>• penjelasan:</b> untuk merubah qrcode menjadi text
"""

@CB.UBOT("qrgen", sudo=False)
async def _(client, message):
    await qr_gen_cmd(client, message)


@CB.UBOT("qrread", sudo=False)
async def _(client, message):
    await qr_read_cmd(client, message)
