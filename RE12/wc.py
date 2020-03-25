#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 08:32:18 2018

@author: diogo
"""

def wc(filename):
    with open(filename,"r") as f:
        f = f.read()
        return (len(f.split("\n")),len(f.split()),len(f))
    return

print(wc("shakespeare.txt"))