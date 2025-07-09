import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import BOT  # token shu faylda saqlangan
from handlers.user import router  # komandalar shu faylda

async def main():
    logging.basicConfig(level=logging.INFO)
    
    bot = Bot(token=BOT)
    dp = Dispatcher()
    dp.include_router(router)

    print("🤖 Bot started using polling...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
