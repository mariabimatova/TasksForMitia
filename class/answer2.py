'''
Задание 2.

1. В git создать новую ветку class-task2

2. Создать файл answer2.py (в папке class)
В этом файле будем писать программу на языке Питон.
Можно скопировать код из файла answer1.py и продолжить выполнение задания.

3. Добавить в класс Person атрибут:
gender - пол человека. Может принимать значения 'M' или 'F'

4. Добавить в класс Person два метода:
isMale() - возвращает True для мужчин
isFemale() - возвращает False для женщин

5. Для объектов p1, p2, p3 добавить значения атрибута gender (пол).

объект p1: Петр Иванов (муж) 1992
объект p2: Мария Трофимова (жен) 1987
объект p3: Наталья Серафимович (жен) 1970

5. Вывести на экран значения атрибутов объектов p1, p2, p3 в виде:
Петр Иванов (муж) 1992
Мария Трофимова (жен) 1987
Наталья Серафимович (жен) 1970

6. Создать git-коммит, отправить изменения в интернет (на GitHub)

7. На GitHub создать Pull Request - от ветки class-task1 в ветку main

'''
class Person:
    firstName = None
    lastName = None
    yearOfBirth = None # 0
    gender = None

p1 = Person()
p1.firstName = "Petr" 
p1.lastName = "Ivanov"
p1.yearOfBirth = 1992
p1.gender = "(male)"

p2 = Person()
p2.firstName = "Maria" 
p2.lastName = "Trofimova"
p2.yearOfBirth = 1987
p2.gender = "(female)"

p3 = Person()
p3.firstName = "Natalia" 
p3.lastName = "Cerafimova"
p3.yearOfBirth = 1970
p3.gender = "(female)"

print(f'{p1.firstName} {p1.lastName} {p1.gender} {p1.yearOfBirth} ')
print(f'{p2.firstName} {p2.lastName} {p2.gender} {p2.yearOfBirth} ')
print(f'{p3.firstName} {p3.lastName} {p3.gender} {p3.yearOfBirth} ')

def isMale(self):
        if self.gender == "(male)":
            return True
def isFemale(self):
        if self.genger == "(femal)":
            return True