from dispatcher import dp
from bot.buttons.text import login_text, register_text
from bot.state.main import *
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram import F
from bot.buttons.reply import contact_btn
from db.model import Users

import re

EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

@dp.message(lambda message: message.text == register_text)
async def register_handler(message: Message, state: FSMContext):
    await state.set_state(RegisterState.fullname)
    await message.answer("Enter your fullname 👇")


@dp.message(RegisterState.fullname)
async def fullname_handler(message: Message, state: FSMContext):
    await state.update_data(fullname=message.text.strip())
    await state.set_state(RegisterState.age)
    await message.answer("Enter your age 👇")

@dp.message(RegisterState.age)
async def age_handle(message: Message, state: FSMContext):
    age_str = message.text.strip()
    
    if not age_str.isdigit():
        await message.answer("Please enter your age using digits only (e.g 18). ")
        return
    
    if not (5 <= int(age_str) <= 120): # sanity check 
        await message.answer("Please enter a valid age between 5 and 120.")
        return
    
    # data = await state.get_data()
    # data["age"] = int(age_str)
    # await state.set_data(data)
    await state.update_data(age=int(age_str))
    await state.set_state(RegisterState.email)
    await message.answer("Enter your email 👇")


@dp.message(RegisterState.email)
async def email_handler(message: Message, state: FSMContext):
   email = message.text.strip()
   if not EMAIL_REGEX.match(email):
       await message.answer("Pease enter a valid email address (e.g. usersomething@gmail.com)")
       return
   
   await state.update_data(email=email)
   await state.set_state(RegisterState.phone)
   await message.answer("Click the button below 👇", reply_markup=contact_btn())

@dp.message(RegisterState.phone)
async def phone_handler(message: Message, state: FSMContext):

    if not message.contact:
        await message.answer("Пожалуйста, нажми на кнопку, чтобы отправить номер телефона.")
        return
    

    phone = message.contact.phone_number

    data = await state.get_data()
    data["phone"] = phone
    await state.clear()
    Users(**data).insert()
    response = (
        f"✅ Регистрация завершена:\n"
        f"Возраст: {data.get('age')}\n"
        f"Email: {data.get('email')}\n"
        f"Телефон: {data.get('phone')}"
    )

    await message.answer(response)

