#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 08:35:02 2018

@author: diogo
"""

def collisions(alist):
    lista = []
    num = 0
    dicti = {}
    for i in alist:
        for j in str(i):
            num += int(j)
        num = num%8
        lista.append(num)
        num=0

    for i in lista:
        if i in dicti:
            dicti[i] += 1
        if i not in dicti:
            dicti[i] = 1
    return dicti

print(collisions([24, 42]))