#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 08:45:50 2018

@author: diogo
"""

def sparse_dot_product(dict1, dict2):
    result = 0
    for i in dict1:
        if i in dict2:
            result += dict1[i] * dict2[i]
    return result

print(sparse_dot_product({1: 3, 7: 1}, {1: 3, 7: 1}))