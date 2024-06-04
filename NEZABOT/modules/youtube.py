from NEZABOT import *

__MODuLE__ = "youtube"
__HELp__ = f"""
<b>『 bantuan untuk youtube 』</b>

• perintah: <code>{0}song</code> [song title]
• penjelasan: untuk mendownload music yang diinginkan.

• perintah: <code>{0}vsong</code> [video title]
• penjelasan: untuk mendownload video yang diinginkan.
"""


@CB.UBOT("vsong", sudo=True)
async def _(client, message):
    await vsong_cmd(client, message)


@CB.UBOT("song", sudo=True)
async def _(client, message):
    await song_cmd(client, message)
