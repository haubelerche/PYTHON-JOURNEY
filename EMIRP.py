import math
#check xem co phai so nguyen to khong
def nto(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) +1):
        if n % i == 0: return False
    return True

for bo in range(int(input())):
    n = int(input())
    for j in range(1, n):
        k = int(str(j)[::-1])
        if nto(j) and j<k<n and nto(k):
            print(j, k, end=" ")
    print()    