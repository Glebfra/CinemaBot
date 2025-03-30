import re

import validators
from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_storage import StateMemoryStorage
from telebot.states.asyncio import StateContext
from telebot.types import Message

from bot import answers, keyboards
from bot.config import TOKEN
from bot.states import DefaultStates, SpreadsheetStates
from db.Movie import Movie
from db.SpreadSheet import SpreadSheet

state_storage = StateMemoryStorage()
telegram_bot = AsyncTeleBot(TOKEN, state_storage=state_storage)


@telegram_bot.message_handler(commands=['start'])
async def start(message: Message, state: StateContext):
    await state.set(DefaultStates.Default)
    await telegram_bot.reply_to(message, answers.start, reply_markup=keyboards.get_default_keyboard())


@telegram_bot.message_handler(state=DefaultStates.Default, func=lambda message: True)
async def handle_default_message(message: Message, state: StateContext):
    text = message.text.lower()

    if text == 'фильмы':
        await telegram_bot.reply_to(message, answers.movies)
        answer = ''
        for movie in Movie.select():
            answer += f'{movie.name}\n'
        return await telegram_bot.reply_to(message, answer, reply_markup=keyboards.get_default_keyboard())

    if text == 'таблицы':
        await state.set(SpreadsheetStates.Spreadsheets)

        answer, i = f'{answers.spreadsheets}\n', 0
        for spreadsheet in SpreadSheet.select():
            answer += f'{i}: {spreadsheet.url}\n'
            i += 1
        return await telegram_bot.reply_to(message, answer, reply_markup=keyboards.get_spreadsheets_keyboard())


@telegram_bot.message_handler(state=SpreadsheetStates.Spreadsheets, func=lambda message: True)
async def spreadsheets(message: Message, state: StateContext):
    text = message.text.lower()
    if text == 'отмена':
        return await cancel_process(message, state)

    if text == 'добавить':
        await state.set(SpreadsheetStates.AddSpreadsheets)
        return await telegram_bot.reply_to(
            message, answers.add_spreadsheets, reply_markup=keyboards.get_cancel_keyboard()
        )

    if text == 'редактировать':
        await state.set(SpreadsheetStates.EditSpreadsheets)
        return await telegram_bot.reply_to(
            message, answers.edit_spreadsheets, reply_markup=keyboards.get_cancel_keyboard()
        )

    if text == 'удалить':
        await state.set(SpreadsheetStates.DeleteSpreadsheets)
        return await telegram_bot.reply_to(
            message, answers.delete_spreadsheets, reply_markup=keyboards.get_cancel_keyboard()
        )


@telegram_bot.message_handler(state=SpreadsheetStates.AddSpreadsheets, func=lambda message: True)
async def add_spreadsheets(message: Message, state: StateContext):
    text = message.text
    if text.lower() == 'отмена':
        return await cancel_process(message, state)

    if not validators.url(text):
        await telegram_bot.reply_to(message, answers.add_spreadsheets_url_error)
        return await cancel_process(message, state)

    match = re.search('/d/([a-zA-Z0-9-_]+)', text)
    if not match:
        await telegram_bot.reply_to(message, answers.add_spreadsheets_spreadsheet_id_error)
        return await cancel_process(message, state)

    spreadsheet, created = SpreadSheet.get_or_create(url=text, spreadsheet_id=match.group(1))
    if not created:
        await telegram_bot.reply_to(message, answers.add_spreadsheets_exists_error)
        return await cancel_process(message, state)

    spreadsheet.save()
    await state.delete()
    return await telegram_bot.reply_to(message, answers.add_spreadsheets_success, reply_markup=keyboards.get_default_keyboard())


async def cancel_process(message, state: StateContext):
    await state.set(DefaultStates.Default)
    return await telegram_bot.send_message(message.chat.id, answers.cancel, reply_markup=keyboards.get_default_keyboard())
