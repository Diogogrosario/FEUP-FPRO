#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 08:57:15 2018

@author: diogo
"""

import math

def tfidf(documents):
    dict1 = {}
    N = len(documents)
    for l in documents:
        l = l.lower()
        l = l.split(" ")
        for w in l:
            if w not in dict1:
                dict1[w] = []
    for k in dict1:
        for x in documents:
            x = x.lower()	
            x = x.split(" ")
            dict1[k] += [(x.count(k)]
    for i in dict1:
        n = N - dict1[i].count(0)
        for y in range(N):
            dict1[i][y] *= math.log(N/n)
            dict1[i][y] = round(dict1[i][y], 3)
    return dict1