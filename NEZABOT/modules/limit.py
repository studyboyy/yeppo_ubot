from NEZABOT import *

__MODULE__ = "limit"
__HELP__ = f"""
<b>『 bantuan untuk limit 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}limit</code>
  <b>• penjelasan:</b> untuk mengecek status akun apakah terkenal limit atau tidak
"""


@CB.UBOT("limit", sudo=True)
async def _(client, message):
    await limit_cmd(client, message)
