from models.channel import Channel
from aiogram import Bot
from config import ADD_CHANNEL_LINK

async def send_daily_list(bot: Bot):
    """Отправка листа каналов в заданные группы"""
    channels = await Channel.filter(status__in=['free', 'vip']).order_by('-subscribers_count')
    
    message_text = "-----------------------\n"
    message_text += "НАЗВАНИЕ ЛИСТА 🎯\n"
    message_text += "-----------------------\n"

    for channel in channels:
        message_text += f"┏▷ {channel.name} - {channel.subscribers_count} подписчиков\n"
        message_text += f"┣ 🔗 {channel.link}\n"

    message_text += f"📢 МЕСТО ДЛЯ РЕКЛАМНОГО ПОСТА 📢\n"
    message_text += f"🔄 РАБОТА ({ADD_CHANNEL_LINK})\n"
    # ... остальные блоки текста

    # Отправка листа в указанные группы (пример)
    groups = await Channel.filter(status='group')  # Пример фильтрации групп
    for group in groups:
        await bot.send_message(chat_id=group.channel_id, text=message_text)
