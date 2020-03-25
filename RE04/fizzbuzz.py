#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:30:43 2018

@author: diogo
"""

n = int(input("Write ur number here: "))
result = ""
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        result += ""
    elif i % 3 == 0:
        result += "Fizz "
    elif i % 5 == 0:
        result += "Buzz "
    else:
        result += str(i) + " "
print(result)