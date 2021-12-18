'''
Задание 7. Методы.

1. Можно продолжить с задания 6 в том же файле.

2. У нас должно быть три класса: Human, Parent, Child.

3. Давайте в программе создадим

Шесть объектов класса Parent:
p1: 'Zoya', 'F', 33
p2: 'Boris', 'M', 28
p3: 'Vladimir', 'M', 45
p4: 'Olya', 'F', 41
p5: 'Sveta', 'F', 42
p6: 'Petr', 'M', 25

И три ребенка:
c1: 'Anya', 'F', 3 - родители p1 и p2
c2: 'Polya', 'F', 8 - родители p3 и p4
c3: 'Misha', 'M', 12 - родители p3 и p5



4. Поместим всех родителей в список - parents.
Поместим всех детей в отдельный список - children.

5. Добавим в классы Human метод - output().
Этот метод принимает один параметр - self
И выводит информацию о человеке - имя, пол, возраст.

6. Выведем на экран информацию о всех родителях с помощью функции output().
Подсказка: используем цикл по списку родителей

Пример:
Zoya, 'F', 33
Boris, 'M', 28
Vladimir, 'M', 45
Olya, 'F', 41
Sveta, 'F', 42
Petr, 'M', 25



7. Выведем на экран информацию обо всех детях с помощью функции output().

Пример:
'Anya', 'F', 3
'Polya', 'F', 8
'Misha', 'M', 12

8. Продолжаем в задании 8.
'''

class Human():
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def output(self):
        def __str__(self):
            a = f"{self.name} {self.gender} {self.ag}"
            return a
            



class Child (Human):
    def __init__(self, name, gender, age, mother, father):
        super().__init__(name, gender, age)
        self.mother = mother
        self.father = father




class Parent (Human):
    def __init__(self, name, gender, age, children):
        super().__init__(name, gender, age)
        self.children = children

p1 = Parent(name = 'Zoya', gender = 'F', age =33, children=None)
p2 = Parent(name = 'Boris', gender = 'M', age =28, children=None)
p3 = Parent(name = 'Vladimir', gender = 'M', age =45, children=None)
p4 = Parent(name = 'Olga', gender = 'F', age =41, children=None)
p5 = Parent(name = 'Sveta', gender = 'F', age =42, children=None)
p6 = Parent(name = 'Petr', gender = 'M', age =25, children=None)

c1 = Child(name= "Anya", gender = "F", age = 3, mother = p1, father = p2)
c2 = Child(name= "Polya", gender = "F", age = 8, mother = p3, father = p4)
c3 = Child(name= "Misha", gender = "M", age = 12, mother = p5, father = p6)

parent_list = [p1,p2,p3,p4,p5,p6]
child_list = [c1,c2,c3]







