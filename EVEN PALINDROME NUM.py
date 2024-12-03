def thuannghich(n):
    n=str(n)
    a = [int(i) for i in n]
    b = a[::-1]
    if a == b: return 1
    else: return 0

def checkchan(n):
    while n > 0:
        for i in str(n):
            if int(i) % 2 == 1:return 0
            if len(str(n)) % 2 == 1:return 0
        return 1

a = []
for i in range(22, 1000000):
    if thuannghich(i) == 1 and checkchan(i)== 1 :
        a.append(i)