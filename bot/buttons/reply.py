from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from .text import login_text, register_text, phone_text


def auth_btn():
    login_btn  = KeyboardButton(text=login_text)
    register_btn = KeyboardButton(text=register_text)
    return ReplyKeyboardMarkup(keyboard=[[login_btn, register_btn]],resize_keyboard=True,  one_time_keyboard=True)

def contact_btn():
    phone = KeyboardButton(text=phone_text, request_contact=True)
    return ReplyKeyboardMarkup(keyboard=[[phone]], resize_keyboard=True, one_time_keyboard=True)