
# Вариант 8:Дана строка, заканчивающаяся точкой. Подсчитать, сколько слов в строке.
q = input('Введите строку, заканчивающиеся точкой:')
number = 0
flag=0
for i in range(len(q)):
    if q[i] != ' ' and flag == 0:
        number += 1
        flag = 1
    else:
        if q[i] == ' ':
           flag = 0
print('Количество слов:',number)