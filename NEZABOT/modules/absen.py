__MODULE__ = "absen"
__HELP__ = """
<b>『 bantuan untuk absen 』</b>

  <b>• perintah:</b> <code>{0}absen</code></code>
  <b>• penjelasan:</b> untuk membuat list absen kamu.
  
  
  <b>• perintah:</b> <code>{0}delabsen</code></code>
  <b>• penjelasan:</b> untuk menghapus list absen kamu.
  """



from NEZABOT import *

@CB.UBOT("absen", sudo=True)
async def _(client, message):
    await absen_command(client, message)
    
    
@CB.UBOT("delabsen", sudo=True)
async def _(client, message):
    await clear_absen_command(client, message)


@CB.INLINE("^absen_in")
async def _(client, inline_query):
    await absen_query(client, inline_query)

@CB.CALLBACK("absen_hadir")
async def _(client, callback_query):
        await hadir_callback(client, callback_query)


