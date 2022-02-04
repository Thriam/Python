import numpy as np
n=int(input())
def f(c):
    c=np.random.randint(n+1)
    return c
a=f(n)
if a==n:
    print(n-1)
else:
    print(a)
