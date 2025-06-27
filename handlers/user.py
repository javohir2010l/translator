from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router
from deep_translator import GoogleTranslator
from keys.keys import Keyboard

router = Router()
user_language = {}

@router.message(CommandStart())
async def start(message: Message):
    await message.reply(
        "Assalomu alaykum! Bu bot sizga iboralarni tarjima qilib beradi!\nTilni tanlang:",
        reply_markup=Keyboard
    )

@router.message()
async def trans(message: Message):
    user_id = message.from_user.id
    text = message.text.lower()

    if text in ['uzbek', 'russian', 'english']:
        lang_map = {
            'uzbek': 'uz',
            'russian': 'ru',
            'english': 'en'
        }
        user_language[user_id] = lang_map[text]
        await message.reply(f"Til tanlandi: {text}. Endi matn yuboring.")
        return

    lang = user_language.get(user_id, 'uz')
    translated = GoogleTranslator(target=lang).translate(message.text)
    await message.reply(translated)
