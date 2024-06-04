from NEZABOT import *
__MODULE__ = "game"
__HELP__ = """
<b>『 bantuan untuk game 』</b>

  <b>• perintah:</b> <code>{0}catur</code></code>
  <b>• penjelasan:</b> untuk memanggil game catur

  <b>• perintah:</b> <code>{0}game</code></code>
  <b>• penjelasan:</b> untuk memunculkan game random.
  <b>• note : jumlah menu 𝟻𝟶+ game </b>
"""



@CB.UBOT("catur", sudo=True)
async def _(client, message):
    await catur_cmd(client, message)
    

@CB.UBOT("game", sudo=True)
async def _(client, message):
    await game_cmd(client, message)