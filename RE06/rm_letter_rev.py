#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 08:53:57 2018

@author: diogo
"""

def rm_letter_rev(l,astr):
    string = astr.replace(l, "")
    string = string[::-1]
    return(string)
    
print(rm_letter_rev("a","paula"))
    
