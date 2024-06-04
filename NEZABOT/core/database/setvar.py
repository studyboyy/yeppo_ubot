from NEZABOT.core.database import mongodb

varsdb = mongodb.vars


async def set_vars(orang, nama_vars, value, query="datanya"):
    update_data = {"$set": {f"{query}.{nama_vars}": value}}
    await varsdb.update_one({"_id": orang}, update_data, upsert=True)


async def get_vars(orang, nama_vars, query="datanya"):
    result = await varsdb.find_one({"_id": orang})
    return result.get(query, {}).get(nama_vars, None) if result else None


async def remove_all_vars(bot_id):
    await varsdb.delete_one({"_id": bot_id})

async def remove_vars(orang, nama_vars, query="datanya"):
    hapus_data = {"$unset": {f"{query}.{nama_vars}": ""}}

    await varsdb.update_one({"_id": orang}, hapus_data)


async def all_vars(user_id, query="datanya"):
    result = await varsdb.find_one({"_id": user_id})
    return result.get(query) if result else None


async def rmall_vars(orang):
    await varsdb.delete_one({"_id": orang})


async def ambil_list_vars(user_id, nama_vars, query="datanya"):
    data_ = await get_vars(user_id, nama_vars, query)
    return [int(x) for x in str(data_).split()] if data_ else []


async def add_vars(user_id, nama_vars, value, query="datanya"):
    list_data = await ambil_list_vars(user_id, nama_vars, query)
    list_data.append(value)
    await set_vars(user_id, nama_vars, " ".join(map(str, list_data)), query)


async def rem_vars(user_id, nama_vars, value, query="datanya"):
    list_data = await ambil_list_vars(user_id, nama_vars, query)
    if value in list_data:
        list_data.remove(value)
        await set_vars(user_id, nama_vars, " ".join(map(str, list_data)), query)
