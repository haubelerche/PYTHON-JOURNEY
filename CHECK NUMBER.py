# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 19:33:00 2024

@author: admin
"""
t = int(input())
while t > 0:
    t -= 1
    s = input()
    res = "NO"
    if s[0] == s[len(s)-2] and s[1] == s[-1]: res = "YES"
    print(res)
        
    
