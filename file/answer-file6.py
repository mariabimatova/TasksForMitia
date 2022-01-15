'''Задание 6.

Открыть файл 1.txt в папке data и читать строки этого файла одну за одной.
Если строка начинается с # - это комментарий, игнорируем эту строку.
Иначе - строка состоит из пары 
<город> <страна>

В процессе чтения мы должны получить словарь:
ключ словаря это имя страны, а значение - список городов этой страны.

Вывести получившийся словарь на экран (порядок стран-городов внутри словаря не важен):

Ожидается результат
{'Russia': ['Tomsk', 'Moscow'], 
 'Italy':['Milan', 'Bologna', 'Rome'], 
 'USA':['New-York', 'San-Francisco'],
 'UK':['London']
}'''
dict1 = {}
for key,value in dict1.items():
    value == []
    



with open('data/1.txt') as file:
    file.readline()
    file.readline()
    file.readline()
    ff = file.readline()
    flist = ff.split()
    if flist[1] == "Russia":
        dict1.setdefault(flist[1],flist[0])
    ff1 = file.readline()
    flist1 = ff1.split()
    if flist1[1] == "Russia":
        
        
print(dict1)







