# scheduler.py

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from services.list_generator import send_daily_list
from services.statistics import update_statistics

scheduler = AsyncIOScheduler()

def setup_scheduler():
    scheduler.add_job(send_daily_list, 'cron', hour=10, timezone='Europe/Moscow')
    scheduler.add_job(update_statistics, 'interval', hours=1)
    scheduler.start()
