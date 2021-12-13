'''
Задание 1.
Написать функцию isNumberEven(), 
которая принимает одно число и возвращает True, 
если чисто четное и ложь - если число нечетное.

Можно удалить комментарий внутри функции и пустой оператор pass
Возвращаемое значение логического типа (True/False) передается обратно с помощью
оператора return
'''


def isNumberEven(num):
    if num % 2 == 0:
        return "True"
    else:
        return "False"

    


a = int(input("Enter the number: "))
even = isNumberEven(a)
if even:
    print("Your number is even")
else:

    print("Your number is odd")
