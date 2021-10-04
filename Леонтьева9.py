
def fibonacci(n):
    x, y = 0, 1
    for _ in range(n):
        yield x
        x, y = y, x + y

def fib_sum(n):
    return sum(fibonacci(n))

print("Введите число N:")
num = int(input())
print(fib_sum(num))