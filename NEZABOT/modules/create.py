from NEZABOT import *

__MODULE__ = "create"
__HELP__ = """
 <b>『 bantuan untuk create 』</b>

<b>• perintah:</b> <code>{0}buat</code> gc namagc
<b>• penjelasan:</b> untuk membuat grup telegram.

<b>• perintah:</b> <code>{0}buat</code> ch namach
<b>• penjelasan:</b> untuk membuat channel telegram.
"""


@CB.UBOT("buat", sudo=True)
async def _(client, message):
    await create_grup(client, message)
