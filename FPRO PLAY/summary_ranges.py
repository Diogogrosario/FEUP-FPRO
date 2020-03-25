#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:06:42 2018

@author: diogo
"""

def summary_ranges(astring):
    astring = astring.replace(",", " ")
    astring = astring.split()
    astring = astring + [-1]
    tag = 0
    result = ""
    for i in range(len(astring)):
        if i > 0:
            if int(astring[i]) - int(astring[i-1]) == 1 and tag == 0:
                result += str(astring[i-1]) 
                tag = 1
            elif int(astring[i]) - int(astring[i-1]) != 1 and tag == 1:
                result += "->" + str(astring[i-1]) + ","
                tag = 0
            elif int(astring[i]) - int(astring[i-1]) != 1 and tag == 0:
                result += str(astring[i-1]) + ","
                tag = 0
    result = result[:-1]
    return result
