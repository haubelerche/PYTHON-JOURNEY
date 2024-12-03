def checkso(n):
    number = [int(x) for x in str(n)]
    for i in range(len(number) - 1):
        if number[i] > number[i + 1]:
            return "NO"
    return "YES"
for _ in range(int(input())):
    n = int(input())
    print(checkso(n))