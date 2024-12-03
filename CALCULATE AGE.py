# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 00:48:30 2024

@author: admin
"""
import datetime
birthyear = int(input("When were you born ? "))
age = datetime.datetime.now().year - birthyear
print("Your age is: ", age)