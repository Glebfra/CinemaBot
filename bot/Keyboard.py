from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup


class Keyboard:
    @staticmethod
    def get_inline_keyboard():
        keyword = InlineKeyboardMarkup()
        keyword.add(InlineKeyboardButton('Подробнее', callback_data='detailed_movies_btn'))
        return keyword

    @staticmethod
    def get_default_keyboard():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(KeyboardButton('Фильмы'))
        return keyboard
