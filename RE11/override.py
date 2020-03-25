#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 19:47:02 2018

@author: diogo
"""

def override(l1, l2):
    for i in l2:
        for index,j in enumerate(l1):
            if i[0] == j[0]:
                l1[index] = i
            else:
                l1.append(i)
    return sorted(set(l1))
