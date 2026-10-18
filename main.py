import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.filters import Command

from buttons import main_menu, school_lessons_buttons, it_course_buttons, ielts_course_buttons

bot = Bot(token="8651654192:AAE1mgOFChPshjAhW--rgkJ1PI0vQ2sdSYU")
dp = Dispatcher()



@dp.message(Command('start'))
async def start(message: Message):
    full_name = message.from_user.full_name
    await message.answer(f"Assalomu Alekum {full_name}", reply_markup=await main_menu())



@dp.callback_query(F.data == "it_course")
async def reaction_to_it_course(call: CallbackQuery):
    await call.answer()
    await call.message.answer("IT Course bo'limi!", reply_markup=await it_course_buttons())



@dp.callback_query(F.data == "ielts_course")
async def reaction_to_ielts_course(call: CallbackQuery):
    await call.answer()
    await call.message.answer("IELTS Course bo'limi!", reply_markup=await ielts_course_buttons())



@dp.callback_query(F.data == "school_lesson")
async def reaction_to_school_lessons(call: CallbackQuery):
    await call.answer()
    await call.message.answer("Sinfni tanlang!", reply_markup=await school_lessons_buttons())



@dp.callback_query(F.data.startswith("lesson_"))
async def reaction_to_lesson(call: CallbackQuery):
    class_id = int(call.data.split("_")[-1])
    await call.answer()

    if class_id == 1:
        photo = FSInputFile(r"c:\Users\user\Pictures\341077371800626416 - Copy.jpg")
    elif class_id == 2:
        photo = FSInputFile(r"c:\Users\user\Pictures\rasm (4).jpg")
    elif class_id == 3:
        photo = FSInputFile(r"c:\Users\user\Pictures\rasm (6).jpg")
    elif class_id == 4:
        photo = FSInputFile(r"c:\Users\user\Pictures\rasm (10).jpg")
   

    await call.message.answer_photo(photo, caption=f"{class_id}-sinf rasmi")



@dp.callback_query(F.data == "go_back")
async def reaction_to_go_back(call: CallbackQuery):
    await call.answer()
    await call.message.answer("Qaysi biri qiziq bolsa tanlang:", reply_markup=await main_menu())


async def main():
    await dp.start_polling(bot)


asyncio.run(main())