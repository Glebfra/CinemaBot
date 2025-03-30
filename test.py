import re

string = "'Лист1'!A1:Z1000"
match = re.search(r'([A-Z]+\d+):([A-Z]+\d+)', string)

if match:
    start_cell, end_cell = match.groups()
    print("Начальная ячейка:", start_cell)
    print("Конечная ячейка:", end_cell)

list1 = ['1', '2', '3']
list2 = [1, 2, 3]
print(dict(zip(list1, list2)))
