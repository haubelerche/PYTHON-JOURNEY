# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:11:30 2024

@author: admin
"""

D = {}

for _ in range(int(input())):
    s = input()
    w =""
    for c in s.lower() + " ":
        if c.isalnum():
            w += c
        else:
            if w != "":
                D[w] = D.get(w, 0) + 1
            w = ""
            
m = sorted(D.items(), key=lambda x: (-x[1], x[0]))
for i in m:
    print(i[0], i[1])