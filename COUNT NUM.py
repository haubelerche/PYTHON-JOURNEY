# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 08:23:22 2024

@author: admin
"""

a = int(input("Nhập số A: "))
b = int(input("Nhập số B: "))
for i in range(a+1,b):
    is_prime=1
    for j in range(2,i):
        if i%j==0:
            is_prime=0
            break
    if is_prime==1: print(i)
