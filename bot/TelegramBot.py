import asyncio
import os

import dotenv
from telebot.async_telebot import AsyncTeleBot
from telebot.types import CallbackQuery, Message

import bot.BotAnswer as BotAnswer
from bot.Keyboard import Keyboard
from db.Material import Material
from db.Movie import Movie

dotenv.load_dotenv('../.env')
TOKEN = os.getenv('BOT_TOKEN')

telegram_bot = AsyncTeleBot(TOKEN)


@telegram_bot.message_handler(commands=['start'])
async def start(message: Message):
    return await telegram_bot.reply_to(message, BotAnswer.start_answer, reply_markup=Keyboard.get_default_keyboard())


@telegram_bot.message_handler(content_types=['text'])
async def get_text_messages(message: Message):
    if message.text.lower() == 'фильмы':
        text = BotAnswer.movies_answer
        for movie in Movie.select():
            text += f'{movie.get_id()}: {movie.name}\n'
        return await telegram_bot.reply_to(message, text, reply_markup=Keyboard.get_inline_keyboard())


@telegram_bot.callback_query_handler(func=lambda call: True)
async def callback_handler(call: CallbackQuery):
    if call.data == 'detailed_movies_btn':
        for movie in Movie.select():
            text = f'{movie.name}:\n'
            for material in Material.filter(movie_id=movie.id):
                text += f'Name: {material.name}\n'
                text += f'Status: {material.status}\n'
                text += f'Url: {material.url}\n'
                text += f'Plan: {material.plan}\n'
            await telegram_bot.send_message(call.message.chat.id, text)
        return await telegram_bot.answer_callback_query(call.id, "Более подробное описание")


if __name__ == '__main__':
    asyncio.run(telegram_bot.polling(none_stop=True))
