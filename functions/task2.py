'''
Задание 2.
Написать функцию getLongerWord(w1, w2)
которая принимает две строки w1 и w2 и возвращает ту строку, длина которой больше.
В случае, если обе строки имеют одинаковую длину - функция должна возвратить
первую строку.

В данном примере код функции реализован с ошибками, исправить ошибку внутри функции getLongerWord()

'''


def getLongerWord(w1, w2):
    # ...
    # return ...
    return w1


# Testing:
a1 = getLongerWord("apple", "car")
a2 = getLongerWord("ball", "abrakadabra")
a3 = getLongerWord("foo", "bar")

print(a1)
print(a2)
print(a3)

# Expected output:
# apple
# abrakadabra
# foo
