from aiogram import Dispatcher, Bot
from config import BOT
import asyncio
import sys
import logging
from handlers.user import router


dp = Dispatcher()

async def main():
    print("bot ishga tushdi")
    bot = Bot(token=BOT)
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__=='__main__':
    logging.basicConfig(level=logging.INFO,stream=sys.stdout)
    try:
        asyncio.run(main())
    except Exception:
        logging.info("bot to'xtadi")