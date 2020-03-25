#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:56:41 2018

@author: diogo
"""

def translate(astring, table):
    result = ""
    for i in astring:
        for j in range(len(table)):
            if i == table[j][0]:
                result += str(table[j][1])
                break
        else:
            result += i
            
    return result

