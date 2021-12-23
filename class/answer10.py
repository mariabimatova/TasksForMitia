'''
Задание 10. Работа с объектами. is и ==.

Оператор is означает: это ОДНО и ТО ЖЕ или два объекта?
Оператор == означает: это ОДИНАКОВЫЕ два объекта?

1. Создать новый файл: answer10.py

2. Добавить класс Human из предыдущего задания:

class Human:
    def __init__(self, n, g, a):
        self.name = n
        self.gender = g
        self.age = a

3. Создать два объекта с одинаковыми значениями.

h1 = Human('vova', 'M', 25)
h2 = Human('vova', 'M', 25)

4. Так как переменные h1 и h2 указывают на два РАЗНЫХ объекта (хотя и с одинаковыми значениями),
то оператор "is" возвращает ложь:

if h1 is h2: 
    print("h1 is h2")
else:
    print("h1 is NOT h2)

5. Создадим переменную h3.

Добавить код:

h3 = h1
if h1 is h3:
    print("h1 is h3)
else:
    print("h1 is NOT h3")

6. В результате программа должна вывести:

h1 is NOT h2
h1 is h3

7. К сожалению, оператор == для h1 и h2 возвращает False!
Несмотря на то, что все атрибуты, все данные объектов h1 и h2 совпадают.

Добавить код и выполнить программу.
if h1 == h2:
    print("H1 == H2")
else:
    print("H1 != H2")

Почему?
Смотрим в следующем задании.

'''


class Human:
    def __init__(self, n, g, a):
        self.name = n
        self.gender = g
        self.age = a


h1 = Human('vova', 'M', 25)
h2 = Human('vova', 'M', 25)
if h1 is h2:
    print("h1 is h2")
else:
    print("h1 is NOT h2")

h3 = h1
if h1 is h3:
    print("h1 is h3")
else:
    print("h1 is NOT h3")

if h1 == h2:
    print("H1 == H2")
else:
    print("H1 != H2")
