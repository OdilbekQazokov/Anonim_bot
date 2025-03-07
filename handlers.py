
from aiogram import Bot, types
from aiogram.types import Message
from config import GROUP_ID
from keyboards import get_group_keyboard
from utils import escape_markdown_v2

user_groups = {}  # Foydalanuvchi tanlagan guruhlarni saqlash uchun lug‘at

async def start_command(message: Message):
    await message.answer("Guruhingizni tanlang:", reply_markup=get_group_keyboard())

async def select_group(message: Message):
    user_groups[message.from_user.id] = message.text  # Tanlangan guruhni saqlash
    await message.answer("✅ Habar yozishingiz mumkin!", reply_markup=types.ReplyKeyboardRemove())

async def is_group_selected(user_id: int) -> bool:
    return user_id in user_groups  # Foydalanuvchi guruh tanlagan yoki tanlamaganligini tekshiramiz

async def forward_to_group(message: Message, bot: Bot):
    if message.chat.type == "private":
        user_id = message.from_user.id
        
        if not await is_group_selected(user_id):          # Agar foydalanuvchi hali guruh tanlamagan bo‘lsa, unga ogohlantirish yuboramiz
            await message.answer("⚠️ Iltimos, avval guruhingizni tanlang!", reply_markup=get_group_keyboard())
            return
        
        group_name = user_groups.get(user_id, "F0")  # Agar foydalanuvchi guruh tanlamagan bo‘lsa, F0

        log_message = (
            f"📢 Group: *{group_name}*\n\n"
            f"✉️ Message: {message.text}\n\n"
            f"👤 Profile name: {message.from_user.full_name}\n"
            f"📌 Username: @{message.from_user.username if message.from_user.username else 'Not exist'}\n"
            f"🆔 User ID: {message.from_user.id}"
        )
        safe_message = escape_markdown_v2(log_message)
        
        await bot.send_message(GROUP_ID, safe_message, parse_mode="MarkdownV2")
