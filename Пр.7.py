#Леонтьева Е.Е. Вариант-8.1
#Найти все натуральные числа, не превосходящие заданного n, которые делятся на каждую из своих цифр.
def delnaseb(number):
    q = number
    while(q):
        z = q % 10
        q //= 10
        if (z == 0 or number % z):
            return False
    return True
n = int(input('Введите натуральное число:'))
for number in range(1, n + 1):
    if (delnaseb(number) and number % 10 != 0):
        print(number)    