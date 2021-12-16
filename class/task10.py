'''
Задание 10. Работа с объектами. is и ==.

1. Создать новый файл: answer10.py

2. Скопировать класс Human из предыдущего задания:

class Human:
    def __init__(n, g, a):
        self.name = n
        self.gender = g
        self.age = a

'''


class Human:
    def __init__(self, n, g, a):
        self.name = n
        self.gender = g
        self.age = a


h1 = Human('vova', 'M', 25)
h2 = Human('vova', 'M', 25)

print(h1 is h2)
print(h1 == h2)
