import math
def songuyen(n):
    if n < 2:
        return 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return 1
def uochung():
    a, b = map(int, input().split())
    ucln = str(math.gcd(a,b))
    sum = 0
    for i in ucln:
        sum += int(i)
    if songuyen(sum) == 1:
        print("YES")
    else: print("NO")
for i in range(int(input())): uochung()
