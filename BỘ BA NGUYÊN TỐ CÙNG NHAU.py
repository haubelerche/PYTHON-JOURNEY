from math import gcd
l,r = map(int,input().split())
#a<b<c
for a in range(l,r+1):
    for b in range(a+1,r+1):
        if gcd(a,b)==1:
            for c in range(b + 1, r + 1):
                if gcd(a, c)==1 and gcd(b, c)==1:
                    print(f'({a}, {b}, {c})')