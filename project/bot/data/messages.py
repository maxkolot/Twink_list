# messages.py

# Сообщения для бота
MESSAGES = {
    "start": {
        "ru": """
Привет! 👋 Меня зовут Твист, я руководитель листа продвижения.

Ты можешь добавить свой канал или группу для продвижения и получить доступ к нашей огромной аудитории! 🔥

Также у нас есть платный тариф без публикации в твоем канале. Если интересно, расскажу подробнее! 💬

<a href="https://t.me/GPORNLIST/2">ПРОЧИТАЙТЕ ПРАВИЛА</a>""",
        "en": """
Hi! 👋 My name is Twist, and I'm the manager of the promotion list.

You can add your channel or group for promotion and gain access to our massive audience! 🔥

We also offer a paid plan that doesn't require posting in your channel. If you're interested, I can tell you more! 💬

<a href="https://t.me/GPORNLIST/2">READ THE RULES</a>"""
    },
    "choose_language": {
        "ru": "ВЫБЕРИ СВОЙ ЯЗЫК\nCHOOSE YOUR LANGUAGE",
        "en": "CHOOSE YOUR LANGUAGE\nВЫБЕРИ СВОЙ ЯЗЫК"
    },
    "change_language": {
        "ru": "Язык переключен на русский 🇷🇺",
        "en": "Language switched to English 🇬🇧"
    },
    "showme": {
        "ru": "Вот актуальный лист: 📋\n\nЗдесь будет информация о текущем листе продвижения.",
        "en": "Here is the current list: 📋\n\nThis is where information about the current promotion list will be."
    },
    "audlist": {
        "ru": "Общая аудитория списка: {total} подписчиков",
        "en": "Total audience of the list: {total} subscribers"
    },
    "audbot": {
        "ru": "Общая аудитория бота: {total} пользователей",
        "en": "Total audience of the bot: {total} users"
    },
    "adsbot": {
        "ru": "Ты можешь заказать рекламу в боте. Пожалуйста, пришли мне свой пост (медиа + описание). 📩",
        "en": "You can order advertising in the bot. Please send me your post (media + description). 📩"
    },
    "adslist": {
        "ru": "Ты можешь заказать рекламу в списке. Пожалуйста, пришли мне свой пост (фото + описание). 📩",
        "en": "You can order advertising in the list. Please send me your post (photo + description). 📩"
    },
    "promo": {
        "ru": "Пожалуйста, отправь промо пост (фото/видео/медиагруппа). 📷🎥",
        "en": "Please send the promo post (photo/video/media group). 📷🎥"
    },
    "smm": {
        "ru": "Пожалуйста, отправь пост для рассылки всем подписчикам. ✉️",
        "en": "Please send the post for distribution to all subscribers. ✉️"
    },
    "no_permission": {
        "ru": "У тебя нет прав для использования этой команды. 🚫",
        "en": "You don't have permission to use this command. 🚫"
    },
    "blocked_bot": {
        "ru": "Ты заблокировал бота. 😔 Если передумаешь, я всегда здесь!",
        "en": "You've blocked the bot. 😔 If you change your mind, I'm always here!"
    },
    "unblocked_bot": {
        "ru": "Ты разблокировал бота. Рад видеть тебя снова! 😊",
        "en": "You've unblocked the bot. Happy to see you back! 😊"
    },
    "bot_added": {
        "ru": "Бот добавлен в канал или группу. 👍",
        "en": "Bot added to the channel or group. 👍"
    },
    "payment_request": {
        "ru": "Выберите способ оплаты: 💳 или ⭐",
        "en": "Choose a payment method: 💳 or ⭐"
    },
    "payment_confirm": {
        "ru": "Платеж подтвержден. Пожалуйста, отправь свою ссылку и название канала.",
        "en": "Payment confirmed. Please send your channel link and name."
    },
    "promo_fire_activated": {
        "ru": "🔥 Промо-огонь добавлен к твоему каналу на 2 недели!",
        "en": "🔥 Promo fire added to your channel for 2 weeks!"
    }
}

# Кнопки для бота
BUTTONS = {
    "main_menu": {
        "ru": {
            "channel": "Канал",
            "group": "Группа",
            "vip_tariff": "🔥VIP ТАРИФ🔥",
            "add_channel": "➕ Добавить канал",
            "statistics": "📊 Статистика",
            "change_language": "Поменять язык"
        },
        "en": {
            "channel": "Channel",
            "group": "Group",
            "vip_tariff": "🔥VIP TARIFF🔥",
            "add_channel": "➕ Add channel",
            "statistics": "📊 Statistics",
            "change_language": "Change language"
        }
    },
    "language_selection": {
        "ru": {
            "rus": "Русский 🇷🇺",
            "eng": "English 🇬🇧"
        },
        "en": {
            "rus": "Русский 🇷🇺",
            "eng": "English 🇬🇧"
        }
    },
    "payment_methods": {
        "ru": {
            "semi_auto": "💳 Полуавтоматический перевод",
            "telegram_stars": "⭐ Оплатить звездами Telegram"
        },
        "en": {
            "semi_auto": "💳 Semi-automatic transfer",
            "telegram_stars": "⭐ Pay with Telegram stars"
        }
    },
    "payment_confirmation": {
        "ru": {
            "spam": "Спам ❌",
            "confirm": "Подтвердить ✅"
        },
        "en": {
            "spam": "Spam ❌",
            "confirm": "Confirm ✅"
        }
    },
    "vip_subscription": {
        "ru": {
            "pay": "Оплатить VIP тариф",
            "back": "Назад"
        },
        "en": {
            "pay": "Pay VIP tariff",
            "back": "Back"
        }
    },
    "date_selection": {
        "ru": {
            "today": "Сегодня",
            "tomorrow": "Завтра",
            "select_date": "Выбрать дату",
            "now": "Сейчас"
        },
        "en": {
            "today": "Today",
            "tomorrow": "Tomorrow",
            "select_date": "Select date",
            "now": "Now"
        }
    },
    "time_selection": {
        "ru": {
            "00_05": "00:05",
            "00_30": "00:30",
            "01_00": "01:00",
            "01_30": "01:30"
            # и т.д.
        },
        "en": {
            "00_05": "00:05",
            "00_30": "00:30",
            "01_00": "01:00",
            "01_30": "01:30"
            # и т.д.
        }
    },
    "back_button": {
        "ru": "⬅️ Назад",
        "en": "⬅️ Back"
    }
}
