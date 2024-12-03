# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 01:39:44 2024

@author: admin
"""
import math
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

delta = b**2 - 4*a*c

def xeths(delta):
    
    if delta == 0:
        x = -b/(2*a)
        return "Phương trình trên có nghiệm kép x1 = x2 =", x
    elif delta > 0:
        x1=(-b + math.sqrt(delta))/(2*a)
        x2=(-b - math.sqrt(delta))/(2*a)
        return "Phương trình trên có 2 nghiệm phân biệt: x1 =", x1, " và x2 =", x2
    else: 
        return "Phương trình không có nghiệm thực"
print("Kết quả giải phương trình:", xeths(delta))    