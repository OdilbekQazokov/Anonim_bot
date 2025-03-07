import logging
from aiogram import Bot, Dispatcher, executor
from config import TOKEN
from handlers import start_command, select_group, forward_to_group

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

dp.register_message_handler(start_command, commands=['start'])
dp.register_message_handler(select_group, lambda message: message.text.startswith("F") and message.text[1:].isdigit())
dp.register_message_handler(lambda message: forward_to_group(message, bot))

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
