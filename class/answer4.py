'''
Задание 4. Конструктор (__init__)

1. В git создать новую ветку class-task4
Переключиться на эту вновь созданную ветку.

2. Создать файл answer4.py (в папке class)
В этом файле будем писать программу на языке Питон.

3. Скопировать код из задания 1 (task 1)
У нас уже должен быть класс Person c тремя атрибутами:
* firstName - имя человека
* lastName - фамилия человека
* yearOfBirth - год рождения

Также у нас уже должны быть три объекта в переменных p1, p2, p3:
объект p1: Петр Иванов 1992
объект p2: Мария Трофимова 1987
объект p3: Наталья Серафимович 1970

4. В класс Person добавить "конструктор" - специальный метод с именем __init__().
Как и любой метод - конструктор __init__ должен иметь первый параметр - self (этот объект).
Дополнительно, добавить к конструктору __init__ еще три параметра:
а) имя
б) фамилия
в) год рждения

В конструкторе мы должны установить значения соответствующих атрибутов объекта
self.firstName = ...
self.lastName = ...
self.yearOfBirth = ...

5. Теперь мы не можем создавать объекты класса Person без параметров:
p1 = Person() - будет ошибка

6. Соответственно, мы должны изменить код, который создает и устанавливает значения
атрибутов объектов p1, p2, p3:

p1 = Person(..., ..., ...)
p2 = Person(..., ..., ...)

7. Поздравляю! Теперь у нас есть класс Person с конструктором,
который принимает три параметра: имя, фамилию, год рождения.
Теперь при создании объекта требуется лишь 1 строчка!
Также, мы не можем случайно забыть установить какой-то атрибут (имя, фамилия, год рождения).

8. Создать git-коммит, отправить изменения в интернет (на GitHub)
На GitHub создать Pull Request - от ветки class-task1 в ветку main.

9. Одобрить Pull-Request, убедиться, что изменения появились на GitHub.
В локальном репозитории переключиться на ветку main
и скачать изменения с GitHub (pull)

'''


# class Person:
#     firstName = None
#     lastName = None
#     yearOfBirth = None # 0

# p1 = Person()
# p1.firstName = "Petr" 
# p1.lastName = "Ivanov"
# p1.yearOfBirth = 1992

# p2 = Person()
# p2.firstName = "Maria" 
# p2.lastName = "Trofimova"
# p2.yearOfBirth = 1987

# p3 = Person()
# p3.firstName = "Natalia" 
# p3.lastName = "Cerafimova"
# p3.yearOfBirth = 1970

# print(f'{p1.firstName} {p1.lastName} {p1.yearOfBirth} ')
# print(f'{p2.firstName} {p2.lastName} {p2.yearOfBirth} ')
# print(f'{p3.firstName} {p3.lastName} {p3.yearOfBirth} ')



class Person:
    def __init__(self,firstName,lastName,yearOfBirth):
        self.firstName =  firstName
        self.lastName = lastName
        self.yearOfBirth = yearOfBirth

p1 = Person("Petr", "Ivanov", 1992)


p2 = Person("Maria", "Trofimova", 1987)

p3 = Person("Natalia", "Cerafimova", 1970)



# print(str(p2))
# print(str(p3))
print(p1.__dict__)
# не помню как сделать принт.... искала везде .... не нашла..... помню ты говорил про стр но не помню как делать....