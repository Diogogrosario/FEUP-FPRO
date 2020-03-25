#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 18:34:01 2018

@author: diogo
""" 
def unique(atuple):
    
    result = ()
    
    for i in atuple:
        if i not in result:
            result += (i,)
            
    result = sorted(result)
    return tuple(result)