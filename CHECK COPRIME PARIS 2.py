from math import gcd
def timntocn(N,K):
    res = []
    for i in range(10**(K-1), 10**K):
        if gcd(i,N) == 1:
            res.append(i)
    return res

a,b = map(int, input().split())
ntocn = timntocn(a,b)
for i in range(0, len(ntocn),10):
    print(' '.join(map(str, ntocn[i:i+10])))
