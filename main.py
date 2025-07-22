import sys 

from aiogram import Bot
from aiogram.enums import ParseMode
import asyncio
import logging
from aiogram.client.default import DefaultBotProperties

from dispatcher import TOKEN, dp

from bot.handlers import * 

async def main() -> None:
    await dp.start_polling(Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML)))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())