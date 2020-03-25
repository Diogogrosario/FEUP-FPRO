#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 08:42:18 2019

@author: diogo
"""

def count_exceptions(f, n1, n2):
    count = 0
    for i in range(n1,n2+1):
        try:
            f(i)
        except Exception:
            count += 1
    return count