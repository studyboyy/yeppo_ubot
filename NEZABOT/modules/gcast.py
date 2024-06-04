from NEZABOT import *

__MODULE__ = "gcast"
__HELP__ = f"""
<b>『 bantuan untuk gcast 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}ucast</code> [text/reply to text/media]
  <b>• penjelasan:</b> untuk mengirim pesan ke semua user

  <b>• perintah:</b> <code>{PREFIX[0]}gcast</code> [text/reply to text/media]
  <b>• penjelasan:</b> untuk mengirim pesan ke semua group

  <b>• perintah:</b> <code>{PREFIX[0]}spamg</code> [jumlah_pesan - rep_pesan]
  <b>• penjelasan:</b> untuk spam pesan gcast

  <b>• perintah:</b> <code>{PREFIX[0]}send</code> [userid/username - text/reply]
  <b>• penjelasan:</b> untuk mengirim pesan ke user/group/channeld

  <b>gcast: untuk menggunakan button, gunakan format:</b>
  <code>text ~> button_text:button_url</code>
"""


@CB.UBOT("gcast", sudo=True)
async def _(client, message):
    await broadcast_group_cmd(client, message)


@CB.UBOT("ucast", sudo=True)
async def _(client, message):
    await broadcast_users_cmd(client, message)


@CB.UBOT("send", sudo=True)
async def _(client, message):
    await send_msg_cmd(client, message)


@CB.INLINE("^get_send")
@INLINE.QUERY
async def _(client, inline_query):
    await send_inline(client, inline_query)


@CB.INLINE("^gcast_button")
@INLINE.QUERY
async def _(client, inline_query):
    await gcast_inline(client, inline_query)

