from NEZABOT import *


@CB.UBOT("help", sudo=True)
async def _(client, message):
    await help_cmd(client, message)


@CB.INLINE("^user_help")
@INLINE.QUERY
async def _(client, inline_query):
    await menu_inline(client, inline_query)


@CB.CALLBACK("help_(.*?)")
# @INLINE.DATA
async def _(client, callback_query):
    try:
        await menu_callback(client, callback_query)
    except:
        pass
