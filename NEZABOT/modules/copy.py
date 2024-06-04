from NEZABOT import *

__MODULE__ = "copy"
__HELP__ = f"""
<b>『 bantuan untuk copy 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}copy</code> [link_konten_telegram]
  <b>• penjelasan:</b> untuk mengambil pesan dan postingan chanel telegram melalui link mereka
  """

@CB.UBOT("copy", sudo=False)
async def _(client, message):
    await nyolongnih(client, message)

