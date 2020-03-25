#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:25:37 2018

@author: diogo
"""

def fib(n):
    fib = [0,1]
    for i in range(2,n):
        fib += [fib[i-1] + fib[i-2]]
    if n == 1:
        fib = [0]
    return fib

print(fib(9))