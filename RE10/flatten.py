#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 08:35:34 2018

@author: diogo
"""
final = []

def flatten(alist):
    for i,v in enumerate(alist):
        if type(v) != list:
            final.append(v)
        else:
            flatten(alist[i])
    return final
        
