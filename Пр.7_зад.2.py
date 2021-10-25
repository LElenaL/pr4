def zam(number):
    q=number[0]
    number[0]=number[len(number)-1]
    number[len(number)-1]=q
A=[]
m=int(input('Введите длину массива:'))
for i in range(m):
    print('Введите элемент массива:')
    A.append(int(input()))
print('Исходный массив:',A)
zam(A)
print('Полученный массив:',A)

