import os
import logging
from flask import Flask, request
from aiogram import Bot, Dispatcher, types
import asyncio
from config import BOT  # token shu faylda saqlangan bo'lishi kerak
from handlers.user import router

# Flask app
app = Flask(__name__)

# Bot va Dispatcher
bot = Bot(token=BOT)
dp = Dispatcher()
dp.include_router(router)

# Webhook route
@app.route(f"/{BOT}", methods=["POST"])
async def webhook():
    update = types.Update(**request.get_json())
    await dp.feed_update(bot, update)
    return "ok"

# Webhook URL (Render beradigan domen bo'lishi kerak)
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

# Startup — webhook URL o‘rnatish
async def on_startup():
    await bot.set_webhook(f"{WEBHOOK_URL}/{BOT}")
    print("✅ Webhook o‘rnatildi:", f"{WEBHOOK_URL}/{BOT}")

# Main ishga tushirish
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(on_startup())
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
