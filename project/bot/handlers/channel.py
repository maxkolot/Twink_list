# channel.py

from aiogram import Router, types
from aiogram.types import ChatMemberUpdated, Message
from aiogram.utils.exceptions import ChatAdminRequired

from models.user import User
from models.channel import Channel, TemporaryChannel
from utils.helpers import generate_password
from config import ADMIN_ID

router = Router()

# Обработчик добавления бота в канал/группу
@router.my_chat_member()
async def my_chat_member_handler(chat_member_update: ChatMemberUpdated):
    if chat_member_update.chat.type in ['supergroup', 'channel']:
        if chat_member_update.new_chat_member.status == 'administrator':
            channel_id = chat_member_update.chat.id
            user_id = chat_member_update.from_user.id

            # Проверяем права бота в канале
            bot_permissions = chat_member_update.new_chat_member
            required_permissions = ['can_post_messages', 'can_edit_messages', 'can_invite_users', 'can_manage_chat', 'can_pin_messages']
            for perm in required_permissions:
                if not getattr(bot_permissions, perm, False):
                    # Уведомляем пользователя о недостаточных правах
                    await chat_member_update.bot.send_message(
                        chat_id=user_id,
                        text="У бота недостаточно прав. Пожалуйста, предоставьте все необходимые права."
                    )
                    return

            # Проверяем, есть ли пользователь в базе данных
            user = await User.get_or_none(user_id=user_id)
            if not user:
                user = await User.create(user_id=user_id, language='ru', status='active')

            # Создаем временную связку в БД
            password = generate_password()
            temp_channel = await TemporaryChannel.create(
                channel_id=channel_id,
                password=password,
                user=user,
                expires_at=None  # Установите время истечения при необходимости
            )

            # Отправляем пользователю сообщение с инструкциями
            instruction = f"Чтобы завершить добавление канала в список, отправьте в свой канал сообщение:\n\n<code>/add {password}</code>"
            await chat_member_update.bot.send_message(chat_id=user_id, text=instruction)

# Обработчик команды /add в канале
@router.message(Command("add"))
async def add_channel_handler(message: Message):
    if message.chat.type in ['supergroup', 'channel']:
        args = message.get_args()
        if not args:
            return
        password = args.strip()

        # Ищем временную связку по channel_id и password
        temp_channel = await TemporaryChannel.get_or_none(
            channel_id=message.chat.id,
            password=password
        )
        if temp_channel:
            # Удаляем сообщение
            try:
                await message.delete()
            except ChatAdminRequired:
                pass  # Бот должен иметь права на удаление сообщений

            # Создаем постоянную запись канала в БД
            channel, created = await Channel.get_or_create(
                channel_id=message.chat.id,
                defaults={
                    'name': message.chat.title,
                    'link': message.chat.username or '',
                    'user': temp_channel.user,
                    'status': 'free',
                    'date_expiration': None
                }
            )
            if not created:
                channel.status = 'free'
                channel.date_expiration = None
                await channel.save()

            # Удаляем временную запись
            await temp_channel.delete()

            # Генерируем ссылку с запросами на вступление (если необходимо)

            # Отправляем подтверждение пользователю
            await message.bot.send_message(
                chat_id=channel.user.user_id,
                text="Канал успешно добавлен в список!"
            )
