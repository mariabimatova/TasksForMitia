'''
Задание 3.
Написать функцию getNextDigit(num)
которая принимает цифру от 0 до 9
и возвращает "следующее число"
0 -> 1
1 -> 2
...
8 -> 9
9 -> 0

'''

# Testing


def getNextDigit(num):
    # TODO: add implementation here!
    pass


numbers = [0, 7, 2, 9]
for n in numbers:
    next = getNextDigit(n)
    print(f"{n} -> {next}")
