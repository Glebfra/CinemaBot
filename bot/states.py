from telebot.states import State, StatesGroup


class SpreadsheetStates(StatesGroup):
    Spreadsheets = State()
    AddSpreadsheets = State()
    EditSpreadsheets = State()


class DefaultStates(StatesGroup):
    Default = State()
