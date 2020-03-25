#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:32:17 2018

@author: diogo
"""

n1 = int(input("Number 1 is: "))
n2 = int(input("Number 2 is: "))
num_2 = n2
dig2 = 0
    
while num_2 >= 1:
    num_2 = num_2//10
    dig2 += 1
        
result=n1*(10**dig2)+n2
print(result)