#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:15:49 2018

@author: diogo
"""

def find_dtype(atuple, data_type):
    result = ()
    for i in atuple:
        if type(i).__name__ == data_type:
            result += (i,)
    return result    

