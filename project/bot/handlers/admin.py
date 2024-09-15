# admin.py

from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message
from models.promo import Promo
from utils.helpers import generate_promo_code
from config import ADMIN_ID

router = Router()

@router.message(Command("promo"))
async def promo_handler(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    await message.answer("Пожалуйста, отправьте промо пост (фото/видео/медиагруппа).")
    await PromoState.waiting_for_promo.set()

from aiogram.fsm.context import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class PromoState(StatesGroup):
    waiting_for_promo = State()

@router.message(PromoState.waiting_for_promo, content_types=types.ContentType.ANY)
async def receive_promo(message: Message, state: FSMContext):
    # Сохраняем промо в БД
    promo_code = generate_promo_code()
    promo = await Promo.create(
        media_id=message.photo[-1].file_id if message.photo else None,
        description=message.caption or message.text,
        code=promo_code
    )

    await message.answer(f"Промо сохранено с кодом: {promo_code}")
    await state.finish()

@router.message(Command("smm"))
async def smm_handler(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    await message.answer("Пожалуйста, отправьте пост для рассылки всем подписчикам.")
    await SMMState.waiting_for_post.set()

class SMMState(StatesGroup):
    waiting_for_post = State()

@router.message(SMMState.waiting_for_post, content_types=types.ContentType.ANY)
async def receive_smm_post(message: Message, state: FSMContext):
    # Логика рассылки всем подписчикам
    await message.answer("Пост отправлен всем подписчикам.")
    await state.finish()
