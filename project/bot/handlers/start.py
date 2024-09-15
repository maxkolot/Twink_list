# start.py

from aiogram import Router, types, Bot
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from data.messages import MESSAGES, BUTTONS
from models.user import User
from utils.commands import set_user_commands

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message, lang: str = None, user: User = None):
    if not lang:
        # Если язык не установлен, предлагаем выбрать язык
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text=BUTTONS["language_selection"]["ru"]["rus"], callback_data="lang_ru"),
                InlineKeyboardButton(text=BUTTONS["language_selection"]["ru"]["eng"], callback_data="lang_en"),
            ]
        ])
        await message.answer(MESSAGES["choose_language"]["ru"], reply_markup=keyboard)
    else:
        # Формируем клавиатуру в зависимости от языка
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=BUTTONS["main_menu"][lang]["channel"],
                    url=f"http://t.me/{message.bot.username}?startchannel&admin=post_messages+edit_messages+invite_users+manage_chat+restrict_members"
                ),
                InlineKeyboardButton(
                    text=BUTTONS["main_menu"][lang]["group"],
                    url=f"http://t.me/{message.bot.username}?startgroup&admin=post_messages+edit_messages+invite_users+manage_chat+restrict_members"
                ),
            ],
            [InlineKeyboardButton(text=BUTTONS["main_menu"][lang]["vip_tariff"], callback_data="VIP")]
        ])
        await message.answer(MESSAGES["start"][lang], reply_markup=keyboard)

# Обработчик выбора языка
@router.callback_query(lambda c: c.data.startswith("lang_"))
async def change_language(callback_query: CallbackQuery, user: User):
    lang_code = callback_query.data.split("_")[1]
    if lang_code not in ['ru', 'en']:
        lang_code = 'ru'

    # Обновляем язык пользователя в базе данных
    user.language = lang_code
    await user.save()

    # Обновляем команды бота для пользователя
    await set_user_commands(user_id=user.user_id, lang=lang_code)

    # Отправляем приветственное сообщение на выбранном языке
    await start_handler(callback_query.message, lang=lang_code, user=user)
    await callback_query.answer()
