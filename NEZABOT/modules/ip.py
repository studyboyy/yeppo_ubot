from NEZABOT import *


__MODULE__ = "ipinfo"
__HELP__ = f"""
<b>『 bantuan untuk ipinfo 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}ipinfo</code> [ip addreꜱ]
  <b>• penjelasan:</b> untuk mendapatkan informaꜱi ip addreꜱ 
  """


@CB.UBOT("ipinfo", sudo=False)
async def _(client, message):
    await hacker_lacak_target(client, message)
