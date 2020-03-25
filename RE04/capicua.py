#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:33:03 2018

@author: diogo
"""

num = int(input("Number: "))
n = num
digit=0
    
while n >= 1:
    digit=digit*10 + (n % 10)
    n=n//10
  
    
if digit == num:
    result = str(num) + " is a palindrome."
else:
    result = str(num) + " is not a palindrome."
    
print(result)
        
        