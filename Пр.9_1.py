file = open(r"Леонтьева Е.Е._УБ-11_vvod.txt", "r")
file1 = open(r"Леонтьева Е.Е._УБ-11_vivod.txt", "w")
n = 5
k = 2
a = []
a = [ [ int(j) for j in i.split()] for i in file]
file.close()
c1 = a.copy()
print(c1)

for i in range(n):
    for j in range(n):
        print(c1[i][j], '', end='')
    print()
for i in range(n):
    print(c1[k][i], ':', c1[i][i],'=', c1[k][i] / c1[i][i])
    c1[k][i] = c1[k][i] / c1[i][i]
with open('Леонтьева Е.Е._УБ-11_vivod.txt', 'w') as out:
   out.write('Изменёная матрица:' + '\n')
   for i in c1:
       out.write(' '.join([str(c1) for c1 in i]) + '\n')
