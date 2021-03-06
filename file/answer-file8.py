'''Задание 8.
Продолжение от задачи 7.

Прочитать файл, получившийся в задании7,
и восстановить тот же самый словарь. Вывести словарь на экран.

Для чтения по паре строк можно использовать метод f.readline()
f = open('file.txt')
while True:
    line1 = f.readline()
    line2 = f.readline()
    if not line1 or not line2:
        break
    ...

В файле:
Russia
Tomsk Moscow
Italy
Milan Bologna Rome
USA
New-York San-Francisco
UK
London

Словарь (порядок стран и городов не важен):
{'Russia': ['Tomsk', 'Moscow'], 
 'Italy':['Milan', 'Bologna', 'Rome'], 
 'USA':['New-York', 'San-Francisco'],
 'UK':['London']
}'''
fdict = {}
with open('data/1_out.txt') as f:
    while True:
        line1 = f.readline()
        line2 = f.readline()
        
        if line1 == "" or line2 == "":
            break
        line1 = line1.strip()
        line2 = line2.strip()
        cities = line2.split()
        fdict[line1] = cities
        
        
print(fdict)
