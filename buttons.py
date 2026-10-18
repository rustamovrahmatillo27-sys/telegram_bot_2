from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def main_menu():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="IT course", callback_data="it_course"),
                InlineKeyboardButton(text="IELTS course", callback_data="ielts_course"),
                InlineKeyboardButton(text="Maktab darsliklari", callback_data="school_lesson")
            ]
        ]
    )
    return markup


async def it_course_buttons():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Kiber xafsizlik", callback_data="it_kiber")],
            [InlineKeyboardButton(text="Full Satck", callback_data="it_full")],
            [InlineKeyboardButton(text="Go Back", callback_data="go_back")],
        ]
    )
    return markup


async def ielts_course_buttons():
    markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Beginner", callback_data="general_beginner")],
            [InlineKeyboardButton(text="Elementary", callback_data="general_elementary")],
            [InlineKeyboardButton(text="Go Back", callback_data="go_back")],
        ]
    )
    return markup


async def school_lessons_buttons():
    buttons = []
    for i in range(1, 12):
        buttons.append([InlineKeyboardButton(text=f"{i}-sinf darsliklari", callback_data=f"lesson_{i}")])
    buttons.append([InlineKeyboardButton(text="Go Back", callback_data="go_back")])
    return InlineKeyboardMarkup(inline_keyboard=buttons)