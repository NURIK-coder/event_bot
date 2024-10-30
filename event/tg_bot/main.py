import asyncio
import logging
import sys
from os import getenv

from aiogram import Dispatcher, Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv

from app.hendlers import router as handler_router

load_dotenv()

TOKEN = getenv('TOKEN')
dp = Dispatcher()


async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML), proxy='http://proxy.server:3128')
    dp.include_router(handler_router)
    await dp.start_polling(bot)




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    # logging.basicConfig(level=logging.INFO, filename='logs.log')
    asyncio.run(main())


