# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 08:50:23 2024

@author: admin
"""
a=int(input("Nhập số A: "))
b=int(input("Nhập số B: "))

def maxuochung(a, b):
    while b:
        a, b = b, a%b
    return a
def minboichung(a, b):
    return a*b//maxuochung(a, b)

print("Ước số chung lớn nhất của A, B: ", maxuochung(a, b))
print("Bội số chung nhỏ nhất của A, B: ", minboichung(a, b))

"""
a=int(input('A=')) 
b=int(input('B='))
T=a*b
while a!=b:
    if a>b:
         a=a-b
    else:
        b=b-a
print(a)
BCNN=T/a
print(BCNN)
"""