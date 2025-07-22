from os import getenv
from aiogram import Dispatcher
from dotenv import load_dotenv

load_dotenv('/home/salokhiddin/Python/tg_bot_projects/RegisterLoginBot/.env')


TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()