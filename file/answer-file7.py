
'''Задание 7.
Продолжение от задачи 6.

Записать получившийся словарь из задания 6 в файл
data/1_out.txt

Вот словарь:
{'Russia': ['Tomsk', 'Moscow'], 
 'Italy':['Milan', 'Bologna', 'Rome'], 
 'USA':['New-York', 'San-Francisco'],
 'UK':['London']
}

Файл должен выглядеть так:
<страна>
<город> <город>... <город>

Например:
Russia
Tomsk Moscow
Italy
Milan Bologna Rome
USA
New-York San-Francisco
UK
London'''



from turtle import fd


fdict = {'Russia': ['Tomsk', 'Moscow'], 
 'Italy':['Milan', 'Bologna', 'Rome'], 
 'USA':['New-York', 'San-Francisco'],
 'UK':['London']
}

lines = []
for contry,cities in fdict.items():
    lines.append(contry)

    # varian1: without <join>
    '''s = cities[0]
    for city in cities[1:]:
        s = s + ' ' + city'''

    # varian2: with special function <join>
    space = ' '
    s = space.join(cities)

    lines.append(s)

# write lines one by one
with open('data/1_out.txt','w') as document:
    for n in lines:
        document.write(n)
        document.write('\n')


  
 
