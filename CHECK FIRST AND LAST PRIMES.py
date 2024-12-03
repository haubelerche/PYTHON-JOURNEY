import math
def nto(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def checkso(s):
    while len(str(s)) < 500:
        basodau = int(str(s)[:3])
        basocuoi = int(str(s)[-3:])
        if nto(basodau) and nto(basocuoi):
            return True
        return False

for _ in range(int(input())):
    n = int(input())
    if checkso(n):
        print("YES")
    else:
        print("NO")
    
