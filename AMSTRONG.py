# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 00:53:14 2024

@author: admin
"""

num=input('enter num: ')
sum=0
for i in num:
    sum+=int(i)**3
if sum==int(num):
    print('amstrong')
else: print('not amstrong')