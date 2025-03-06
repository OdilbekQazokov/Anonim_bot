from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import logging

TOKEN = "7445824823:AAEH4JlekZQmelCg3rWjUQtsA3QnOz-uprQ" 
GROUP_ID = -1002315408239

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def escape_markdown_v2(text: str) -> str:
    """MarkdownV2 formatiga moslash uchun maxsus belgilarni eskap qilish"""
    special_chars = r'_*[]()~`>#+-=|{}.!'
    for char in special_chars:
        text = text.replace(char, f'\{char}')
    return text

@dp.message_handler(commands=['start'])
async def start_command(message: Message):
    """Foydalanuvchi /start bosganda chiqadigan xabar"""
    await message.answer("Xush kelibsiz!\nXabar jo‘natishingiz mumkin.")

@dp.message_handler()
async def forward_to_group(message: Message):
    """Faqat botga shaxsiy chatdan kelgan xabarlarni guruhga yuboradi"""
    if message.chat.type == "private":  # Faqat shaxsiy chatlarni tekshiramiz
        log_message = f"Message: {message.text}\n\nProfile name: {message.from_user.full_name}\nUsername:  @{message.from_user.username if message.from_user.username else 'Mavjud emas'}\nUser ID: {message.from_user.id}"
        safe_message = escape_markdown_v2(log_message)
        await bot.send_message(GROUP_ID, safe_message, parse_mode="MarkdownV2")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

