from NEZABOT import *

__MODULE__ = "efect"
__HELP__ = f"""
<b>『 bantuan untuk efect 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}efect</code> [efek_code - reply to voice note]
  <b>• penjelasan:</b> untuk mengubah suara voice note

  <b>• perintah:</b> <code>{PREFIX[0]}listefect</code>
  <b>• penjelasan:</b> untuk melihat daftar efect

"""


@CB.UBOT("efect", sudo=False)
async def _(client, message):
    await convert_efek(client, message)


@CB.UBOT("listefect", sudo=False)
async def _(client, message):
    await list_cmd_efek(client, message)


