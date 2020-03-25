#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 19:06:47 2018

@author: diogo
"""

def odd_range(start, stop, step):
    for i in range(start,stop,step*2):
        if start%2 ==0:
            yield i+1
        else:
            yield i
    

        