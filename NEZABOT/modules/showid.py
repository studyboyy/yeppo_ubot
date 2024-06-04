from NEZABOT import *
from pyrogram.enums import ParseMode

__MODULE__ = "showid"
__HELP__ = f"""
<b>『 bantuan untuk showid 』</b>

  <b>• perintah:</b> <code>{PREFIX[0]}id</code>
  <b>• penjelasan:</b> untuk mengetahui id dari user/grup/channel

  <b>• perintah:</b> <code>{PREFIX[0]}idm</code>
  <b>• penjelasan:</b> untuk mengetahui id dari emoji prem

  <b>• perintah:</b> <code>{PREFIX[0]}id</code> [reply to user/media]
  <b>• penjelasan:</b> untuk mengetahui id dari user/media

  <b>• perintah:</b> <code>{PREFIX[0]}id</code> [username user/grup/channel]
  <b>• penjelasan:</b> untuk mengetahui id user/grup/channel melalui username
"""

@CB.UBOT("id", sudo=True)
async def _(client, message):
    await id_cmd(client, message)

@CB.UBOT("idm", sudo=True)
async def _(client, message):
    zeb = message.reply_to_message
    if not zeb:
        return await message.reply_text("<emoji id=6113872536968104754>❎</emoji> mohon balasa ke emoji")
    try:
        emoji_text = zeb.text
        emoji_id = zeb.entities[0].custom_emoji_id
        await message.reply_text(f"`<emoji id={emoji_id}>{emoji_text}</emoji>`", parse_mode=ParseMode.MARKDOWN)
    except NoneType:
        await message.reply_text("<emoji id=6113872536968104754>❎</emoji> mohon balas ke emoji premium!")