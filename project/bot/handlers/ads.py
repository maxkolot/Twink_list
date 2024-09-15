# ads.py

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message
from models.user import User
from models.advertisement import Advertisement
from data.messages import MESSAGES
from config import ADMIN_ID
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

router = Router()

class AdvertisementState(StatesGroup):
    waiting_for_ad = State()
    waiting_for_buttons = State()
    waiting_for_confirmation = State()

@router.message(Command("adsbot"))
async def adsbot_handler(message: Message, state: FSMContext, user: User):
    lang = user.language
    await message.answer(MESSAGES["adsbot"][lang])
    await state.set_state(AdvertisementState.waiting_for_ad)
    await state.update_data(ad_type='ads_in_bot')

@router.message(Command("adslist"))
async def adslist_handler(message: Message, state: FSMContext, user: User):
    lang = user.language
    await message.answer(MESSAGES["adslist"][lang])
    await state.set_state(AdvertisementState.waiting_for_ad)
    await state.update_data(ad_type='ads_in_list')

@router.message(AdvertisementState.waiting_for_ad, content_types=types.ContentType.ANY)
async def receive_ad(message: Message, state: FSMContext, user: User):
    data = await state.get_data()
    ad_type = data.get('ad_type')

    # Сохраняем медиа и описание
    media_id = None
    if message.content_type == 'photo':
        media_id = message.photo[-1].file_id
    elif message.content_type == 'video':
        media_id = message.video.file_id
    # Добавьте обработку других типов контента при необходимости

    ad = await Advertisement.create(
        user=user,
        ad_type=ad_type,
        description=message.caption or message.text,
        media_id=media_id,
        status='pending'
    )

    # Отправляем админу на проверку
    admin_message = f"Новая реклама от пользователя {user.user_id}.\nID рекламы: {ad.id}"
    await message.bot.send_message(chat_id=ADMIN_ID, text=admin_message)
    await message.copy_to(chat_id=ADMIN_ID)

    await message.answer("Спасибо! Ваше объявление отправлено на проверку.")
    await state.clear()
