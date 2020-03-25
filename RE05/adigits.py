#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 21:45:01 2018

@author: diogo
"""

def adigits(n1, n2, n3):
    
    n1=int(n1)
    n2=int(n2)
    n3=int(n3)
    
    if n1>=n2>=n3:
        return  (n1*100)+(n2*10)+n3
    elif n1>=n3>=n2:
        return  (n1*100)+(n3*10)+n2
    elif n2>=n1>=n3:
        return  (n2*100)+(n1*10)+n3
    elif n2>=n3>=n1:
        return  (n2*100)+(n3*10)+n1
    elif n3>=n1>=n2:
        return  (n3*100)+(n1*10)+n2
    elif n3>=n2>=n1:
        return  (n3*100)+(n2*10)+n1