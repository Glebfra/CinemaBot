from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


def get_inline_keyboard():
    keyword = InlineKeyboardMarkup()
    keyword.add(InlineKeyboardButton('Подробнее', callback_data='detailed_movies_btn'))
    return keyword


def get_default_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_names = ['Фильмы', 'Таблицы']
    buttons = [KeyboardButton(name) for name in button_names]
    keyboard.add(*buttons)
    return keyboard


def get_cancel_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_names = ['Отмена']
    buttons = [KeyboardButton(name) for name in button_names]
    keyboard.add(*buttons)
    return keyboard
