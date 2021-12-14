'''
Задание 5.
Написать функцию returnDigits(a),
которая принимает двузначное целое число а
и возвращает первую и вторую цифру этого числа.

Если число однозначное или больше двузначного - вернуть две цифры None (ошибка)
'''

# Testing


def returnDigits(a):
    num = str(a)
    
    if (len(num)) !=2:
        return None, None
    else:
        for i in num:
            b = num[0]
            c = num[1]
            return b,c

   
    
            

d1, d2 = returnDigits(25)
print(f"{d1} and {d2}")

d3, d4 = returnDigits(10)
print(f"{d3} and {d4}")

d5, d6 = returnDigits(9)
print(f"{d5} and {d6}")

d7, d8 = returnDigits(100)
print(f"{d7} and {d8}")

# Expected output:
# 2 and 5
# 1 and 0
# None and None
# None and None
