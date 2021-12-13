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
    if 0<=num<=8:
        a = num +1
        return a
    elif num == 9:
        a = 0
        return a

    


numbers = [0, 7, 2, 9]
for n in numbers:
    next = getNextDigit(n)
    print(f"{n} -> {next}")
