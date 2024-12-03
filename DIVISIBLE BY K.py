a, k, n = map(int,input().split())
res = -1
n = int(n/k) + 1
for i in range(n):
    x = i * k - a
    if x > 0:
        res = 1
        print(x, end = " ")
if res == -1: print("-1")