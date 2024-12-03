# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 08:08:51 2024

@author: admin
"""
operation = input()

# Tách các phần a, b, c
a, rest = operation.split('+')
b, c = rest.split('=')

# Chuyển các phần thành số nguyên
a, b, c = int(a), int(b), int(c)

# Kiểm tra điều kiện đề bài và in ra kết quả
result = "YES" if a + b == c and 1 <= a <= 9 and 1 <= b <= 9 and 1 <= c <= 9 else "NO"
print(result)




