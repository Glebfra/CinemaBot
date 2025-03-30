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
    await telegram_bot.reply_to(message, answers.start_answer, reply_markup=keyboards.get_default_keyboard())


@telegram_bot.message_handler(state=SpreadsheetStates.Spreadsheets, func=lambda message: True)
async def spreadsheets(message: Message, state: StateContext):
    text = message.text.lower()
    if text == 'отмена':
        return await cancel_process(message, state)

    if text == 'добавить':
        await state.set(SpreadsheetStates.AddSpreadsheets)

    if text == 'редактировать':
        await state.set(SpreadsheetStates.EditSpreadsheets)


@telegram_bot.message_handler(state=DefaultStates.Default, func=lambda message: True)
async def handle_message(message: Message, state: StateContext):
    text = message.text.lower()

    if text == 'фильмы':
        await telegram_bot.reply_to(message, answers.movies_answer)
        answer = ''
        for movie in Movie.select():
            answer += f'{movie.name}\n'
        return await telegram_bot.reply_to(message, answer, reply_markup=keyboards.get_default_keyboard())

    if text == 'таблицы':
        await state.set(SpreadsheetStates.Spreadsheets)
        await telegram_bot.reply_to(message, answers.spreadsheets_answer)

        answer, i = '', 0
        for spreadsheet in SpreadSheet.select():
            answer += f'{i}: {spreadsheet.spreadsheet_id}\n'
            i += 1
        return await telegram_bot.reply_to(message, answer, reply_markup=keyboards.get_cancel_keyboard())


async def cancel_process(message, state: StateContext):
    await state.set(DefaultStates.Default)
    await telegram_bot.send_message(
        message.chat.id, "Операция отменена.", reply_markup=keyboards.get_default_keyboard()
    )
