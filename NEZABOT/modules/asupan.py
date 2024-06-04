from NEZABOT import *

__MODULE__ = "asupan"
__HELP__ = f"""
<b>『 bantuan untuk asupan 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}asupan</code>
  <b>• penjelasan:</b> untuk mengirim video asupan random

  <b>• perintah:</b> <code>{PREFIX[0]}cewek</code>
  <b>• penjelasan:</b> untuk mengirim photo cewek random

  <b>• perintah:</b> <code>{PREFIX[0]}cowok</code>
  <b>• penjelasan:</b> untuk mengirim photo cowok random

  <b>• perintah:</b> <code>{PREFIX[0]}anime</code>
  <b>• penjelasan:</b> untuk mengirim photo anime random
  
  <b>• perintah:</b> <code>{PREFIX[0]}bokep</code>
  <b>• penjelasan:</b> untuk mencari video bokep

"""


@CB.UBOT("asupan", sudo=True)
async def _(client, message):
    await video_asupan(client, message)


@CB.UBOT("cewek", sudo=True)
async def _(client, message):
    await photo_cewek(client, message)


@CB.UBOT("cowok", sudo=True)
async def _(client, message):
    await photo_cowok(client, message)


@CB.UBOT("anime", sudo=True)
async def _(client, message):
    await photo_anime(client, message)


@CB.UBOT("bokep", sudo=True)
async def _(client, message):
    await video_bokep(client, message)
