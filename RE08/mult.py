#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 08:40:27 2018

@author: diogo
"""
def zero_matrix(lines,column):
    result = []
    line = []
    for i in range(0,column):
        line.append(0)
    for i in range(lines):
        result.append(line.copy())
    return result

def mult(M, N):
    lengM = len(M)
    if len(M[0]) != len(N):
        return []
    
    result = zero_matrix(len(M),len(N[0]))
    
    for i in range(lengM):
        for j in range(len(N[0])):
            for a in range(len(M[0])):
                result[i][j] += M[i][a]*N[a][j]
    return result
    
    
    
    
print(mult([[1, 2, 4], [3, 4, 1]], [[2, 0], [1, 2], [9, 8]]))