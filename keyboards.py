from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_group_keyboard():
    buttons = [KeyboardButton(f"F{i}") for i in range(1, 26)]
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=5)  # Har qatorga 5 ta tugma
    keyboard.add(*buttons)
    return keyboard
