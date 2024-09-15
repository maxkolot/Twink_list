# vip.py

from aiogram import Router, types
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from models.user import User
from models.transaction import Transaction
from config import ADMIN_ID
from data.messages import MESSAGES, BUTTONS
from utils.payment import process_payment

router = Router()

@router.callback_query(lambda c: c.data == "VIP")
async def vip_tariff_handler(callback_query: CallbackQuery, user: User):
    lang = user.language
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text=BUTTONS["payment_methods"][lang]["semi_auto"], callback_data="pay_semi_auto"),
            InlineKeyboardButton(text=BUTTONS["payment_methods"][lang]["telegram_stars"], callback_data="pay_telegram_stars")
        ],
        [
            InlineKeyboardButton(text=BUTTONS["back_button"][lang], callback_data="back_to_main")
        ]
    ])
    await callback_query.message.edit_text(MESSAGES["payment_request"][lang], reply_markup=keyboard)
    await callback_query.answer()

@router.callback_query(lambda c: c.data.startswith("pay_"))
async def process_vip_payment(callback_query: CallbackQuery, user: User):
    lang = user.language
    payment_method = callback_query.data.split("_")[1]

    # Создаем транзакцию в БД
    transaction = await Transaction.create(
        user=user,
        amount=800.00,  # Укажите стоимость VIP тарифа
        payment_method=payment_method,
        status='pending',
        transaction_type='vip_subscription'
    )

    if payment_method == 'semi_auto':
        # Отправляем реквизиты для оплаты
        payment_details = "Реквизиты для оплаты:\nКарта: 1234 5678 9012 3456\nСумма: 800₽"
        await callback_query.message.answer(payment_details)

        # Уведомляем администратора о новом платеже
        admin_text = f"Новая заявка на оплату VIP тарифа от пользователя {user.user_id}.\nТранзакция ID: {transaction.id}"
        await callback_query.bot.send_message(chat_id=ADMIN_ID, text=admin_text)
    elif payment_method == 'telegram_stars':
        # Реализуйте оплату через звезды Telegram, если возможно
        pass

    await callback_query.answer()

# Обработчик подтверждения платежа администратором
@router.message(commands=['confirm_payment'])
async def confirm_payment_handler(message: Message):
    if message.from_user.id != ADMIN_ID:
        return

    args = message.get_args()
    if not args:
        await message.answer("Укажите ID транзакции для подтверждения.")
        return

    transaction_id = int(args.strip())
    transaction = await Transaction.get_or_none(id=transaction_id)
    if transaction and transaction.status == 'pending':
        transaction.status = 'confirmed'
        await transaction.save()

        # Обновляем статус пользователя и канала
        user = transaction.user
        user.status = 'vip'
        await user.save()

        # Уведомляем пользователя
        await message.bot.send_message(
            chat_id=user.user_id,
            text=MESSAGES["payment_confirm"][user.language]
        )
    else:
        await message.answer("Транзакция не найдена или уже подтверждена.")
