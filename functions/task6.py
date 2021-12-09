'''
Задание 6.
Написать функцию rangeList(beg, end)
которая принимает два числа: from, to
и возвращает список, содержащий числа от from до to (исключая to).

Функция должна возвратить пустой список, если from больше или равно to
'''

# Testing


def rangeList(beg, end):
    return []


l1 = rangeList(2, 5)
print(l1)

l2 = rangeList(5, 2)
print(l2)

# Expected output:
# [2, 3, 4]
# []
