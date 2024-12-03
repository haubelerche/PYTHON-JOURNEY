def checkso(n):
    count = 0
    while n % 7 != 0 and count < 1000:
        n += int(str(n)[::-1])
        count += 1
    if n % 7 ==0:
        return n
    else: return -1

for _ in range(int(input())):
    n = int(input())
    re = checkso(n)
    print(re)
