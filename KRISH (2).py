from math import factorial as f
def checkrish(n):
    sum = 0
    temp = n
    while temp != 0:
        x = temp % 10 
        sum += f(x) 
        temp //= 10
    return n == sum

for i in range(int(input())):
    i = int(input())
    if checkrish(i):
        print("Yes")
print("No")