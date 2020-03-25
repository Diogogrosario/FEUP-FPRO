#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 18:47:03 2018

@author: diogo
"""
import functools as ft

def map_reduce(n1, n2):
    return ft.reduce(lambda x, y:x*y if x*y<50 else x+y,[x**2 for x in range(n1,n2) if x%2 != 0])
    
