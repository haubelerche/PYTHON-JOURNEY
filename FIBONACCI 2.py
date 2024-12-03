# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 00:30:04 2024

@author: admin
"""

n = int(input("N = "))
a = 0
b = 1
while b!=n:
    if b>n:
        break
    a=b
    b=b+a
if b == n: 
    print("N là số Fibonacci.")
else:
    print("N không phải là số Fibonacci")