# statistics.py

from models.channel import Channel
from models.user import User

async def get_total_list_audience():
    channels = await Channel.filter(status__in=['free', 'vip'])
    total_audience = 0
    for channel in channels:
        total_audience += channel.subscribers_count
    return total_audience

async def get_total_bot_audience():
    total_users = await User.filter(status='active').count()
    return total_users

async def generate_list_preview(lang='ru'):
    # Логика генерации листа
    channels = await Channel.filter(status__in=['free', 'vip']).order_by('-subscribers_count')
    list_text = "Актуальный лист:\n\n"
    for channel in channels:
        list_text += f"🔗 {channel.name} ({channel.link})\n"
    return list_text

from models.channel_statistic import ChannelStatistic
from models.channel import Channel
from datetime import date

async def update_statistics():
    """Обновление статистики каналов"""
    channels = await Channel.filter(status__in=['free', 'vip'])
    
    for channel in channels:
        # Пример обновления количества подписчиков (нужно интегрировать с API Telegram для получения подписчиков)
        current_subscribers = channel.subscribers_count  # Заглушка
        await ChannelStatistic.create(
            channel=channel,
            date=date.today(),
            subscribers_count=current_subscribers,
            joins_from_bot=0,  # Заглушка
            joins_from_list=0  # Заглушка
        )
