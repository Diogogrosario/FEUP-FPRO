#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:44:18 2018

@author: diogo
"""

def palindrome(astring):
    count = 0
    for i in range(len(astring)):
        for c in range(len(astring)):
            if astring[i:c+1+i] == astring[c+1+i:i:-1]:
                count += 1
    return "For string '{}': {} palindrome substrings".format(astring,count)
