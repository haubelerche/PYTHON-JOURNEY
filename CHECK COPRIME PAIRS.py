from math import gcd
x = int(input())
a = [int(n) for n in input().split()]
a = sorted(a)
for i in range(x): #i la vi tri cac so
    for j in range(i+1,x): #bat dau tu so 0
        if gcd(a[i],a[j]) == 1: print(f'{a[i]} {a[j]}')






