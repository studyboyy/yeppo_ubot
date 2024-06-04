from NEZABOT import *

__MODULE__ = "carbon"
__HELP__ = f"""
<b>『 bantuan untuk font 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}carbon</code> [reply/text]
  <b>• penjelasan:</b> untuk membuat tekꜱ carbonara
"""

@CB.UBOT("carbon", sudo=True)
async def _(client, message):
    await carbon_func(client, message)
