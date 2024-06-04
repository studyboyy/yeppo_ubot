from NEZABOT import *

__MODULE__ = "control"
__HELP__ = f"""
<b>『 bantuan untuk control 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}setprefix</code> [simbol prefix]
  <b>• penjelasan:</b> untuk mengubah prefix/handler command

  <b>• perintah:</b> <code>{PREFIX[0]}setemoji</code> [query] [valeu]
  <b>• query: </b>
       <b>•> PONG </b>
       <b>•> MENTION </b>
  <b>• penjelasan: untuk merubah tampilan pong pada ping</b>

"""

@CB.UBOT("setprefix", sudo=True)
async def _(client, message):
    await setprefix(client, message)

@CB.UBOT("setemoji", sudo=True)
async def _(client, message):
    await change_emot(client, message)

