'''Задание 5. Добавление информации в файл.

Задание.
1) Открыть файл out_append.txt и добавить туда только одну строчку,
содержащую текущее время.
2) Запустить программу несколько раз и убедиться, что файл out_append.txt
содержит несколько строк!

Для открытия файла использовать режим 'a':
open('myfile.txt', 'a')

Для открытия файла использовать конструкцию with.

Для того, чтобы получить текущее время можно использовать следующий код:

# import library - should be in the beginning of file
from datetime import datetime

# now we have time in variable called "now"
now = datetime.now().time()

# you don't need that, but just to make sure
print(f"now = {now}")'''

with open ('out_append.txt','a') as file:
    file.write('qqqqqq')

with open ('out_append.txt') as file:
    for line in file:
        print(line)

