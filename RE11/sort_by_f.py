#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 18:42:13 2018

@author: diogo
"""

def sort_by_f(l):
    return sorted(l, key=lambda x:5-x if x>=5 else x)
