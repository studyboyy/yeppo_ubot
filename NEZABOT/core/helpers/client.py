from pyrogram import filters

from NEZABOT import *

class FILTERS:
    ME = filters.me
    GROUP = filters.group
    PRIVATE = filters.private
    INCOMING = filters.incoming
    SERVICE = filters.service
    BOT = filters.bot
    OWNER = filters.user(OWNER_ID)
    ME_GROUP = filters.me & filters.group
    ME_OWNER = filters.me & filters.user(OWNER_ID)
    ME_USER = filters.me & filters.user(USER_ID)
    PM = filters.me & filters.private
    

class CB:
    def BOT(command, filter=FILTERS.PRIVATE):
        def wrapper(func):
            @bot.on_message(filters.command(command) & filter)
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper
        
    def OWNER(func):
        async def function(client, message):
            kon = message.from_user.id
            if kon != OWNER_ID:
                return
            return await func(client, message)

        return function
        
    def SELES(func):
        async def function(client, message):
            kon = message.from_user.id
            if kon not in await get_seles():
                return
            return await func(client, message)

        return function
        
    def UBOT(command, sudo=False):
        def wrapper(func):
            sudo_command = ubot.cmd_prefix(command) if sudo else ubot.cmd_prefix(command) & filters.me

            @ubot.on_message(sudo_command)
            async def wrapped_func(client, message):
                if sudo:
                    sudo_id = await ambil_list_vars(client.me.id, "SUDO_USER", "ID_NYA")
                    if client.me.id not in sudo_id:
                        sudo_id.append(client.me.id)
                    if message.from_user.id in sudo_id:
                        return await func(client, message)
                else:
                    return await func(client, message)

            return wrapped_func

        return wrapper
        
    @staticmethod
    def AFK(afk_no):
        def wrapper(func):
            afk_check = (
                (filters.mentioned | filters.private)
                & ~filters.bot
                & ~filters.me
                & filters.incoming
                if afk_no
                else filters.me & ~filters.incoming
            )

            @ubot.on_message(afk_check, group=10)
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper
     
    def INLINE(command):
        def wrapper(func):
            @bot.on_inline_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper

    def CALLBACK(command):
        def wrapper(func):
            @bot.on_callback_query(filters.regex(command))
            async def wrapped_func(client, message):
                await func(client, message)

            return wrapped_func

        return wrapper
        