from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

Keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="english")],
        [KeyboardButton(text="russian")],
        [KeyboardButton(text="uzbek")]
    ],
    resize_keyboard=True
)
