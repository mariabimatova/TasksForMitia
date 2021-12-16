'''
Задание 5. Магическая функция __str__.

1. Делаем с git и GitHub как обычно:
а) создаем новую ветку для задания
б) создаем там коммиты - в процессе выполнения задания
в) записываем изменения на GitHub
г) делаем Pull-Request и одобряем (merge) - на GitHub-е
д) скачиваем измнения из GitHub в основную ветку локального репозитория (git pull)

2. Создаем файл answer5.py (в папке class)
В этом файле будем писать программу на языке Питон.

3. Скопировать код из задания 4 (answer4.py)

4. Добавить в самом низу код:
print(p1)
print(p2)
print(p3)

5. Выполнить программу и убедиться, что объекты выводятся
в непонятной форме.

6. Добавить в класс Person магический метод __str__.
Этот метод принимает только один параметр - как и все методы - self.
Этот метод возвращает строку, которая представляет данный объект.

В этот метод добавляем код, чтоб операторы print(p1), print(p2), print(p3)
внизу выводил состояние объекта в виде:

First name: <...>. Last name: <...>. Year: <...>

7. Убедиться, что теперь програма выводит людей в виде:
First name: Петр. Last name: Иванов. Year: 1992
First name: Мария. Last name: Трофимова. Year: 1987
First name: Наталья. Last name: Серафимович. Year 1970'''

class Person:
    def __init__(self,firstName,lastName,yearOfBirth):
        self.firstName =  firstName
        self.lastName = lastName
        self.yearOfBirth = yearOfBirth

    def __str__(self):
        line1 = f"First name: {self.firstName}.  Last name: {self.lastName}. Year: {self.yearOfBirth}"  
        return line1
        

p1 = Person("Petr", "Ivanov", 1992)


p2 = Person("Maria", "Trofimova", 1987)

p3 = Person("Natalia", "Cerafimova", 1970)

print(p1)
print(p2)
print(p3)