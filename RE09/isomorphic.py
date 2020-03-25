#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 09:33:36 2018

@author: diogo
"""

def isomorphic(astring1, astring2):
    d1={}
    d2={}
    alist = []
    for i,c in enumerate(astring1):
        if c not in d1:
            d1[c] =  astring2[i]
            alist += [(c,astring2[i])]
        elif d1[c] != astring2[i]:
            return  "'{0}' and '{1}' are not isomorphic".format(astring1,astring2)
    for i,c in enumerate(astring2):
        if c not in d2:
            d2[c] =  astring1[i]
        elif d2[c] != astring1[i]:
            return  "'{0}' and '{1}' are not isomorphic".format(astring1,astring2)
    return "'{0}' and '{1}' are isomorphic because we can map: {2}".format(astring1,astring2,alist)

print(isomorphic('turtle', 'tletur'))
    
            