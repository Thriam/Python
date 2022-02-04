import math
a=int(input())
b=int(input())
l1=[]
for i in range(1000):
    if (math.factorial(b))%(a**i)==0:
        l1.append(i)
print(max(l1))
print(l1)

