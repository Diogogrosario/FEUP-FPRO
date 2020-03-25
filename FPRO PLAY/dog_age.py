#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 18:22:44 2018

@author: diogo
"""

def dogs(h_age):
    dog = 0
    if h_age <= 2:
        dog = h_age*10.5
    else: 
        dog = 21+(h_age-2)*4
    return dog

print(dogs(16))
