#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:23:39 2018

@author: diogo
"""

def uppercase(astring):
    count = 0
    for i in range(3):
        if astring[i].upper() == astring[i] and astring[i].isalpha():
            count = 1
            break
        
    if count == 1:
        return astring.upper()
    else:
        return astring
    

print(uppercase("Καληµέρα"))
            