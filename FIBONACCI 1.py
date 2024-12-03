# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 08:10:52 2024

@author: admin
"""
#liệt số fibonacci
fi=[0,1,1]
for i in range(3,93):
    fi.append(fi[i-1] + fi[i -2])
for _ in range(int(input())):
    a, b = map(int, input().split())
    for i in range(a, b+1):
        print(fi[i], end = ' ')
    print()