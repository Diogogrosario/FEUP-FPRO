#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 08:45:21 2019

@author: diogo
"""

def compatible(A, B):
    try:
        assert len(A[0]) == len(B), "A and B cannot be multiplied"
    except Exception as ex:
        return ex
    else:
        return "A and B can be multiplied"