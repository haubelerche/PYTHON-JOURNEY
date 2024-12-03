import math
def nto(n) :
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True

t = int(input())
for _ in range(t):
    n = (input())
    socuoi = int(n[-4:])
    if nto(socuoi):
        print("YES")
    else:
        print("NO")