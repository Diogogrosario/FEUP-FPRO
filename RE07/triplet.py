#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 09:11:36 2018

@author: diogo
"""

def triplet(atuple):
    
    for i in range(len(atuple)):
        for j in range(len(atuple)):
            for k in range(len(atuple)):
                if atuple[i]+atuple[j]+atuple[k] == 0 and i!=j!=k:
                    result = (atuple[i],atuple[j],atuple[k])
                    return result
                else:
                    result = ()
    return result
                
print(triplet((5,8,2,3,-4,-6,-8,-9,-1,7)))