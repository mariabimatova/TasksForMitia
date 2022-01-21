cook_book = {
    'Омлет': [
        {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
        {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
        {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
    'Утка по-пекински': [
        {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
        {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
        {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
        {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
    'Запеченный картофель': [
        {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
        {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
        {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
}

# read all lines from file
lines = []
filename = 'data-netology.txt'
with open(filename) as f:
    print(f"Reading from file: {filename}")
    lines = f.readlines()
    print(f"Read {len(lines)} lines")

# print all lines
for line in lines:
    print(line, end='')

# you can try processing lines in data list
data = [
    'Омлет\n',
    '3\n',
    'Яйцо | 2 | шт\n',
    'Молоко | 100 | мл\n',
    'Помидор | 2 | шт\n',
    '\n',
    'Утка по-пекински\n',
    '4\n',
    'Утка | 1 | шт\n',
    'Вода | 2 | л\n',
    'Мед | 3 | ст.л\n',
    'Соевый соус | 60 | мл\n',
    '\n',
    'Запеченный картофель\n',
    '3\n',
    'Картофель | 1 | кг\n',
    'Чеснок | 3 | зубч\n',
    'Сыр гауда | 100 | г\n',
    '\n',
    'Фахитос\n',
    '5\n',
    'Говядина | 500 | г\n',
    'Перец сладкий | 1 | шт\n',
    'Лаваш | 2 | шт\n',
    'Винный уксус | 1 | ст.л\n',
    'Помидор | 2 | шт\n',
]
