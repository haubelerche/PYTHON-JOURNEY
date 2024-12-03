# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 02:06:30 2024

@author: admin
"""

a= float(input("Nhập hệ số a = "))
b= float(input("Nhập hệ số b = "))
c= float(input("Nhập hệ số c = "))
d= float(input("Nhập hệ số d = "))
e= float(input("Nhập hệ số e = "))
f= float(input("Nhập hệ số f = "))

delta=a*e-b*d

def xetdt(delta):
   if delta != 0:
    x = (c * e - b * f) / delta
    y = (a * f - c * d) / delta
    return x, y
   else:
    return "Hệ phương trình vô nghiệm hoặc có vô số nghiệm"

print(xetdt(delta))