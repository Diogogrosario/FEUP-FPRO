#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 10:17:47 2018

@author: diogo
"""

def sort_by_field(filename, field):
    lista = []
    index = 0
    with open(filename) as f:
        f = f.read()
    f = f.split("\n")
    for i in f:
        lista.append(i.split(","))
    index = lista[0].index(field)
    lista = sorted(lista[1:], key = lambda x:x[index])
    for index,x in enumerate(lista):
        lista[index] = ",".join(x)
    lista = "\n".join(lista)
    return f[0] + "\n" + lista
        
print(sort_by_field("emails.txt","surname"))
        