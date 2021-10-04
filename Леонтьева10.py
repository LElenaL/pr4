f1,f2,f3,sum = (0,1,0,0)
n=int(input("Введите число n\n"))
k=int(input("Введите число k\n"))
for i in range(2,n+1):
   f1,f3 = f3,f1 + f2
   f1 = f2
   f2 = f3
   if i >= k:
     sum += f3
print(sum)
