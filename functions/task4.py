'''
Задание 4.
Написать функцию printNumbersUntil(num),
которая выводит на экран (print) 
все числа, начиная от 1 заканчивая num (включительно)

'''

# Testing:


def printNumbersUntil(n):
    if n>0:
        a = list(range(n+1))
        for i in a:
            if i != 0:
                print (i)
# Программа написана правильно но работает не самым лучшим образом.
# Не нужно делать list(range(n+1))
# Лучше писать range непосредственно в цикле for:

# for i in range(n+1):

# Программа написана правильно но работает не самым лучшим образом.
# Не нужно делать list(range(n+1))
# Лучше писать range непосредственно в цикле for:

# for i in range(n+1):

print("All numbers until 5:")
printNumbersUntil(5)

print("All numbers until 1:")
printNumbersUntil(1)

print("All numbers until 0:")
printNumbersUntil(0)

# Expected output:
# All numbers until 5:
# 1
# 2
# 3
# 4
# 5
# All numbers until 1:
# 1
# All numbers until 0:
# (ничего)
