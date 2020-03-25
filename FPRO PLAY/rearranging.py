#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 17 21:36:29 2018

@author: diogo
"""

def rearrange(l):
    for x in l:
        for y in l:
            if y < 0 and x > 0:
                return list(map(lambda x, y:abs(x) if x <= 0,l))
    return l


print(rearrange([12, 11, -13, -5, 6, -7, 5, -3, -6, 0]))