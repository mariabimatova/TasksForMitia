'''Задание 6.

Открыть файл 1.txt в папке data и читать строки этого файла одну за одной.
Если строка начинается с # - это комментарий, игнорируем эту строку.
Иначе - строка состоит из пары 
<город> <страна>

В процессе чтения мы должны получить словарь:
ключ словаря это имя страны, а значение - список городов этой страны.

Вывести получившийся словарь на экран (порядок стран-городов внутри словаря не важен):

File:
=============================================================
# This is data file
# Lines starting with '#' are comments and should be ignored
# Here we have pairs: <city> <country>
Tomsk Russia
Moscow Russia
Milan Italy
Bologna Italy
Rome Italy
New-York USA
San-Francisco USA
Seattle USA
London UK
=============================================================

Ожидается результат
{'Russia': ['Tomsk', 'Moscow'], 
 'Italy':['Milan', 'Bologna', 'Rome'], 
 'USA':['New-York', 'San-Francisco'],
 'UK':['London']
}
'''

dict1 = {}

def processLine(line):
    flist = line.split()
    city = flist[0]
    country = flist[1]
    
    if country in dict1:
        cities = dict1[country]
        cities.append(city)
    else:
        dict1[country] = [city]
    
def processLine2(line):
    flist = line.split()
    city = flist[0]
    country = flist[1]
    
    dict1.setdefault(country, [])
    cities = dict1[country]
    cities.append(city)

with open('data/1.txt') as file:
    text = file.readlines()
    for line in text:
        if line[0] != "#":
            processLine2(line)
     
print(dict1)









