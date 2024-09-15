# user_middleware.py

from typing import Any, Awaitable, Callable, Dict

from aiogram import types
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from models.user import User

class UserMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[types.TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: types.TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        if isinstance(event, (types.Message, types.CallbackQuery)):
            user_id = event.from_user.id

            # Проверяем, существует ли пользователь в базе данных
            user = await User.get_or_none(user_id=user_id)
            if not user:
                # Если пользователь не существует, создаем его с языком по умолчанию ('ru')
                user = await User.create(user_id=user_id, language='ru', status='active')

            # Получаем язык пользователя
            data['lang'] = user.language

            # Добавляем пользователя в data для возможного использования
            data['user'] = user

        return await handler(event, data)
