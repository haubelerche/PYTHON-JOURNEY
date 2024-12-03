import math
def nto(n) :
    if n < 2 : return 0
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return 0
    return 1

n = int(input())
a = [int(i) for i in input().strip().split()]
f = {}
for i in a:
    if i in f:
        f[i] += 1
    else: f[i] = 1
for i in a:
    if nto(i) == True and f[i] >= 1:
        print(i, f[i])
        f[i] = 0


