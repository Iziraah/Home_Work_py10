import logging
from convert import get_eth
from convert import get_btc
from aiogram import *
from aiogram.types import *

API_TOKEN = 'ТУТ МОЙ ТОКЕН'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["BTC", "ETH"]
    keyboard.add(*buttons)
    await message.answer("Какая монетка интересует?", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text =="BTC")
async def with_puree(message: types.Message):
    need_value = get_btc()
    await message.reply(f'курс Биткоина = {need_value}$')


@dp.message_handler(lambda message: message.text == "ETH")
async def without_puree(message: types.Message):
    need_value = get_eth()
    await message.reply(f'курс Эфира = {need_value}$')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)