from NEZABOT import *


__MODULE__ = "locks"
__HELP__ = f"""
<b>『 bantuan untuk lockꜱ 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}lock</code> [type]
  <b>• penjelasan:</b> untuk mengunci izin group

  <b>• perintah:</b> <code>{PREFIX[0]}unlock</code> [type]
  <b>• penjelasan:</b> untuk membuka izin group

  <b>• perintah:</b> <code>{PREFIX[0]}locks</code>
  <b>• penjelasan:</b> untuk melihat izin ꜱaat ini.

  <b>• type : `msg`|`media`|`stickers`|`polls`|`info`|`invite`|`webprev`|`pin`
"""


@CB.UBOT("lock|unlock", sudo=False)
async def _(client, message):
    await locks_func(client, message)


@CB.UBOT("locks", sudo=False)
async def _(client, message):
    await locktypes(client, message)
