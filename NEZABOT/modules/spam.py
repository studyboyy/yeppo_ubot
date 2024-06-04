from NEZABOT import *

__MODULE__ = "spam"
__HELP__ = f"""
<b>『 bantuan untuk spam 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}spam</code> [jumlah_pesan - pesan_spam]
  <b>• penjelasan:</b> untuk spam pesan

  <b>• perintah:</b> <code>{PREFIX[0]}dspam</code> [jumlah_pesan - jumlah_delay_detik - pesan_spam]
  <b>• penjelasan:</b> untuk spam pesan delay
  
"""

@CB.UBOT("spam|dspam", sudo=False)
async def _(client, message):
    if message.command[0] == "spam":
        await spam_cmd(client, message)
    if message.command[0] == "dspam":
        await dspam_cmd(client, message)

@CB.UBOT("spamg", sudo=True)
async def _(client, message):
    if message.command[0] == "spamg":
        await spam_broadcast_cmd(client, message)
