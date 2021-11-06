#Задана матрица порядка n и число k. Разделить элементы k-й строки на диагональный элемент,расположенный в этой строке.
import numpy as np
n = 5
k = np.random.randint(n)
q = np.random.randint(1, 50, size=(n, n))
print(q)
for n in range(0, len(q)):
    print(f'{q[k, n]} : {q[n,n]} = {q[k,n] / q[n, n]:.1f}')


