# events.py

from aiogram import Router, types
from aiogram.types import ChatMemberUpdated
from models.user import User
from models.channel import Channel

router = Router()

@router.my_chat_member()
async def my_chat_member_handler(chat_member_update: ChatMemberUpdated):
    # Этот обработчик уже реализован в channel.py
    pass
