# main.py

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage  # Подключаем FSM
from tortoise import Tortoise
from utils.logging_config import setup_logging
from config import API_TOKEN, DB_CONFIG
from middlewares.user_middleware import UserMiddleware
from handlers import start, channel, vip, ads, admin, statistics, channel_owner, referral
from utils.scheduler import setup_scheduler

# Конфигурация логирования
logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)

async def main():
    logger.info("Starting bot")
    setup_logging()

    bot = Bot(token=API_TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher(storage=MemoryStorage())  # Настраиваем FSM storage

    # Подключаем middleware
    dp.message.middleware(UserMiddleware())
    dp.callback_query.middleware(UserMiddleware())

    # Регистрируем роутеры
    dp.include_router(start.router)
    dp.include_router(channel.router)
    dp.include_router(vip.router)
    dp.include_router(ads.router)
    dp.include_router(admin.router)
    dp.include_router(statistics.router)
    dp.include_router(channel_owner.router)
    dp.include_router(referral.router)

    # Инициализируем базу данных
    await Tortoise.init(config=DB_CONFIG)
    await Tortoise.generate_schemas()

    # Настраиваем планировщик
    setup_scheduler()

    # Запускаем поллинг
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
