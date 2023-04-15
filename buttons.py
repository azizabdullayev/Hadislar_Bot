from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start_1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Namoz vaqtlarini bilish⏳"),
            KeyboardButton(text="Hadislar📖")
        ],
    ],
    resize_keyboard=True
)
start_2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Afg'oniston"),
            KeyboardButton(text="Qozog'iston"),
            KeyboardButton(text="Qizg'iziston")
        ],
        [
            KeyboardButton(text="Tojikiston"),
            KeyboardButton(text="Turkmaniston"),
            KeyboardButton(text="O'zbekiston")
        ],
        [
            KeyboardButton(text="Ortga  qaytish")
        ]
    ],
    resize_keyboard=True
)
start_3 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Ortga qaytish")
        ]
    ],
    resize_keyboard=True
)
start_4 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bosh sahifaga qaytish")
        ]
    ],
    resize_keyboard=True
)