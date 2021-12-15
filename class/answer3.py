'''Задание 3.

1. В git создать новую ветку class-task3

2. Создать файл answer3.py (в папке class)
В этом файле будем писать программу на языке Питон.
Можно скопировать код из файла answer2.py и продолжить выполнение задания.

3. Добавить в класс Person методы:
* age(year) - принимает значение текущего года (например, 2021) и возвращает возраст человека

* output() - выводит на экран (print) информацию о данном человеке.
Например:
Петр Иванов (муж) 1992

4. Поместить объекты p1, p2, p3 в список people.
Проходим по всем элементам списка и выводим на экран только женщин младше 30 лет,
используя вновь созданный метод output() в классе Person().
Для определения возраста используем метод age() в классе Person() - и передаем ему значение текущего года (например, 2021).

Программа должна напечатать только одного человека:
Наталья Серафимович (жен) 1970

5. Создать git-коммит, отправить изменения в интернет (на GitHub)

6. На GitHub создать Pull Request - от ветки class-task1 в ветку mainclass Person:'''


class Person:
    firstName = None
    lastName = None
    yearOfBirth = None  # 0
    gender = None

    def isPersonMale(self):
        if self.gender == "M":
            return True
        else:
            return False

    def isFemale(self):
        if self.gender == "F":
            return True
        else:
            return False

    def year(self, current_year):
        y = current_year - self.yearOfBirth
        return y

    def output(self):
        if self.isPersonMale():
            a = "(муж)"
        else:
            a = "(жен)"
        print(f'{self.firstName} {self.lastName} {a} {self.yearOfBirth} ')


p1 = Person()
p1.firstName = "Petr"
p1.lastName = "Ivanov"
p1.yearOfBirth = 1992
p1.gender = "M"

p2 = Person()
p2.firstName = "Maria"
p2.lastName = "Trofimova"
p2.yearOfBirth = 1997
p2.gender = "F"

p3 = Person()
p3.firstName = "Natalia"
p3.lastName = "Cerafimova"
p3.yearOfBirth = 1970
p3.gender = "F"

print("*** All people:")
p1.output()
p2.output()
p3.output()

people = [p1, p2, p3]
cy = 2021  # current year

print("*** Only young ladies")
for i in people:
    yy = i.year(cy)
    if yy < 30 and i.gender == "F":
        i.output()
