#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:37:16 2018

@author: diogo
"""

def is_perfect(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum = sum + i
    
    return(sum)
    
print(is_perfect(2521347))