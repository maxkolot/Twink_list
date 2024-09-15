# statistics.py

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message
from data.messages import MESSAGES
from services.statistics import get_total_list_audience, get_total_bot_audience, generate_list_preview

router = Router()

@router.message(Command("audlist"))
async def audlist_handler(message: Message, user: User):
    lang = user.language
    total_audience = await get_total_list_audience()
    await message.answer(MESSAGES["audlist"][lang].format(total=total_audience))

@router.message(Command("audbot"))
async def audbot_handler(message: Message, user: User):
    lang = user.language
    total_users = await get_total_bot_audience()
    await message.answer(MESSAGES["audbot"][lang].format(total=total_users))

@router.message(Command("showme"))
async def showme_handler(message: Message, user: User):
    lang = user.language
    list_preview = await generate_list_preview(lang)
    await message.answer(list_preview)
