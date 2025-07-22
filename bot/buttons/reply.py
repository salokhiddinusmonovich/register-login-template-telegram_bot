from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def auth_btn():
    login_btn  = KeyboardButton(text="Login")
    register_btn = KeyboardButton(text="Register")
    return ReplyKeyboardMarkup(keyboard=[[login_btn, register_btn]])