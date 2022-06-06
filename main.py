import asyncio
import logging
from wikipedia import set_lang
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand
from aiogram import Bot, Dispatcher, types

from config import config

config = config('./config/config.ini')
bot = Bot(token=config.TgBot.token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())

async def set_commands(bot : Bot):
    commands = [
        BotCommand(command='/start', description='Старт')
    ]
async def main():
    set_lang("ru")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    await set_commands(bot)
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())