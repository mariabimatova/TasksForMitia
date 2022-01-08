'''
Задание 9. Работа с объектами. Осторожней с оператором присваивания.

1. Создать новый файл answer9.txt.

2. Создаем только один класс - Human.
Можно скопировать описание класса отсюда:

class Human:
    def __init__(self, n, g, a):
        self.name = n
        self.gender = g
        self.age = a

3. Создать два объекта классa Human.
Вывести их имена на экран

h1 = Human('anya', 'F', 20)
h2 = Human('vova', 'M', 25)
print(h1.name)
print(h2.name)

4. Запустить программу. Убедиться, что на экран выводится:
anya
vova

5. Если мы заводим ЕЩË одну переменную h3, и присваиваем ее h1,
то сам объект НЕ копируется, а обе переменные h1 и h3 указывают на ОДИН и ТОТ ЖЕ объект.

Добавить в код:

h3 = h1
h3.name = 'masha'
print(h3.name)
print(h1.name)

6. Запустить программу. Убедиться, что на экран выводится:

Сначала - как в 4
anya
vova

Потом - то что мы добавили в 5
masha
masha

7. Если же мы теперь будем изменять имя объекта h1, то h3 тоже изменится!
Потому что обе переменные указывают на ОДНО и ТО ЖЕ значение (на один и тот же объект):

Добавить в код:

h1.name = 'olya'
print(h1.name)
print(h3.name)

8. Запустить программу. Убедиться, что на экран выводится:

anya
vova
masha
masha
olya
olya

'''

class Human:
    def __init__(self, n, g, a):
        self.name = n
        self.gender = g
        self.age = a

h1 = Human('anya', 'F', 20)
h2 = Human('vova', 'M', 25)
print(h1.name)
print(h2.name)

h3 = h1
h3.name = 'masha'
print(h3.name)
print(h1.name)

h1.name = 'olya'
print(h1.name)
print(h3.name)



