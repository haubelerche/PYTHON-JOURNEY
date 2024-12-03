from math import gcd
x = int(input())
a = [int(x) for x in input().split()]
a = sorted(a)
for i in range(x):
    for j in range(i+1,x):
        if gcd(a[i],a[j]) == 1:
            print(f"{a[i]} {a[j]}")
