from NEZABOT import *

__MODULE__ = "invite"
__HELP__ = f"""
<b>『 bantuan untuk invite 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}invite</code> [username] 
  <b>• penjelasan:</b> untuk mengundang anggota ke grup anda

  <b>• perintah:</b> <code>{PREFIX[0]}inviteall</code> [username_group - colldown=detik per invite]
  <b>• penjelasan:</b> untuk mengundang anggota dari obrolan grup lain ke obrolan grup anda

  <b>• perintah:</b> <code>{PREFIX[0]}cancel</code>
  <b>• penjelasan:</b> untuk membatalkan perintah inviteall
  """


@CB.UBOT("invite", sudo=False)
async def _(client, message):
    await invite_cmd(client, message)


@CB.UBOT("inviteall", sudo=False)
async def _(client, message):
    await inviteall_cmd(client, message)


@CB.UBOT("cancel", sudo=False)
async def _(client, message):
    await cancel_cmd(client, message)
