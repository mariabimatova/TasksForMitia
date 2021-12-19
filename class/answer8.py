'''
Задание 8. Наследование (перегрузка) методов

1. Скопировать файл с предыдущего задания в новый файл - answer8.py.

2. У нас должно быть три класса: Human, Parent, Child.

В класе Human мы добавили метод output(),
который выводит на экран информацию об объекте.

3. Сейчас информация о детях и о родителях выводится одинаково: имя, пол, возраст.
Мы хотим сделать так, чтобы информация об объекте класса Parent (родитель) содержала список детей.
Мы хотим сделать так, чтобы информация об объекте класса Child (ребенок) содержала данные о родителях.

Для этого наобходимо сделать следующее:
а) добавить в класс Parent метод output().
б) добавить в класс Child метод output().

4. Реализовать метод output() класса Child так, чтобы на экран выводились дети в виде:

Girl: Anya, 3. Father: Boris. Mother: Zoya.
Girl: Polya, 8. Father: Vladimir. Mother: Olya.
Boy: Misha, 12. Father: Vladimir. Mother: Sveta.

Подсказка:
чтобы оператор print() не переводил строку после своего завершения, нужно добавить второй параметр end=""
 (пустая строка).
Например:
# один оператор print
print("Hello, world!") 

# два оператора print - в первом мы просим НЕ переводить строчку на следующую при печати с помощью end="". Вот так:
print("Hello, ", end="")
print("world!)

5. Реализовать методы output() так, чтобы на экран выводились родители в виде:

Mother: Zoya, 33. Children: Anya
Father: Boris, 28. Children: Anya
Father: Vladimir, 45. Children: Polya, Misha
Mother: Olya, 41. Children: Polya
Mother: Sveta, 42. Children: Misha
Father: Petr, 25. No children.

Подсказка:
Когда мы выводим список детей, важно проверить:
а) если нет детей - вывести No children.
б) если есть дети, то нужно выводить запятую всегда, кроме ПОСЛЕДНЕГО ребенка
Для того, чтобы определить, что ребенок последний можно использовать его индекс - или - номер в списке.

# вот этот цикл просто проходит по всем элементам списка
for c in self.children:
    print(c.name)

# а вот этот цикл также выдает НОМЕР (или - индекс, элемента в списке)
for no,c in enumerate(self.children):
    print(c.name, end="")
    if (...) : # подумай над условием, как определить что номер элемента в списке последний .... ?
        print(", ", end="")


'''


class Human():
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def output(self):
        print(f'{self.name},{self.gender},{self.age}')


class Child (Human):
    def __init__(self, name, gender, age, mother, father):
        super().__init__(name, gender, age)
        self.mother = mother
        self.father = father

    def output(self):
        if self.gender == "M":
            print(
                f'boy: {self.name},{self.gender},{self.age},father: {self.father}, mother: {self.mother}')
        else:
            print(
                f'girl: {self.name},{self.gender},{self.age},father: {self.father}, mother: {self.mother}')


class Parent (Human):
    def __init__(self, name, gender, age, children=None):
        super().__init__(name, gender, age)
        self.children = children

    def output(self):
        if self.gender == "M":
            print(
                f'father: {self.name},{self.age}, children: {self.children}')
        else:
            print(
                f'mother: {self.name},{self.age}, children: {self.children}')


p1 = Parent(name='Zoya', gender='F', age=33, children="Anya")
p2 = Parent(name='Boris', gender='M', age=28, children="ANya")
p3 = Parent(name='Vladimir', gender='M', age=45, children="Polya")
p4 = Parent(name='Olga', gender='F', age=41, children="Polya")
p5 = Parent(name='Sveta', gender='F', age=42, children="Misha")
p6 = Parent(name='Petr', gender='M', age=25, children="Misha")

c1 = Child(name="Anya", gender="F", age=3, mother="Zoya", father="Boris")
c2 = Child(name="Polya", gender="F", age=8, mother="Olga", father="Vladimir")
c3 = Child(name="Misha", gender="M", age=12, mother="Sveta", father="Petr")

parent_list = [p1, p2, p3, p4, p5, p6]
child_list = [c1, c2, c3]
parent_child_list = parent_list + child_list

for i in parent_list:
    i.output()

for i in child_list:
    i.output()
