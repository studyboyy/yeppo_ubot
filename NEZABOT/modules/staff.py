from NEZABOT import *

__MODULE__ = "staff"
__HELP__ = f"""
<b>『 bantuan untuk staff 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}staff</code> [ip addreꜱ]
  <b>• penjelasan:</b> untuk mendapatkan informasi seluruh staff grup
  """


@CB.UBOT("staff", sudo=False)
async def _(client, message):
    await staff_cmd(client, message)