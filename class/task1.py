'''
Задание1.

1. В git создать новую ветку class-task1

2. Создать файл answer1.py (в папке class)
В этом файле будем писать программу на языке Питон.

3. Создать класс Person.

Атрибуты:
* firstName - имя человека
* lastName - фамилия человека
* yearOfBirth - год рождения

4. Создать три объекта типа (класса) Person и поместить их в переменные p1, p2, p3.
Установить значения для соответствующих атрибутов:

объект p1: Петр Иванов 1992
объект p2: Мария Трофимова 1987
объект p3: Наталья Серафимович 1970

5. Вывести на экран значения атрибутов объектов p1, p2, p3 в виде:
Петр Иванов 1992
Мария Трофимова 1987
Наталья Серафимович 1970

6. Создать git-коммит, отправить изменения в интернет (на GitHub)

7. На GitHub создать Pull Request - от ветки class-task1 в ветку main


'''

class Person:
    firstName = None
    lastName = None
    yearOfBirth = None # 0

p1 = Person()
p1.firstName = "Petr" 
p1.lastName = "Ivanov"
p1.yearOfBirth = 1992

p2 = Person()
p2.firstName = "Maria" 
p2.lastName = "Trofimova"
p2.yearOfBirth = 1987

p3 = Person()
p3.firstName = "Natalia" 
p3.lastName = "Cerafimova"
p3.yearOfBirth = 1970

print(f'{p1.firstName} {p1.lastName} {p1.yearOfBirth} ')
print(f'{p2.firstName} {p2.lastName} {p2.yearOfBirth} ')
print(f'{p3.firstName} {p3.lastName} {p3.yearOfBirth} ')
