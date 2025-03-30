from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

SPREADSHEETS_KEYBOARD_NAMES = ['Добавить', 'Редактировать', 'Удалить', 'Отмена']
DEFAULT_KEYBOARD_NAMES = ['Фильмы', 'Таблицы']
CANCEL_KEYBOARD_NAMES = ['Отмена']


def get_default_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [KeyboardButton(name) for name in DEFAULT_KEYBOARD_NAMES]
    keyboard.add(*buttons)
    return keyboard


def get_spreadsheets_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [KeyboardButton(name) for name in SPREADSHEETS_KEYBOARD_NAMES]
    keyboard.add(*buttons)
    return keyboard


def get_cancel_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [KeyboardButton(name) for name in CANCEL_KEYBOARD_NAMES]
    keyboard.add(*buttons)
    return keyboard
