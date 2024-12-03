# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 23:40:23 2024

@author: admin
"""
# tính tổng

tong = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        tong -= 1 / i
    else:
            tong += 1 / i
return tong

n = int(input("Nhập n: "))
print("Tổng của dãy là:", tong)