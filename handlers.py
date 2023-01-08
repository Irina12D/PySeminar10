import aiohttp
from aiogram import types
from utils import *

async def start(message: types.Message):
    await message.answer("Введите акроним криптовалюты из доступных сетей")

async def help(message: types.Message):
    await message.answer("Доступные сети:\n" + "\n".join(networks))

async def get_price(message: types.Message):
    network = message.text.upper()
    if network in networks:
        session = aiohttp.ClientSession()
        async with session.get(API_URL + f"get_price/{message.text}/USD") as resp:
            data = await resp.json()
            if data["status"] == "success":
                price = calc_price(data)
                await message.answer(price)
            else:
                await message.answer("Произошла ошибка")
    else:
        await message.answer("Выбранная крипта не поддерживается")
