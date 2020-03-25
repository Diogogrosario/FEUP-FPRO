#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 08:29:32 2018

@author: diogo
"""

def inner(u,v):
    produto = []
    soma = 0
    for i in range(len(u)):
        produto += [u[i]*v[i]]
        soma += produto[i]
    return soma
