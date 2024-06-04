import re

from importlib import import_module

from pyrogram.types import *

from NEZABOT import *
from NEZABOT.core.function.emoji import emoji

async def help_cmd(client, message):
    if not get_arg(message):
        try:
            x = await client.get_inline_bot_results(bot.me.username, "user_help")
            await message.reply_inline_bot_result(x.query_id, x.results[0].id)
        except Exception as error:
            await message.reply(error)
    else:
        module = get_arg(message)
        if module in HELP_COMMANDS:
            await message.reply(
                HELP_COMMANDS[module].HELP + '\n<b>©CHIHOODBOT</b>',
                quote=True,
                disable_web_page_preview=True,
            )
        else:
            await message.reply(
                f"<b>❌ tidak dapat ditemukan module dengan nama <code>{module}</code></b>"
            )
            


async def menu_inline(client, inline_query):
    SH = await ubot.get_prefix(inline_query.from_user.id)
    msg = f"<b>❏ Help </b>\n<b>├  Prefixes: {' '.join(SH)}</b>\n<b>╰  Commands: {len(HELP_COMMANDS)}</b>"
    await client.answer_inline_query(
        inline_query.id,
        cache_time=60,
        results=[
            (
                InlineQueryResultArticle(
                    title="Help Menu!",
                    reply_markup=InlineKeyboardMarkup(
                        paginate_modules(0, HELP_COMMANDS, "help")
                    ),
                    input_message_content=InputTextMessageContent(msg),
                )
            )
        ],
    )


async def menu_callback(client, callback_query):
    mod_match = re.match(r"help_module\((.+?)\)", callback_query.data)
    prev_match = re.match(r"help_prev\((.+?)\)", callback_query.data)
    next_match = re.match(r"help_next\((.+?)\)", callback_query.data)
    back_match = re.match(r"help_back", callback_query.data)
    SH = await ubot.get_prefix(callback_query.from_user.id)
    top_text = f"<b>❏ Help </b>\n<b>├  Prefixes: {' '.join(SH)}</b>\n<b>╰  Commands: {len(HELP_COMMANDS)}</b>"
    if mod_match:
        module = (mod_match.group(1)).replace(" ", "_")
        text = HELP_COMMANDS[module].__HELP__.format(next((p) for p in SH))
        button = [[InlineKeyboardButton(" kembali ", callback_data="help_back")]]
        await callback_query.edit_message_text(
            text=text + '\n<b>©CHIHOODBOT</b>',
            reply_markup=InlineKeyboardMarkup(button),
            disable_web_page_preview=True,
        )
    if prev_match:
        curr_page = int(prev_match.group(1))
        await callback_query.edit_message_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(curr_page - 1, HELP_COMMANDS, "help")
            ),
            disable_web_page_preview=True,
        )
    if next_match:
        next_page = int(next_match.group(1))
        await callback_query.edit_message_text(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(next_page + 1, HELP_COMMANDS, "help")
            ),
            disable_web_page_preview=True,
        )
    if back_match:
        await callback_query.edit_message_text(
            text=top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELP_COMMANDS, "help")
            ),
            disable_web_page_preview=True,
        )
