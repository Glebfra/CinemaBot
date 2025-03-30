import asyncio

from telebot.asyncio_filters import StateFilter
from telebot.states.asyncio import StateMiddleware

from bot.handlers import telegram_bot

telegram_bot.add_custom_filter(StateFilter(telegram_bot))
telegram_bot.setup_middleware(StateMiddleware(telegram_bot))

asyncio.run(telegram_bot.polling(none_stop=True))
