#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 09:00:29 2019

@author: diogo
"""

def raise_exception(alist, value):
    result = []
    for i in alist:
        if i <= value:
            result.append(ValueError("{0} is not greater than {1}".format(i,value))) 
    return result
            