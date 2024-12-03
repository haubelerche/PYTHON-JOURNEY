# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 09:45:37 2024

@author: admin
"""
txt = input()
thuong=hoa=0
for i in txt:
    if i.isupper(): hoa += 1
else: thuong += 1
if thuong > hoa:
    print(txt.lower())
else: print(txt.upper())
