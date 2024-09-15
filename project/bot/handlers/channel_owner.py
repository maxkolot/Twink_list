# channel_owner.py

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from models.channel import Channel
from models.user import User
from utils.helpers import create_pdf_report

router = Router()

@router.message(Command("my_projects"))
async def my_projects_handler(message: Message, user: User):
    channels = await Channel.filter(user=user)
    if channels:
        keyboard = InlineKeyboardMarkup()
        for channel in channels:
            keyboard.add(
                InlineKeyboardButton(
                    text=channel.name,
                    callback_data=f"channel_{channel.id}"
                )
            )
        await message.answer("Ваши проекты:", reply_markup=keyboard)
    else:
        await message.answer("У вас нет добавленных каналов.")

@router.callback_query(lambda c: c.data.startswith("channel_"))
async def channel_options(callback_query: CallbackQuery):
    channel_id = int(callback_query.data.split("_")[1])
    channel = await Channel.get_or_none(id=channel_id)
    if channel:
        keyboard = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="Добавить 🔥 к названию", callback_data=f"add_fire_{channel_id}")
            ],
            [
                InlineKeyboardButton(text="Статистика", callback_data=f"stats_{channel_id}")
            ]
        ])
        await callback_query.message.edit_text(f"Опции для канала {channel.name}:", reply_markup=keyboard)
        await callback_query.answer()

@router.callback_query(lambda c: c.data.startswith("add_fire_"))
async def add_fire(callback_query: CallbackQuery, user: User):
    channel_id = int(callback_query.data.split("_")[2])
    channel = await Channel.get_or_none(id=channel_id)
    if channel:
        # Создаем транзакцию для оплаты
        # Реализуйте логику оплаты
        channel.promo_fire = True
        # Устанавливаем дату окончания через 2 недели
        channel.promo_fire_expiration_date = datetime.now() + timedelta(weeks=2)
        await channel.save()
        await callback_query.message.answer("🔥 добавлен к вашему каналу на 2 недели!")
        await callback_query.answer()
