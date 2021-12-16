'''
Задание 6. Наследование.

1. Делаем с git и GitHub как обычно:
а) создаем новую ветку для задания
б) создаем там коммиты - в процессе выполнения задания
в) записываем изменения на GitHub
г) делаем Pull-Request и одобряем (merge) - на GitHub-е
д) скачиваем измнения из GitHub в основную ветку локального репозитория (git pull)

2. В новом файле answer6.py - cоздать класс Human (человек).

Добавить атрибуты класса:
* name - имя
* gender - пол ('M' или 'F')
* age - возраст

Добавить конструктор: __init__() принимает три параметра:
name, gender, age.
Конструктор должен устанавливать значения соответствующих атрибутов.

3. Создать класс Child (ребенок) - подкласс от Human

Добавить атрибуты:
* mother 
* father

Добавить конструктор: __init__() - принимает пять параметров:
name, gender, age, mother, father.
Конструктор должен устанавливать значения соответствующих атрибутов.

В первой строке конструктор должен вызывать конструктор родительского класса:
super().__init__(name, gender, age)

Посмотри подробнее про super() в слайдах к лекции.

4. Создать класс Parent (родитель) - подкласс от Human

Добавить атрибут:
* children

Конструктор Parent принимает также три параметра:
name, gender, age.

5. Продолжение - в задании 7 (можно задание делать в одном файле).

'''


class Human():
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


class Child (Human):
    def __init__(self, name, gender, age, mother, father):
        super().__init__(name, gender, age)
        self.mother = mother
        self.father = father


class Parent (Human):
    def __init__(self, name, gender, age, children):
        super().__init__(name, gender, age)
        self.children = children
