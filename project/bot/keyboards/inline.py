# inline.py

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.messages import BUTTONS

def main_menu_keyboard(lang: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=BUTTONS["main_menu"][lang]["channel"],
                callback_data="channel"
            ),
            InlineKeyboardButton(
                text=BUTTONS["main_menu"][lang]["group"],
                callback_data="group"
            )
        ],
        [
            InlineKeyboardButton(
                text=BUTTONS["main_menu"][lang]["vip_tariff"],
                callback_data="VIP"
            )
        ],
        [
            InlineKeyboardButton(
                text=BUTTONS["main_menu"][lang]["add_channel"],
                callback_data="add_channel"
            )
        ],
        [
            InlineKeyboardButton(
                text=BUTTONS["main_menu"][lang]["statistics"],
                callback_data="statistics"
            ),
            InlineKeyboardButton(
                text=BUTTONS["main_menu"][lang]["change_language"],
                callback_data="change_language"
            )
        ]
    ])
