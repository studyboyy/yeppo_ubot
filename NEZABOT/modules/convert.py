from NEZABOT import *

__MODULE__ = "convert"
__HELP__ = f"""
<b>『 bantuan untuk convert 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}toanime</code> [reply to photo/sticker/gift]
  <b>• penjelasan:</b> untuk merubah photo/sticker/gift menjadi gambar anime

  <b>• perintah:</b> <code>{PREFIX[0]}toimg</code> [reply to sticker/gift]
  <b>• penjelasan:</b> untuk merubah sticker/gift menjadi photo

  <b>• perintah:</b> <code>{PREFIX[0]}tosticker</code> [reply to photo]
  <b>• penjelasan:</b> untuk merubah foto menjadi sticker

  <b>• perintah:</b> <code>{PREFIX[0]}togif</code> [reply to sticker]
  <b>• penjelasan:</b>  untuk merubah sticker menjadi gif

  <b>• perintah:</b> <code>{PREFIX[0]}toaudio</code> [reply to video]
  <b>• penjelasan:</b> untuk merubah video menjadi audio mp3
  
  <b>• perintah:</b> <code>{PREFIX[0]}colong</code> [reply to media timer]
  <b>• penjelasan:</b> untuk mengambil media timer dan menyimpan ke pesan tersimpan
"""


@CB.UBOT("toanime", sudo=False)
async def _(client, message):
    await convert_anime(client, message)


@CB.UBOT("toimg", sudo=False)
async def _(client, message):
    await convert_photo(client, message)


@CB.UBOT("tosticker", sudo=False)
async def _(client, message):
    await convert_sticker(client, message)


@CB.UBOT("togif", sudo=False)
async def _(client, message):
    await convert_gif(client, message)


@CB.UBOT("toaudio", sudo=False)
async def _(client, message):
    await convert_audio(client, message)


@CB.UBOT("colong", sudo=False)
async def _(client, message):
    await colong_cmn(client, message)
