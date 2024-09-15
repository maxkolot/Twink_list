# referral.py

from aiogram import Router, types
from aiogram.filters import Command
from models.user import User

router = Router()

@router.message(Command("referral"))
async def referral_handler(message: types.Message, user: User):
    referral_link = f"http://t.me/{message.bot.username}?start={user.user_id}"
    await message.answer(f"Ваша реферальная ссылка: {referral_link}")
