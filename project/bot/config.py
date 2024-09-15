import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

# Настройки базы данных
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME')

# Настройки логирования
LOGGING_LEVEL = os.getenv('LOGGING_LEVEL', 'INFO')

# Переменные для платежей
PAYMENT_PROVIDER_TOKEN = os.getenv('PAYMENT_PROVIDER_TOKEN')

# Ссылки для списка (работа и др.)
WORK_LINK = os.getenv('WORK_LINK')
PROMO_LINK = os.getenv('PROMO_LINK')
ADD_CHANNEL_LINK = os.getenv('ADD_CHANNEL_LINK')

# Настройки администратора
ADMIN_ID = int(os.getenv('ADMIN_ID'))

# Другие настройки
TIMEZONE = os.getenv('TIMEZONE', 'Europe/Moscow')

DB_CONFIG = {
    'connections': {
        'default': {
            'engine': 'tortoise.backends.asyncpg',
            'credentials': {
                'host': os.getenv('DB_HOST', 'localhost'),
                'port': '5432',
                'user': os.getenv('DB_USER'),
                'password': os.getenv('DB_PASSWORD'),
                'database': os.getenv('DB_NAME'),
            }
        }
    },
    'apps': {
        'models': {
            'models': [
                'models.user',
                'models.channel',
                'models.temporary_channel',
                'models.transaction',
                'models.advertisement',
                'models.scheduled_task',
                'models.promo',
                'models.referral',
                'models.channel_statistic',
                'models.user_statistic',
                'aerich.models'  # Если используете Aerich для миграций
            ],
            'default_connection': 'default',
        }
    }
}

