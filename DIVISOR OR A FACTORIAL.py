# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:26:20 2024

@author: admin
"""
#Uoc so cua giai thua
def test(n, p):
    count = 0
    for i in range(1, n+1):
        t = i
        while t % p == 0:
            count +=1
            t //= p
            return count
        
def main():
    t = int(input())
    for _ in range(t):
        n, p = map(int, input().split())
        print(test(n, p))
if __name__ == "__main__":
    main()
