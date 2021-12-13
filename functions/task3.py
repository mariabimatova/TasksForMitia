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

# Хороший стиль такой: заводишь переменную для ответа. Возвращаешь ее один раз с помощью одного оператора return в конце

# if num == 9:
#    result = 0
# else
#    result = num+1
# return result

# Можно ещё вот так:
# result = num + 1
# if result > 9:
#     result = 0
# return result

# Самое красивое математическое решение такое:
# result = (num + 1) % 10
# return result

    


numbers = [0, 7, 2, 9]
for n in numbers:
    next = getNextDigit(n)
    print(f"{n} -> {next}")
