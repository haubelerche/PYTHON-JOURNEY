
def rate(r):
    if 3<=int(r)<=4:
        return 2.5
    if 5<=int(r)<=6:
        return 3.0
    if 7<=int(r)<=9:
        return 3.5
    if 10<=int(r)<=12:
        return 4.0
    if 13<=int(r)<=15:
        return 4.5
    if 16<=int(r)<=19:
        return 5.0
    if 20<=int(r)<=22:
        return 5.5
    if 23<=int(r)<=26:
        return 6.0
    if 27<=int(r)<=29:
        return 6.5
    if 30<=int(r)<=32:
        return 7.0
    if 33<=int(r)<=34:
        return 7.5
    if 35<=int(r)<=36:
        return 8.0
    if 37<=int(r)<=38:
        return 8.5
    if 39<=int(r)<=40:
        return 9.0
    
t = int(input())
for i in range(t):
    n = input().split()
    all = (rate(int(n[0])) + rate(int(n[1])) + float(n[2]) + float(n[3])) / 4
    if all - int(all) >= 0.75: 
        print(int(all) + 1.0)
    elif all - int(all) >= 0.25:
        print(int(all) + 0.5)
    else:
        print(int(all)+ 0.0)





