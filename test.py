import re

import validators

string = "'Лист1'!A1:Z1000"
match = re.search(r'([A-Z]+\d+):([A-Z]+\d+)', string)

if match:
    start_cell, end_cell = match.groups()
    print("Начальная ячейка:", start_cell)
    print("Конечная ячейка:", end_cell)

list1 = ['1', '2', '3']
list2 = [1, 2, 3]
print(dict(zip(list1, list2)))


url = "https://docs.google.com/spreadsheets/d/1f71Sg5VRWk5S0IOIhifKjCCHMdWbwwOnzZTE-5uA7iM/edit?gid=0#gid=0"

# Регулярное выражение
pattern = r"/d/([a-zA-Z0-9-_]+)"

# Поиск ID таблицы
match = re.search(pattern, url)

if match:
    sheet_id = match.group(1)
    print("Google Sheet ID:", sheet_id)
else:
    print("ID не найден.")