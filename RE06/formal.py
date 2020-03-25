#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 09:02:43 2018

@author: diogo
"""

def formal(name):
    name = name.replace(" de ", " ")
    name = name.replace(" da ", " ")
    name = name.replace(" do ", " ")
    name = name.replace(" e ", " ")
    nomes = name.split()
    result = ""
    for i in range (len(nomes)-1):
        result += nomes[i][0] + ". "
    final = nomes[-1] + ", " + result
    
    return final

print(formal("Diogo Guimarães do Rosário"))