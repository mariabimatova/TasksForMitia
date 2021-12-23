'''
Задание 11. Магический метод __eq__.

Если мы хотим сравнивать два объекта нашего класса,
то необходимо в класс добавить магический метод __eq__()

1. Создать новый файл: answer11.py

2. Добавить класс Human из предыдущего задания:

class Human:
    def __init__(self, n, g, a):
        self.name = n
        self.gender = g
        self.age = a

3. Создать два объекта с одинаковыми значениями.
Третий объект h3 - отличается лишь возрастом, а имя одинаковое.

h1 = Human('vova', 'M', 25)
h2 = Human('vova', 'M', 25)
h3 = Human('vova', 'M', 30)

Добавить код и выполнить программу.
if h1 == h2:
    print("H1 == H2")
else:
    print("H1 != H2")

if h1 == h3:
    print("H1 == H3")
else:
    print("H1 != H3")

4. Убедиться, что программа выводит
H1 != H2
H1 != H3

5. Добавить магический метод __eq__() в класс Human.
Этот метод (как и все другие методы) - принимает параметр self.
Также, метод принимает второй параметр - other (объект с которым сравниваем)

def __eq__(self, other):
    if self.name == other.name:
        return True
    else:
        return False

6. Запустить программу и убедиться, что программа выводит:
H1 == H2
H1 == H3

7. Первая строчка по смыслу верная (все атрибуты совпадают - значит и объекты "одинаковые").
Вторая строчка по смыслу не верная - возраст h1 не равен возрасту h3.

Поэтому необходимо модифицировать код метода __eq__ (условие внутри метода) так,
чтобы программа выводила:

H1 == H2
H1 != H3

Подсказка: нужно внутри метода __eq__ сравнивать ВСЕ атрибуты, а не только один атрибут name.

'''


class Human:
    def __init__(self, n, g, a):
        self.name = n
        self.gender = g
        self.age = a

    def __eq__(self, other):
        if self.name == other.name and self.gender == other.gender and self.age == other.age:
            return True
        else:
            return False


h1 = Human('vova', 'M', 25)
h2 = Human('vova', 'M', 25)
h3 = Human('vova', 'M', 30)

if h1 == h2:
    print("H1 == H2")
else:
    print("H1 != H2")

if h1 == h3:
    print("H1 == H3")
else:
    print("H1 != H3")
