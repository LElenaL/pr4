def showMatrix(a):
    for i in range(len(a)):
        print(a[i])

def writeMatrixToFile(a):
    with open('Леонтьева Е.Е._УБ-11_vivod.txt', 'w') as f:
        for i in range(len(a)):
            for j in range(len(a)):
                f.write(a[i][j] + " ")
            f.write("\n")

fil = open('Леонтьева Е.Е._УБ-11_vvod.txt','r')
a = []
for rows in fil:
    a.append(rows.split())

print(a)
print("Изначальная матрица:")
showMatrix(a)
print("\n")

n = len(a)

for i in range(n):
    for j in range(i):
        tmp = a[i][j];
        a[i][j] = a[j][i];
        a[j][i] = tmp;
print("Транспонированная матрица:")
showMatrix(a)
writeMatrixToFile(a)
