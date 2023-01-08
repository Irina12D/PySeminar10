from aiogram import Bot, Dispatcher, executor
import handlers

API_TOKEN = '5603584523:AAFtjO-0i2TxdC--65UAeumBIQXN11mpggU'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

dp.register_message_handler(handlers.start, commands=["start"])
dp.register_message_handler(handlers.help, commands=["help"])
dp.register_message_handler(handlers.get_price)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
